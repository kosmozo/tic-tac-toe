field = list(input('Enter cells: '))

game_state = [[field[0], field[1], field[2]],
              [field[3], field[4], field[5]],
              [field[6], field[7], field[8]]]

def print_field():
    print('''---------
|''', game_state[0][0], game_state[0][1], game_state[0][2], '''|
|''', game_state[1][0], game_state[1][1], game_state[1][2], '''|
|''', game_state[2][0], game_state[2][1], game_state[2][2], '''|
---------''')

print_field()

finished = False

while not finished:
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
                if game_state[i][j] != '_':
                    print('This cell is occupied! Choose another one!')
                else:
                    game_state[i][j] = 'X'
                    finished = True
        except ValueError:
            print('You should enter numbers!')

print_field()

results = []
x_count = 0
o_count = 0
__count = 0

# handling the X and O total number to calculate if the situation is ever possible
for row in game_state:
    if row[0] == row[1] == row[2] and row[0] != '_':
        results.append(row[0])
    for state in row:
        if state == 'X':
            x_count += 1
        if state == 'O':
            o_count += 1
        if state == '_':
            __count += 1

# handling vertical and diagonal states
if game_state[0][0] == game_state[1][1] == game_state[2][2]:
    results.append(game_state[0][0])
if game_state[0][2] == game_state[1][1] == game_state[2][0]:
    results.append(game_state[0][2])
if game_state[0][0] == game_state[1][0] == game_state[2][0]:
    results.append(game_state[0][0])
if game_state[0][1] == game_state[1][1] == game_state[2][1]:
    results.append(game_state[0][1])
if game_state[0][2] == game_state[1][2] == game_state[2][2]:
    results.append(game_state[0][2])

# calculating results if the field not filled
if x_count + o_count < 9:
    if x_count - o_count == 2 or o_count - x_count == 2:
        print('Impossible')
    elif len(results) == 1:
        print(results[0], 'wins')
    elif len(results) > 1:
        print('Impossible')


# calculating results if the field is filled
elif x_count + o_count == 9:
    if len(results) == 0:
        print('Draw')
    elif len(results) == 1:
        print(results[0], 'wins')
    elif len(results) == 2:
        print('Draw')
    elif len(results) > 2:
        print('Impossible')