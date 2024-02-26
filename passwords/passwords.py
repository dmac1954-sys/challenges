import bcrypt
import csv
def main():
    user_choice = input("Press A to add a password, D to delete a password, R to retrieve a password and U to update a password: ")
    if user_choice == "A":
        username = input("Please enter the username you wish to store: ")
        password_input = input("Please enter the password you would like to store: ")
        add_pw(username, password_input)
    if user_choice == "R":
        username = input("Please enter the username for the password you wish to retrieve: ")
        retrieve_pw(username)
    if user_choice == "U":
        username = input("Please enter the username you wish to update the password for: ")
        new_password = input("Please enter the new password: ")
        update_pw(username, new_password)


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def add_pw(username, password_input):
    with open("passwords.txt", 'a') as file:
        hashed_password = hash_password(password_input)
        file.write(f"{username}:{hashed_password}")

def retrieve_pw(username):
    with open("passwords.txt", 'r') as file:
        stored_username, hashed_password = line.strip().split(":")
        if stored_username == username:
            return hashed_password
    return "Password cannot be found!"

def update_pw(username, new_password):
    with open("passwords.txt", 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        stored_username, _ = line.strip().split(":")
        if stored_username == username:
            lines[i] = f"{username}:{hash_password(new_password)}\n"
            break

    with open("passwords.txt", 'w') as file:
        file.writelines(lines)

def delete_pw(username):
    with open("passwords.txt", 'r') as file:
        lines = file.readlines()
    
    updated_lines = [line for line in lines if not line.startswith(f"{username}:")]

    with open("passwords.txt", "w") as file:
        file.writelines(updated_lines)
        print(f"Password for '{username}' deleted.")


if __name__ == "__main__":
    main()