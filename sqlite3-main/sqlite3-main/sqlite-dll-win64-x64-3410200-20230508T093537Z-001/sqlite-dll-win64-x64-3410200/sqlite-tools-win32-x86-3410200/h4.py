import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

def search_people():
    search_text = search_entry.get()
    c.execute("SELECT * FROM avinogradov WHERE first_name LIKE ?", ('%' + search_text + '%',))
    search_results = c.fetchall()
    populate_table(search_results)

def populate_table(data):
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert("", "end", values=row)

def add_person():
    nimi = nimi_entry.get()
    perenimi = perenimi_entry.get()
    email = email_entry.get()
    car_make = car_make_entry.get()
    car_model = car_model_entry.get()
    car_year = car_year_entry.get()
    car_price = car_price_entry.get()

    c.execute("INSERT INTO avinogradov (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (nimi, perenimi, email, car_make, car_model, car_year, car_price))
    conn.commit()
    
    search_people()

def delete_person():
    selected_item = tree.selection()
    if selected_item:
        item_id = selected_item[0]
        person_id = tree.item(item_id)['values'][0]
        c.execute("DELETE FROM avinogradov WHERE id=?", (person_id,))
        conn.commit()
        search_people()

conn = sqlite3.connect('avinogradov.db')
c = conn.cursor()

root = tk.Tk()
root.geometry("800x400")  # Width and height of the window

add_frame = tk.Frame(root)
add_frame.pack(pady=10)

nimi_label = tk.Label(add_frame, text="Nimi:")
nimi_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
nimi_entry = tk.Entry(add_frame)
nimi_entry.grid(row=0, column=1, padx=5, pady=5)

perenimi_label = tk.Label(add_frame, text="Perenimi:")
perenimi_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
perenimi_entry = tk.Entry(add_frame)
perenimi_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(add_frame, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(add_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

car_make_label = tk.Label(add_frame, text="Auto mark:")
car_make_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
car_make_entry = tk.Entry(add_frame)
car_make_entry.grid(row=3, column=1, padx=5, pady=5)

car_model_label = tk.Label(add_frame, text="Auto mudel:")
car_model_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
car_model_entry = tk.Entry(add_frame)
car_model_entry.grid(row=4, column=1, padx=5, pady=5)

car_year_label = tk.Label(add_frame, text="Auto aasta:")
car_year_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
car_year_entry = tk.Entry(add_frame)
car_year_entry.grid(row=5, column=1, padx=5, pady=5)

car_price_label = tk.Label(add_frame, text="Auto hind:")
car_price_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
car_price_entry = tk.Entry(add_frame)
car_price_entry.grid(row=6, column=1, padx=5, pady=5)

add_button = tk.Button(add_frame, text="Lisa inimene", command=add_person)
add_button.grid(row=7, columnspan=2, padx=5, pady=5)

delete_button = tk.Button(add_frame, text="Kustuta inimene", command=delete_person)
delete_button.grid(row=8, columnspan=2, padx=5, pady=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Otsi nime järgi:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = tk.Button(search_frame, text="Otsi", command=search_people)
search_button.grid(row=0, column=2, padx=5, pady=5)

tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

tree_columns = ["ID", "Nimi", "Perenimi", "Email", "Auto mark", "Auto mudel", "Auto aasta", "Auto hind"]
tree = ttk.Treeview(tree_frame, columns=tree_columns, show="headings")

for column in tree_columns:
    tree.heading(column, text=column)
    tree.column(column, width=100)

tree.pack(side="left", fill="y")

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")

tree.configure(yscrollcommand=scrollbar.set)

search_people()

root.mainloop()


