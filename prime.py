'''
    program to determine if a number is prime or not
'''

from sys import exit, argv

def main():
    print(is_prime(argv[1]))

def is_prime(n):
    if type(n) != int: 
        try:
            n = int(n)
        except ValueError:
            return "Bad input"
    if n <= -1: raise ValueError
    if n == 1 or n == 0: return f"{n} is prime"
    else: 
        for i in range(2, n):
            if n % i == 0:
                return "Not prime"
            else:
                continue
        return f"{n} is prime"
    
if __name__ == "__main__":
    main()