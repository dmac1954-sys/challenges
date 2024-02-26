def main():
    user_input = input("Input here: ")
    print(double(user_input))

def double(user_input):
    new_string = ""
    for character in user_input:
        new_string += character*2
    return new_string


if __name__ == "__main__":
    main()