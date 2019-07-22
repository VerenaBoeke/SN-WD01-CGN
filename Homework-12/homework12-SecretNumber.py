#Imports
import json
import random
from datetime import date


#JSON File "Highscore"
filename = "highscore.json"


#Global Variables
fromNum = 1
toNum = 10
today = date.today()
player = input("Tell me your Player Name: ")
numGuess = 0
wrongGuesses = 0


#Start the Game
print("Welcome to 'Guess the Secret Number' But first...")


#The Secret Number
def secret(fromNum, toNum):
   secretNum = random.randint(fromNum, toNum)
   return secretNum

secret = secret(fromNum, toNum)


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


#Define variable für JSON File
listContent = {}
listContent['games'] = []


#Open and read JSON File
def get_score_list():
    with open(filename) as json_file:
       listContent = json.load(json_file)
    return listContent
listContent = get_score_list()


#Get content for Score List
listContent['games'].append({
   "secretnumber": secret,
   "date": str(today),
   "player": player,
   "gTotal": numGuess,
   "gWrong": wrongGuesses
})


#Write Infos about the session in the JSON File
with open(filename, 'w') as f:
   json.dump(listContent, f)


#Get and Print the Top Score List
def get_topscore_list(list):
   global sorted
   sorted = sorted(list, key = lambda i: i['gTotal'])
   print("Top three Players: ")
   countGames = 0

   for game in sorted:
        countGames = countGames + 1
        print("#" + str(countGames) + " " + game["player"] + " with " + str(game["gTotal"]) + " attempts.")
        if countGames == 3:
            break

get_topscore_list(listContent['games'])
