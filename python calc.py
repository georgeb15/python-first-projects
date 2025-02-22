#python calc
import math
print("calcuator project")
print("you can choose between \n a simple calculator, \n a rectangle calculator, \n a triangle calcuator \n a circle calculator \n and a weight conversion calculator")
calc = input("which calcuator do you want to use? ")
if calc == "simple":
    num1 = float(input('Enter first number: '))
    opertor = input('Enter operator(+-*/): ')
    num2 = float(input('Enter second number: '))
    print("if you want to add another number, type 'yes'")
    add = input("do you want to add another number? ")
    if add == "yes":
        num3 = float(input('Enter third number: '))
        result = float
    if add == "no":
        num3 = float(0)
    if opertor == '+':
        result = num1 + num2 + num3
    elif opertor == '-':
        result = num1 - num2 + num3
    elif opertor == '*':
        result = num1 * num2 + num3
    elif opertor == '/':
        result = num1 / num2 + num3
    else:
        print('Invalid operator')
    print (f'{num1} {opertor} {num2} {opertor} {num3} = {result}')
if calc == "rectangle":
    l= input("what is the length of the rectangle? ")
    w = input("what is the width of the rectangle? ")
    l = float(l)
    w = float(w)
    area = l * w
    print(f"the area of the rectangle is {area}cm²")
if calc == "circle":
    circle = input("what do you want to calculate? (diameter, circumference, area): ")
    if circle == "diameter":
        r = float(input("what is the radius of the circle? "))
        d = 2 * r
        print(f"the diameter of the circle is {d}")
    elif circle == "circumference":
        r = float(input("what is the radius of the circle? "))
        c = 2 * 3.14159 * r
        print(f"the circumference of the circle is {c}")
    elif circle == "area":
        r = float(input("what is the radius of the circle? "))
        a = 3.14159 * r ** 2
        print(f"the area of the circle is {a}")
    else:
        print("invalid input")
if calc == "triangle":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    print(f"The length of side c is {c}")
if calc == "weight":
    weight = float(input("what is the weight? "))
    unit = input("is the weight in kg or lbs? ")
    if unit == "kg":
        lbs = weight * 2.20462
        print(f"the weight is {lbs}lbs")
    elif unit == "lbs":
        kg = weight / 2.20462
        print(f"the weight is {kg}kg")
    else:
        print("invalid input")