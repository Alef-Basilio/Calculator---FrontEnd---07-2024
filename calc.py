import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("626x780")

image_path = Image.open("d:/NonProCode/projetos/Calc---FrontEnd/bkgd.jpg")
bkgd = ImageTk.PhotoImage(image_path)
bg_image = tk.Label(root, image = bkgd)
bg_image.place(relheight = 1, relwidth = 1)

calculation = ""

frame = tk.Frame(root)
frame.pack()

text_result = tk.Text(frame, height=2, width=16, font=("Arial", 22))
text_result.grid(columnspan = 5)
text_result.pack()

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

colm1 = tk.Frame(root)
colm1.place(x = 170, y = 320)

colm2 = tk.Frame(root)
colm2.place(x = 240, y = 320)

colm3 = tk.Frame(root)
colm3.place(x = 312, y = 320)

colm4 = tk.Frame(root)
colm4.place(x = 384, y = 320)


tk.Button(colm1, text="1", command=lambda: add_to_calculation(1), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm1, text="4", command=lambda: add_to_calculation(4), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm1, text="7", command=lambda: add_to_calculation(7), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm1, text="0", command=lambda: add_to_calculation(0), width=5, height=2,
font=("Arial", 14)).pack()

tk.Button(colm2, text="2", command=lambda: add_to_calculation(2), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm2, text="5", command=lambda: add_to_calculation(5), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm2, text="8", command=lambda: add_to_calculation(8), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm2, text="C", command=clear_field, width=5, height=2,
font=("Arial", 14)).pack()

tk.Button(colm3, text="3", command=lambda: add_to_calculation(3), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm3, text="6", command=lambda: add_to_calculation(6), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm3, text="9", command=lambda: add_to_calculation(9), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm3, text="+", command=lambda: add_to_calculation("+"), width=5, height=2,
font=("Arial", 14)).pack()

tk.Button(colm4, text="/", command=lambda: add_to_calculation("/"), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm4, text="*", command=lambda: add_to_calculation("*"), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm4, text="-", command=lambda: add_to_calculation("-"), width=5, height=2,
font=("Arial", 14)).pack()
tk.Button(colm4, text="=", command=evaluate_calculation, width=5, height=2,
font=("Arial", 14)).pack()

root.mainloop()