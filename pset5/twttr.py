def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    for letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
