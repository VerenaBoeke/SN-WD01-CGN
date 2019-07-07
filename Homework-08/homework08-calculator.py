"""
Homework 7.3: Calculator

Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""


def getNumber(pos):
    num = input("Enter number {}: ".format(pos))
    if num == "":
        num = getNumber(pos)
    return num

num01 = getNumber("01")

num02 = getNumber("02")

inputtxt = "Which arithemtic operation you wanna use? ('+', '-', '*' or '/'): "

ao = input(inputtxt)

result = 0


if ao == "+":
    result = float(num01) + float(num02)
elif ao == "-":
    result = float(num01) - float(num02)
elif ao == "*":
    result = float(num01) * float(num02)
elif ao == "/":
    if num02 == "0":
        result = "Error"
    else:
        result = float(num01) / float(num02)
else:
    result = "Error"

print(result)