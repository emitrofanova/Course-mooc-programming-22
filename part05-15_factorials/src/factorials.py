# Write your solution here
def factorials(n: int):
    dct = {}
    for i in range(1, n + 1):
        if i != 1:
            dct[i] = i * dct[i-1]
        else:
            dct[i] = 1
    return dct

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
