import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

conn = sqlite3.connect('avinogradov.db')
c = conn.cursor()

c.execute("SELECT * FROM avinogradov")
results = c.fetchall()

columns = [
    {"text": "id", "stretch": False},
    {"text":"nimi","stretch":True},
    {"text":"perenimi","stretch":True},
    {"text":"email","stretch":True},
    {"text":"car_make","stretch":True},
    {"text":"car_model","stretch":True},
    {"text":"car_year","stretch":True},
    {"text":"car_price","stretch":True},
]
rows = [list(row) for row in results]

my_w = ttk.Window()
my_w.geometry("810x810")
colors = my_w.style.colors
my_w.style.theme_use("cyborg")
dv = Tableview(
    master=my_w,
    paginated=True,
    coldata=columns,
    rowdata=rows,
    searchable=True,
    pagesize=10,
    height=10,
    stripecolor=(colors.dark, None),
)
dv.grid(row=0, column=0, padx=10, pady=5)
dv.autofit_columns()

entry_fields = [    {"label": "Nimi", "name": "nimi"},    {"label": "Perenimi", "name": "perenimi"},    {"label": "Email", "name": "email"},    {"label": "Auto mark", "name": "car_make"},    {"label": "Auto mudel", "name": "car_model"},    {"label": "Auto aasta", "name": "car_year"},    {"label": "Auto hind", "name": "car_price"}]

button_frame = ttk.Frame(my_w)
button_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")
add_button = ttk.Button(button_frame, text="Lisa uus kirje")
add_button.pack(side="left", padx=5, pady=5)

entry_frame = ttk.Frame(my_w)
entry_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_vars = {}
for i, field in enumerate(entry_fields):
    label = ttk.Label(entry_frame, text=field["label"])
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry_var = ttk.StringVar()
    entry_vars[field["name"]] = entry_var
    entry = ttk.Entry(entry_frame, textvariable=entry_var)
    entry.grid(row=i, column=1, padx=5, pady=5)
   

def add_to_database():
    values = []
    for field in entry_fields:
        values.append(entry_vars[field["name"]].get())
    c.execute("INSERT INTO avinogradov (nimi, perenimi, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)", tuple(values))
    conn.commit()
    c.execute("SELECT * FROM avinogradov")
    results = c.fetchall()
    rows = [list(row) for row in results]
    dv.refresh_data(rows)
    message = "ANDMED ON LISATUD ANDMEBAASI"
    ttk.Label(my_w, text=message, foreground='red').grid(row=3, column=0, padx=5, pady=5)

add_button.configure(command=add_to_database)