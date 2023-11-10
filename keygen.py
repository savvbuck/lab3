from tkinter import *
from tkinter import ttk
import re
import itertools
import random

def generate(enter):
    key = ''
    letters = []
    numbers = []
    for i in range(len(enter)):
        letters.append(enter[i])
        numbers.append(str((ord(enter[i]) - ord('a') + 1) % 10))
    key += ''.join(random.choice(list(itertools.permutations(''.join(letters), 3))))
    key += ''.join(random.choice(list(itertools.permutations(''.join(numbers), 6))))
    key += ''.join(random.choice(list(itertools.permutations(''.join(letters), 3))))
    return key
    
def show_text():
    label_output['text'] = generate(entry.get())

def is_valid(newval):
    result = re.match("([A-Z]|[a-z]){0,6}$", newval) is not None
    if not result and len(newval) <= 7:
        errmsg.set("Word should consist of 6 latinic letters")
    else:
        errmsg.set("")
    return result


window = Tk()
window.title('Keygen')
window.geometry('1024x576')
window.resizable(False, False)

bg = PhotoImage(file='simple.png')
errmsg = StringVar()
check = (window.register(is_valid), "%P")

canvas1 = Canvas(window, width=1024, height=576)
canvas1.pack(fill=BOTH, expand=True)
canvas1.create_image(0, 0, anchor='nw', image=bg)

frame = ttk.Frame(canvas1, borderwidth=1, relief=SOLID, padding=[8, 10])
frame.place(anchor='c', relx=0.5, rely=0.5)

label_ent = ttk.Label(frame, text="Enter 6-letter word")
label_ent.pack(anchor='nw')

entry = ttk.Entry(frame, validate="key", validatecommand=check)
entry.pack(anchor='nw', padx=6, pady=6)

label_output = ttk.Label(frame)
label_output.pack(anchor='nw', padx=6, pady=6)

label_err = ttk.Label(frame, foreground='red', textvariable=errmsg)
label_err.pack(anchor='nw', padx=6, pady=6)

button1 = ttk.Button(canvas1, text="Generate key", command=show_text) 
button1.place(anchor='c', relx=0.5, y=390) 


window.mainloop()