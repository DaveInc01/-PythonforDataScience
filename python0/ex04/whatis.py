import sys

def main():
    argsLength = 0
    for arg in sys.argv:
        argsLength = argsLength + 1
    if argsLength > 2:
        print("AssertionError: more than one argument is provided")
        return
    if argsLength == 1:
        return
    arg = sys.argv[1]
    len = 0
    isNegative = False
    for n in arg:
        if ((len == 0) and (n == '-')):
            len+=1
            isNegative = True
            continue
        if n >= '0' and n <= '9':
            len += 1
            continue
        else:
            print("AssertionError: argument is not an integer")
            return
    number = int(arg)
    if number % 2 == 1:
        print("I'm Odd.")
    else:
        print("I'm Even.")
main()

