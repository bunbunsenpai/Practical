def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return 10 if row[0] == ai_player else -10

    for col in range(len(board)):
        check_col = [row[col] for row in board]
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != " ":
            return 10 if check_col[0] == ai_player else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == ai_player else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == ai_player else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_player
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human_player
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_player
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_tic_tac_toe():
    global ai_player, human_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = input("Choose X or O: ").upper()
    while human_player not in ["X", "O"]:
        human_player = input("Invalid choice. Choose X or O: ").upper()
    ai_player = "O" if human_player == "X" else "X"
    print_board(board)
    move_count = 0

    while evaluate(board) == 0 and is_moves_left(board):
        if move_count % 2 == 0:
            move = int(input("Your move (1-9): "))
            while move < 1 or move > 9 or board[(move - 1) // 3][(move - 1) % 3] != " ":
                move = int(input("Invalid move. Try again (1-9): "))
            board[(move - 1) // 3][(move - 1) % 3] = human_player
        else:
            print("AI is thinking...")
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = ai_player
            print(f"AI played at {(ai_move[0] * 3) + ai_move[1] + 1}")
        print_board(board)
        move_count += 1

    result = evaluate(board)
    if result == 10:
        print("AI wins!")
    elif result == -10:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
