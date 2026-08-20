import tkinter as tk
from card import load_characters, choose_card

characters = load_characters()

player_card = choose_card(characters)



window = tk.Tk()

window.title("Spider-Gent: A Card Game")
window.geometry("800x600")

title_label = tk.Label(window, text="Spider-Gent and the nefarious criminals of New Bristol")
title_label.pack()

card_image = tk.PhotoImage(
    file=player_card["image"]
)
card_image = card_image.subsample(4, 4)

cards_container = tk.Frame(window)
cards_container.pack()

player_card_frame = tk.Frame(
    cards_container,
    bg="#e8e0d0",
    bd=3,
    relief="solid",
    padx=20,
    pady=20
)

player_card_frame.pack(
    side="left",
    padx=20
)

computer_card_frame = tk.Frame(
    cards_container,
    bg="#d3d3d3",
    bd=3,
    relief="solid",
    padx=20,
    pady=20
)

computer_card_frame.pack(
    side="left",
    padx=20
)

computer_title_label = tk.Label(
    computer_card_frame,
    text="Computer Card",
    font=("Ariel", 10, "bold"),
    bg="#d3d3d3"
)
computer_title_label.pack()
card_name_label = tk.Label(
    player_card_frame, 
    text=player_card["name"], 
    font=("Arial", 20, "bold"),
    bg="#e8e0d0"
    )
card_name_label.pack()

computer_image_label = tk.Label (
    computer_card_frame,
    text="[HIDDEN]",
    width=25,
    height=8,
    relief="solid"
)
computer_image_label.pack(pady=10)

computer_power_label = tk.Label(
    computer_card_frame,
    text="Power: ???",
    bg="#d3d3d3"
)

computer_speed_label = tk.Label(
    computer_card_frame,
    text="Speed: ???",
    bg="#d3d3d3"
)

computer_intelligence_label = tk.Label(
    computer_card_frame,
    text="Intelligence = ???",
    bg="#d3d3d3"
)

content_frame = tk.Frame(
    player_card_frame,
    bg="#e8e0d0"
)
content_frame.pack(pady=10)

image_frame = tk.Frame(
    content_frame,
    bg="#e8e0d0"
)
image_frame.pack(side="left",padx=10)

stats_frame = tk.Frame(
    content_frame,
    bg="#e8e0d0"
)
stats_frame.pack(side="right", padx=10)

image_label= tk.Label(
    image_frame,
    image=card_image
)

image_label.pack(pady=10)

power_label = tk.Label(
    stats_frame, 
    text=f"Power: {player_card['power']}",
    font=("Ariel", 10, "bold"),
    bg="#e8e0d0"
    )
power_label.pack(anchor="w")

speed_label = tk.Label(
    stats_frame, 
    text=f"Speed: {player_card['speed']}",
    font=("Ariel", 10, "bold"),
    bg="#e8e0d0"
    )
speed_label.pack(anchor="w")

intelligence_label = tk.Label(
    stats_frame, 
    text=f"Intelligence: {player_card['intelligence']}",
    font=("Ariel", 10, "bold"),
    bg="#e8e0d0"
    )
intelligence_label.pack(anchor="w")

info_label = tk.Label(
    stats_frame, 
    text=player_card["info"],
    font=("Ariel", 6, "italic"),
    bg="#e8e0d0"
    )
info_label.pack()

display_card(player_card)

def deal_new_card():

    new_card = choose_card(characters)
    display_card(new_card)
    

   
    
    

def display_card(card):
    card_name_label.config(
        text=new_card["name"]
        )
    info_label.config(
        text=new_card["info"]
        )
    power_label.config(
        text=f"Power: {new_card['power']}"
        )
    speed_label.config(
        text=f"Speed: {new_card['speed']}"
        )
    intelligence_label.config(
        text=f"Intelligence: {new_card["intelligence"]}"
        )
    new_image = tk.PhotoImage(
        file=new_card["image"]
        )
    new_image = new_image.subsample(4, 4)
    
    image_label.config(
        image=new_image
        )
    image_label.image = new_image #this keeps the image in memory

deal_button = tk.Button(
    window,
    text="Deal New Card",
    command=deal_new_card
)  
deal_button.pack(pady=10)  

window.mainloop()
