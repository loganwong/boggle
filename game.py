from random import randint, shuffle
from arrayutils import arrayContent,arrayCopy
import BinarySearch as bs
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
                nextpossibles = find_next_possibles(board_idx)
                found = rec_find_on_board(board,word_tokens,nextvisited,nextpossibles)
                if found:
                    return True

    return False
def find_next_possibles(board_index):
    if board_index % 4 == 3:
        unfilteredpossiblities = [
          board_index - 5, board_index - 4, board_index - 3,
          board_index - 1,                  board_index + 1,
          board_index + 3, board_index + 4, board_index + 5,
        ]
    elif board_index % 4 == 0:
        unfilteredpossiblities = [
            board_index - 4, board_index - 3,
            board_index + 1,
            board_index + 4, board_index + 5,
        ]
    else:
        unfilteredpossiblities = [
            board_index - 5, board_index - 4,
            board_index - 1,
            board_index + 3, board_index + 4,
        ]
    filteredpossiblities = []
    for possible in unfilteredpossiblities:
        if possible >= 0 and possible < 16:
            filteredpossiblities.append(possible)
    return filteredpossiblities

def load_lexicon():
    with open('twl06.txt')as f:
        lexicon = f.read().splitlines()
        return lexicon

def main():
    lexicon = load_lexicon()
    board = createboard()
    shuffle(board)
    printboard(board)
    found_words = []
    while True:
        player_word = input('find a word? ')
        tokens, is_valid = tokenize(player_word)
        is_valid = tokenize(player_word)
        if not is_valid:
            print("Couldn't tokenize")
            continue
        is_valid = find_on_board(board, tokens)
        if not is_valid:
            print("Not on board")
            continue
        is_valid = bs.find(lexicon, player_word)
        if not is_valid:
            print("Not in lexicon")
            continue
        is_valid = not arrayContent(found_words, player_word)
        if not is_valid:
            print("Words already used")
            continue
        found_words.append(player_word)
        print("Word was valid")



if __name__ == "__main__":
    main()

