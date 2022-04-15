#!/usr/bin/python

# Title: Brutos Directory Scanner
# Developed by Sérgio Corrêa
# Tested on: MacOS / Linux

import time
import requests
import sys
import argparse
from progress.bar import ChargingBar
from requests.exceptions import ConnectionError


class Color:
    RED = '\033[1;31;48m'
    GREEN = '\033[1;32;48m'
    END = '\033[1;37;0m'


parser = argparse.ArgumentParser(description="Brutos Directory Scanner - Version  1.0",
                                 usage="Ex: python3 brutos.py -i just-an-example-CTF.com.br -f wordlist.txt")
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help="The list of words for analysis")
parser.add_argument("-u", "--url", help="The address reflected in the target")
parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')

banner = '''[√] - Brutos Directory Scanner - v. 1.0\n'''

args = parser.parse_args()

if not args.file or not args.url:

    parser.print_help()

    sys.exit()

names = args.file.read().splitlines()

file = args.file

url = str(args.url)

url_list = []

bar = ChargingBar('Processing ...', max=len(names))

start_time = time.time()

for nome_check in names:

    url_format = (('http://{}/{}'.format(url, nome_check)))

    try:

        connection = requests.get(url_format)

        bar.next()

        if connection.status_code == 200:
            url_list.append(url_format)

    except ConnectionError:

        print(Color.RED + " \n[!] - Connection failed - Exiting the script..." + Color.END)

        sys.exit()

bar.finish()

cont = 0

if not url_list:

    print(Color.RED + "[!] - No directories found..." + Color.END)

    sys.exit()

for url_found in url_list:

    cont += 1

    print(Color.GREEN + '[√]', url_found + Color.END)

end_time = time.time()

total_time = end_time - start_time

print('\n[√] - Processing Time :', '-', total_time)

print('[√] - We found {}'.format(cont) + ' directory(ies)')

print(banner)
