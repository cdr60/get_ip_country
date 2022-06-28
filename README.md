# get_ip_country
Get country from a file containing a lot of ipv4 address

Dependancies :
- Needs python3
- Needs python3-geoip2 (apt install or dnf install)
- Needs GeoLite2-Country.mmdb file from GeoLite2, put your path at line : geodbfile="/usr/share/GeoIP/GeoLite2-Country.mmdb" 

Usage :
python3 geticountry.py filein fileout

filein : texte file contaning one ipv4 by line
fileout : texte file containint each ipv4 + country ISO code separated by :

Ex : 
file in : 80.11.102.108
fileout : 80.11.102.108:FR

Speed : 1000 ip in about 10 secondes.



