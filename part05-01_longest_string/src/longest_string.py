# Write your solution here

def longest(strings: list):
    max = 0
    for i in strings:
        if len(i) > max:
            max = len(i)
            answ = i
    return answ

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
