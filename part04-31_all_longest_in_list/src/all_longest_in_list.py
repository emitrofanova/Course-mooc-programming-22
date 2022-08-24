# Write your solution here
# Write your solution here
def all_the_longest(l):
    length = 0
    answ = []
    for i in l:
        if len(i) > length:
            length = len(i)
    for i in l:
        if len(i) == length:
            answ.append(i)
    return answ

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)
