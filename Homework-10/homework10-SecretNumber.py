"""
HW 11.1: Add some more data in the dictionary
[X] Save number of attempts and the date
[X] Save the Players Name an the secret number in each game

HW 11.2: Add unsuccessful guesses into the dictionary
[X] Save the unsuccessful guesses
[X] Store the unsuccessful guesses in the dictionary ("wrong_guesses")

HW 11.3: Print out only the top 3 results
[X] Find a way to sort the scores ("score_lost.sort()" doesn`t work with dictionarys)

"""
import json
import random

filename = "highscore.json"

fromNum = 1
toNum = 10


print("Welcome to 'Guess the Secret Number' But first...")

#The Secret Number
secret = random.randint(fromNum, toNum)

#The Date
from datetime import date
today = date.today()

#The Players Name
player = input("Tell me your Player Name: ")

#Guess Number
numGuess = 0

#Wrong Guess Number
wrongGuesses = 0

#Ask for guess and check about valid number
while True:
    try:
        UserGuess = int(input("Abracadabra, which number is in my mind? Tell me number between " + str(fromNum) + " and " + str(toNum) + ": "))
        numGuess = numGuess + 1
        if UserGuess < fromNum or UserGuess > toNum:
            raise ValueError
        elif int(UserGuess) == secret:
            print("Uh wow! That is absolutly correct. Congrats my dear!")
            break
        else:
            wrongGuesses = wrongGuesses + 1
            print("Nope! Far, far away! That is not my number!")
    except ValueError:
        print("Oops! That was no valid number. Try again...")

listContent = {}
listContent['games'] = []

with open(filename) as json_file:
    listContent = json.load(json_file)

listContent['games'].append({
    "secretnumber": secret,
    "date": str(today),
    "player": player,
    "gTotal": numGuess,
    "gWrong": wrongGuesses
})

with open(filename, 'w') as f:
    json.dump(listContent, f)

sorted = sorted(listContent['games'], key = lambda i: i['gTotal'])

print("Top three Players: ")

countGames = 0

for game in sorted:
    countGames = countGames + 1
    print("#" + str(countGames) + " " + game["player"] + " with " + str(game["gTotal"]) + " attempts.")
    if countGames == 3:
        break