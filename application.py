"""This program store the countries and the capitals"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from collections import OrderedDict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
CAP_AND_COUN = {}
CAPITALS = []
COUNTRIES = []
ORDERED_LIST = {}
A = "Countries"
B = "Capitals"
import smtplib, getpass
def email():
    """this function send the to the email"""
    limpiar()
    print "This are your Countries and capital that you will send:"
    print ""
    print A.center(20, "="), B.center(20, "=")
    for i in CAP_AND_COUN:
        print i.center(20), CAP_AND_COUN[i].center(20)
    print ""
    print "Send email by gmail\n"
    try:
        fromaddr = raw_input("Count from gmail: ")
        password = getpass.getpass("Password: ")
        toaddrs = raw_input("to: ")
        print "Sending message..."
        body = "Countries\t==========\tCapitals\n"
        for msg in CAP_AND_COUN:
            body = body + str(msg).center(15)+":"+ str(CAP_AND_COUN[msg]).rjust(30) + "\n"
        msg = MIMEMultipart()
        msg['From'] = fromaddr #This saves the mail of the sender
        msg['To'] = toaddrs  #This saves the mail of the receiver
        msg['Subject'] = "Countries and Capitals"  #This saves the subject
        msg.attach(MIMEText(body, 'plain')) #This saves the message
    except TypeError:
        raw_input("Error please try again")
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        raw_input("Message sended")
        menu()
    except Exception as inst:
        raw_input("ups, we find an error, try again")
        email()

def order():
    """This function order the capitals"""
    limpiar()
    ordered = OrderedDict(sorted(CAP_AND_COUN.items(), key=lambda x: x[1:]))
    print A.center(20, "="), B.center(20, "=")
    for key, value in ordered.items():
        print key.center(20), value.center(20)
        ORDERED_LIST[key] = value
    raw_input("press enter")
    menu()
def capitalandcountries():
    """Here shows the capitals and countries"""
    print A.center(20, "="), B.center(20, "=")
    for i in CAP_AND_COUN:
        print i.center(20), CAP_AND_COUN[i].center(20)
    raw_input("Press enter")
    limpiar()
    menu()
def listcapital():
    """Here shows the list of the capitals"""
    print B.center(20, "=")
    for i in CAPITALS:
        print i.center(20)
    raw_input("Press enter")
    limpiar()
    menu()
def listcountries():
    """Here Shows the list of the Countries"""
    print A.center(20, "=")
    for i in COUNTRIES:
        print i.center(20)
    raw_input("Press enter")
    limpiar()
    menu()
def quest():
    """This function ask the user if he wants to insert another Country and Capital"""
    ans = raw_input("Do you want to insert another Country? y/n\n")
    ans = ans.lower()
    if ans == "y" or ans == "yes":
        insertcountries()
    elif ans == "n" or ans == "no":
        limpiar()
        menu()
    else:
        print "Choose a correct option"
        raw_input("Press enter")
        limpiar()
        quest()
def insertcountries():
    """Here the user insert the Country and the Capital"""
    try:
        coun = True
        while coun == True:
            country = raw_input("Insert a Country\n")
            country = country.capitalize()
            for character in country:
                if character.isdigit() == False:
                    coun = False
                else:
                    print "write only words n.n"
                    raw_input("Press enter")
                    coun = True
                    limpiar()
                    break
        COUNTRIES.append(country)
        cap = True
        while cap == True:
            capital = raw_input("Insert a Capital\n")
            capital = capital.capitalize()
            for character in capital:
                if character.isdigit() == False:
                    cap = False
                else:
                    print "write only words n.n"
                    raw_input("Press enter")
                    cap = True
                    limpiar()
                    break
        CAPITALS.append(capital)
    except ValueError:
        print "Insert a valid option"
    CAP_AND_COUN[country] = capital
    print CAP_AND_COUN
    limpiar()
    quest()
def limpiar():
    """This function cleans the screen"""
    os.system("cls")
    os.system("clear")
def out():
    """This function exit the program"""
    sys.exit()
def menu():
    """This is the menu that the user watch"""
    limpiar()
    print "Welcome to Captials and Countries".center(40, "=")
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
        limpiar()
        insertcountries()
    elif men == "2" or men == "countries":
        limpiar()
        listcountries()
    elif men == "3" or men == "capitals":
        limpiar()
        listcapital()
    elif men == "4" or men == "all":
        limpiar()
        capitalandcountries()
    elif men == "5" or men == "allordered":
        order()
    elif men == "6" or men == "allmail":
        email()
    elif men == "7":
        out()
    else:
        print "Choose a correct option please"
        raw_input("Press enter")
        menu()
menu()

