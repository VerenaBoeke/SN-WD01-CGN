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