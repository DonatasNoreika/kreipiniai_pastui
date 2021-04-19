import re

def gauti_kreipini(vardas):
    kreipiniai = {
        'a': 'a',
        'as': 'ai',
        'ė': 'e',
        'is': 'i',
        'us': 'au',
        'ys': 'y'
    }
    for galune in kreipiniai.keys():
        pattern = re.compile(f'({galune})$')
        res = pattern.search(vardas)
        if res:
            isimta = res.group()
            kreipinys = re.sub(isimta, kreipiniai[isimta], vardas)
            print(kreipinys)
            return kreipinys


gauti_kreipini("Donatas")
gauti_kreipini("Laura")
gauti_kreipini("Robertas")
gauti_kreipini("Kamilė")
gauti_kreipini("Augis")
gauti_kreipini("Šaulys")
