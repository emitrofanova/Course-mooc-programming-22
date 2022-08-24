# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as f:
        words = "".join([ch for ch in f.read() if ch.isalpha() or ch == " " or ch == "\n"]).split()
        return {word : words.count(word) for word in words if words.count(word) >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
