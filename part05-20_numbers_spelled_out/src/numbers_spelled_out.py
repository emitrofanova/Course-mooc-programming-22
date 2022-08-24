# Write your solution here
def dict_of_numbers():
    dct = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty"}
    for i in range(21, 100):
        if i % 10 == 0 and i != 20 and i != 80 and i != 40:
            dct[i] = dct[10 + i // 10][0:len(dct[10 + i // 10]) - 3] + "y"
        elif i == 40:
            dct[i] = "forty"
        elif i == 80:
            dct[i] = "eighty"
        else:
            dct[i] = dct[i - i % 10] + "-" + dct[i % 10]
        
    return(dct)


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[18])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
