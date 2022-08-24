# Write your solution here
def even_numbers(l):
    new_l = []
    for i in l:
        if i % 2 == 0:
            new_l.append(i)
    return new_l

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
