import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    Prints 10 random numbers from 1 to 100 serially.
    """
    for _ in range(10):
        print(random.randint(1, 100))

if __name__ == '__main__':
    main()