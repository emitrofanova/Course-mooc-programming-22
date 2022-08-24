# Write your solution here
from fractions import Fraction as frac

def fractionate(amount: int):
    cnt = 0
    answ = []
    while cnt != amount:
        answ.append(frac(1, amount))
        cnt += 1
    return answ

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))
