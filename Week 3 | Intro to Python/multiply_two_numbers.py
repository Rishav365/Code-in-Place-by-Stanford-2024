"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    num1 = input("Enter first number:")
    num1 = int(num1)
    num2 = input("Enter second number:")
    num2 = int(num2)
    total = num1 * num2
    print(str(total))



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()