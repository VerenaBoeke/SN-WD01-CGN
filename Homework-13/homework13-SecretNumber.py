#coding=utf8

#Imports
import json
from datetime import date

from secretnumber import secret
from topscore import get_topscore_list
from result import result


#JSON File "Highscore"
filename = "highscore.json"


#Global Variables
player = input("Tell me your Player Name: ")
numGuess = 0
wrongGuesses = 0


#Start the Game
print("Welcome to 'Guess the Secret Number' But first...")

class game():
    def __init__(self):
        self.fromNum = 1
        self.toNum = 10
        self.today = date.today()

        # The Secret Number
        self.secret = secret(self.fromNum, self.toNum)
game = game()

print(game.secret)



#Ask for guess and check about valid number
while True:
   try:
       UserGuess = int(input("Abracadabra, which number is in my mind? Tell me number between " + str(game.fromNum) + " and " + str(game.toNum) + ": "))
       numGuess = numGuess + 1
       if UserGuess < game.fromNum or UserGuess > game.toNum:
           raise ValueError
       elif int(UserGuess) == game.secret:
           print("Uh wow! That is absolutly correct. Congrats my dear!")
           break
       else:
           wrongGuesses = wrongGuesses + 1
           print("Nope! Far, far away! That is not my number!")
   except ValueError:
       print("Oops! That was no valid number. Try again...")

newGame = result(score=numGuess, player_name=player, date=str(game.today))

#Define variable für JSON File
listContent = {}
listContent['games'] = []

#Open and read JSON File
def get_score_list():
    with open(filename) as json_file:
       listContent = json.load(json_file)
    return listContent
listContent = get_score_list()

#Check Key in dict
if(not "games" in listContent):
    listContent['games'] = []

#Get content for Score List
listContent['games'].append({
   "secretnumber": game.secret,
   "date": str(newGame.date),
   "player": newGame.player_name,
   "gTotal": newGame.score,
})

#Write Infos about the session in the JSON File
with open(filename, 'w') as f:
   json.dump(listContent, f)

#Function for Top Score is imported from topscore.py
if __name__ == '__main__':
    get_topscore_list(listContent['games'])
