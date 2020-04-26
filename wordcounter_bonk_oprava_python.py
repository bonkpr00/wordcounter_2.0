import urllib.request
import sys
import argparse


stranka = urllib.request.urlopen('https://www.novinky.cz/koronavirus/clanek/vedci-ve-wu-chanu-delali-s-koronavirem-absolutni-silenosti-tvrdi-predni-rusky-mikrobiolog-40321795')
obsah_stranky = stranka.read()
obsah_stranky_dekodovany = obsah_stranky.decode('utf-8')
stranka.close()

znaky = len(obsah_stranky)
print (f"Počet znaků: {znaky}")
slova = slova = len(obsah_stranky_dekodovany.split(" ")) + len (obsah_stranky_dekodovany.split ('\n')) - 1
print (f"Počet slov: {slova}")
radky = len(obsah_stranky_dekodovany.split("\n"))
print (f"Počet řádků: {radky}")







