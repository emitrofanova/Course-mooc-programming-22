# Write your solution here
from random import shuffle

def words(n: int, beginning: str):
    answ = []
    with open("words.txt") as f:
        for line in f:
            line = line[:-1]
            if line.startswith(beginning):
                answ.append(line)
    shuffle(answ)
    if len(answ) < n:
        raise ValueError
    else:
        return answ[0:n]       

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)