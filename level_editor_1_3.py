import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import json

class LevelEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("2D Level Editor")
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        # Undo/Redo Stacks
        self.undo_stack = []
        self.redo_stack = []

        # Shapes management
        self.shapes = []
        self.current_shape = None

        # Asset management
        self.assets = {
            'Square': {'type': 'shape', 'data': [(0, 0, 50, 50)]},
            'Circle': {'type': 'shape', 'data': [(0, 0, 50, 50)]},
            'Triangle': {'type': 'shape', 'data': [(0, 0, 50, 50, 25, 0)]},
            'Image 1': {'type': 'image', 'data': None},  # Placeholder for image data
            'Image 2': {'type': 'image', 'data': None},  # Placeholder for image data
        }

        self.current_asset = None

        self.setup_menu()
        self.setup_bindings()

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_level)
        filemenu.add_command(label="Open", command=self.open_level)
        filemenu.add_command(label="Save", command=self.save_level)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Edit menu
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="Redo", command=self.redo)
        editmenu.add_separator()
        editmenu.add_command(label="Pick Color", command=self.pick_color)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        # Assets menu
        assetmenu = tk.Menu(menubar, tearoff=0)
        for asset_name in self.assets:
            asset_info = self.assets[asset_name]
            if asset_info['type'] == 'shape':
                assetmenu.add_command(label=asset_name, command=lambda name=asset_name: self.use_shape(name))
            elif asset_info['type'] == 'image':
                assetmenu.add_command(label=asset_name, command=lambda name=asset_name: self.use_image(name))
        menubar.add_cascade(label="Assets", menu=assetmenu)

        self.root.config(menu=menubar)

    def use_shape(self, asset_name):
        self.current_asset = asset_name
        self.current_shape = None
        self.redraw_assets()
        messagebox.showinfo("Asset Selected", f"Selected shape: {asset_name}")

    def use_image(self, asset_name):
        # Placeholder for loading image data
        self.current_asset = asset_name
        self.current_shape = None
        self.redraw_assets()
        messagebox.showinfo("Asset Selected", f"Selected image: {asset_name}")

    def redraw_assets(self):
        # Clear previous assets display
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

        # Redraw assets window
        assets_window = tk.Toplevel(self.root)
        assets_window.title("Assets")
        assets_window.geometry("200x300")

        for asset_name in self.assets:
            tk.Button(assets_window, text=asset_name, command=lambda name=asset_name: self.use_asset(name)).pack()

    def use_asset(self, asset_name):
        asset_info = self.assets[asset_name]
        if asset_info['type'] == 'shape':
            self.current_asset = asset_name
            self.current_shape = None
            self.redraw_assets()
            messagebox.showinfo("Asset Selected", f"Selected shape: {asset_name}")
        elif asset_info['type'] == 'image':
            self.current_asset = asset_name
            self.current_shape = None
            self.redraw_assets()
            messagebox.showinfo("Asset Selected", f"Selected image: {asset_name}")

    def save_state(self):
        current_state = self.shapes.copy()
        self.undo_stack.append(current_state)
        self.redo_stack.clear()
    
    def undo(self):
        if self.undo_stack:
            last_state = self.undo_stack.pop()
            self.redo_stack.append(last_state)
            self.shapes = last_state
            self.redraw()
        else:
            messagebox.showinfo("Undo", "Nothing to undo")
        
    def redo(self):
        if self.redo_stack:
            next_state = self.redo_stack.pop()
            self.undo_stack.append(next_state)
            self.shapes = next_state
            self.redraw()
        else:
            messagebox.showinfo("Redo", "Nothing to redo")

    def setup_bindings(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def new_level(self):
        self.shapes = []
        self.redraw()

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
        if self.current_asset:
            if self.current_asset in self.assets:
                asset_info = self.assets[self.current_asset]
                if asset_info['type'] == 'shape':
                    self.add_shape(event.x, event.y, asset_info['data'])
                    self.save_state()
                    self.redraw()
                elif asset_info['type'] == 'image':
                    pass  # Placeholder for image handling
            else:
                messagebox.showerror("Error", "Invalid asset selected")
        else:
            messagebox.showerror("Error", "No asset selected")

    def add_shape(self, x, y, shape_data):
        for shape_coords in shape_data:
            self.shapes.append((x + shape_coords[0], y + shape_coords[1], x + shape_coords[2], y + shape_coords[3]))

    def on_drag(self, event):
        pass  # Handle drag events as needed

    def on_release(self, event):
        pass  # Handle release events as needed

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code:
            self.current_color = color_code[1]
    
    def redraw(self):
        self.canvas.delete("all")
        for shape_coords in self.shapes:
            self.canvas.create_rectangle(shape_coords, outline="black", fill="")
    
    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LevelEditor(root)
    app.main()
