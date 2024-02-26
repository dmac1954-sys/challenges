import json


def main():
    file_path = "/workspaces/challenges/file_io/cities.json"
    for city in residency(file_path):
        print(city)


def residency(file_path):
    cities = set()
    with open(file_path) as file:
        reader = file.read()
    people = json.loads(reader)
    for person in people:
        if person["age"] < 30:
            cities.add(person["city"])
    return cities


if __name__ == "__main__":
    main()
