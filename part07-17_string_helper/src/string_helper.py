# Write your solution here
def change_case(orig_string: str):
    answ = ""
    for ch in orig_string:
        if ch.isupper():
            answ += ch.lower()
        else:
            answ += ch.upper()
    return answ

def split_in_half(orig_string: str):
    return (orig_string[0:len(orig_string) // 2], orig_string[len(orig_string) // 2:])

def remove_special_characters(orig_string: str):
    answ = ""
    for ch in orig_string:
        if ch.isalnum() or ch == " ":
            answ += ch
    return answ
