# write your code here
winners = {'x': False, 'o': False}


def print_board():
    print('---------')
    print(f'| {saved_data[0]} {saved_data[1]} {saved_data[2]} |')
    print(f'| {saved_data[3]} {saved_data[4]} {saved_data[5]} |')
    print(f'| {saved_data[6]} {saved_data[7]} {saved_data[8]} |')
    print('---------')


def analyse_game():
    for i in range(3):
        if saved_data[3 * i] == saved_data[3 * i + 1] == saved_data[3 * i + 2] and saved_data[3 * i] != '_':
            if saved_data[3 * i].lower() == 'x':
                winners['x'] = True
            else:
                winners['o'] = True
        if saved_data[i] == saved_data[i + 3] == saved_data[i + 6] and saved_data[i] != '_':
            if saved_data[i].lower() == 'x':
                winners['x'] = True
            else:
                winners['o'] = True
    if saved_data[0] == saved_data[4] == saved_data[8] and saved_data[0] != '_':
        if saved_data[0].lower() == 'x':
            winners['x'] = True
        else:
            winners['o'] = True
    if saved_data[2] == saved_data[4] == saved_data[6] and saved_data[2] != '_':
        if saved_data[2].lower() == 'x':
            winners['x'] = True
        else:
            winners['o'] = True
    if abs(len([saved_data[x] for x in range(9) if saved_data[x].lower() == 'x']) - len(
            [saved_data[x] for x in range(9) if saved_data[x].lower() == 'o'])) > 1:
        winners['x'] = True
        winners['o'] = True
    if winners['x'] and not winners['o']:
        return 'X wins'
    elif not winners['x'] and winners['o']:
        return 'O wins'
    elif winners['x'] and winners['o']:
        return 'Impossible'
    elif not winners['x'] and not winners['o']:
        if len([a for a in range(9) if saved_data[a] == '_']):
            return 'Game not finished'
        else:
            return 'Draw'


def next_move(player_symbol):
    global saved_data
    move = input('Enter the coordinates: ')
    try:
        int(move.split()[0])
    except ValueError:
        print('You should enter numbers!')
        next_move(player_symbol)
    else:
        if not (1 <= int(move.split()[0]) <= 3 and 1 <= int(move.split()[1]) <= 3):
            print('Coordinates should be from 1 to 3!')
            next_move(player_symbol)
        elif saved_data[(int(move.split()[0]) - 1) * 3 + (int(move.split()[1]) - 1)] == '_':
            saved_data = list(saved_data)
            saved_data[(int(move.split()[0]) - 1) * 3 + (int(move.split()[1]) - 1)] = player_symbol
            saved_data = ''.join(saved_data)
        else:
            print('This cell is occupied! Choose another one!')
            next_move(player_symbol)


saved_data = '_________'
print_board()
while analyse_game() == "Game not finished":
    next_move('X')
    print_board()
    if analyse_game() != "Game not finished":
        break
    next_move('O')
    print_board()
print(analyse_game())