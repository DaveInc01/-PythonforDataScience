import sys


def checkBuilding(text: str) -> None:
    '''takes a single string argument and displays the sums of its
    upper-case characters, lower-casecharacters, punctuation characters,
    digits and spaces'''

    charN = 0
    upperN = 0
    lowerN = 0
    spaceN = 0
    digitN = 0
    marksN = 0
    charN = len(text)
    for n in text:
        if n.isalpha():
            if n.islower():
                lowerN += 1
            elif n.isupper():
                upperN += 1
        elif n.isspace():
            spaceN += 1
        elif n.isdigit():
            digitN += 1
        else:
            marksN += 1
    print(f"The text contains {charN} characters:\n"
          f"{upperN} upper letters\n"
          f"{lowerN} lower letters\n"
          f"{marksN} punctuation marks\n"
          f"{spaceN} spaces\n"
          f"{digitN} digits")


def main():
    args = sys.argv
    if len(args) > 2:
        print("AssertionError.")
        return
    text: any
    if len(args) < 2:
        text = input("What is the text to count?\n")
    else:
        text = args[1]
    checkBuilding(text)
    return


if __name__ == "__main__":
    main()
