import netifaces
from utils import Utils 

class Firewall:
    """UFW Firewall management here"""

    @staticmethod
    def get_default_iface_name():
        """returns the name of the default interface"""
        return netifaces.gateways()['default'][netifaces.AF_INET][1]
 
    @staticmethod
    def write_new_gufw_profile(vpn_protocol, vpn_ip_address, vpn_port):
	"""writes out a new gufw profile from the templates files"""
        iface=Firewall.get_default_iface_name()
	print "Replacing instances of the interface name with {0}".format(iface)

	input_path = "./templates/ufwrules.profile.tmpl"
	output_path = "./templates/output/ufwrules.profile"

        with open(input_path, "rt") as fin:
            Utils.create_directory_path(output_path)
            with open(output_path, "wt") as fout:
                for line in fin:
                    line = line.replace("INTERFACE_NAME", iface)
                    line = line.replace("VPN_PROTOCOL", vpn_protocol)
                    line = line.replace("VPN_PORT", vpn_port)
                    fout.write(line)

        print '''
1. open gufw

2. import profile from ./templates/output/ufwrules.profile
'''
        raw_input("Press enter when you're done importing the rules")
        
        return
