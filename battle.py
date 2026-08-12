#battle logic

def battle_cards(player_card, computer_card):

    if player_card["power"] > computer_card["power"]:
        print("You win!")
    elif player_card["power"] < computer_card["power"]:
        print("Computer wins...")
    else:
        print("It's a draw...")        
