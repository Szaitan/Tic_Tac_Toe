row1 = ["⬜️", "|", "⬜️", "|", "⬜️"]
row2 = ["_________________________"]
row3 = ["⬜️", "|", "⬜️", "|", "⬜️"]
row4 = ["_________________________"]
row5 = ["⬜️", "|", "⬜️", "|", "⬜️"]
board = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")

position_dict = {
    "tl": 11,
    "tm": 13,
    "tr": 15,
    "ml": 31,
    "mm": 33,
    "mr": 35,
    "bl": 51,
    "bm": 53,
    "br": 55,
}

logo = """___________.__         ___________               ___________            
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___     |    |(  <_> )  ___/ 
  |____|   |__|\_____>   |____|  (______/\_____>   |____| \____/ \_____>"""

print("Welcome to the Tic Tac Toe Game.")
print(logo)
game_on = True
player_1_sign = "X"
player_2_sign = "O"

while game_on:
    print("")