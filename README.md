# VPN Gate auto-grabber

## Greetz

shouts to sh3llg0d, an0n_l1t3, daemochi, akatz!!!!

## Overview

You need a VPN if you want to keep prying eyes away from your network traffic - big brother, network admins, bad actors.

Use this script to grab a free VPN from vpngate.net

## Quickstart
```
git clone https://github.com/hook-s3c/vpngate-automator.git
cd vpngate-automator
sudo chmod +x ./fetchvpns.py
pip install -r ./requirements.txt

./fetchvpns.py
```

## Requirements

Should work on all Debian systems, tested on Ubuntu 16.04.
You will neeed to install OpenVPN on your system.

```
apt-get install openvpn
apt-get install python-notify
```


## Breakdown

1. initial load will pull down the CSV, parse and output it to the console
2. you will be asked which country shortcode to filter by
3. after choosing a country shortcode, you will then be presented with the filtered results
4. the program will then ask you to choose a VPN config by the identifier in the first column
5. choose an identifier and the program will create the OpenVPN config file in ./.vpnconfigs/ 
6. it will then run the openvpn client with escalated privileges and you will now be tunnelled to another country
7. profit!

## Consider a firewall (optional)

After investing some time in Wireshark, I noticed that some traffic liked to leak outside of the VPN - this part will help close this down.

This script will automatically generate a UFW profile from a template found in `./templates/`.

- export ufw rules
- helpful output to explain which iptables/firewall rules to import

```
apt-get install ufw
apt-get install gufw
```

### Steps

1. Run script with optional firewall paramter `--firewall`
2. Open GUFW 
3. change permissions on file;
 `sudo chmod 0600 ./templates/output/ufwrules.profile`
3. `file > import profile`
4. choose ufwrules from dropdown
5. press enter to launch the VPN

--------------------------------------------------------------------------------------------

## Roadmap

must have;
- add firewall configuration (see above)
should have;
- allow mirrors for CSV URL
could have;
- abstract configuration
- dockerize to alpine container
- format the data in the columns to something more meaningful
- filter base64 output for UDP/TCP and port
- refactor user input to allow adjustments of filters
- command line arguments (country/filters, auto-start) to just get going
- unit tests

## Notes

This is one of my first python scripts as I learn, so some parts may look hella ugly.

There is no support, fork/PR as you wish. 
MIT license, so attribution is mandatory.

Support for notifications in the gnome interface.

There are no unit tests, sorry.

## References

Here are some links to some bits I had to pull together, when I had no clue of the subtleties of python;

- https://stackoverflow.com/questions/431752/python-csv-reader-how-do-i-return-to-the-top-of-the-file
- https://stackoverflow.com/questions/14017996/is-there-a-way-to-pass-optional-parameters-to-a-function
- https://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
- https://stackoverflow.com/questions/11310248/find-number-of-columns-in-csv-file
- https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
- https://evanhahn.com/python-skip-header-csv-reader/
- https://stackoverflow.com/questions/24659006/unpack-only-the-first-few-columns-from-the-csv-reader
- https://stackoverflow.com/questions/19143667/how-to-read-a-csv-without-the-first-column
- https://stackoverflow.com/questions/107405/how-do-you-send-a-head-http-request-in-python-2/2070916#2070916
- https://stackoverflow.com/questions/39176935/formatting-output-of-csv-file-in-python
- https://stackoverflow.com/questions/2100353/sort-csv-by-column
- https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
python static methods;
- https://stackoverflow.com/questions/11759269/calling-static-method-in-python
inetfaces;
- https://stackoverflow.com/questions/30698521/python-netifaces-how-to-get-currently-used-network-interface
clint lib;
- https://github.com/kennethreitz/clint
working with requirements;
- https://stackoverflow.com/questions/7225900/how-to-pip-install-packages-according-to-requirements-txt-from-a-local-directory
replacing strings in files;
- https://stackoverflow.com/questions/4128144/replace-string-within-file-contents
