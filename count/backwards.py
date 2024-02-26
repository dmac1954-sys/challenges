import time

def main():
    numbers = [
        "One...",
        "Two...",
        "Three...",
        "Four...",
        "Five...",
        "Six...",
        "Seven...",
        "Eight...",
        "Nine...",
        "Ten...",
    ]

    for number in reversed(numbers):
        time.sleep(1)
        print(number)


if __name__ == "__main__":
    main()
