# Write your solution here
def length_of_longest(l):
    length = 0
    for i in l:
        if len(i) > length:
            length = len(i)
    return length

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
