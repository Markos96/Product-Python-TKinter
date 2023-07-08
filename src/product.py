from tkinter import Tk, Canvas, Frame, Label, Entry, Button
import psycopg2

root = Tk()
root.title("Product crud")

# Canvas
canvas = Canvas(root, height=380, width=400)
canvas.pack()

# Frame
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


# Labels
label = Label(frame, text="Add Product")
label.grid(row=0, column=1)

label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name_product = Entry(frame)
entry_name_product.grid(row=1, column=1)

label = Label(frame, text="Category")
label.grid(row=2, column=0)

entry_price_product = Entry(frame)
entry_price_product.grid(row=2, column=1)

label = Label(frame, text="Price")
label.grid(row=3, column=0)

entry_category_product = Entry(frame)
entry_category_product.grid(row=3, column=1)


# Button

button = Button(frame, text="Add")
button.grid(row=4, column=1)

root.mainloop()
