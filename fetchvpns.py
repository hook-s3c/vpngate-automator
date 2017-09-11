#!/usr/bin/env python

from classes.vpngate import VPNGate


CSV_URL = 'http://www.vpngate.net/api/iphone/'

def main():

    vpngate = VPNGate(CSV_URL)

    vpngate.grab_csv()
    vpngate.parse_csv()

    print "\r\n"
    print "----------------------------------"
    countryshortcode = raw_input("Now choose a country shortcode you sonofabitch: ")
    print "you entered:", countryshortcode, "and I'm searching..."
    print "\r\n"
    vpngate.parse_csv(countryshortcode)

    print "\r\n"
    print "----------------------------------"
    vpnidentifier = raw_input("Give me a VPN name and let's go: ")
    print "you entered:", vpnidentifier
    print "\r\n"

    vpndata = vpngate.grab_vpndata(vpnidentifier)
    vpngate.write_openvpn_file(vpndata,vpnidentifier)
    vpngate.run_ovpn_config(".vpnconfigs/vpnconfig_"+ vpnidentifier +".ovpn")

if __name__ == '__main__':
    main()
