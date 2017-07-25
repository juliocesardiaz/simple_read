from sys import argv

try:
    path = argv[1]
    with open(path) as f:
        s = f.read()
        print(s)
except IndexError:
    print("You did not specify a file you wish to read.")