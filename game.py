# write your code here
game_state = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

x_count = 0
o_count = 0
counter = 0
results = []
finished = False

def print_field():
    print('''---------
|''', game_state[0][0], game_state[0][1], game_state[0][2], '''|
|''', game_state[1][0], game_state[1][1], game_state[1][2], '''|
|''', game_state[2][0], game_state[2][1], game_state[2][2], '''|
---------''')

def make_move(x):
    done = False
    while not done:
        user_move = input('Enter the coordinates: ').split(' ')
        if len(user_move) != 2:
            print('You should put just 2 items divided by space')
        else:
            try:
                coordinates = [int(coordinate) for coordinate in user_move]
                if coordinates[0] < 1 or coordinates[0] > 3 or coordinates[1] < 1 or coordinates[1] > 3:
                    print('Coordinates should be from 1 to 3!')
                else:
                    i = 3 - coordinates[1]
                    j = coordinates[0] - 1
                    if game_state[i][j] != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        game_state[i][j] = x
                        global counter
                        counter += 1
                        done = True
            except ValueError:
                print('You should enter numbers!')

def analyze_field():
    # handling horizontal states
    for row in game_state:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            results.append(row[0])
    # handling vertical and diagonal states
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != ' ':
        results.append(game_state[0][0])
    if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != ' ':
        results.append(game_state[0][2])
    if game_state[0][0] == game_state[1][0] == game_state[2][0] and game_state[0][0] != ' ':
        results.append(game_state[0][0])
    if game_state[0][1] == game_state[1][1] == game_state[2][1] and game_state[0][1] != ' ':
        results.append(game_state[0][1])
    if game_state[0][2] == game_state[1][2] == game_state[2][2] and game_state[0][2] != ' ':
        results.append(game_state[0][2])

def get_winner():
    if len(results) == 1:
        print_field()
        print(results[0], 'wins')
        return True
    elif len(results) == 2:
        print_field()
        print('Draw')
        return True
    elif len(results) > 2:
        print_field()
        print('Impossible')
        return True
    elif len(results) == 0 and counter == 9:
        print_field()
        print('Draw')
        return True
    else:
        pass

while not finished:
    print_field()
    if counter % 2:
        make_move('O')
    else:
        make_move('X')
    analyze_field()
    if get_winner():
        break