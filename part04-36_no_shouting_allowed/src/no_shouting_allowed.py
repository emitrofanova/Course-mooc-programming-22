# Write your solution here

def no_shouting(l):
    new_l = []
    for i in l:
        if not i.isupper():
            new_l.append(i)
    return new_l

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
