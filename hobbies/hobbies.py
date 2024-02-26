def main():
    data = [
        {"name": "John", "age": 25, "hobbies": ["reading", "writing", "coding"]},
        {"name": "Alice", "age": 30, "hobbies": ["painting", "photography", "football", "golf"]},
        {"name": "Bob", "age": 22, "hobbies": ["gaming", "swimming"]},
    ]

    find_person_with_most_hobbies(data)
    # print(result)


def find_person_with_most_hobbies(data):
    hobby_lengths = []
    for person in data:
        hobby_lengths.append(len(person["hobbies"]))
    
    for person in data:
        if len(person["hobbies"]) == max(hobby_lengths):
            print(person["name"])
       
if __name__ == "__main__":
    main()
