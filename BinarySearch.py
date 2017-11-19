from arrayutils import arrayContent
from time import time

def find(array,word):
    return rec_find(array, word, 0, len(array))
def rec_find(array, word, start, end):
    if end == start:
        return False
    mid = start + int((end - start)/2)
    check = array[mid]
    if check == word:
        return True
    elif check > word:
        return rec_find(array, word, start, mid)
    elif check < word:
        return rec_find(array, word, mid + 1, end)

def main():
    with open('twl06.txt')as f:
        lexicon = f.read().splitlines()

    testwords = ['aardvark','drywall','offramp','zygote','ziop']
    for testword in testwords:
        start = time()
        iscontained = arrayContent(lexicon,testword)
        end = time()
        print(testword,iscontained,end-start)
    for testword in testwords:
        start = time()
        iscontained = find(lexicon,testword)
        end = time()
        print(testword,iscontained,end-start)


if __name__ == "__main__":
    main()
