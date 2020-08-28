#!/usr/bin/python3
#import getpass function
import getpass
#create dictionary with credentials
logindic = {'scott':'bucket', 'katie':'brixton', 'sean':'shadow'}

#take user input
user = input("\nPlease enter your username: ")

#set count to 0 and login = False
count = 0
login = False
# if x in dictionary and pwd matches x, login success
for x in logindic.keys():
    if x == user:
    pwd = getpass.getpass(prompt= "Please enter your password: ")
        if pwd == logindic[x]:
            print("\nLogin successful")
            print("Welcome " + user)
#login becomes true
            login = True
#break loop
            break
#else while count <5 print credentials & login fail message
    else:
        while(count <5):
            if login == False:
                print("\Username: " + user)
                print("Password: " + pwd)
                print("Login failed. Please try again")
# add 1 to count
                count += 1
#take input again
                user = input("\nPlease enter your username: ")
#restart loop
