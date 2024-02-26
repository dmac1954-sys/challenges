import random
import sys


def main():
    lives = 8
    file_path = "/workspaces/challenges/hangman/wordle_dict (1).txt"
    random_word = get_word(file_path)
    start = ["-", "-", "-", "-", "-"]
    guesses = []
    while lives > 0:
        guess = input("Please guess a letter: ")
        guesses.append(guess)
        if guess in random_word:
            start = update_word(start, guess, random_word)
            if "".join(start) == random_word:
                sys.exit(f"You have won the game! The word was {random_word}!")
        else:
            lives -= 1
            print(f"You have lost a life! You have {lives} left!")

        print(" ".join(start))
        print('Your guesses are: ', ", ".join(guesses))

    print(f"Game over! You have run out of lives! The word was {random_word}!")


def get_word(file_path):
    words = []
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split(" "):
                words.append(word)
    return random.choice(words)


def update_word(start, guess, random_word):
    for i in range(len(random_word)):
        if guess == random_word[i]:
            start[i] = guess
    return start


if __name__ == "__main__":
    main()
