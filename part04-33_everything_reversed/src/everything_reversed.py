# Write your solution here

def everything_reversed(l):
    new_l = []
    for i in l:
        new_l.append(i[::-1])
    return new_l[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
