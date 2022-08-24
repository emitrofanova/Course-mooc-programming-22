# Write your solution here
from string import ascii_lowercase, digits
from random import randint, shuffle

def generate_strong_password(numb, stat1, stat2):
    answ = []
    abc_str = ascii_lowercase
    abc = []
    for ch in abc_str:
        abc.append(ch)
    shuffle(abc)
    numbers_str = digits + digits
    numbers = []
    for ch in numbers_str:
        numbers.append(ch)
    shuffle(numbers)
    spc_ch_str = "!?=+-()#!?=+-()#!?=+-()#"
    spc_ch = []
    for ch in spc_ch_str:
        spc_ch.append(ch)
    shuffle(spc_ch)
    if stat1:
        if stat2:
            amount1 = randint(1, numb // 3)
            amount2 = randint(1, numb // 3)
            amount3 = numb - amount1 - amount2
            answ = abc[:amount1] + numbers[:amount2] + spc_ch[:amount3]
        else:
            amount1 = randint(1, numb // 2)
            amount2 = numb - amount1
            answ = abc[:amount1] + numbers[:amount2]
    elif stat2:
        amount1 = randint(1, numb // 2)
        amount2 = numb - amount1
        answ = abc[:amount1] + spc_ch[:amount2]
    else:
        answ = abc[:numb]
    shuffle(answ)
    answ_str = ""
    for ch in answ:
        answ_str += ch
    return answ_str

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(12, True, True))
