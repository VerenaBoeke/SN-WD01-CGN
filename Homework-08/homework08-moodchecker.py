"""
if the mood is "happy", the program should print out "It is great to see you happy!"
if the mood is "nervous", respond with "Take a deep breath 3 times.". Use elif to enter more if statements: elif mood == "nervous":.
Make up responses also for "sad", "excited" and "relaxed".
The last option should be the normal else, which responds with "I don't recognize this mood".
"""

def moodChecker():
    feeling = input("Enter your actual Mood. Are you 'happy', 'nervous'. 'sad', 'excited' or 'relaxed': ")
    return feeling

mood = moodChecker()

if mood == "happy":
    print(":-) It is great to see you happy!")
elif mood == "nervous":
    print(":-/ Take a deep breath 3 times.")
elif mood == "sad":
    print(":.-( Sorry to hear that! Make yourself a present: A litte bit 'Me-Time' Hope to see you feel better soon...")
elif mood == "excited":
    print(":-D Oh really!? Thats awesome to hear!")
elif mood == "relaxed":
    print(" = ^.^ = That's purrrfect! That is an pawsome mood, i like that very well.")
else:
    print("I don't recognize this mood")