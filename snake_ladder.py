import time
import random
import operator


snake_squares = {31: 14, 37: 17, 73: 53, 78: 39, 92: 35, 99: 7}
ladder_squares = {5: 25, 10: 29, 22: 41, 28: 55, 44: 95, 70: 89, 79: 81}

def roll_dice():
    # dice roller
    # generates a random number between 1 to 6
    return random.randint(1,6)

def setup_game(players=None):
    # set up the game for the players
    if not players:
        players = 6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 1:
                print("number of players must be in between 1 to 4")
            else:
                break
        except ValueError:
            print("Must be a number")

    names = {}
    for i in range(1, players+1):
        while True:
            print("What is the name of Player {}? ".format(i))
            name = str(raw_input())
            if not name in names.keys():
                names[name] = 0
                break
            else:
                print('Players cannot have duplicate names')
    return names


def game_order(players):
    # find the order in which the game will be played
    order = {}
    print("Now we will decide the order of the game.")
    for name in players.keys():
        raw_input("Press Enter to Roll dice")
        score = roll_dice()
        print("Player {0} scored {1}".format(name, score)) 
        if not score in order.keys():
            order[name] = score
    sorted_namedata = sorted(order.items(), key=operator.itemgetter(1))[::-1]
    sorted_names = [i[0] for i in sorted_namedata]
    print("The order of the game will be : {}".format(', '.join(sorted_names)))
    return sorted_names

def move_player(player, current_pos):
    throw = roll_dice()
    next_pos = current_pos + throw
    if next_pos > 100:
        # if the player throws dice final position which is greater than 100
        print("{0} rolled a {1} but that is invalid".format(player, throw))
        return current_pos

    print("{0} rolled a {1} and is now on {2}".format(player, throw, next_pos))

    if next_pos in snake_squares:
        print("Player got bitten by a snake and is now on square {}".format(snake_squares[next_pos]))
        next_pos = snake_squares[next_pos]
    elif next_pos in ladder_squares:
        print("Player climbed a ladder and is now on square {}".format(ladder_squares[next_pos]))
        next_pos = ladder_squares[next_pos]
    return next_pos


def game(players, player_order):
    print("\n{} :  Welcome To Snakes And Ladders!".format(", ".join(players)))
    raw_input("Press Enter")
    while True:

        # Foreach player
        for player in player_order:
            current_pos = players[player]
            # Move player
            players[player] = move_player(player, current_pos)

            # Check win
            if players[player] >= 100:
                return player

            # Next player
            raw_input("Press Enter")


if __name__ == "__main__":
    players = setup_game()
    playing_order = game_order(players)
    winner = game(players, playing_order)
    print("Player {} won the game".format(winner))
