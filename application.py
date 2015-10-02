import os
import sys

CAP_AND_COUN = {}
CAPITALS = []
COUNTRIES = []
def CAPITALS_AND_COUNTRIES():
    """Here shows the capitals and countries"""
    print CAP_AND_COUN
    raw_input("Press enter")
    LIMPIAR()
    MENU()
def LIST_CAPITAL():
    """Here shows the list of the capitals"""
    print CAPITALS
    raw_input("Press enter")
    LIMPIAR()
    MENU()
def LIST_COUNTRIES():
    """Here Shows the list of the Countries"""
    print COUNTRIES
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
            if str(country).isalpha() == True:
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
            if str(country).isalpha() == True:
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
def MENU():
    """This is the menu that the user watch"""
    LIMPIAR()
    print "1. Insert a country"
    print "2. Countries list"
    print "3. Capital list"
    print "4. Countries and Capitals"
    print "5. Countries and capitals by order"
    print "6. All by mail"
    print "7. Exit"
    men = raw_input("Choose an option\n")
    if men == "1":
        LIMPIAR()
        INSERT_COUNTRIES()
    elif men == "2":
        LIST_COUNTRIES()
    elif men == "3":
        LIST_CAPITAL()
    elif men == "4":
        CAPITALS_AND_COUNTRIES()
    else:
        print "Choose a correct option please"
        raw_input("Press enter")
        MENU()
MENU()
