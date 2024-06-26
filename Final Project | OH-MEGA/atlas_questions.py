import random

# Dictionary of countries and their capitals with increasing difficulty levels
atlas_questions = [
    {"country": "United States", "capital": "Washington, D.C.", "difficulty": 1},
    {"country": "United Kingdom", "capital": "London", "difficulty": 1},
    {"country": "Germany", "capital": "Berlin", "difficulty": 1},
    {"country": "France", "capital": "Paris", "difficulty": 1},
    {"country": "Canada", "capital": "Ottawa", "difficulty": 1},
    {"country": "Australia", "capital": "Canberra", "difficulty": 1},
    {"country": "Japan", "capital": "Tokyo", "difficulty": 1},
    {"country": "China", "capital": "Beijing", "difficulty": 1},
    {"country": "India", "capital": "New Delhi", "difficulty": 1},
    {"country": "Brazil", "capital": "Brasília", "difficulty": 1},
    {"country": "Italy", "capital": "Rome", "difficulty": 1},
    {"country": "Russia", "capital": "Moscow", "difficulty": 1},
    {"country": "South Africa", "capital": "Pretoria", "difficulty": 1},
    {"country": "Mexico", "capital": "Mexico City", "difficulty": 1},
    {"country": "Argentina", "capital": "Buenos Aires", "difficulty": 1},
    {"country": "Spain", "capital": "Madrid", "difficulty": 1},
    {"country": "Turkey", "capital": "Ankara", "difficulty": 1},
    {"country": "Egypt", "capital": "Cairo", "difficulty": 1},
    {"country": "Saudi Arabia", "capital": "Riyadh", "difficulty": 1},
    {"country": "Nigeria", "capital": "Abuja", "difficulty": 1},
    {"country": "Sweden", "capital": "Stockholm", "difficulty": 2},
    {"country": "Norway", "capital": "Oslo", "difficulty": 2},
    {"country": "Finland", "capital": "Helsinki", "difficulty": 2},
    {"country": "Denmark", "capital": "Copenhagen", "difficulty": 2},
    {"country": "Netherlands", "capital": "Amsterdam", "difficulty": 2},
    {"country": "Belgium", "capital": "Brussels", "difficulty": 2},
    {"country": "Switzerland", "capital": "Bern", "difficulty": 2},
    {"country": "Austria", "capital": "Vienna", "difficulty": 2},
    {"country": "Portugal", "capital": "Lisbon", "difficulty": 2},
    {"country": "Greece", "capital": "Athens", "difficulty": 2},
    {"country": "Poland", "capital": "Warsaw", "difficulty": 2},
    {"country": "Hungary", "capital": "Budapest", "difficulty": 2},
    {"country": "Czech Republic", "capital": "Prague", "difficulty": 2},
    {"country": "Ireland", "capital": "Dublin", "difficulty": 2},
    {"country": "South Korea", "capital": "Seoul", "difficulty": 3},
    {"country": "North Korea", "capital": "Pyongyang", "difficulty": 3},
    {"country": "Vietnam", "capital": "Hanoi", "difficulty": 3},
    {"country": "Thailand", "capital": "Bangkok", "difficulty": 3},
    {"country": "Malaysia", "capital": "Kuala Lumpur", "difficulty": 3},
    {"country": "Singapore", "capital": "Singapore", "difficulty": 3},
    {"country": "Philippines", "capital": "Manila", "difficulty": 3},
    {"country": "Indonesia", "capital": "Jakarta", "difficulty": 3},
    {"country": "New Zealand", "capital": "Wellington", "difficulty": 3},
    {"country": "Pakistan", "capital": "Islamabad", "difficulty": 3},
    {"country": "Iran", "capital": "Tehran", "difficulty": 3},
    {"country": "Iraq", "capital": "Baghdad", "difficulty": 3},
    {"country": "Israel", "capital": "Jerusalem", "difficulty": 3},
    {"country": "Australia", "capital": "Canberra", "difficulty": 4},
    {"country": "New Zealand", "capital": "Wellington", "difficulty": 4},
    {"country": "Fiji", "capital": "Suva", "difficulty": 4},
    {"country": "Papua New Guinea", "capital": "Port Moresby", "difficulty": 4},
    {"country": "Vanuatu", "capital": "Port Vila", "difficulty": 4},
    {"country": "Samoa", "capital": "Apia", "difficulty": 4},
    {"country": "Tonga", "capital": "Nuku'alofa", "difficulty": 4},
    {"country": "Kiribati", "capital": "Tarawa", "difficulty": 4},
    {"country": "Tuvalu", "capital": "Funafuti", "difficulty": 4},
    {"country": "Nauru", "capital": "Yaren", "difficulty": 4},
    {"country": "Marshall Islands", "capital": "Majuro", "difficulty": 4},
    {"country": "Solomon Islands", "capital": "Honiara", "difficulty": 4},
    {"country": "Palau", "capital": "Ngerulmud", "difficulty": 4},
    {"country": "Micronesia", "capital": "Palikir", "difficulty": 4},
    {"country": "United States", "capital": "Washington, D.C.", "difficulty": 5},
    {"country": "Canada", "capital": "Ottawa", "difficulty": 5},
    {"country": "Mexico", "capital": "Mexico City", "difficulty": 5},
    {"country": "Brazil", "capital": "Brasília", "difficulty": 5},
    {"country": "Argentina", "capital": "Buenos Aires", "difficulty": 5},
    {"country": "Chile", "capital": "Santiago", "difficulty": 5},
    {"country": "Colombia", "capital": "Bogotá", "difficulty": 5},
    {"country": "Peru", "capital": "Lima", "difficulty": 5},
    {"country": "Venezuela", "capital": "Caracas", "difficulty": 5},
    {"country": "Ecuador", "capital": "Quito", "difficulty": 5},
    {"country": "Bolivia", "capital": "Sucre", "difficulty": 5},
    {"country": "Paraguay", "capital": "Asunción", "difficulty": 5},
    {"country": "Uruguay", "capital": "Montevideo", "difficulty": 5},
    {"country": "Guyana", "capital": "Georgetown", "difficulty": 5},
    {"country": "Suriname", "capital": "Paramaribo", "difficulty": 5},
    {"country": "French Guiana", "capital": "Cayenne", "difficulty": 5},
    {"country": "Belize", "capital": "Belmopan", "difficulty": 5},
    {"country": "Costa Rica", "capital": "San José", "difficulty": 5},
    {"country": "El Salvador", "capital": "San Salvador", "difficulty": 5},
    {"country": "Guatemala", "capital": "Guatemala City", "difficulty": 5},
    {"country": "Honduras", "capital": "Tegucigalpa", "difficulty": 5},
    {"country": "Nicaragua", "capital": "Managua", "difficulty": 5},
    {"country": "Panama", "capital": "Panama City", "difficulty": 5},
    {"country": "Bahamas", "capital": "Nassau", "difficulty": 5},
    {"country": "Cuba", "capital": "Havana", "difficulty": 5},
    {"country": "Jamaica", "capital": "Kingston", "difficulty": 5},
    {"country": "Trinidad and Tobago", "capital": "Port of Spain", "difficulty": 5},
    {"country": "Barbados", "capital": "Bridgetown", "difficulty": 5},
    {"country": "Saint Lucia", "capital": "Castries", "difficulty": 5},
    {"country": "Saint Vincent and the Grenadines", "capital": "Kingstown", "difficulty": 5},
    {"country": "Grenada", "capital": "St. George's", "difficulty": 5},
    {"country": "Dominica", "capital": "Roseau", "difficulty": 5},
    {"country": "Saint Kitts and Nevis", "capital": "Basseterre", "difficulty": 5},
]

# Function to get a random set of questions for a given round
def get_round_questions(num_questions):
    return random.sample(atlas_questions, num_questions)