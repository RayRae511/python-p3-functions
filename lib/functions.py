#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
greet_programmer()    

def greet(name = 'Guest'):
    pass
    print(f'Hello, {name}')
greet()

def greet_with_default(name = "programmer"):
    pass
    print(f'Hi there {name}')
greet_with_default()
    
def add(num1, num2):
    pass
    return num1 + num2
add(34, 35)
# 69

def halve(number):
    pass
    return number / 2
halve(420)
#420