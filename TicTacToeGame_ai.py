import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

current_player = "X"
winner = False

label = tk.Label(root, text="Your Turn (X)", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

buttons = []

# Winning combinations
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def get_board():
    return [btn["text"] for btn in buttons]


def check_board(board):
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def check_winner():
    global winner

    board = get_board()
    result = check_board(board)

    if result == "X":
        winner = True
        messagebox.showinfo("Game Over", "You Win!")
        return

    elif result == "O":
        winner = True
        messagebox.showinfo("Game Over", "AI Wins!")
        return

    elif result == "Draw":
        winner = True
        messagebox.showinfo("Game Over", "It's a Draw!")
        return


def minimax(board, is_maximizing):
    result = check_board(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == "":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = ""

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == "":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = ""

                best_score = min(best_score, score)

        return best_score


def best_move():
    board = get_board()

    best_score = -100
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    return move


def ai_move():
    global winner

    if winner:
        return

    move = best_move()

    if move is not None:
        buttons[move]["text"] = "O"

        check_winner()

        if not winner:
            label.config(text="Your Turn (X)")


def button_click(index):
    global winner

    if winner:
        return

    if buttons[index]["text"] == "":
        buttons[index]["text"] = "X"

        check_winner()

        if not winner:
            label.config(text="AI Thinking...")
            root.after(300, ai_move)


def reset_game():
    global winner

    winner = False

    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")

    label.config(text="Your Turn (X)")


# Create buttons
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

reset_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 12),
    command=reset_game
)

reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()