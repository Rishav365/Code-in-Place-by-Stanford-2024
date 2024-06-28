def main():
    """
    The program takes an integer as input and doubles it until the number is greater than or equal to 100"
    """
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        print(curr_value * 2)
        curr_value = curr_value * 2
        
if __name__ == '__main__':
    main()