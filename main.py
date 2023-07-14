row1 = ["⬜️", "|", "⬜️", "|", "⬜️"]
row2 = ["_________________________"]
row3 = ["⬜️", "|", "⬜️", "|", "⬜️"]
row4 = ["_________________________"]
row5 = ["⬜️", "|", "⬜️", "|", "⬜️"]
board = [row1, row2, row3, row4, row5]

position_dict = {
    "tl": [0, 0],
    "tm": [0, 2],
    "tr": [0, 4],
    "ml": [2, 0],
    "mm": [2, 2],
    "mr": [2, 4],
    "bl": [4, 0],
    "bm": [4, 2],
    "br": [4, 4],
}

logo = """
___________.__         ___________               ___________            
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___     |    |(  <_> )  ___/ 
  |____|   |__|\_____>   |____|  (______/\_____>   |____| \____/ \_____>
  """

print("Welcome to the Tic Tac Toe Game.")
print(logo)
print("Game info: to place a sign in chosen position use commands: for top left 'tl', bottom right 'br' and so one.\n")
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
# Game options and settings
game_on = True
player_1_sign = "X"
player_2_sign = "0"
sign_list = ["X", "0"]
board_positions_horizontal = [[0, 0, 0, 2, 0, 4], [2, 0, 2, 2, 2, 4], [4, 0, 4, 2, 4, 4]]
board_positions_vertical = [[0, 0, 2, 0, 4, 0], [0, 2, 2, 2, 4, 2], [0, 4, 2, 4, 4, 4]]
board_positions_axis = [[0, 0, 2, 2, 4, 4], [0, 4, 2, 2, 4, 0]]
player_turn = 0
number_of_signs = 0

while game_on:
    if player_turn == 0:
        print("\nPlayer One turn")
        player_input = input("Where would you like to place sign?\n")
        board_position = position_dict[player_input]
        board[board_position[0]][board_position[1]] = player_1_sign
        print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
        player_turn += 1
        number_of_signs += 1
    else:
        print("\nPlayer Two turn")
        player_input = input("Where would you like to place sign?\n")
        board_position = position_dict[player_input]
        board[board_position[0]][board_position[1]] = player_2_sign
        print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
        player_turn -= 1
        number_of_signs += 1
    if number_of_signs >= 5:
        for sign in sign_list:
            for position in board_positions_horizontal:
                if board[position[0]][position[1]] == sign and board[position[2]][position[3]] == sign and \
                        board[position[4]][position[5]] == sign:
                    if player_1_sign == sign:
                        print(f"Player One Wins!!!")
                        game_on = False
                        break
                    else:
                        print(f"Player Two Wins!!!")
                        game_on = False
                        break
            for position in board_positions_vertical:
                if board[position[0]][position[1]] == sign and board[position[2]][position[3]] == sign and \
                        board[position[4]][position[5]] == sign:
                    if player_1_sign == sign:
                        print(f"Player One Wins!!!")
                        game_on = False
                        break
                    else:
                        print(f"Player Two Wins!!!")
                        game_on = False
                        break
            for position in board_positions_axis:
                if board[position[0]][position[1]] == sign and board[position[2]][position[3]] == sign and \
                        board[position[4]][position[5]] == sign:
                    if player_1_sign == sign:
                        print(f"Player One Wins!!!")
                        game_on = False
                        break
                    else:
                        print(f"Player Two Wins!!!")
                        game_on = False
                        break

