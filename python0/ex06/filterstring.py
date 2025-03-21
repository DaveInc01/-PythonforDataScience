import sys


def getWordsList(text: str) -> list:
    '''recieves string and returns a list of words seperated with space'''
    wordlist = []
    pos = text.find(' ')
    while pos != -1:
        if not text[0:pos].isspace() and pos != 0:
            wordlist.append(text[0:pos])
        pos += 1
        text = text[pos: len(text)]
        pos = text.find(' ')
    if len(text) > 0 and not text.isspace():
        wordlist.append(text)
    return wordlist


def main():
    '''program that accepts two arguments: a string(S),
    and an integer(N).
    The program should output a list of words from S
    that have a length greater than N'''
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    givenlength = sys.argv[2]
    try:
        givenlength = int(givenlength)
    except Exception:
        print("AssertionError: the arguments are bad")
        return
    text = sys.argv[1]
    wordslist = getWordsList(text)
    newlist = [word for word in wordslist
               if (lambda word: len(word) > givenlength)(word)]
    print(newlist)
    return


if __name__ == "__main__":
    main()
