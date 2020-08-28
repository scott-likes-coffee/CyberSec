#!/usr/bin/python3
# create dictionary with credentials
logindic = {'scott':'scooby', 'sarah':'remy', 'katie':'brixton'}
#set count to 0
count = 0
#create boolean for flag
login = False
#create while loop for iteration
while login == False:
#take iput
    user = input("\nPlease enter your username: ")
    pwd = input("Please enter your password: ")
#start count
    count += 1
#stop loop if count ==3
    if count == 3:
        print("You have tried too many times. Goodbye.")
        break
#if count does not == 3, compare x to its value in logindic
    else:
       for x in logindic.keys():
            if x == user and pwd == logindic[x]:
                print("\nLogin Success")
                login == True
                break
#if creds don't match, print failure and start loop again
    if login == False:
        print("\nLogin Failure. Try again")
#break loop
    break
