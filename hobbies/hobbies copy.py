def main():
    data = [
        {"name": "John", "age": 25, "hobbies": ["reading", "writing", "coding"]},
        {
            "name": "Alice",
            "age": 30,
            "hobbies": ["painting", "photography"],
        },
        {"name": "Bob", "age": 22, "hobbies": ["gaming", "swimming", "football", "golf"]},
    ]

    print(find_person_with_most_hobbies(data))
    # print(result)


def find_person_with_most_hobbies(data):
    people = {}
    people["max"] = 0
    people["name"] = ""
    for person in data:
        if len(person["hobbies"]) > people["max"]:
            people["max"] = len(person["hobbies"])
            people["name"] = person["name"]
    return people["name"]
    
if __name__ == "__main__":
    main()
