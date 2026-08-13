#COMIC BOOK INSPIRED CARD GAME W/ GOTHIC AESTHETIC
from card import load_characters, choose_card, show_card
from battle import battle_cards

player_score = 0
computer_score = 0

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

winner = battle_cards(player_card, computer_card, chosen_stat)

if winner == "player":
    player_score += 1
elif winner == "computer":
    computer_score += 1

print("Score")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")        





