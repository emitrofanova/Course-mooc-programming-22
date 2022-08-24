# write your solution here
def read_fruits():
    with open("fruits.csv") as file:
        dct = {}
        for line in file:
            fruit = line.replace("\n", "")
            fruit = fruit.split(";")
            dct[fruit[0]] = float(fruit[1])
    return dct

if __name__ == "__main__":
    print(read_fruits())
