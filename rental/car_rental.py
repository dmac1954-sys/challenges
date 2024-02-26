def main():
    car_data = {
    "Ford": {
        "Mustang": {
        "type": "sports car",
        "year": 1964
        },
        "F150": {
        "type": "pickup truck",
        "year": 1948
        }
    },
    "Toyota": {  
        "Camry": {
        "type": "sedan",
        "year": 1982
        },
        "Prius": {
        "type": "hybrid",
        "year": 1997
        }
    },
    "Tesla": {
        "Model S": {
        "type": "sedan",
        "year": 2012
        },
        "Model 3": {
        "type": "sedan",
        "year": 2017
        }
    }
    }

    user_input = input("Please enter a manufacturer: ")
    print(parse_data(car_data, user_input))

def parse_data(car_data, user_input):
    return car_data[user_input]

if __name__ == "__main__":
    main()