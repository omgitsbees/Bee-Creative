import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import json

class LevelEditor:
    def __init__(self, root):
        self.new_level_data = None
        self.root = root
        self.root.title("2D Level Editor")
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        # Undo/Redo Stacks
        self.undo_stack = []
        self.redo_stack = []

        self.shapes = []
        self.current_shape = None
        self.current_color = "black"  # Default color

        self.setup_menu()
        self.setup_bindings()

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_level)
        filemenu.add_command(label="Open", command=self.open_level)
        filemenu.add_command(label="Save", command=self.save_level)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Pick Color", command=self.pick_color)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.root.config(menu=menubar)

    def setup_bindings(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def save_state(self):
        current_state = self.canvas.find_all()
        self.undo_stack.append(current_state)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            last_state = self.undo_stack.pop()
            self.redo_stack.append(last_state)
            self.canvas.delete("all")
            for item in last_state:
                self.canvas.create_rectangle(self.canvas.coords(item), fill='blue')
        else:
            messagebox.showinfo("Undo", "Nothing to undo")

    def redo(self):
        if self.redo_stack:
            next_state = self.redo_stack.pop()
            self.undo_stack.append(next_state)
            self.canvas.delete("all")
            for item in next_state:
                self.canvas.create_rectangle(self.canvas.coords(item), fill='blue')
        else:
            messagebox.showinfo("Redo", "Nothing to redo")

    def new_level(self):
        self.canvas.delete("all")
        self.shapes = []

    def open_level(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                self.shapes = json.load(file)
                self.redraw()

    def save_level(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.shapes, file)

    def on_click(self, event):
        self.current_shape = {'coords': (event.x, event.y, event.x, event.y), 'color': self.current_color}
        self.shapes.append(self.current_shape)
        self.redraw()

    def on_drag(self, event):
        if self.current_shape:
            self.current_shape['coords'] = (self.current_shape['coords'][0], self.current_shape['coords'][1], event.x, event.y)
            self.redraw()

    def on_release(self, event):
        self.current_shape = None

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code:
            self.current_color = color_code[1]

    def redraw(self):
        self.canvas.delete("all")
        for shape in self.shapes:
            self.canvas.create_rectangle(shape['coords'], outline=shape['color'], fill="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LevelEditor(root)
    root.mainloop()
