"""
User enters a number between 1 and 100
FizzBuzz program starts to count to that number (it prints them in the Terminal).
In case the number is divisible with 3, it prints "fizz" instead of the number.
If the number is divisible with 5, it prints "buzz". If it's divisible with both 3 and 5, it prints "fizzbuzz".

[x] Input for a Number
[x] Text "A number between 1 and 100"
[x] Count from 0 to the User-Number in the Terminal
[x] If the number is divisiable with 3 - Print "fizz"
[x] If the number is divisable with 5 - Print "buzz"
[x] If the number divisable with 3 _and_ 5 - Print "fizzbuzz"

[x] Prüfen ob die Zahl sich zwischen 1 und 100 befindet
[x] Prüfen ob die Eingabe eine Zahl ist
"""

while True:
    try:
        userNumber = int(input("Let`s play a game! Gimme a number between 1 and 100 and i tell you which one is a Fizz, a Buzz or a FizzBuzz: "))
        if userNumber < 1 or userNumber > 100:
            raise ValueError
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")


for number in range(1, userNumber + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz!!!!")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

print("Fertig!")

