


import random
import sys
snakes = {
    17:7,54:34,62:19,98:79}
ladders = {
    3:38,24:33,42:93,72:84}
max_value = 100
dice_face = 6

player_turn_text = [
    "Go.",
    "Please proceed.",
    "Are you ready?",
    "",
]


    
def welcome_message():
    message="##### welcocme to snakes and ladeer's game #####"
    print(message)

def get_players_name():
    player1_name = None
    while not player1_name:
        player1_name = input("Enter the name of player1:").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Enter the name of player2:").strip()

    print("\n Match will be played between " + player1_name + " and " + player2_name + "\n")
    return player1_name,player2_name

def get_dice_value():
    dice_value= random.randint(1,dice_face)
    print("its a " + str(dice_value))
    return dice_value

def got_snake_bite(old_value, current_value, player_name):
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > max_value:
        print("You need " + str(max_value - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    if max_value == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("#### Game succesfully finished ####")
        sys.exit(1)
        


def start():
    welcome_message()
    player1_name, player2_name = get_players_name()

    player1_current_position = 0
    player2_current_position = 0

    while True:
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()
    
    
    
    
