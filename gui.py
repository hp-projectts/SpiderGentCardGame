import tkinter as tk
from card import load_characters, choose_card

#LOAD GAME DATA

characters = load_characters()
player_card = choose_card(characters)

# CREATE MAIN WINDOW

window = tk.Tk()

window.title("Mr Arachnid & the Fiends of New Bristol: A Card Game")
window.geometry("1200x700")

#CARDS CONTAINER

cards_container = tk.Frame(window)
cards_container.pack(
    pady=20
)

#PLAYER CARD

player_card_frame = tk.Frame(
    cards_container,
    bg="#e8e0d0",
    bd=3,
    relief="solid",
    width=600,
    height=550,
)

player_card_frame.pack(
    side="left",
    padx=10
)

player_card_frame.pack_propagate(False)

#This frame holds images and stats side by side
content_frame = tk.Frame(
    player_card_frame,
    bg="#e8e0d0",
)
content_frame.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=10)


#Player image area
image_frame = tk.Frame(
    content_frame,
    bg="#e8e0d0",
)
image_frame.pack(
    side="left",
    padx=5
)
card_image = tk.PhotoImage(
    file=player_card["image"]
)

card_image = card_image.subsample(3, 3)

image_label= tk.Label(
    image_frame,
    image=card_image
)

image_label.pack()

#Player stats area
stats_frame = tk.Frame(
    content_frame,
    bg="#e8e0d0"
)
stats_frame.pack(
    side="right",
    fill="both",
    expand=True, 
    padx=10
)

card_name_label = tk.Label(
    stats_frame, 
    text=player_card["name"], 
    font=("Arial", 16, "bold"),
    bg="#e8e0d0"
    )
card_name_label.pack(
    anchor="n",
    pady=(30, 120)
)

power_label = tk.Label(
    stats_frame, 
    text=f"Power: {player_card['power']}",
    font=("Arial", 16, "bold"),
    bg="#e8e0d0"
    )
power_label.pack(anchor="w")

speed_label = tk.Label(
    stats_frame, 
    text=f"Speed: {player_card['speed']}",
    font=("Arial", 16, "bold"),
    bg="#e8e0d0"
    )
speed_label.pack(anchor="w")

intelligence_label = tk.Label(
    stats_frame, 
    text=f"Intelligence: {player_card['intelligence']}",
    font=("Arial", 16, "bold"),
    bg="#e8e0d0"
    )
intelligence_label.pack(anchor="w")

#Player card info area

info_label = tk.Label(
    stats_frame, 
    text=player_card["info"],
    font=("Arial", 8, "italic"),
    bg="#e8e0d0",
    wraplength=200,
    justify="center"
    )
info_label.pack(pady=(30, 0))









# COMPUTER CARD


computer_card_frame = tk.Frame(
    cards_container,
    bg="#d3d3d3",
    bd=3,
    relief="solid",
    width=670,
    height=550,
)

computer_card_frame.pack(
    side="left",
    padx=10
)

computer_card_frame.pack_propagate(False)

#This frame holds images and stats side by side
computer_content_frame = tk.Frame(
    computer_card_frame,
    bg="#d3d3d3",
)
computer_content_frame.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=10
    )

#Computer image area

computer_image_frame = tk.Frame(
    computer_content_frame,
    bg="#d3d3d3",
)
computer_image_frame.pack(
    side="left",
    padx=5
)

computer_image_label = tk.Label (
    computer_image_frame,
    text="[HIDDEN]",
    font=("Arial", 20),
    width=18,
    height=35,
    relief="solid",
)
computer_image_label.pack(pady=10)

#Computer stats area

computer_stats_frame = tk.Frame(
    computer_content_frame,
    bg="#d3d3d3"
)
computer_stats_frame.pack(
    side="right",
    fill="both",
    expand=True, 
    padx=10
)

computer_title_label = tk.Label(
    computer_stats_frame,
    text="Computer Card",
    font=("Ariel", 18, "bold"),
    bg="#d3d3d3"
)
computer_title_label.pack(
    anchor="n",
    pady=(30, 120)
)

computer_power_label = tk.Label(
    computer_stats_frame,
    text="Power: ???",
    font=("Arial", 16, "bold"),
    bg="#d3d3d3"
)
computer_power_label.pack(anchor="w")

computer_speed_label = tk.Label(
    computer_stats_frame,
    text="Speed: ???",
    font=("Arial", 16, "bold"),
    bg="#d3d3d3"
)
computer_speed_label.pack(anchor="w")

computer_intelligence_label = tk.Label(
    computer_stats_frame,
    text="Intelligence = ???",
    font=("Arial", 16, "bold"),
    bg="#d3d3d3"
)
computer_intelligence_label.pack(anchor="w")

#Computer card info

computer_info_label = tk.Label(
    computer_stats_frame, 
    text="????????????????????????????????????????????????????????",
    font=("Arial", 8, "italic"),
    bg="#d3d3d3",
    wraplength=200,
    justify="center"
    )
computer_info_label.pack(pady=(30, 0))

# FUNCTIONS 

#~~~~~~GO FROM HERE~~~~~~












def deal_new_card():

    new_card = choose_card(characters)
    display_card(new_card)

   
    
    

def display_card(card):
    card_name_label.config(
        text=card["name"]
        )
    info_label.config(
        text=card["info"]
        )
    power_label.config(
        text=f"Power: {card['power']}"
        )
    speed_label.config(
        text=f"Speed: {card['speed']}"
        )
    intelligence_label.config(
        text=f"Intelligence: {card['intelligence']}"
        )
    new_image = tk.PhotoImage(
        file=card["image"]
        )
    new_image = new_image.subsample(3, 3)
    
    image_label.config(
        image=new_image
        )
    image_label.image = new_image #this keeps the image in memory

display_card(player_card)

deal_button = tk.Button(
    window,
    text="Deal New Card",
    command=deal_new_card
)  
deal_button.pack(pady=10)  

window.mainloop()
