import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("400x300")  # width and height
colors = my_w.style.colors
l1 = [
    {"text": "id", "stretch": False},
    {"text":"Eesnimi","stretch":True},
    {"text":"perenimi","stretch":True},
    {"text":"email","stretch":True},
    {"text":"auto tootja","stretch":True},
    {"text":"auto mudel ","stretch":True},
    {"text":"auto aasta ","stretch":True},
    {"text":"auto price ","stretch":True},

]  # Columns with Names and style 
# Data rows as list 
r_set = [SELECT * FROM avingradov]

dv = ttk.tableview.Tableview(
    master=my_w,
    paginated=True,
    coldata=l1,
    rowdata=r_set,
    searchable=True,
    bootstyle=SUCCESS,
    pagesize=10,
    height=10,
    stripecolor=(colors.light, None),
)
dv.grid(row=0, column=0, padx=10, pady=5)
dv.autofit_columns() # Fit in current view 
my_w.mainloop()