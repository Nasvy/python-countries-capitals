#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from collections import OrderedDict
import smtplib
import smtplib, socket, getpass
CAP_AND_COUN = {}
CAPITALS = []
COUNTRIES = []
ORDERED_LIST = {}
a = "Countries"
b = "Capitals"
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
ddef main():
    print "Send email by gmail"
    username = raw_input("Count from gmail")
    password = getpass.getpass("Password:")

    fromaddr = raw_input("from, ejemplo: I")
    toaddrs = raw_input("to, ejemplo : You")
    #asunto = raw_input("subject, from message: ")
    body = raw_input("Message html:")

    msg = MIMEMultipart()
    msg['From'] = fromaddr #This saves the mail of the sender
    msg['To'] = toaddrs  #This saves the mail of the receiver
    msg['Subject'] = "Countres and Capitals"  #This saves the subject
    msg.attach(MIMEText(body, 'plain')) #This saves the message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "yes"
    except:
        print "ups"

def ORDER():
    """This function order the capitals"""
    LIMPIAR()
    ordered = OrderedDict(sorted(CAP_AND_COUN.items(), key=lambda x: x[1:]))
    print a.center(20,"="), b.center(20,"=")
    for k , v in ordered.items():
        print k.center(20), v.center(20)
        ORDERED_LIST[k]=v
    raw_input("press enter")
    MENU()
def CAPITALS_AND_COUNTRIES():
    """Here shows the capitals and countries"""
    print a.center(20,"="), b.center(20,"=")
    for i in CAP_AND_COUN:
        print i.center(20), CAP_AND_COUN[i].center(20)
    raw_input("Press enter")
    LIMPIAR()
    MENU()
def LIST_CAPITAL():
    """Here shows the list of the capitals"""
    print b.center(20,"=")
    for i in CAPITALS:
        print i.center(20)
    raw_input("Press enter")
    LIMPIAR()
    MENU()
def LIST_COUNTRIES():
    """Here Shows the list of the Countries"""
    print a.center(20,"=")
    for i in COUNTRIES:
        print i.center(20)
    raw_input("Press enter")
    LIMPIAR()
    MENU()
def QUEST():
    """This function ask the user if he wants to insert another Country and Capital"""
    ans = raw_input("Do you want to insert another Country? y/n\n")
    ans = ans.lower()
    if ans == "y" or ans == "yes":
        INSERT_COUNTRIES()
    elif ans == "n" or ans == "no":
        LIMPIAR()
        MENU()
    else:
        print "Choose a correct option"
        raw_input("Press enter")
        LIMPIAR()
        QUEST()
def INSERT_COUNTRIES():
    """Here the user insert the Country and the Capital"""
    try:
        coun = True
        while coun == True:
            country = raw_input("Insert a Country\n")
            country = country.title()
            if str(country).isalpha() == True or " " in country:
                COUNTRIES.append(country)
                coun = False
            else:
                print "write only words n.n"
                raw_input("Press enter")
                LIMPIAR()
                coun = True
        cap = True
        while cap == True:
            capital = raw_input("Insert a Capital\n")
            capital = capital.title()
            if str(country).isalpha() == True or " " in capital:
                CAPITALS.append(capital)
                cap = False
            else:
                print "write only words n.n"
                raw_input("Press enter")
                LIMPIAR()
                cap = True
    except ValueError:
        print "Insert a valid option"
    CAP_AND_COUN[country] = capital
    print CAP_AND_COUN
    LIMPIAR()
    QUEST()
def LIMPIAR():
    """This function cleans the screen"""
    os.system("cls")
    os.system("clear")
def OUT():
    """This function exit the program"""
    sys.exit()
def MENU():
    """This is the menu that the user watch"""
    LIMPIAR()
    print "Welcome to Captials and Countries".center(40,"=")
    print "-----1. Insert a country----------------"
    print "-----2. Countries list------------------"
    print "-----3. Capital list--------------------"
    print "-----4. Countries and Capitals----------"
    print "-----5. Countries and capitals by order-"
    print "-----6. All by mail---------------------"
    print "-----7. Exit----------------------------"
    men = raw_input("Choose an option:\n")
    men = men.lower()
    if men == "1" or men == "country":
        LIMPIAR()
        INSERT_COUNTRIES()
    elif men == "2" or men == "countries":
        LIMPIAR()
        LIST_COUNTRIES()
    elif men == "3" or men == "capitals":
        LIMPIAR()
        LIST_CAPITAL()
    elif men == "4" or men == "all":
        LIMPIAR()
        CAPITALS_AND_COUNTRIES()
    elif men == "5" or men =="allordered":
        ORDER()
    elif men == "6" or men == "allmail":
        main()
    elif men == "7":
        OUT()
    else:
        print "Choose a correct option please"
        raw_input("Press enter")
        MENU()
MENU()
