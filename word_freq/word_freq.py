def main():
    word_freq = {}
    text_file = "/workspaces/challenges/word_freq/news.txt"
    for key, value in build_freq(word_freq, text_file).items():
        print(key, value, sep='=')


def build_freq(word_freq, text_file):
    with open(text_file) as file:
        for line in file:
            print("###")
            # print(line)
            print("###")
            words = line.strip().split(" ")
            for word in words:
                if word.istitle() and word.isalpha():
                    try:
                        word_freq[word] += 1
                    except KeyError:
                        word_freq[word] = 1
    return word_freq


if __name__ == "__main__":
    main()
