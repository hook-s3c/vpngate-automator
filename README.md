# VPN Gate auto-grabber

## Greetz

shouts to sh3llg0d, an0n_lit3, daemochi, akatz!!!!

## Overview



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

- initial load will pull down the CSV, parse and output it to the console

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

## Notes

This is one of my first python scripts as I learn, so some parts may look hella ugly.

There is no support, fork/PR as you wish.

Support for notifications in the gnome interface.

There are no unit tests, sorry.

## References

Here are some links to some bits I had to pull together, when I had no clue of the subtleties of python;
