from tkinter import Tk, Frame, Label, Entry, Button, END, ttk, W, E, Listbox, font
from function.product import save_new_product, get_product_by_id, get_products, delete_product, update_product
from text.message import Message

root = Tk()
root.title(Message.TITLE.value)
root.geometry("720x340")
root.resizable(width=False, height=False)

bold_font = font.Font(weight="bold")

# Frame
frame = Frame(borderwidth=2, relief="sunken")
frame.grid(row=0, column=0, pady=10, padx=10)

# Frame
frame_search = Frame()
frame_search.grid(row=1, column=0)

frame_product_result = Frame()
frame_product_result.grid(row=1, column=1)

lbl_title_product = Label(frame_product_result, text=Message.PRODUCT.value, font=bold_font)
lbl_title_product.grid(row=0, column=0)

# Labels
label = Label(frame, text=Message.ADD_PRODUCT.value)
label.grid(row=0, column=1)

label = Label(frame, text=Message.NAME.value)
label.grid(row=1, column=0)

entry_name_product = Entry(frame)
entry_name_product.grid(row=1, column=1)

label = Label(frame, text=Message.CATEGORY.value)
label.grid(row=2, column=0)

entry_category_product = Entry(frame)
entry_category_product.grid(row=2, column=1)

label = Label(frame, text=Message.PRICE.value)
label.grid(row=3, column=0)

label_error = Label(frame, text="", foreground="red")
label_error.grid(row=9, column=1)

entry_price_product = Entry(frame)
entry_price_product.grid(row=3, column=1)

# Button Add Product

btn_add = Button(frame, text=Message.ADD.value, bg="#4EE172", command=lambda: add_and_display())
btn_add.grid(row=6, column=1, sticky=W + E)

# TreeView of products

tree = ttk.Treeview(root)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=2, pady=20, sticky="ns")

tree.configure(yscrollcommand=scrollbar.set)

tree["columns"] = (Message.ID.value, Message.NAME.value, Message.CATEGORY.value, Message.PRICE.value)

tree.heading("#0", text="", anchor="w")
tree.heading(Message.ID.value, text=Message.ID.value)
tree.heading(Message.NAME.value, text=Message.NAME.value)
tree.heading(Message.CATEGORY.value, text=Message.CATEGORY.value)
tree.heading(Message.PRICE.value, text=Message.PRICE.value)

tree.column("#0", width=0, stretch=False)
tree.column(Message.NAME.value, width=150)
tree.column(Message.CATEGORY.value, width=150)
tree.column(Message.PRICE.value, width=100)
tree.column(Message.ID.value, width=0, stretch=False)
tree.grid(row=0, column=1, padx=5, pady=20)

item_selected = None

lbl_search = Label(frame_search, text=Message.SEARCH_PRODUCT.value)
lbl_search.grid(row=0, column=0)

txt_search = Entry(frame_search)
txt_search.grid(row=1, column=0)

listbox = Listbox(frame_product_result, width=50, height=1)
listbox.grid(row=3, column=0)

# Button Delete
btn_delete = Button(frame, text=Message.DELETE.value, bg="#C82222", command=lambda: delete_and_display(item_selected[0]))
btn_delete.grid(row=7, column=1, sticky=W + E)

btn_search = Button(frame_search, text=Message.SEARCH.value, bg="#ABABAB", command=lambda: get_product(txt_search.get()))
btn_search.grid(row=1, column=1)

for x in get_products():
    tree.insert("", "end", values=x)


def get_product(product_id):
    product_found = get_product_by_id(int(product_id))

    listbox.delete(0, END)

    if product_found is not None:
        listbox.config(bg="#C9CACC")
        lbl_result_product = f'The product {product_found[0]} with category {product_found[1]} and price ${product_found[2]}'
        listbox.insert(END, lbl_result_product)
    else:
        listbox.config(bg="white")
        listbox.insert(END, Message.NOT_PRODUCT.value)


def on_treeview_click(event):
    global item_selected

    item_id = tree.identify_row(event.y)
    if item_id:
        item_selected = tree.item(item_id)["values"]
        modify_field_form(item_selected)
    return item_selected


def modify_field_form(data_field):
    entry_name_product.delete(0, END)
    entry_name_product.insert(0, data_field[1])
    entry_category_product.delete(0, END)
    entry_category_product.insert(0, data_field[2])
    entry_price_product.delete(0, END)
    entry_price_product.insert(0, data_field[3])

    btn_add.config(text=Message.UPDATE.value, bg="#6971FF")


tree.bind("<Button-1>", on_treeview_click)


def clear_table():
    children = tree.get_children()
    for child in children:
        tree.delete(child)


def clear_fields():
    entry_name_product.delete(0, END)
    entry_category_product.delete(0, END)
    entry_price_product.delete(0, END)


def update_product_list():
    clear_table()
    for prod in get_products():
        tree.insert("", "end", values=prod)


def add_and_display():
    if entry_name_product.get() == "" or \
            entry_price_product.get() == "" \
            or entry_category_product.get() == "":
        label_error.config(text=Message.FIELD_REQUIRED.value)
    else:
        if btn_add.cget("text") == Message.ADD.value:
            save_new_product(entry_name_product.get(),
                             entry_category_product.get(),
                             entry_price_product.get())
            label_error.config(text="")
        else:
            update_product(item_selected[0],
                           entry_name_product.get(),
                           entry_category_product.get(),
                           entry_price_product.get())
            btn_add.config(text=Message.ADD.value, bg="#4EE172")
            label_error.config(text="")

    clear_fields()
    update_product_list()


def delete_and_display(product_id):
    delete_product(product_id)
    update_product_list()
    clear_fields()
    btn_add.config(text=Message.ADD.value, bg="#4EE172")


root.mainloop()
