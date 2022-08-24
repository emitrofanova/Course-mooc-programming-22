# Write your solution here
# You can test your function by calling it within the following block
def first_word(sent):
    sent = sent.split()
    return sent[0]
def second_word(sent):
    sent = sent.split()
    return sent[1]
def last_word(sent):
    sent = sent.split()
    return sent[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))