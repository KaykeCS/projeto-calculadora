import tkinter as tk
from tkinter import ttk
from tkinter import RAISED, RIDGE, FLAT, RIGHT

historical = []


class Colors():
    color1 = '#3b3b3b'  # Preto
    color2 = '#feffff'  # Branca
    color3 = '#38576b'  # Azul
    color4 = '#ECEFF1'  # Cinzenta
    color5 = '#FFAB40'  # Laranja


class MyApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.geometry('235x305')
        self.root.config(bg=Colors.color2)
        self.create_widgets()
        self.buttons()
        self.create_label()
        self.display_value = tk.StringVar()
        self.display_value.set("")
        self.all_values = ''

    def create_widgets(self):
        self.frm_head = tk.Frame(self.root,
                                 width=235,
                                 height=50,
                                 bg=Colors.color1)
        self.frm_head.grid(row=0, column=0)

        self.frm_body = ttk.Frame(self.root,
                                  width=235,
                                  height=268)
        self.frm_body.grid(row=1, column=0)

    def entry_values(self, event):
        global all_values
        self.all_values += str(event)
        self.value_text.set(self.all_values)

    def create_label(self):
        self.value_text = tk.StringVar()
        self.visor_label = tk.Label(self.frm_head,
                                    textvariable=self.value_text,
                                    width=16,
                                    height=2,
                                    padx=7,
                                    relief=FLAT,
                                    anchor='e',
                                    justify=RIGHT,
                                    font=('Arial', 18),
                                    bg=Colors.color3,
                                    fg=Colors.color2

                                    )
        self.visor_label.place(x=2, y=0)

    def calcular(self):
        global all_values
        self.result = eval(self.all_values)
        self.value_text.set(str(self.result))

    def clear_visor(self):
        global all_values
        self.all_values = ''
        self.value_text.set('')

    def buttons(self):
        self.button_C = tk.Button(
            self.frm_body,
            text='C',
            width=11,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=self.clear_visor)
        self.button_C.place(x=3, y=0)

        self.button_module = tk.Button(
            self.frm_body,
            text='%',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('%'))
        self.button_module.place(x=118, y=0)

        self.button_division = tk.Button(
            self.frm_body,
            text='/',
            width=5,
            height=2,
            bg=Colors.color5,
            fg=Colors.color2,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('/'))
        self.button_division.place(x=177, y=0)

        self.button_number_7 = tk.Button(
            self.frm_body,
            text='7',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('7'))
        self.button_number_7.place(x=0, y=52)

        self.button_number_8 = tk.Button(
            self.frm_body,
            text='8',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('8'))
        self.button_number_8.place(x=59, y=52)

        self.button_number_9 = tk.Button(
            self.frm_body,
            text='9',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('9'))
        self.button_number_9.place(x=118, y=52)

        self.button_multiplication = tk.Button(
            self.frm_body,
            text='*',
            width=5,
            height=2,
            bg=Colors.color5,
            fg=Colors.color2,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('*'))
        self.button_multiplication.place(x=177, y=52)

        self.button_number_4 = tk.Button(
            self.frm_body,
            text='4',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('4'))
        self.button_number_4.place(x=0, y=104)

        self.button_number_5 = tk.Button(
            self.frm_body,
            text='5',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('5'))
        self.button_number_5.place(x=59, y=104)

        self.button_number_6 = tk.Button(
            self.frm_body,
            text='6',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('6'))
        self.button_number_6.place(x=118, y=104)

        self.button_subtraction = tk.Button(
            self.frm_body,
            text='-',
            width=5,
            height=2,
            bg=Colors.color5,
            fg=Colors.color2,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('-'))
        self.button_subtraction.place(x=177, y=104)

        self.button_number_1 = tk.Button(
            self.frm_body,
            text='1',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('1'))
        self.button_number_1.place(x=0, y=155)

        self.button_number_2 = tk.Button(
            self.frm_body,
            text='2',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('2'))
        self.button_number_2.place(x=59, y=155)

        self.button_number_3 = tk.Button(
            self.frm_body,
            text='3',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('3'))
        self.button_number_3.place(x=118, y=155)

        self.button_adiction = tk.Button(
            self.frm_body,
            text='+',
            width=5,
            height=2,
            bg=Colors.color5,
            fg=Colors.color2,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('+'))

        self.button_adiction.place(x=177, y=155)

        self.button_number_0 = tk.Button(
            self.frm_body,
            text='0',
            width=11,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('0'))
        self.button_number_0.place(x=0, y=208)

        self.button_point = tk.Button(
            self.frm_body,
            text='.',
            width=5,
            height=2,
            bg=Colors.color4,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: self.entry_values('.'))
        self.button_point.place(x=118, y=208)

        self.button_equal = tk.Button(
            self.frm_body,
            text='=',
            width=5,
            height=2,
            bg=Colors.color5,
            fg=Colors.color2,
            font=('Ivy', 13, 'bold'),
            relief=RAISED,
            overrelief=RIDGE,
            command=self.calcular)
        self.button_equal.place(x=177, y=208)


def main():
    root = tk.Tk()
    MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
