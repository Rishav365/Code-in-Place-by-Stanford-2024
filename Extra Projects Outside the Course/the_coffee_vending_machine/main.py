"""
Coffee Vending Machine

Author: Rishav Dey
Date: 15th June 2024
Version: 1.0

Description:
This program simulates a coffee vending machine where users can browse categories of drinks,
select a drink, and insert money to purchase it. The program handles user inputs, displays menus,
and processes payments. It provides a seamless experience for users to enjoy their selected drinks.

How to Use:
Run the script and follow the on-screen instructions to select a drink, insert money, and receive your order.

Libraries Used:
- time: For managing delays and timing in the user interface.
- drinks: Module containing the list of available drinks categorized by type.

Usage:
Ensure the 'drinks' module is correctly imported and accessible. Execute the script to start the vending machine interface.
"""

import time
from drinks import drinks

def display_categories():
    print("\n----- CATEGORIES -----")
    time.sleep(0.9)
    for category in drinks:
        print(f"- {category}")
        time.sleep(0.9)

def display_drinks(category):
    print(f"\n----- {category.upper()} DRINKS -----")
    time.sleep(0.9)
    for drink in drinks[category]:
        print(f"{drink['name']} - ${drink['price']:.2f}")
        time.sleep(0.6)

def get_user_category():
    while True:
        category = input("\nWhich category would you like to browse? ").strip().lower()
        time.sleep(0.9)
        for valid_category in drinks:
            if valid_category.lower() == category:
                return valid_category
        print("Invalid category. Please select a valid category from the list.")
        time.sleep(0.2)

def get_user_drink(category):
    while True:
        drink_name = input("\nWhat would you like to have? ").strip().lower()
        time.sleep(0.9)
        for drink in drinks[category]:
            if drink['name'].lower() == drink_name:
                return drink
        print("Invalid drink. Please select a valid drink from the list.")
        time.sleep(0.2)

def insert_money(drink_price):
    while True:
        try:
            money = float(input(f"Insert money (${drink_price}): "))
            time.sleep(0.6)
            if money >= drink_price:
                return money
            else:
                print(f"Insufficient money. Please insert at least ${drink_price}.")
                time.sleep(0.6)
        except ValueError:
            print("Invalid input. Please insert a valid amount of money.")
            time.sleep(0.6)

def main():
    print("----- WELCOME TO THE COFFEE VENDING MACHINE -----")
    time.sleep(0.9)
    print("Experience the finest selection of coffee and beverages.")
    time.sleep(1)
    print("Our menu features a wide variety of drinks to cater to every taste.")
    time.sleep(1)
    print("Take your time to explore and enjoy a delightful coffee experience.\n")
    time.sleep(1)
    
    print("Here are the categories of drinks we offer:\n")
    time.sleep(1.5)
    while True:
        display_categories()
        category = get_user_category()
        display_drinks(category)
        drink = get_user_drink(category)
        
        print(f"\nYou have selected {drink['name']}. Great choice!")
        time.sleep(0.6)
        money = insert_money(drink['price'])
        
        change = money - drink['price']
        print(f"Processing your order...")
        time.sleep(1.6)
        print(f"Here is your {drink['name']} and ${change:.2f} change. Enjoy!\n")
        time.sleep(0.9)

        another = input("Would you like to buy another drink? (yes/no): ").strip().lower()
        time.sleep(0.9)
        if another != 'yes':
            print("\nThank you for using the Coffee Vending Machine.")
            time.sleep(0.9)
            print("We hope you enjoyed your coffee experience. Have a wonderful day!")
            time.sleep(0.9)
            break

if __name__ == '__main__':
    main()