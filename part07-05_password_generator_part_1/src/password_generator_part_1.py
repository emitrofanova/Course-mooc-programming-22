# Write your solution here
from string import ascii_letters
from random import randint

def generate_password(numb):
    abc = ascii_letters
    answ = ""
    for i in range(numb):
        answ += abc[randint(0, len(abc) - 1)].lower()
    return answ

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
