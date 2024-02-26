import random

countries = {
    'Afghanistan': 'Kabul',
    'Albania': 'Tirana',
    'Algeria': 'Algiers',
    'Andorra': 'Andorra la Vella',
    'Angola': 'Luanda',
    'Antigua and Barbuda': "St. John's",
    'Argentina': 'Buenos Aires',
    'Armenia': 'Yerevan',
    'Australia': 'Canberra',
    'Austria': 'Vienna',
    'Azerbaijan': 'Baku',
    'Bahamas': 'Nassau',
    'Bahrain': 'Manama',
    'Bangladesh': 'Dhaka',
    'Barbados': 'Bridgetown',
    'Belarus': 'Minsk'
}

def play_game():
    user1_score = 0
    user2_score = 0
    countries_list = list(countries.keys())
    random.shuffle(countries_list)
    for i in range(10):
        if i % 2 == 0:
            user = "User 1"
        else:
            user = "User 2"
        country = countries_list[i]
        capital = countries[country]
        guess = input(f"{user}, what is the capital of {country}? ")
        if guess.lower() == capital.lower():
            print("Correct!")
            if user == "User 1":
                user1_score += 1
            else:
                user2_score += 1
        else:
            print(f"Wrong! The capital of {country} is {capital}.")
    print(f"User 1 score: {user1_score}/10")
    print(f"User 2 score: {user2_score}/10")

play_game()
