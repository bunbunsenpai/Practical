def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup):
    return not (row_lookup[row] or slash_code_lookup[slash_code[row][col]] or backslash_code_lookup[backslash_code[row][col]])


def solve_n_queens_util(board, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup):
    n = len(board)
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup):
            board[i][col] = 1
            row_lookup[i] = True
            slash_code_lookup[slash_code[i][col]] = True
            backslash_code_lookup[backslash_code[i][col]] = True

            if solve_n_queens_util(board, col + 1, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup):
                return True

            board[i][col] = 0
            row_lookup[i] = False
            slash_code_lookup[slash_code[i][col]] = False
            backslash_code_lookup[backslash_code[i][col]] = False

    return False


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    slash_code = [[0] * n for _ in range(n)]
    backslash_code = [[0] * n for _ in range(n)]

    row_lookup = [False] * n
    slash_code_lookup = [False] * (2 * n - 1)
    backslash_code_lookup = [False] * (2 * n - 1)

    for r in range(n):
        for c in range(n):
            slash_code[r][c] = r + c
            backslash_code[r][c] = r - c + n - 1

    if not solve_n_queens_util(board, 0, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


if __name__ == "__main__":
    N = 8  # Change N for a different board size
    solve_n_queens(N)
