#!/usr/bin/python3

# Script created by glavstroy (hermione)
# Thanks to @reewardius

import requests
from bs4 import BeautifulSoup
import url_list
import time
import random
import os
import urllib.parse
import sys
import platform

# ANSI color codes for better readability
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

# function printing banner
def printBanner():
    banner = f"""
    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝██║  ██║██║  ██╗██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(banner)
    print('\n')

# Logging function
def log_debug_info(response):
    #print status code and headers for debugging.
    #print("Status Code:", response.status_code)
    #print("Headers:", response.headers)

    content = None
    if response.headers.get('Content-Encoding') == 'gzip':
        import gzip
        from io import BytesIO
        buf = BytesIO(response.content)
        f = gzip.GzipFile(fileobj=buf)
        content = f.read().decode('utf-8')
    elif response.headers.get('Content-Encoding') == 'br':
        try:
            import brotli
            content = brotli.decompress(response.content).decode('utf-8')
        except Exception as e:
            # Print decompression errros 
            # print(f"Error decompressing Brotli content: {str(e)}")
            content = response.content.decode('utf-8', errors='replace')
    else:
        content = response.text
    # Print content for debugging
    #print("Content:", content[:500])  # Print the first 500 characters of the decompressed content
    return content

def performGoogleSearchDarwin(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US;q=0.5,en;q=0.3",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers"
    }

    try:
        r = requests.get('https://www.google.com/search?q=' + urllib.parse.quote(url), headers=headers, timeout=95)
        html = log_debug_info(r)  # Log response details
        if r.status_code == 200:
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('h3')
        elif r.status_code == 429:
            print(f"{RED}You've got a captcha from Google. Try again later or use another proxy{END}")
            sys.exit()
        else:
            print(f'{RED}Unknown error{END}')
            sys.exit()

        if len(links) >= 1:
            print(f'{BLUE}[+]{END} {url}   {CYAN}======>{END}  {GREEN}Found{END}')
            return True
        else:
            print(f'{BLUE}[!]{END} {url}   {CYAN}======>{END}  {RED}Not found{END}')
            return False
    except Exception as e:
        print(f"{RED}An error occurred while performing Google search: {str(e)}{END}")
        sys.exit()

def performGoogleSearchLinux(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US;q=0.5,en;q=0.3",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers"
    }

    try:
        r = requests.get('https://www.google.com/search?q=' + urllib.parse.quote(url), headers=headers, timeout=95)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('h3')
        elif r.status_code == 429:
            print("You've got a captcha from Google. Try again later or use another proxy")
            sys.exit()
        else:
            print('Unknown error')
            sys.exit()

        if len(links) >= 1:
            print(f'[+] {url}   ======>  Found')
            return True
        else:
            print(f'[!] {url}   ======>  Not found')
            return False
    except Exception as e:
        print(f"An error occurred while performing Google search: {str(e)}")
        sys.exit()

# Function to clean output file
def cleanOutput():
    file_path = 'output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)

# Function to write URLs to output file
def writeOutput(url):
    file_path = 'output.txt'
    with open(file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(f'[+] {url}\n')

# Main function
def main():
    print(f"\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mIt's very important not to stress the Google during usage of dork payloads. \n\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mThat's why, we wait about 60 seconds delay between requests. Just be patient...\033[0m")

    cleanOutput()

    for url in url_list.urls:
        if url_list.cli:
            if platform.system() == "Darwin":
                result = performGoogleSearchDarwin(url)
            elif platform.system() == "Linux":
                result = performGoogleSearchLinux(url)
            else:
                print("Unsupported platform")
                sys.exit()
                
            if result and url_list.args.output:
                writeOutput(url)
        # Delay between requests
        time.sleep(random.randint(58, 66))

# Exception handling
try:
    main()
except KeyboardInterrupt:
    print('\nInterrupted')
    exit()

# function cleaning output file
def cleanOutput():
    file_path = 'output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)

# function writing URLs to output file
def writeOutput(url):
    file_path = 'output.txt'
    with open(file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(f'[+] {url}\n')

# main
def main():
    printBanner()
    print(f"\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mIt's very important not to stress the Google during usage of dork payloads. \n\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mThat's why, we wait about 60 seconds delay between requests. Just be patient...\033[0m")

    cleanOutput()

    for url in url_list.urls:
        if url_list.cli:
            if performGoogleSearch(url):
                if url_list.args.output:
                    writeOutput(url)
        # delay between requests
        time.sleep(random.randint(58,66))

# exception handling
try:
    main()
except KeyboardInterrupt:
    print(f'\nInterrupted')
    exit()
