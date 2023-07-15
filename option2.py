import random
board = 9 * ["⬜️"]
position_dict = {
    "tl": 0,
    "tm": 1,
    "tr": 2,
    "ml": 3,
    "mm": 4,
    "mr": 5,
    "bl": 6,
    "bm": 7,
    "br": 8,
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
sign_list = ["x", "o"]
board_positions_horizontal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
board_positions_vertical = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
board_positions_axis = [[0, 4, 8], [2, 4, 6]]


def board_visualisation():
    print(f" {board[0]} | {board[1]} | {board[2] }")
    print("_______________")
    print(f" {board[3]} | {board[4]} | {board[5] }")
    print("_______________")
    print(f" {board[6]} | {board[7]} | {board[8] }")


def human_vs_human():
    player_turn = 0
    number_of_signs = 0
    list_with_players_choices = []
    board_visualisation()

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
                board[board_position] = 'x'
                board_visualisation()
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
                board[board_position] = "o"
                board_visualisation()
                player_turn -= 1
                number_of_signs += 1

        if number_of_signs >= 5:
            for sign in sign_list:
                for position in board_positions_horizontal:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nPlayer Two Wins!!!")
                        game_human_continue_decision()

                for position in board_positions_vertical:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nPlayer Two Wins!!!")
                        game_human_continue_decision()

                for position in board_positions_axis:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nPlayer Two Wins!!!")
                        game_human_continue_decision()

                if number_of_signs == 9:
                    print("It's a draw.")
                    game_on = False
                    game_human_continue_decision()


def human_vs_computer():

    player_turn = 0
    number_of_signs = 0
    list_with_players_choices = []
    board_visualisation()

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
                board[board_position] = 'x'
                board_visualisation()
                player_turn += 1
                number_of_signs += 1
                print("\nComputer turn")
        else:
            computer_choice = random.choice(list(position_dict.items()))
            print(computer_choice[0])
            if computer_choice in list_with_players_choices:
                continue
            else:
                list_with_players_choices.append(computer_choice)
                board_position = position_dict[computer_choice[0]]
                board[board_position] = "o"
                board_visualisation()
                player_turn -= 1
                number_of_signs += 1

        if number_of_signs >= 5:
            for sign in sign_list:
                for position in board_positions_horizontal:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nComputer Wins!!!")
                        game_computer_continue_decision()

                for position in board_positions_vertical:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nComputer Wins!!!")
                        game_computer_continue_decision()

                for position in board_positions_axis:
                    if board[position[0]] == sign and board[position[1]] == sign and board[position[2]] == sign:
                        if sign == "x":
                            print(f"Player One Wins!!!")
                        else:
                            print(f"\nComputer Two Wins!!!")
                        game_computer_continue_decision()

                if number_of_signs == 9:
                    print("It's a draw.")
                    game_on = False
                    game_computer_continue_decision()


def game_human_continue_decision():
    global game_on, board
    game_cont_decision = input("Would you like to play another game? Type 'Y' to continue or 'N' "
                               "to finish.\n")
    if game_cont_decision.lower() == 'y':
        board.clear()
        board = 9 * ["⬜️"]
        human_vs_human()
    else:
        game_on = False


def game_computer_continue_decision():
    global game_on, board
    game_cont_decision = input("Would you like to play another game? Type 'Y' to continue or 'N' "
                               "to finish.\n")
    if game_cont_decision.lower() == 'y':
        board.clear()
        board = 9 * ["⬜️"]
        human_vs_computer()
    else:
        game_on = False


if game_mode.lower() == 'h':
    human_vs_human()
elif game_mode.lower() == 'c':
    human_vs_computer()
else:
    print("Wrong game option. Try again.")
