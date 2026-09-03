import tkinter as tk
 
# 1. Create root window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
 
#Tell grid to split window width across 4 columns and 5 rows.
# Without this, each column only takes up as much width as it needs

for col in range(4):
    root.columnconfigure(col, weight=1)

for row in range(5):
    root.rowconfigure(row, weight=1)
 
 
# create a Display box where numbers and results show up.
# We use an Entry widget, not a Label, because we want it to look like a real calculator screen
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")  # spans all 4 columns

def click(char):
    display.insert(tk.END, char)

btn_7 = tk.Button(root, text="7", font=("Arial", 18), command=lambda: click("7"))
btn_7.grid(row=1, column=0, sticky="nsew")

btn_8 = tk.Button(root, text="8", font=("Arial", 18), command=lambda: click("8"))
btn_8.grid(row=1, column=1, sticky="nsew")

btn_9 = tk.Button(root, text="9", font=("Arial", 18), command=lambda: click("9"))
btn_9.grid(row=1, column=2, sticky="nsew")

btn_divide = tk.Button(root, text="/", font=("Arial", 18), command=lambda: click("/"))
btn_divide.grid(row=1, column=3, sticky="nsew")

btn_4 = tk.Button(root, text="4", font=("Arial", 18), command=lambda: click("4"))
btn_4.grid(row=2, column=0, sticky="nsew")

btn_5 = tk.Button(root, text="5", font=("Arial", 18), command=lambda: click("5"))
btn_5.grid(row=2, column=1, sticky="nsew")

btn_6 = tk.Button(root, text="6", font=("Arial", 18), command=lambda: click("6"))
btn_6.grid(row=2, column=2, sticky="nsew")

btn_times = tk.Button(root, text="*", font=("Arial", 18), command=lambda: click("*"))
btn_times.grid(row=2, column=3, sticky="nsew")

btn_1 = tk.Button(root, text="1", font=("Arial", 18), command=lambda: click("1"))
btn_1.grid(row=3, column=0, sticky="nsew")

btn_2 = tk.Button(root, text="2", font=("Arial", 18), command=lambda: click("2"))
btn_2.grid(row=3, column=1, sticky="nsew")

btn_3 = tk.Button(root, text="3", font=("Arial", 18), command=lambda: click("3"))
btn_3.grid(row=3, column=2, sticky="nsew")

btn_minus = tk.Button(root, text="-", font=("Arial", 18), command=lambda: click("-"))
btn_minus.grid(row=3, column=3, sticky="nsew")

btn_0 = tk.Button(root, text="0", font=("Arial", 18), command=lambda: click("0"))
btn_0.grid(row=4, column=1, sticky="nsew")

btn_plus = tk.Button(root, text="+", font=("Arial", 18), command=lambda: click("+"))
btn_plus.grid(row=4, column=3, sticky="nsew")

def clear():
    display.delete(0, tk.END)

btn_clear = tk.Button(root, text="C", font=("Arial", 18), command=clear)
btn_clear.grid(row=4, column=0, sticky="nsew")

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

btn_equals = tk.Button(root, text="=", font=("Arial", 18), command=calculate)
btn_equals.grid(row=4, column=2, sticky="nsew")

# 4. Start the loop nothing below this line will run until the window closes
root.mainloop()