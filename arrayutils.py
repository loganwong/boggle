def arrayCopy(orig):
    copy = []
    for item in orig:
        copy.append(item)
    return copy

def arrayContent(array,item):
    for arrayitem in array:
        if arrayitem == item:
            return True
    return False

def main():
    deck = ['1','2','3','4','5']
    copy = arrayCopy(deck)
    print(deck)
    print(copy)
    content = '1'
    print(arrayContent(deck,content))
    content = '6'
    print(arrayContent(deck, content))


if __name__ == "__main__":
    main()
