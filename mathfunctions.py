import math
pi = float(math.pi)

def triangleArea(b, h):
    return (1/2)*b*h

def squareArea(b, h):
    return b*h

def circleArea(r):
    a = pi * r ** 2
    return round(a, 2)

def ConsoleText():
    while True:
        print("Welcome to the Area Calculator!")
        print("Pick a shape")
        print("1. Triangle")
        print("2. Square")
        print("3. Circle")
        print("4. Exit")
        answer = input("Type your number here: ")     
        if answer == "1":
            base = int(input("What is the base? "))
            height = int(input("What is the height? "))
            area = triangleArea(base, height)   
            print(f"The triange is {area} units in size!")
        elif answer == "2":
            base = int(input("What is the base? "))
            height = int(input("What is the height? "))
            area = squareArea(base, height)   
            print(f"The square is {area} units in size!")
        elif answer == "3":
            radius = int(input("What is the radius of the circle? "))
            area = circleArea(radius)
            print(f"Your circle is {area} units!")
        elif answer == "4":
            exit()
        else: 
            print("Invalid Number, try again.")
            
ConsoleText()