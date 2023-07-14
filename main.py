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
game_mode = input("\nPlease chose game type: human vs human press 'h' or human vs computer press 'c'.\n")

# Game options and settings
game_on = True
player_1_sign = "X"
player_2_sign = "0"
sign_list = ["X", "0"]
board_positions_horizontal = [[0, 0, 0, 2, 0, 4], [2, 0, 2, 2, 2, 4], [4, 0, 4, 2, 4, 4]]
board_positions_vertical = [[0, 0, 2, 0, 4, 0], [0, 2, 2, 2, 4, 2], [0, 4, 2, 4, 4, 4]]
board_positions_axis = [[0, 0, 2, 2, 4, 4], [0, 4, 2, 2, 4, 0]]


def human_vs_human():
    player_turn = 0
    number_of_signs = 0
    list_with_players_choices = []
    print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
    global game_on
    while game_on:
        if player_turn == 0:
            print("\nPlayer One turn")
            player_input = input("Where would you like to place sign?\n")
            if player_input not in position_dict:
                print("Please chose location according to the game information.\n"
                      "Game info: to place a sign in chosen position use commands:"
                      " for top left 'tl', bottom right 'br' and so one.")
                continue
            elif player_input in list_with_players_choices:
                print("Please chose other position that wasn't taken")
                continue
            else:
                list_with_players_choices.append(player_input)
                board_position = position_dict[player_input]
                board[board_position[0]][board_position[1]] = player_1_sign
                print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
                player_turn += 1
                number_of_signs += 1
        else:
            print("\nPlayer Two turn")
            player_input = input("Where would you like to place sign?\n")
            if player_input not in position_dict:
                print("Please chose location according to the game information.\n"
                      "Game info: to place a sign in chosen position use commands:"
                      " for top left 'tl', bottom right 'br' and so one.")
                continue
            elif player_input in list_with_players_choices:
                print("Please chose other position that wasn't taken")
                continue
            else:
                list_with_players_choices.append(player_input)
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
                        else:
                            print(f"\nPlayer Two Wins!!!")
                        game_continue_decision()

                for position in board_positions_vertical:
                    if board[position[0]][position[1]] == sign and board[position[2]][position[3]] == sign and \
                            board[position[4]][position[5]] == sign:
                        if player_1_sign == sign:
                            print(f"\nPlayer One Wins!!!")
                        else:
                            print(f"Player Two Wins!!!")
                        game_continue_decision()

                for position in board_positions_axis:
                    if board[position[0]][position[1]] == sign and board[position[2]][position[3]] == sign and \
                            board[position[4]][position[5]] == sign:
                        if player_1_sign == sign:
                            print(f"Player One Wins!!!")
                        else:
                            print(f"Player Two Wins!!!")
                        game_continue_decision()

                if number_of_signs == 9:
                    print("It's a draw.")
                    game_on = False
                    game_continue_decision()


def game_continue_decision():
    global game_on, row1, row3, row5, board
    game_cont_decision = input("Would you like to play another game? Type 'Y' to continue or 'N' "
                               "to finish.\n")
    if game_cont_decision.lower() == 'y':
        row1 = ["⬜️", "|", "⬜️", "|", "⬜️"]
        row3 = ["⬜️", "|", "⬜️", "|", "⬜️"]
        row5 = ["⬜️", "|", "⬜️", "|", "⬜️"]
        board = [row1, row2, row3, row4, row5]
        human_vs_human()
    else:
        game_on = False


if game_mode.lower() == 'h':
    human_vs_human()
