# Write your solution here
def invert(dictionary: dict):
    dct_invert = {}
    for key, value in dictionary.items():
        dct_invert[value] = key
    dictionary.clear()
    for i in dct_invert:
        dictionary[i] = dct_invert[i]

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
