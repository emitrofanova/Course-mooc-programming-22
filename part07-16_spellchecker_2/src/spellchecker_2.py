# Write your solution here
from difflib import get_close_matches

with open("wordlist.txt") as file:
    vocab = file.read()
    vocab = vocab.split()
wrong = []
text = input("Write text: ")
text = text.split()
answ = ""
for word in text:
    flag = True
    for word_vocab in vocab:
        if word.lower() == word_vocab.lower():
            answ += word + " "
            flag = False
    if flag:
        answ += "*" + word + "* "
        wrong.append(word)
print(answ[:len(answ) - 1])
print("suggestions:")
for word in wrong:
    print(f"{word}: ", end = "")
    sugg = get_close_matches(word, vocab)
    print(*sugg, sep = ", ")
