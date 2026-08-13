#COMIC BOOK INSPIRED CARD GAME W/ GOTHIC AESTHETIC
from card import load_characters, choose_card, show_card
from battle import battle_cards


characters = load_characters() #run load_characters function from card.py and assigns characters to variable 

player_card = choose_card(characters)
characters.remove(player_card)
computer_card = choose_card(characters)  #randomly assigns player/computer card using choose card function

show_card(player_card, "Your")

valid_stats = ["power","speed", "intelligence"]

chosen_stat = input("Choose a stat (power, speed, intelligence): ").lower()

while chosen_stat not in valid_stats:
    print("Invalid stat")
    chosen_stat = input("Choose again:").lower()
print()
show_card(computer_card, "Computer")

battle_cards(player_card, computer_card, chosen_stat)







