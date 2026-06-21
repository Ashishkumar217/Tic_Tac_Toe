import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game state
current_player = "X"
winner = False

# Label to show current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Create 3x3 buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: None)  # placeholder, will set below
    buttons.append(btn)

def check_winner():
    global winner
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combos:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} Wins!")
            winner = True
            return

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def button_click(index):
    global winner
    if winner:
        return
    btn = buttons[index]
    if btn["text"] == "":
        btn["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# Attach correct command handlers and place buttons in grid
for i, btn in enumerate(buttons):
    btn.config(command=lambda i=i: button_click(i))
    btn.grid(row=i // 3, column=i % 3)

root.mainloop()