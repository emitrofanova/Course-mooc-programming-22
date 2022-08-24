# Write your solution here
def shortest(l):
    length = 100
    for i in l:
        if len(i) < length:
            length = len(i)
            answ = i
    return answ

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
