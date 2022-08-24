# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        dct_numb = {}
        for numb in my_list:
            if numb not in dct_numb:
                dct_numb[numb] = 0
            dct_numb[numb] += 1
        most_common = 0
        answ = ""
        for numb in dct_numb:
            if dct_numb[numb] > most_common:
                most_common = dct_numb[numb]
                answ = numb
        return answ

    @classmethod
    def doubles(cls, my_list: list):
        dct_numb = {}
        answ = 0
        for numb in my_list:
            if numb not in dct_numb:
                dct_numb[numb] = 0
            dct_numb[numb] += 1
        for numb in dct_numb:
            if dct_numb[numb] >= 2:
                answ += 1
        return answ

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
