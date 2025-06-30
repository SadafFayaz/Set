"""
Enter in this format ---

first number: eg - 5
operator: eg = +
second number: eg - 20
"""

"""
Try running it on your local compiler, and see the magic --
upvote if you like the code@ and please feel free to correct me, i know the code is not that clean
"""

import time
import sys

"""
import os
import platform
"""
def sleep():
    time.sleep(0.95)
    
def menu():
    print("Enter one of these options below--\n")
    print("1 - Add(+):\n")
    sleep()
    print("2 - Subtract(-):\n")
    sleep()
    print("3 - Multiply(*):\n")
    sleep()
    print("4 - Divide(/):\n")
    sleep()
    print("0 - Exit(0):\n\n")
    sleep()
    
#running = False

#addition
def add(x, y):
    return x + y

#subtraction
def sub(x, y):
    return x - y
    
#multiplecation
def mul(x, y):
    return x * y
    
#division
def div(x, y):
    if y == 0:
        print('Error: Cannot divide by 0')
        sys.exit(0)
    else:
        return x / y
        
def main():
    menu()
    x = int(input("Enter the first number: "))
    op = str(input("Enter the operator: "))
    y = int(input("Enter the second number: "))
    if op == '1' or op == '+':
        print(f"{x} + {y} is {add(x, y)}\n")
    elif op == '2' or op == '-':
        print(f"{x} - {y} is {sub(x, y)}\n")
    elif op == '3' or op == '*' or op == '×':
        print(f"{x} * {y} is {mul(x, y)}\n")
    elif op == '4' or op == '/' or op == '÷':
        print(f"{x} ÷ {y} is {div(x, y)}\n")
    elif op == '0' or op == 'Exit':
        print("Exitting...")
        sys.exit(0)
        
main()