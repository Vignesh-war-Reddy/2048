import tkinter as tk
from tkinter import messagebox
import logic

class Game2048(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2048")
        self.geometry("600x600")
        self.configure(bg="lightgray")

        self.mat = logic.start_game()

        self.grid_frame = tk.Frame(self, bg="gray")
        self.grid_frame.pack(padx=10, pady=10, expand=True, fill="both")

        self.buttons = [[tk.Button(self.grid_frame, text="", font=('Arial', 24), width=5, height=2, bg="white", command=lambda r=r, c=c: None) for c in range(4)] for r in range(4)]
        for r in range(4):
            for c in range(4):
                self.buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

        self.update_grid()

        self.bind("<KeyPress>", self.handle_keypress)

    def update_grid(self):
        for r in range(4):
            for c in range(4):
                value = self.mat[r][c]
                self.buttons[r][c].config(text="" if value == 0 else str(value))
                self.buttons[r][c].config(bg=self.get_color(value))

    def get_color(self, value):
        colors = {
            0: "white",
            2: "lightyellow",
            4: "lightblue",
            8: "lightgreen",
            16: "lightcoral",
            32: "lightpink",
            64: "lightgray",
            128: "lightcyan",
            256: "lightgoldenrod",
            512: "lightseagreen",
            1024: "lightsalmon",
            2048: "lightsteelblue"
        }
        return colors.get(value, "lightgrey")

    def handle_keypress(self, event):
        if event.keysym in ('Up', 'Down', 'Left', 'Right'):
            if event.keysym == 'Up':
                self.mat, changed = logic.move_up(self.mat)
            elif event.keysym == 'Down':
                self.mat, changed = logic.move_down(self.mat)
            elif event.keysym == 'Left':
                self.mat, changed = logic.move_left(self.mat)
            elif event.keysym == 'Right':
                self.mat, changed = logic.move_right(self.mat)
            
            if changed:
                logic.add_new_2(self.mat)
                self.update_grid()
                status = logic.get_current_state(self.mat)
                if status == 'WON':
                    messagebox.showinfo("2048", "Congratulations! You won!")
                    self.mat = logic.start_game()
                    self.update_grid()
                elif status == 'LOST':
                    messagebox.showinfo("2048", "Game Over!")
                    self.mat = logic.start_game()
                    self.update_grid()

if __name__ == "__main__":
    app = Game2048()
    app.mainloop()
