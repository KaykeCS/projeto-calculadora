import tkinter as tk
from tkinter import ttk

# Cores
cor1 = '#3b3b3b'  # Preto
cor2 = '#feffff'  # Branca
cor3 = '#38576b'  # Azul
cor4 = '#ECEFF1'  # Cinzenta
cor5 = '#FFAB40'  # Laranja


class MyApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.geometry('235x318')
        self.root.config(bg=cor1)
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure('My.TFrame', background=cor3)

        self.frm = ttk.Frame(self.root, width=235,
                             height=50, style='My.TFrame')
        self.frm.grid(row=0, column=0)

        self.frm_body = ttk.Frame(self.root, width=235, height=268)
        self.frm_body.grid(row=1, column=0)


def main():
    root = tk.Tk()
    MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
