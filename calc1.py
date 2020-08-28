#!/usr/bin/python3


print("Basic Calculator 2")
###Taking values for X & Y
x =  int(input("\nEnter a value for x: "))
y = int(input("Enter a value for y: "))
###Choosing an operation
choice = input("\nChoose from the following operations: \n'add' for addition \n'sub' for subtraction \n'div' for division \n'mul' for multiplication\n:")

###Conditions based on operation
if choice == 'add':
    print("\nYou have chosen addition!")
    print("The answer is: ", x+y)
elif choice == 'sub':
    print("\nYou have chose subtraction!")
    print("The answer is: ", x-y)
elif choice == 'div':
    print("\nYou have chosen division!")
    print("The answer is: ", x/y)
elif choice == 'mul':
    print("\nYou have chose division!")
    print("The answer is: ", x*y)
