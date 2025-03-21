import sys


def to_morse(s):
    '''recieve a char and cast to morse'''
    MORSE_CODE_DICT = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  " ": "/ "}
    return (MORSE_CODE_DICT.get(s.upper()))


def main():
    '''a program that takes a string as an argument
    and encodes it into Morse Code.'''
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    text = sys.argv[1]
    morseString = ""
    for s in text:
        try:
            morseString += to_morse(s)
            if s != text[-1]:
                morseString += ' '
        except Exception:
            print("AssertionError: the arguments are bad")
            return
    print(morseString)
    return


if __name__ == '__main__':
    main()
