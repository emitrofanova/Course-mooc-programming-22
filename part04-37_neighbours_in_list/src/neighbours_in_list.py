# Write your solution here

def longest_series_of_neighbours(l):
    cnt = 0
    max = 0
    for i in range(0, len(l)-1):
        if l[i] + 1 == l[i + 1] or l[i] - 1 == l[i + 1]:
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
    return max + 1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
