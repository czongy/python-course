from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=entry.get())


# calls action() when pressed
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=3, row=0)

# Entries
entry = Entry(width=30)
# Gets text in entry
print(entry.get())
entry.grid(column=4, row=3)


window.mainloop()
