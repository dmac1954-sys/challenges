import csv
from people import People
def main():
    people_list = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age = int(row["Age"])  # Assuming "Age" is a column in your CSV
            height = float(row["Height (cm)"])  # Convert height to float
            weight = float(row["Weight (kg)"])  # Convert weight to float
            person = People(age, height, weight)
            people_list.append(person)

        while True:
            user_calc_choice = input("Please choose whether you want to see the average (A), max (MAX), min (MIN), total (T) or to quit the program (Q): ")
            user_categ_choice = input("Please choose which category of data you wish to see: age (A), height (H), weight (W) or to quit the program (Q): ")
            if user_calc_choice == "A" and user_categ_choice == "A":
                print(average_age(people_list))
            if user_calc_choice == "MAX" and user_categ_choice == "A":
                print(max_age(people_list))
            if user_calc_choice == "MIN" and user_categ_choice == "A":
                print(min_age(people_list))
            if user_calc_choice == "T" and user_categ_choice == "A":
                print(total_age(people_list))
            if user_calc_choice == "A" and user_categ_choice == "H":
                print(average_height(people_list))
            if user_calc_choice == "MAX" and user_categ_choice == "H":
                print(max_height(people_list))
            if user_calc_choice == "MIN" and user_categ_choice == "H":
                print(min_height(people_list))
            if user_calc_choice == "T" and user_categ_choice == "H":
                print(total_height(people_list))
            if user_calc_choice == "A" and user_categ_choice == "W":
                print(average_weight(people_list))
            if user_calc_choice == "MAX" and user_categ_choice == "W":
                print(max_weight(people_list))
            if user_calc_choice == "MIN" and user_categ_choice == "W":
                print(min_weight(people_list))
            if user_calc_choice == "T" and user_categ_choice == "W":
                print(total_weight(people_list))
            if user_calc_choice == "Q" or user_categ_choice == "Q":
                break
            
    
    
def average_height(people_list):
    total_height = sum(person.height for person in people_list)
    total_entries = len(people_list)
    average_height = total_height/total_entries
    return f"The average height is {average_height:.2f}"

def max_height(people_list):
    maximum_height = max(person.height for person in people_list)
    return f"The maximum height is {maximum_height:.2f}"

def min_height(people_list):
    min_height = min(person.height for person in people_list)
    return f"The minimum height is {min_height:.2f}"

def total_height(people_list):
    total_h = sum(person.height for person in people_list)
    return f"The total height is {total_h}"

def average_weight(people_list):
    total_weight = sum(person.weight for person in people_list)
    total_entries = len(people_list)
    average_weight = total_weight/total_entries
    return f"The average weight is {average_weight:.2f}"

def max_weight(people_list):
    maximum_weight = max(person.weight for person in people_list)
    return f"The maximum weight is {maximum_weight:.2f}"

def min_weight(people_list):
    min_weight = min(person.weight for person in people_list)
    return f"The minimum weight is {min_weight:.2f}"

def total_weight(people_list):
    total_w = sum(person.weight for person in people_list)
    return f"The total height is {total_w}"

def average_age(people_list):
    total_age = sum(person.age for person in people_list)
    total_entries = len(people_list)
    average_age = total_age/total_entries
    return f"The average age is {average_age:.2f}"

def max_age(people_list):
    maximum_age = max(person.age for person in people_list)
    return f"The oldest person is {maximum_age:.2f}"

def min_age(people_list):
    min_age = min(person.age for person in people_list)
    return f"The youngest person is {min_age:.2f}"

def total_age(people_list):
    total_a = sum(person.age for person in people_list)
    return f"The total age is {total_a}"


if __name__ == "__main__":
    main()