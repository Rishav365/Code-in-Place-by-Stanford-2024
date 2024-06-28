"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.360
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.14
EARTH = 1.0

def main():
    # Prompt user for Earth weight
    earth_weight_input_str = input("Enter a weight on Earth: ")
    
    # Convert Earth weight to a float
    earth_weight = float(earth_weight_input_str)
    
    # Prompt user for planet choice
    planet_choice_str = input("Enter a planet: ")
    
    # Initialize weight in case none of the if conditions below are true.
    weight = 0
    
   # Check the user's planet choice and calculate the equivalent weight
    if planet_choice_str == "Mars":
        weight = earth_weight * MARS
    elif planet_choice_str == "Mercury":
        weight = earth_weight * MERCURY
    elif planet_choice_str == "Venus":
        weight = earth_weight * VENUS
    elif planet_choice_str == "Jupiter":
        weight = earth_weight * JUPITER
    elif planet_choice_str == "Saturn":
        weight = earth_weight * SATURN
    elif planet_choice_str == "Uranus":
        weight = earth_weight * URANUS
    elif planet_choice_str == "Neptune":
        weight = earth_weight * NEPTUNE
    elif planet_choice_str == "Earth":
        weight = earth_weight * EARTH
    else:
        print("Invalid planet name")
    
    # Round weight to 2 decimal places
    weight = round(weight, 2)
    
    # Print the equivalent weight on the chosen planet
    print(f"The equivalent weight on {planet_choice_str}: {str(weight)}")

if __name__ == "__main__":
    main()