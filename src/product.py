from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END, ttk
from function.product import save_new_product, get_products, get_product_by_id

root = Tk()
root.title("Product crud")

# Canvas
canvas = Canvas(root, height=250, width=450)
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

entry_category_product = Entry(frame)
entry_category_product.grid(row=2, column=1)

label = Label(frame, text="Price")
label.grid(row=3, column=0)

entry_price_product = Entry(frame)
entry_price_product.grid(row=3, column=1)

label_search = Label(frame, text="Search Data")
label_search.grid(row=5, column=1)

label = Label(frame, text="Search by ID: ")
label.grid(row=5, column=0)

entry_search_by_id = Entry(frame)
entry_search_by_id.grid(row=5, column=1)

button_search = Button(frame, text="Search", command=lambda: get_product_by_id(entry_search_by_id.get()))
button_search.grid(row=5, column=2)

# Button Add Product

button = Button(frame, text="Add", command=lambda: add_and_display())
button.grid(row=4, column=1)

# ListBox Search by ID

listbox_result_search = Listbox(frame, width=40, height=1)
listbox_result_search.grid(row=9, columnspan=4, sticky=W + E)

# TreeView of products

tree = ttk.Treeview()

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree["columns"] = ("Name", "Category", "Price")

tree.heading("#0", text="", anchor="w")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Price", text="Price")

tree.column("#0", width=0, stretch=False)
tree.column("Name", width=150)
tree.column("Category", width=150)
tree.column("Price", width=100)
tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def clear_table():
    children = tree.get_children()
    for child in children:
        tree.delete(child)


def update_product_list():
    clear_table()
    for prod in get_products():
        tree.insert("", "end", values=prod)


for x in get_products():
    tree.insert("", "end", values=x)


def add_and_display():
    save_new_product(entry_name_product.get(),
                     entry_category_product.get(),
                     entry_price_product.get())
    update_product_list()


root.mainloop()
