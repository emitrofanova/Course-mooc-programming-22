# Write your solution here
from random import randint

def roll(die: str):
    dct_dice = {"A": (3,3,3,3,3,6), "B": (2,2,2,5,5,5), "C": (1,4,4,4,4,4)}
    return dct_dice[die][randint(0, 5)]

def play(die1: str, die2: str, times: int):
    dct_dice = {"A": (3,3,3,3,3,6), "B": (2,2,2,5,5,5), "C": (1,4,4,4,4,4)}
    die1_won = 0
    die2_won = 0
    for i in range(times):
        first = dct_dice[die1][randint(0, 5)]
        second = dct_dice[die2][randint(0, 5)]
        if first > second:
            die1_won += 1
        elif first < second:
            die2_won += 1
    ties = times - die1_won - die2_won
    return (die1_won, die2_won, ties)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
