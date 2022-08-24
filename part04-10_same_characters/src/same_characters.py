# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, ch1, ch2):
    if ch1 >= len(word) or ch2 >= len(word):
        return False
    return word[ch1] == word[ch2]

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))