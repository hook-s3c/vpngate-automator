# VPN Gate auto-grabber

## Greetz

shouts to sh3llg0d, an0n_l1t3, daemochi, akatz!!!!

## Overview

You need a VPN if you want to keep prying eyes away from your network traffic - big brother, network admins, bad actors.

Use this script to grab a free VPN from vpngate.net

```
./fetchvpns.py
```

## Requirements

Should work on all Debian systems, tested on Ubuntu 16.04

```
apt-get install openvpn
```

## Breakdown

1. initial load will pull down the CSV, parse and output it to the console
- you will be asked which country shortcode to filter by
- after choosing a country shortcode, you will then be presented with the filtered results
- the program will then ask you to choose a VPN config by the identifier in the first column
- choose an identifier and the program will create the OpenVPN config file in ./.vpnconfigs/ 
- it will then run the openvpn client with escalated privilges and you will now be tunneled to another country
- profit!

## Roadmap

- sort the list by score
- format the data in the columns to something more meaningful
- refactor user input to allow adjustments of filters
- filter base64 output for UDP/TCP and port 
- command line arguments (country/filters, auto-start) to just get going
- helpful output to explain which iptables/firewall rules to import

## Notes

This is one of my first python scripts as I learn, so some parts may look hella ugly.

There is no support, fork/PR as you wish.

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
- https://stackoverflow.com/questions/39176935/formatting-output-of-csv-file-in-python
- https://stackoverflow.com/questions/2100353/sort-csv-by-column
- https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output