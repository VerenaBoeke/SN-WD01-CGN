import json

filename = "basketball_players.txt"


class basketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, mpg, ppg, team):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.mpg = mpg  #Minuten pro Spiel
        self.ppg = ppg #Punkte pro Spiel
        self.team = team #NBA Team Abkürzungen z.B. BOS für Bosten Celtics

print("Tell me something about your Fantasy Basketball Team. Who's in...")

f_name = input("What is the first name: ")
l_name = input("Tell me the last name: ")
height = input("How tall or small is he/she (in cm): ")
weight = input("Tell me the weight of the player (in kg): ")
mpg = input("Enter the Time, your Player was in the game in this season: ")
ppg = input("How many Points earnd your Player this Season: ")
team = input("In which Team plays your Player right now? (Short Version) ")

player = basketballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
    mpg=int(mpg), ppg=int(ppg), team=team)

listContent = {}

#Open and read JSON File
def get_player_list():
    with open(filename) as json_file:
       listContent = json.load(json_file)
    return listContent
listContent = get_player_list()

#Check Key in dict
if(not "players" in listContent):
    listContent['players'] = []

#Get content for Score List
listContent['players'].append({
    "Name: ": player.first_name,
    "Last Name: ": player.last_name,
    "Height: ": float(player.height_cm),
    "Weight: ": float(player.weight_kg),
    "MPG: ": int(player.mpg),
    "PPG: ": int(player.ppg),
    "Team: ": player.team
})

#Write all Data
with open(filename, 'w') as f:
   json.dump(listContent, f)

print("You`ve got a new Player in your Team! Congrats!")
print("Player's data: {0}".format(listContent))