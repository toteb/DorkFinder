#!/usr/bin/python3

# Script created by glavstroy
# Thanks to @reewardius

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""{CYAN}
██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝{PURPLE}
██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝{END}"""
print(banner)
print(f'\n')

import requests
from bs4 import BeautifulSoup
import url_list
import time
import random
import os

def main():

    #clean output file
    file_path = 'output.txt'
    if os.path.exists(file_path):
        os.remove("output.txt")

    for url in url_list.urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Site": "cross-site",
            "TE": "trailers"
            }
        
        #check if the -t flag is specified before sending requests and analyzing them
        if url_list.cli:
            r = requests.get(url, headers=headers, timeout=70)
            if r.status_code == 200:
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.find_all('h3')
            elif r.status_code == 429:
                print(f"{RED}You've got a captcha from Google. Try again later or use an another proxy{END}")
                break
            else:
                print(f'{RED}Unknown error{END}')
                break

            if len(links) >= 1:
                url_found = url
                print(f'{url_found}   {CYAN}======>{END}  {GREEN}Found{END}')

                #print all dorks to an output file
                if url_list.args.output:
                    with open('output.txt', 'a', encoding='utf-8') as output_file:
                        output_file.write(f'[+] {url_found}\n')
            else:
                print(f'{url}   {CYAN}======>{END}  {RED}Not found{END}')

            time.sleep(random.randint(58,66))

try:
    main()
except KeyboardInterrupt:
    print(f'\nInterrupted')
    exit()
