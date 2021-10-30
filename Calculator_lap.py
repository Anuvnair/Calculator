from tkinter import *


window = Tk()
window.title("Calculator")
i = 0


def btn_click(num):
    global i
    display.insert(i, num)
    i += 1


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        btn_clear()
        display.insert(0, result)
    except:
        btn_clear()
        display.insert(0, "error")


def btn_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def btn_clear():
    display.delete(0, END)


def btn_undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        btn_clear()
        display.insert(0, new_string)
    else:
        display.insert(0, "Error")
        btn_clear()


# adding the input field
display = Entry(window)
display.grid(row=1, columnspan=6, sticky=W + E)
# adding button to the calculator
Button(window, text="7", command=lambda: btn_click(7)).grid(row=2, column=0)
Button(window, text="8", command=lambda: btn_click(8)).grid(row=2, column=1)
Button(window, text="9", command=lambda: btn_click(9)).grid(row=2, column=2)

Button(window, text="4", command=lambda: btn_click(4)).grid(row=3, column=0)
Button(window, text="5", command=lambda: btn_click(5)).grid(row=3, column=1)
Button(window, text="6", command=lambda: btn_click(6)).grid(row=3, column=2)

Button(window, text="1", command=lambda: btn_click(1)).grid(row=4, column=0)
Button(window, text="2", command=lambda: btn_click(2), ).grid(row=4, column=1)
Button(window, text="3", command=lambda: btn_click(3)).grid(row=4, column=2)

Button(window, text="AC", command=lambda: btn_clear()).grid(row=5, column=0)
Button(window, text="0", command=lambda: btn_click(0)).grid(row=5, column=1)
Button(window, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(window, text="+", command=lambda: btn_operation("+")).grid(row=2, column=3)
Button(window, text="-", command=lambda: btn_operation("-")).grid(row=3, column=3)
Button(window, text="*", command=lambda: btn_operation("*")).grid(row=4, column=3)
Button(window, text="/", command=lambda: btn_operation("/")).grid(row=5, column=3)

Button(window, text="pi", command=lambda: btn_operation("*3.14")).grid(row=2, column=4)
Button(window, text="%", command=lambda: btn_operation("%")).grid(row=3, column=4)
Button(window, text="(", command=lambda: btn_operation("(")).grid(row=4, column=4)
Button(window, text="exp", command=lambda: btn_operation("**")).grid(row=5, column=4)

Button(window, text="<-", command=lambda: btn_undo()).grid(row=2, column=5)
Button(window, text=".", command=lambda: btn_operation(".")).grid(row=3, column=5)
Button(window, text=")", command=lambda: btn_operation(")")).grid(row=4, column=5)
Button(window, text="^2", command=lambda: btn_operation("**2")).grid(row=5, column=5)
window.mainloop()
