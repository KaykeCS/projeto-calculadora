import tkinter as tk
from tkinter import ttk

# Cores


class Colors():
    color1 = '#3b3b3b'  # Preto
    color2 = '#feffff'  # Branca
    color3 = '#2a78f5'  # Azul
    color4 = '#575959'  # Cinzenta
    color5 = '#FFAB40'  # Laranja


class MyApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.geometry('235x318')
        self.root.config(bg=Colors.color2)
        self.create_widgets()

    def create_widgets(self):
        self.frm_head = tk.Frame(self.root, width=235,
                                 height=50, bg=Colors.color1)
        self.frm_head.grid(row=0, column=0)


def main():
    root = tk.Tk()
    MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
