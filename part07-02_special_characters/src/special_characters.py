# Write your solution here
import string

def separate_characters(my_string: str):
    answ_list = ["", "", ""]
    for word in my_string:
        for ch in word:
            if ch in string.ascii_letters:
                answ_list[0] += ch
            elif ch in string.punctuation:
                answ_list[1] += ch
            else:
                answ_list[2] += ch
    return (answ_list[0], answ_list[1], answ_list[2])


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
