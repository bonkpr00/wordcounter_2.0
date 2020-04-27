import urllib.request
import sys
import argparse

def main():
   pb_parser = argparse.ArgumentParser(description='počítadlo slov, znaků a řádků pro webovou stránku')
   pb_parser.add_argument("stranka", help="Název stránky")
   pb_parser.add_argument("--znaky",action="store_true")
   pb_parser.add_argument("--slova",action="store_true")
   pb_parser.add_argument("--radky",action="store_true")

   p = pb_parser.parse_args()

   try:
       if p.znaky and p.slova and p.radky:
        stranka = urllib.request.urlopen(p.stranka)
        obsah_stranky = stranka.read()
        obsah_stranky_dekodovany = obsah_stranky.decode('utf-8')
        stranka.close()
        znaky = len(obsah_stranky_dekodovany)
        print (f"Počet znaků: {znaky}")
        slova = len(obsah_stranky_dekodovany.split(" ")) + len (obsah_stranky_dekodovany.split ('\n')) - 1
        print (f"Počet slov: {slova}")
        radky = len(obsah_stranky_dekodovany.split("\n"))
        print (f"Počet řádků: {radky}")
       elif p.znaky:
        znaky = len(obsah_stranky_dekodovany)
        print(f"Počet znaků: {znaky}")
       elif p.slova:
        slova = len(obsah_stranky_dekodovany.split(" ")) + len(obsah_stranky_dekodovany.split('\n')) - 1
        print(f"Počet slov: {slova}")
       elif p.radky:
        radky = len(obsah_stranky_dekodovany.split("\n"))
        print(f"Počet řádků: {radky}")
       else:
        stranka = urllib.request.urlopen(p.stranka)
        obsah_stranky = stranka.read()
        obsah_stranky_dekodovany = obsah_stranky.decode('utf-8')
        stranka.close()
        znaky = len(obsah_stranky_dekodovany)
        print(f"Počet znaků: {znaky}")
        slova = len(obsah_stranky_dekodovany.split(" ")) + len(obsah_stranky_dekodovany.split('\n')) - 1
        print(f"Počet slov: {slova}")
        radky = len(obsah_stranky_dekodovany.split("\n"))
        print(f"Počet řádků: {radky}")
   except FileNotFoundError:
      print("STRÁNKA NEEXISTUJE")
      sys.exit()
   except PermissionError:
      print("PŘÍSTUP ODEPŘEN")
      sys.exit()

if __name__ == '__main__':
   main()


