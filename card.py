import json
import random


def load_characters(): #importing characters from json
    with open("characters.json", "r") as file:
        characters = json.load(file)
    return characters


def choose_card(characters): #random card selection
    card = random.choice(characters)
    return card


def show_card(card, owner): #displays who has card + info
    print(owner + " card:")  
    print(card["name"])
    print("Power:", card["power"])
    print("Speed", card["speed"])
    print("Intelligence:", card["intelligence"])
    print()  