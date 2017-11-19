from game import load_lexicon, createboard, printboard, find_next_possibles
from arrayutils import arrayCopy, arrayContent
from BinarySearch import find

def find_words(lexicon,board):
    found_words = []
    rec_find_words(lexicon, board, '', [], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], found_words)
    return found_words

def rec_find_words(lexicon, board, word, visited_dice, possible_next_dice, found_words):
    if find(lexicon, word) and len(word) >= 3 and not arrayContent(found_words, word):
        found_words.append(word)
        print(word, visited_dice, possible_next_dice)

    for die in possible_next_dice:
        if arrayContent(visited_dice, die):
            continue
        letter = board[die]
        nextword = word + letter
        nextvisited = arrayCopy(visited_dice)
        nextvisited.append(die)
        possibles = find_next_possibles(die)
        rec_find_words(lexicon, board, nextword, nextvisited, possibles, found_words)

def main():
    board = createboard()
    printboard(board)
    lexicon = load_lexicon()
    found_words = find_words(lexicon, board)

if __name__ == "__main__":
    main()

