#!/usr/bin/python3
# define funtions for operation
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
# define function for main menu
def main():
    print("Basic Calculator 2!")
    x = int(input("\nChoose an integer for X: "))
    y = int(input("Choose an integer for y: "))
    choice = input("\nChoose from the following operations: \n'add' \n'sub' \n'mul' \n'div'\n \n: ")
# operation for addition
    if choice == 'add':
        answer = addition(x,y)
        print("\nYou have chosen addition!")
        print("Your answer is : ", answer)
# operation for subtraction
    elif choice == 'sub':
        answer = subtraction(x,y)
        print("\nYou have chosen subtraction!")
        print("Your answer is: ", answer)
# operation for multiplication
    elif choice == 'mul':
        answer = multiplication(x,y)
        print("\nYou have chosen multiplication!")
        print("Your answer is: ", answer)
# operation for division
    elif choice == 'div':
        answer = division(x,y)
        print("\nYou have chose division!")
        print("Your answer is: ", answer)
# else, tell user to input an operation from the menu
    else:
        print("Please choose an operation from the menu.")
main()

