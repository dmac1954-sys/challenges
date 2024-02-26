import random
def main():
    letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
    tiles = generate_tiles()
    print(f"Your tiles are {tiles}")
    user_word = input("Please input a word: ")
    score = calculate_value(user_word, letter_value, tiles)
    print(f"The score of the word {user_word} is {score}.")


def generate_tiles():
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels]
    tiles = random.sample(vowels, 2) + random.sample(consonants, 5)
    return tiles

def calculate_value(user_word, letter_value, tiles):
    user_word = user_word.lower()
    for letter in user_word:
        if letter not in tiles:
            return "Invalid word."
    score = sum(letter_value[letter] for letter in user_word)
    return score

if __name__ == "__main__":
    main()