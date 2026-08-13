import json
import random

#importing characters from json

def load_characters():
    with open("characters.json", "r") as file:
        characters = json.load(file)
    return characters

#random card selection

def choose_card(characters):
    card = random.choice(characters)
    return card

#displays who has card + info

def show_card(card, owner):
    print(owner + " card:")  
    print(card["name"])
    print("Power:", card["power"])
    print()  