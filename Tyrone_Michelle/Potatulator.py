import tkinter as tk
import math


# back end
def set_text(text):
    calc.delete(0, "end")
    calc.insert(0, text)


'''equal = bool(False)
def switchEqual():
    equal = True'''


def perf_calc(text):
    text = text.split()
    return eval(text)


def set_product(old, new):
    old += new


# front end

# HEX CODES:
# Yellow: #FFFF00
# Orange: #FF8C00
# Green: #00FF00

main = tk.Tk()
main.title("POTATULATOR")

frame = tk.Frame(width=500, height=500, bg="#D3D3D3")
frame.pack()

calc = tk.Entry(frame, justify="right", bd=3, bg="#D3D3D3", fg="#FF8C00", font=5)
calc.pack()
calc.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.05)

prompt = tk.Label(frame, text="Type with these buttons :)", bd=2,
                  anchor="center", bg="#d3d3d3", fg="black", font=5)
prompt.pack()
prompt.place(relx=0.05, rely=0.05, relheight=0.05, relwidth=0.9)

clear = tk.Button(frame, text="C", font=5, command=lambda: set_text(""))
clear.pack()
clear.place(relx=0.05, rely=0.1, relwidth=0.05, relheight=0.05)

result = tk.Label(frame, text="0", bd=3, anchor="e", bg="#FF69B4", fg="#D3D3D3", font=5)
result.pack()
result.place(relx=0.15, rely=0.1, relwidth=0.8, relheight=0.05)

# first row of buttons
plus = tk.Button(frame, text="+", font=5, bg="black", fg="#FF8C00",
                 command=lambda: set_text(calc.get() + "+"))
plus.pack()
plus.place(relx=0.05, rely=0.2, relwidth=0.1875, relheight=0.1)

sub = tk.Button(frame, text="-", font=5, bg="black", fg="#00ff00",
                command=lambda: set_text(calc.get() + "-"))
sub.pack()
sub.place(relx=0.2875, rely=0.2, relwidth=0.1875, relheight=0.1)

mult = tk.Button(frame, text="x", font=5, bg="black", fg="#ffff00",
                 command=lambda: set_text(calc.get() + "*"))
mult.pack()
mult.place(relx=0.525, rely=0.2, relwidth=0.1875, relheight=0.1)

div = tk.Button(frame, text="÷", font=5, bg="black", fg="#FF69B4",
                command=lambda: set_text(calc.get() + "/"))
div.pack()
div.place(relx=0.7625, rely=0.2, relwidth=0.1875, relheight=0.1)

# second row of buttons
sin = tk.Button(frame, text="sin", font=5, bg='black', fg='#FF8C00',
                command=lambda: set_text(calc.get() + "math.sin("))
sin.pack()
sin.place(relx=0.05, rely=0.35, relwidth=0.1875, relheight=0.1)

one = tk.Button(frame, text="1", font=5, bg="black", fg="#00ff00",
                command=lambda: set_text(calc.get() + "1"))
one.pack()
one.place(relx=0.2875, rely=0.35, relwidth=0.1875, relheight=0.1)

two = tk.Button(frame, text="2", font=5, bg="black", fg="#ffff00",
                command=lambda: set_text(calc.get() + "2"))
two.pack()
two.place(relx=0.525, rely=0.35, relwidth=0.1875, relheight=0.1)

three = tk.Button(frame, text="3", font=5, bg="black", fg="#FF69B4",
                  command=lambda: set_text(calc.get() + "3"))
three.pack()
three.place(relx=0.7625, rely=0.35, relwidth=0.1875, relheight=0.1)

# third row of buttons
cos = tk.Button(frame, text="cos", font=5, bg='black', fg='#FF8C00',
                command=lambda: set_text(calc.get() + "math.cos("))
cos.pack()
cos.place(relx=0.05, rely=0.5, relwidth=0.1875, relheight=0.1)

four = tk.Button(frame, text="4", font=5, bg="black", fg="#00ff00",
                 command=lambda: set_text(calc.get() + "4"))
four.pack()
four.place(relx=0.2875, rely=0.5, relwidth=0.1875, relheight=0.1)

five = tk.Button(frame, text="5", font=5, bg="black", fg="#ffff00",
                 command=lambda: set_text(calc.get() + "5"))
five.pack()
five.place(relx=0.525, rely=0.5, relwidth=0.1875, relheight=0.1)

six = tk.Button(frame, text="6", font=5, bg="black", fg="#FF69B4",
                command=lambda: set_text(calc.get() + "6"))
six.pack()
six.place(relx=0.7625, rely=0.5, relwidth=0.1875, relheight=0.1)

# fourth row of buttons
tan = tk.Button(frame, text="tan", font=5, bg='black', fg='#FF8C00',
                command=lambda: set_text(calc.get() + "math.tan("))
tan.pack()
tan.place(relx=0.05, rely=0.65, relwidth=0.1875, relheight=0.1)

seven = tk.Button(frame, text="7", font=5, bg="black", fg="#00ff00",
                  command=lambda: set_text(calc.get() + "7"))
seven.pack()
seven.place(relx=0.2875, rely=0.65, relwidth=0.1875, relheight=0.1)

eight = tk.Button(frame, text="8", font=5, bg="black", fg="#ffff00",
                  command=lambda: set_text(calc.get() + "8"))
eight.pack()
eight.place(relx=0.525, rely=0.65, relwidth=0.1875, relheight=0.1)

nine = tk.Button(frame, text="9", font=5, bg="black", fg="#FF69B4",
                 command=lambda: set_text(calc.get() + "9"))
nine.pack()
nine.place(relx=0.7625, rely=0.65, relwidth=0.1875, relheight=0.1)

# fifth row of buttons
pi = tk.Button(frame, text="π", font=5, bg='black', fg='#FF8C00',
                 command=lambda: set_text(calc.get() + "3.1416"))
pi.pack()
pi.place(relx=0.05, rely=0.8, relwidth=0.1875, relheight=0.1)

zero = tk.Button(frame, text="0", font=5, bg="black", fg="#00ff00",
                 command=lambda: set_text(calc.get() + "0"))
zero.pack()
zero.place(relx=0.2875, rely=0.8, relwidth=0.1875, relheight=0.1)

exp = tk.Button(frame, text="^", font=5, bg="black", fg="#ffff00",
                command=lambda: set_text(calc.get() + "**"))
exp.pack()
exp.place(relx=0.525, rely=0.8, relwidth=0.1875, relheight=0.1)

sqrt = tk.Button(frame, text="√", font=5, bg="black", fg="#FF69B4",
                 command=lambda: set_text(calc.get() + "math.sqrt("))
sqrt.pack()
sqrt.place(relx=0.7625, rely=0.8, relwidth=0.1875, relheight=0.1)


# equal n brackets
openBra = tk.Button(frame, text="(", font=5, bg="black", fg="#AFEEEE",
                    command=lambda: set_text(calc.get() + "("))
openBra.pack()
openBra.place(relx=0.05, rely=0.95, relwidth=0.18, relheight=0.05)

equals = tk.Button(frame, text="=", font=5, bg="black", fg="#AFEEEE", command=lambda: result.config(text=str(eval(calc.get()))))
equals.pack()
equals.place(relx=0.23, rely=0.95, relwidth=0.54, relheight=0.05)

closeBra = tk.Button(frame, text=")", font=5, bg="black", fg="#AFEEEE",
                     command=lambda: set_text(calc.get() + ")"))
closeBra.pack()
closeBra.place(relx=0.77, rely=0.95, relwidth=0.18, relheight=0.05)



main.mainloop()


