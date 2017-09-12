import csv
import requests
import subprocess
import sys
import time

from utils import Utils

cr = None
MISSING = object()

class VPNGateApp:
    """App class for VPN Gate"""

    def __init__(self, URL):
        self.URL = URL
        #super(VPNGate, self).__init__()
        return


    def write_openvpn_file(self,b64ovpndata, vpnname):
	"""takes a base64 string and saves it out as an .ovpn file"""

	openvpnconfigpath = ".vpnconfigs/vpnconfig_{0}.ovpn".format(vpnname)

        Utils.create_directory_path(openvpnconfigpath)

        fh = open(openvpnconfigpath, "wb")
        fh.write(b64ovpndata.decode('base64'))
        fh.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
        fh.close()
        return


    def run_ovpn_config(self, path):
	"""opens a process on the host OS to launch openvpn with the new config"""

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
            Utils.send_message("vpn terminated","the vpn is now gone")
        return


    def grab_csv(self):
        """grabs the csv from the vpngate website"""

        print "grabbing VPNGate CSV from : {0}, this may take a minute...".format(self.URL)
	print "ctrl+c if you already have a cached list"

        try:
            with requests.Session() as s:
		csvdatapath = ".cache/vpndata.csv"

		Utils.create_directory_path(csvdatapath)

                download = s.get(self.URL)
                decoded_content = download.content.decode('utf-8')
                fh = open(csvdatapath, "wb")
                fh.write(decoded_content)
                fh.close()
            print "grabbed CSV"
        except:
            print "[!ERROR] There was a problem fetching the data from vpngate.net\r\n"
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
                     print('{:<20} {:<20} {:<10} {:<10} {:<10} {:<40} {:<10}'.format(*a))
                else:
                    if a[6] == chosenCountryShortCodeArg:
                        print('{:<20} {:<20} {:<10} {:<10} {:<10} {:<40} {:<10}'.format(*a))
        return


