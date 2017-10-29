from random import randint, shuffle
from arrayutils import arrayContent,arrayCopy
DICE = [
    ['a','a','e','e','g','n'],
    ['a','b','b','j','o','o'],
    ['a','c','h','o','p','s'],
    ['a','f','f','k','p','s'],
    ['a','o','o','t','t','w'],
    ['c','i','m','o','t','u'],
    ['d','e','i','l','r','x'],
    ['d','e','l','r','v','y'],
    ['d','i','s','t','t','y'],
    ['e','e','g','h','n','w'],
    ['e','e','i','n','s','u'],
    ['e','h','r','t','v','w'],
    ['e','i','o','s','s','t'],
    ['e','l','r','t','t','y'],
    ['h','i','m','n','u','qu'],
    ['h','l','n','n','r','z'],

]
def createboard():
    board = []
    for die in DICE:
        idx = randint(0, 5)
        face = die[idx]
        board.append(face)
    return board

def printboard(board):
    count = 0
    line = ''
    for char in board:
        line += char
        count += 1
        if count<4:
            if char =='qu':
                line += " "
            else:
                line += "  "
        else:
            print(line)
            count = 0
            line = ''

def tokenize(player_word):
    is_valid = True
    tokens = []
    word_idx = 0
    while word_idx < len(player_word):
        word_char = player_word[word_idx]
        word_idx += 1
        if word_char == 'q':
            if word_idx == len(player_word):
                is_valid = False
                break

            next_char = player_word[word_idx]
            word_idx += 1
            if next_char == 'u':
                tokens.append('qu')
            else:
                is_valid = False
                break
        else:
            tokens.append(word_char)
        return tokens, is_valid

    print(tokens)
def find_on_board(board,word_tokens):
    return rec_find_on_board(board,word_tokens,[],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

def rec_find_on_board(board,word_tokens,visited,possibles):
    word_idx = len(visited)
    if word_idx == len(word_tokens):
        return True
    word_token = word_tokens[word_idx]
    for board_idx in possibles:
        board_token = board[board_idx]
        if board_token == word_token:
            if not arrayContent(visited, board_idx):
                nextvisited = arrayCopy(visited)
                nextvisited.append(board_idx)
                found = rec_find_on_board(board,word_tokens,nextvisited,nextpossibles)
                if found:
                    return True

    return False



def main():
    board = createboard()
    shuffle(board)
    printboard(board)
    player_word = input('find a word? ')
    print (player_word)
    tokens, is_valid = tokenize(player_word)
    if is_valid:
        is_on_board = find_on_board(board,tokens)
        print(is_on_board)


main()

