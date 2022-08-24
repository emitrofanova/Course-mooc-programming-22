# Write your solution here
def histogram(st: str):
    dct_letters = {}
    for ch in st:
        if ch not in dct_letters:
            dct_letters[ch] = 0
        dct_letters[ch] += 1
    for key, value in dct_letters.items():
        print(key, "*" * value)

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
