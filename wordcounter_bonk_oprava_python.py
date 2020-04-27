import urllib.request
import sys

stranka = urllib.request.urlopen('https://www.novinky.cz/koronavirus/clanek/vedci-ve-wu-chanu-delali-s-koronavirem-absolutni-silenosti-tvrdi-predni-rusky-mikrobiolog-40321795')
obsah_stranky = stranka.read()
obsah_stranky_dekodovany = obsah_stranky.decode('utf-8')
stranka.close()

try:
    znaky = len(obsah_stranky_dekodovany)
    print (f"Počet znaků: {znaky}")
    slova = len(obsah_stranky_dekodovany.split(" ")) + len (obsah_stranky_dekodovany.split ('\n')) - 1
    print (f"Počet slov: {slova}")
    radky = len(obsah_stranky_dekodovany.split("\n"))
    print (f"Počet řádků: {radky}")
except FileNotFoundError:
    print("STRÁNKA NEEXISTUJE")
    sys.exit()
except PermissionError:
    print("PŘÍSTUP ODEPŘEN")
    sys.exit()

