# Write your solution here

def no_vowels(s):
    s = s.replace("a", "")
    s = s.replace("e", "")
    s = s.replace("i", "")
    s = s.replace("o", "")
    s = s.replace("u", "")
    return s


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
