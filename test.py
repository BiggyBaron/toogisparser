# usr/bin/ python3

import urllib.request
import time
from tqdm import tqdm
import ssl


context = ssl._create_unverified_context()

for i in tqdm(range(1)):
    with urllib.request.urlopen('https://2gis.kz/nur_sultan/search/qmobot', context=context) as f:
        print(f.read().decode('utf-8'))

