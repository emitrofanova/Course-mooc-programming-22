# Write your solution here

def most_common_character(s):
    counter = 0
    max = 0
    for ch in s:
        counter = s.count(ch)
        if counter > max:
            answ = ch
            max = counter
        counter = 0
    return answ


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))