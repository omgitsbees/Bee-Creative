import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 15
letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

def initialize_board():
    return [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def place_word(board, word, row, col, direction):
    word = word.upper()
    if direction == 'H':
        if col + len(word) > BOARD_SIZE:
            return False  # Out of bounds
        for i, letter in enumerate(word):
            board[row][col + i] = letter
    elif direction == 'V':
        if row + len(word) > BOARD_SIZE:
            return False  # Out of bounds
        for i, letter in enumerate(word):
            board[row + i][col] = letter
    else:
        return False  # Invalid direction
    return True

def calculate_score(word):
    return sum(letter_points.get(letter, 0) for letter in word.upper())

class ScrabbleGame:
    def __init__(self, root):
        self.board = initialize_board()
        self.root = root
        self.root.title("Scrabble Game")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.grid(row=0, column=0, columnspan=10)

        self.update_board()

        self.word_entry = tk.Entry(root)
        self.word_entry.grid(row=1, column=0, columnspan=2)

        self.row_entry = tk.Entry(root, width=5)
        self.row_entry.grid(row=1, column=2)

        self.col_entry = tk.Entry(root, width=5)
        self.col_entry.grid(row=1, column=3)

        self.direction_var = tk.StringVar(value="H")
        tk.Radiobutton(root, text="Horizontal", variable=self.direction_var, value="H").grid(row=1, column=4)
        tk.Radiobutton(root, text="Vertical", variable=self.direction_var, value="V").grid(row=1, column=5)

        self.place_button = tk.Button(root, text="Place Word", command=self.place_word_on_board)
        self.place_button.grid(row=1, column=6)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.grid(row=1, column=7)

    def update_board(self):
        self.canvas.delete("all")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x0, y0 = j * 40, i * 40
                x1, y1 = x0 + 40, y0 + 40
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                if self.board[i][j] != '.':
                    self.canvas.create_text(x0 + 20, y0 + 20, text=self.board[i][j], font=("Arial", 20))

    def place_word_on_board(self):
        word = self.word_entry.get()
        try:
            row = int(self.row_entry.get())
            col = int(self.col_entry.get())
            direction = self.direction_var.get()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid row and column numbers.")
            return

        if place_word(self.board, word, row, col, direction):
            score = calculate_score(word)
            self.update_board()
            self.score_label.config(text=f"Score: {score}")
            self.word_entry.delete(0, tk.END)
            self.row_entry.delete(0, tk.END)
            self.col_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid move", "The word cannot be placed at the specified location.")

if __name__ == "__main__":
    root = tk.Tk()
    game = ScrabbleGame(root)
    root.mainloop()
