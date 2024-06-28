"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
mars_multiple = 0.378

def main():
    weight_on_earth = input("Enter a weight on Earth: ")
    weight_on_earth = float(weight_on_earth)
    total = weight_on_earth * mars_multiple
    print("The equivalent weight on Mars: " + str(total))

if __name__ == "__main__":
    main()