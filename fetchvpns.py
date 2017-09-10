#!/usr/bin/env python

import csv
import requests
import pynotify
import subprocess
import sys
import time

CSV_URL = 'http://www.vpngate.net/api/iphone/'
cr = None
MISSING = object()

class VPNGate:

    def __init__(self, URL):
        self.URL = URL
        #super(VPNGate, self).__init__()
        return


    def sendmessage(self, title, message):
        pynotify.init("Test")
        notice = pynotify.Notification(title, message)
        notice.show()
        return

    def write_openvpn_file(self,b64ovpndata, vpnname):
        fh = open(".vpnconfigs/vpnconfig_"+ vpnname +".ovpn", "wb")
        fh.write(b64ovpndata.decode('base64'))
        fh.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
        fh.close()
        return

    def run_ovpn_config(self, path):
        x = subprocess.Popen(['sudo', 'openvpn', '--config', path])
        try:
            while True:
                time.sleep(600)
            # termination with Ctrl+C
        except:
            try:
                x.kill()
            except:
                pass
            while x.poll() != 0:
                time.sleep(1)
            print '\nVPN terminated'
            self.sendmessage("vpn terminated","the vpn is now gone")
        return

    def grab_csv(self):
        """grabs the csv from the vpngate website"""
        print "grabbing VPNGate CSV from : " + self.URL
        try:
            with requests.Session() as s:
                download = s.get(self.URL)
                decoded_content = download.content.decode('utf-8')
                fh = open(".cache/vpndata.csv", "wb")
                fh.write(decoded_content)
                fh.close()
            print "grabbed CSV"
        except:
            print "[!ERROR] There was a problem fetching the data from vpngate.net\r\n"
        return


    def grab_vpndata(self, chosenVPNName):
        file_handle.seek(0)
        for utf8_row in cr:
            if(chosenVPNName == utf8_row[0]):
                return utf8_row[14]
        return


    def parse_csv(self, chosenCountryShortCodeArg=MISSING):
        global cr, MISSING, file_handle
        file_handle = open(".cache/vpndata.csv", "r")
        cr = csv.reader(file_handle, delimiter=',')
        for utf8_row in cr:
            (a) = utf8_row[:-1]
            if len(a) != 0:
                if chosenCountryShortCodeArg is MISSING:
                     print('{:<20} {:<20} {:<10} {:<10} {:<10} {:<40} {:<10}'.format(*a))
                else:
                    if a[6] == chosenCountryShortCodeArg:
                        print('{:<20} {:<20} {:<10} {:<10} {:<10} {:<40} {:<10}'.format(*a))
        return

def main():

    vpngate = VPNGate(CSV_URL)

    vpngate.grab_csv()
    vpngate.parse_csv()

    print "\r\n"
    print "----------------------------------"
    var = raw_input("Now choose a country shortcode you sonofabitch: ")
    print "you entered:", var, "and I'm searching..."
    print "\r\n"
    vpngate.parse_csv(var)

    print "\r\n"
    print "----------------------------------"
    vpnidentifier = raw_input("Give me a VPN name and let's go: ")
    print "you entered:", vpnidentifier, ""
    print "\r\n"

    vpndata = vpngate.grab_vpndata(vpnidentifier)
    vpngate.write_openvpn_file(vpndata,vpnidentifier)
    vpngate.run_ovpn_config(".vpnconfigs/vpnconfig_"+ vpnidentifier +".ovpn")

if __name__ == '__main__':
    main()
