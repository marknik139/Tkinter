from tkinter import *


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


def init_interface():
    btn_1 = Button(root, text="1", command = lambda: add_to_calculation(1), width=5, font=("Arial", 15), bg=button_color)
    btn_1.grid(row=2, column=1)
    btn_2 = Button(root, text="2", command = lambda: add_to_calculation(2), width=5, font=("Arial", 15), bg=button_color)
    btn_2.grid(row=2, column=2)
    btn_3 = Button(root, text="3", command = lambda: add_to_calculation(3), width=5, font=("Arial", 15), bg=button_color)
    btn_3.grid(row=2, column=3)
    btn_plus = Button(root, text="+", command = lambda: add_to_calculation("+"), width=5, font=("Arial", 15), bg=button_color)
    btn_plus.grid(row=2, column=4)

    btn_4 = Button(root, text="4", command = lambda: add_to_calculation(4), width=5, font=("Arial", 15), bg=button_color)
    btn_4.grid(row=3, column=1)
    btn_5 = Button(root, text="5", command = lambda: add_to_calculation(5), width=5, font=("Arial", 15), bg=button_color)
    btn_5.grid(row=3, column=2)
    btn_1 = Button(root, text="6", command = lambda: add_to_calculation(6), width=5, font=("Arial", 15), bg=button_color)
    btn_1.grid(row=3, column=3)
    btn_minus = Button(root, text="-", command = lambda: add_to_calculation("-"), width=5, font=("Arial", 15), bg=button_color)
    btn_minus.grid(row=3, column=4)

    btn_7 = Button(root, text="7", command = lambda: add_to_calculation(7), width=5, font=("Arial", 15), bg=button_color)
    btn_7.grid(row=4, column=1)
    btn_8 = Button(root, text="8", command = lambda: add_to_calculation(8), width=5, font=("Arial", 15), bg=button_color)
    btn_8.grid(row=4, column=2)
    btn_9 = Button(root, text="9", command = lambda: add_to_calculation(9), width=5, font=("Arial", 15), bg=button_color)
    btn_9.grid(row=4, column=3)
    btn_mul = Button(root, text="*", command = lambda: add_to_calculation("*"), width=5, font=("Arial", 15), bg=button_color)
    btn_mul.grid(row=4, column=4)

    btn_0 = Button(root, text="0", command = lambda: add_to_calculation(0), width=5, font=("Arial", 15), bg=button_color)
    btn_0.grid(row=5, column=2)
    btn_div = Button(root, text="/", command = lambda: add_to_calculation("/"), width=5, font=("Arial", 15), bg=button_color)
    btn_div.grid(row=5, column=4)
    btn_open = Button(root, text="(", command = lambda: add_to_calculation("("), width=5, font=("Arial", 15), bg=button_color)
    btn_open.grid(row=5, column=1)
    btn_close = Button(root, text=")", command = lambda: add_to_calculation(")"), width=5, font=("Arial", 15), bg=button_color)
    btn_close.grid(row=5, column=3)

    btn_equal = Button(root, text="=", command = lambda: evaluate_calculation(), width=11, font=("Arial", 15), bg=button_color)
    btn_equal.grid(row=6, column=3, columnspan=2)
    btn_clear = Button(root, text="C", command = lambda: clear_field(), width=11, font=("Arial", 15), bg=button_color)
    btn_clear.grid(row=6, column=1, columnspan=2)


root = Tk()
root.geometry("300x275")
root.configure(bg="#363636")
root.resizable(False, False)
text_result = Text(root, height=2, width=16, font=("Arial", 25), bg="#363636", fg="white")
text_result.grid(columnspan=5)

calculation = ""
button_color = "orange"
init_interface()
root.mainloop()