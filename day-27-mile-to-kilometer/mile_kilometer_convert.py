from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(width=400, height=200, padx=20, pady=20)


# Entry
entry = Entry(width=15)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=5)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
miles_label.config(padx=20, pady=5)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=20, pady=5)
result_label = Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=20, pady=5)


# Button
def calculate():
    result = float(entry.get()) * 1.609
    result_label.config(text=f"{result:.2f}")


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()