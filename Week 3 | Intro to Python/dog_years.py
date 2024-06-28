# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    #This program converts age in human years to age in dog years.
    human_years = input("Enter an age in calendar years:")
    human_years = float(human_years)
    total = human_years * 7.18
    print("That's " + str(total) + " in dog years!")

if __name__ == '__main__':
    main()