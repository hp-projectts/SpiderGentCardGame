#COMIC BOOK INSPIRED CARD GAME W/ GOTHIC AESTHETIC
import random
#CHARACTER LIST
characters = [
    {"name": "Spider-Gent",
     "power": 88},
    {"name": "Percival Parkinson",
     "power": 19},
    {"name": "Dr Ignatius Eel",
     "power": 80},
    {"name": "Baron the Hunter",
     "power": 75}
]
player_card = random.choice(characters)
computer_card = random.choice(characters)

print("Your card:")
print(player_card["name"])
print("Power", player_card["power"])

print()

print("Computer card:")
print(computer_card["name"])
print("Power", computer_card["power"])
