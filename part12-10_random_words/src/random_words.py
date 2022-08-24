# Write your solution here:
from random import randint
def word_generator(characters: str, length: int, amount: int):
    i = 1
    while i <= amount:
        yield "".join([characters[randint(0, len(characters) - 1)] for i in range(length)])
        i += 1
       
if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
