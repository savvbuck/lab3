from tkinter import *
from tkinter import ttk
import re
import itertools
import random


WIDTH = 1024
HEIGHT = 576
INDENT = 6
KEY_LENGTH = 6
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

def is_valid(newval, key_l=KEY_LENGTH):
    result = re.match(f"([A-Z]|[a-z]){{0,{key_l}}}$", newval) is not None
    if not result and len(newval) <= key_l + 1:
        errmsg.set("Word should consist of 6 latinic letters")
    else:
        errmsg.set("")
    return result


window = Tk()
window.title('Keygen')
window.geometry(f'{WIDTH}x{HEIGHT}')
window.resizable(False, False)

bg = PhotoImage(file='simple.png')
errmsg = StringVar()
check = (window.register(is_valid), "%P")

canvas1 = Canvas(window, width=WIDTH, height=HEIGHT)
canvas1.pack(fill=BOTH, expand=True)
canvas1.create_image(0, 0, anchor='nw', image=bg)

frame = ttk.Frame(canvas1, borderwidth=1, relief=SOLID, padding=[8, 10])
frame.place(anchor='c', relx=0.5, rely=0.5)

label_ent = ttk.Label(frame, text=f"Enter {KEY_LENGTH}-letter word")
label_ent.pack(anchor='nw')

entry = ttk.Entry(frame, validate="key", validatecommand=check)
entry.pack(anchor='nw', padx=INDENT, pady=INDENT)

label_output = ttk.Label(frame)
label_output.pack(anchor='nw', padx=INDENT, pady=INDENT)

label_err = ttk.Label(frame, foreground='red', textvariable=errmsg)
label_err.pack(anchor='nw', padx=INDENT, pady=INDENT)

button1 = ttk.Button(canvas1, text="Generate key", command=show_text) 
button1.place(anchor='c', relx=0.5, y=HEIGHT//1.5) 


window.mainloop()
