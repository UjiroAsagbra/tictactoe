from bts import draw_board, check_turn, check_for_win
import os

spots = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

player1_name = input(("Enter Player 1's name: "))
player2_name = input(("Enter Player 2's name: "))
playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # RESET THE SCREEN
    os.system('cls' if os.name == 'nt' else 'clear')
    if check_turn(turn) == "X":
        current_player_name = player2_name
    else:
        current_player_name = player1_name
    draw_board(spots)
    #IF AN INVALID TURN OCCURS, LET PLAYER KNOW
    if prev_turn == turn:
        print('Invalid spot selected, please pick another.')
    prev_turn = turn
    print(current_player_name + "'s turn: Pick your spot or press q to quit")
    # GET INPUT FROM PLAYERS
    choice = input()
    if choice == 'q':
        playing = False
        #CHECKS IF THE PLAYER GAVE A NUMBER FROM 1 - 9
    elif str.isdigit(choice) and int(choice) in spots:
        #CHECK IF THE SPOT HAS BEEN TAKEN
        if not spots[int(choice)] in {'X' , 'O'}:
            #VALID INPUT, UPDATE THE BOARD
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # CHECK IF THE GAME HAS ENDED AND IF SOMEONE WON
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#DECLARE WINNER
if complete:
    if check_turn(turn) == 'X': print(f'{player1_name} Wins!!')
    else: print(f"{player2_name} Wins!!")
else:
    print('No Winner')

print('Thanks for playing!')
