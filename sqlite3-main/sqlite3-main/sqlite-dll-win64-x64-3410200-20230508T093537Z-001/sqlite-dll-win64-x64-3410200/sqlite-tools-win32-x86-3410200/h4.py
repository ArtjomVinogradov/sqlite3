import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

conn = sqlite3.connect('avinogradov.db')
c = conn.cursor()

c.execute("SELECT * FROM avinogradov")
results = c.fetchall()
my_w = ttk.Window()
my_w.geometry("800x400")  # width and height
colors = my_w.style.colors
l1 =  [
    {"text": "id", "stretch": False},
    {"text": "first_name", "stretch": True},
    {"text": "last_name", "stretch": True},
    {"text": "email", "stretch": True},
    {"text": "car_make", "stretch": True},
    {"text": "car_model", "stretch": True},
    {"text": "car_year", "stretch": True},
    {"text": "car_price", "stretch": True},
]

def loe_avinogradov():
    print("valisid 2")
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('SELECT * FROM avinogradov')
    tulemused = c.fetchall()
    for tulemus in tulemused:
        print(tulemus)
    conn.close()

loe_avinogradov()
results = c.fetchall()
rows = [list(row) for row in results]
marks = [r[3] for r in results]
print(sum(marks))

dv = ttk.tableview.Tableview(
    master=my_w,
    paginated=True,
    coldata=l1,
    rowdata=rows,  # Kasutame muutujat 'rows' andmetega
    searchable=True,
    bootstyle=SUCCESS,
    pagesize=10,
    height=10,
    stripecolor=(colors.light, None),
)
dv.grid(row=0, column=0, padx=10, pady=5)
dv.autofit_columns()
dv.insert_row("end", values=['-', "---", "All", sum(marks), "All"])
dv.load_table_data()
my_w.mainloop()
