#!/usr/bin/python3
#dnf install python3-geoip2
import geoip2.database
import os.path
import sys

geodbfile="/usr/share/GeoIP/GeoLite2-Country.mmdb" 
print("--------------------------------") 
print("Recherche pays d'origine d'ip par lecture de ")
print(geodbfile) 
print("Usage : argument 1 : fichier liste d'IP en entrée") 
print("        argument 2 : fichier liste IP et Pays en sortie") 
print("Ex : getipcountry.py listeip.txt listeippays.txt") 
print("--------------------------------") 
if len(sys.argv)<3:
   print("Il faut 2 arguments distincts")
   sys.exit(2)

infile=sys.argv[1]
outfile=sys.argv[2]

if (infile==outfile):
   print("Les 2 fichiers doivent êtres distincts")
   sys.exit(2)

if not os.path.isfile(infile):
    print(infile+' does not exist.')
    sys.exit(2)

if not os.path.isfile(infile):
    print(infile+' does not exist.')
    sys.exit(2)

if not os.path.isfile(geodbfile):
    print(geodbfile+' does not exist.')
    sys.exit(2)

nin=0
nout=0
nerr=0
reader = geoip2.database.Reader(geodbfile)
with open(infile,"r") as f:
    content = f.read().splitlines()
f.close()

nin=len(content)
print("fichier "+infile+" "+str(nin)+" lignes lues")


with open(outfile,"w") as f:
    err=0
    for ip in content:
       try:
          response = reader.country(ip)
       except:
          err=1
          nerr=nerr+1
          print("Erreur pour l'ip "+ip)
       if (err==0):
          line=ip+":"+format(response.country.iso_code)
          f.write(line+"\n")
          nout=nout+1
f.close()
reader.close()
print("--------------------------------")
print("Terminé : ")
print(str(nout)+" ligne(s) écrite(s) dans "+outfile)
print(str(nerr)+" erreur(s)")

sys.exit(0)
