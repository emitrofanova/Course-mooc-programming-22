# Write your solution here

def who_won(game_board: list):
    cnt1 = 0
    cnt2 = 0
    for row in game_board:
        for i in row:
            if i == 1:
                cnt1 += 1
            if i == 2:
                cnt2 += 1
    if cnt1 > cnt2:
        return 1
    elif cnt2 > cnt1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    final = who_won([[0, 0, 1], [2, 0, 1]])
    print(final)
