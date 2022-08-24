# Write your solution here
def times_ten(start_index: int, end_index: int):
    dct = {}
    for i in range(start_index, end_index + 1):
        dct[i] = i * 10
    return dct

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
