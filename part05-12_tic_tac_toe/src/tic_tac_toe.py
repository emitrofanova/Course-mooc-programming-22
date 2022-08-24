# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False
    elif game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "X", "O"], ["O", "", "O"], ["O", "X", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
