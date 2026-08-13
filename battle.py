#battle logic

def battle_cards(player_card, computer_card, stat):

    player_value = player_card[stat]
    computer_value = computer_card[stat]

    print("Battle stat:", stat)
    print("Your value", player_value)
    print("Computer value", computer_value)

    if player_value > computer_value:
        print("You win!")
    elif player_value < computer_value:
        print("Computer wins...")
    else:
        print("It's a draw...")        
