'''
    Simple program to print out every number in the fibonacci
    sequence (where each new number is the sum of the 
    last two numbers) up to a user given stopping point
'''

from sys import argv, exit

def main():
    try:
        stop = int(argv[1])
    except TypeError:
        exit("Not a positive number greater than 1")
    else:
        answer = fib(stop)
        for num in answer: print(num)

def fib(_stop):
    if _stop <= 1: raise ValueError()
    nums = [0, 1]
    i = 1
    while (nums[i] + nums[i - 1]) < _stop:
        nums.append(nums[i] + nums[i - 1])
        i += 1
    return nums

if __name__ == "__main__":
    main()