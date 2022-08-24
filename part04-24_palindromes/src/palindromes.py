# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(w):
    if w[len(w):0: -1] + w[0] == w:
        print(w, "is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

def words():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            break

words()
