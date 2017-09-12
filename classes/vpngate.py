import csv
import requests
import subprocess
import sys
import time
import urllib2
from clint.textui import progress
import re

from utils import Utils

cr = None
MISSING = object()
nicely_formatted_csv_data_pattern = "{:<20} {:<20} {:<10} {:<10} {:<10} {:<40} {:<10}"

class VPNGateApp:
    """App class for VPN Gate"""

    def __init__(self, URL):
        self.URL = URL
        #super(VPNGate, self).__init__()
        return
 

    def write_openvpn_file(self,b64ovpndata, vpnname):
	"""takes a base64 string and saves it out as an .ovpn file"""

	openvpnconfigpath = ".vpnconfigs/vpnconfig_{0}.ovpn".format(vpnname)

        decoded_ovpndata = b64ovpndata.decode('base64')

        Utils.create_directory_path(openvpnconfigpath)

        fh = open(openvpnconfigpath, "wb")
        fh.write(decoded_ovpndata)
        fh.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
        fh.close()

        #print decoded_ovpndata
        return self.grab_ovpn_values(openvpnconfigpath)


    def grab_ovpn_values(self,openvpnconfigpath):

        protocol = None
        address_and_port = None
        address = None
        port = None

        for line in open(openvpnconfigpath, 'r'):

            if protocol == None:
                pattern = re.compile("^proto (tcp|udp)\r$") #tcp or udp?
                match = pattern.match(line)

                if match:
                    print "found: " + match.group(1)
                    protocol = match.group(1)
                else:
                   pass

            if address_and_port == None:
                pattern2 = re.compile("^remote ([0-9\.]*) ([0-9]*)\r$") #ip address and port
                match2 = pattern2.match(line)

                if match2:
                    print "found: " + match2.group(1) + " " + match2.group(2) 
                    address_and_port = match2
                    address  = match2.group(1)
                    port     = match2.group(2)
                else:
                   pass

        return protocol, address, port


    def run_ovpn_config(self, path):
	"""opens a process on the host OS to launch openvpn with the new config"""

        x = subprocess.Popen(['sudo', 'openvpn', '--config', path])
        try:
            while True:
                time.sleep(600)
            Utils.send_message("VPN connection established","now connected")
            # termination with Ctrl+C
        except:
            try:
                x.kill()
            except:
                pass
            while x.poll() != 0:
                time.sleep(1)
            print '\nVPN terminated'
            Utils.send_message("vpn terminated","the vpn is now gone")
        return


    def grab_csv(self):
        """grabs the csv from the vpngate website"""

        print "grabbing VPNGate CSV from : {0}, this may take a minute...".format(self.URL)
	print "ctrl+c if you already have a cached list"
 
        try:
            with requests.Session() as session:
                r = session.get(self.URL, stream=True, hooks=dict(response=self.grab_csv_callback))

                csvdatapath = ".cache/vpndata.csv"

                # it seems that the requests module had a bug, or didn't support content-length headers /
                # in the response, so here we use urllib2 to do a HEAD request prior to download 
                request2 = urllib2.Request(self.URL)
                request2.get_method = lambda : 'HEAD'
                response2 = urllib2.urlopen(request2) 
                total_length = int(response2.info()['Content-Length'])

                Utils.create_directory_path(csvdatapath)
                with open(csvdatapath, 'wb') as f:
                    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                            f.write(chunk)
                            f.flush()
        except:
            print "[!ERROR] There was a problem fetching the data from vpngate.net\r\n"
        return

    def grab_csv_callback(self, r, *args, **kwargs):
        print "data returned from {url}".format(url=r.url)

        # playing with callbacks 
        #decoded_content = r.content.decode('utf-8')
        #fh = open(csvdatapath, "wb")
        #fh.write(decoded_content)
        #fh.close()
        return


    def grab_vpndata(self, chosenVPNName):
	"""grabs the VPN data column from the CSV data"""

        file_handle.seek(0)
        for utf8_row in cr:
            if(chosenVPNName == utf8_row[0]):
                return utf8_row[14]
        return None


    def parse_csv(self, chosenCountryShortCodeArg=MISSING):
	"""parses the CSV data and formats the columns in the stdout"""

        global cr, MISSING, file_handle
        file_handle = open(".cache/vpndata.csv", "r")
        cr = csv.reader(file_handle, delimiter=',')

        for utf8_row in cr:
            (a) = utf8_row[:-1]
            if len(a) != 0:
                if chosenCountryShortCodeArg is MISSING:
                     print(nicely_formatted_csv_data_pattern.format(*a))
                else:
                    if a[6] == chosenCountryShortCodeArg:
                        print(nicely_formatted_csv_data_pattern.format(*a))
        return


