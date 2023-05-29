'''
    This is a program to quickly and easily
    generate secure passwords
'''

import string
from sys import argv, exit
import random

def main():
    charset = ""
    charset += string.ascii_letters
    charset += string.digits
    charset += string.punctuation
    try:
        print(generate(int(argv[1]), charset))
    except ValueError:
        exit("Invalid argument given")

def generate(length, chars):
    pw = ""
    for i in range(length):
        pw += chars[random.randint(0, len(chars) - 1)]
    return pw

if __name__ == "__main__":
    main()