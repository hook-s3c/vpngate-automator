#!/usr/bin/env python

from classes.vpngate import VPNGateApp
from classes.firewall import Firewall

CSV_URL = 'http://www.vpngate.net/api/iphone/'
try: 
    def main():
        print ("\n")
        print ("\x1b[1;35mhook's VPNGate autograbber v0.02\x1b[0m")
        print ("\n")
        print ("\n")

        vpngate = VPNGateApp(CSV_URL)

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
        protocol, address, port = vpngate.write_openvpn_file(vpndata,vpnidentifier) 
        Firewall.write_new_gufw_profile(protocol, address, port) 

        vpngate.run_ovpn_config(".vpnconfigs/vpnconfig_{0}.ovpn".format(vpnidentifier))

    if __name__ == '__main__':
        main()

except KeyboardInterrupt:
  print ("\n\x1b[1;35m                             ")
  print ("    _    (^)                             ")
  print ("   (_\   |_|                             ")
  print ("    \_\  |_|                             ")
  print ("    _\_\,/_|                             ")
  print ("   (`\(_|`\|                             ")
  print ("  (`\,)  \ \'                            ")
  print ("   \,)   | |                             ")
  print ("     \__(__|\x1b[0m                      ")
  print ("                                         ")
  print ("Shoutz to sh3llg0d, an0n, daemochi, akatz")
  print ("Peace!                                   ")
  print ("\n                                       ")
