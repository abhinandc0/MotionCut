
from tkinter import *
import tkinter.messagebox as mb
import json

from unicodedata import category

#Class to create expense
class Expense:
    def __init__(self,title,date,category,amount,description):
        self.title = title
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"{self.title}"

#loads expense from the json file
def load_expenses():
    try:
        with open('expense.json','r') as exp:
            return [Expense(**data) for data in json.load(exp)]
    except FileNotFoundError:
        return []

#function to save expenses
def save_expense(expense):
    with open('expense.json','w') as exp:
        json.dump([expense.__dict__ for expense in expenses], exp)

#function to add new expense
def add_expense():
    title = title_entry.get()
    date = date_entry.get()
    category = selected_category.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if title and date and category and amount and description:
        expense = Expense(title,date,category,amount,description)
        expenses.append(expense)
        save_expense(expense)
        update_expense_list()
        title_entry.delete(0,"end")
        date_entry.delete(0,"end")
        amount_entry.delete(0,"end")
        description_entry.delete(0,"end")
    else:
        mb.showerror("Error","Please fill all the fields")

#function to refresh task list to apply any changes
def update_expense_list():
    expense_list.delete(0,"end")
    for i,expense in enumerate(expenses):
        expense_list.insert("end",f"{i+1}. {expense.title} - {expense.category} - {expense.amount} - {expense.date}")

#delete expense by secting
def delete_expense():
    try:
        expense_index = int(expense_list.curselection()[0])
        del expenses[expense_index]
        save_expense(expenses)
        update_expense_list()
    except IndexError:
        mb.showerror("Error","Please select task to delete")

expenses = load_expenses()

et = Tk()
et.title('Expense Traker')
et.resizable(True,True)
et.geometry('600x400')

#List tasks
expense_list_frame = Frame(et)
expense_list_frame.pack(fill="both",expand = True)

scrollbar_x = Scrollbar(expense_list_frame,orient="horizontal")
scrollbar_x.pack(side="bottom",fill="x")

scrollbar_y = Scrollbar(expense_list_frame,orient="vertical")
scrollbar_y.pack(side="right",fill="y")

#create list
expense_list = Listbox(expense_list_frame,width=50,height=8, xscrollcommand = scrollbar_x.set,yscrollcommand=scrollbar_y.set)
expense_list.pack()

scrollbar_x.config(command=expense_list.xview)
scrollbar_y.config(command=expense_list.yview)
update_expense_list()

#Title
title_label = Label(et,text="Title")
title_label.pack()
title_entry = Entry(et)
title_entry.pack()
title_entry.insert(0,"Enter expense title.")

#Amount
amount_label = Label(et,text="Amount")
amount_label.pack()
amount_entry = Entry(et)
amount_entry.pack()
amount_entry.insert(1,"Enter amount")

#date
date_label = Label(et,text="Date")
date_label.pack()
date_entry = Entry(et)
date_entry.pack()
date_entry.insert(0,"Enter date")

#description
description_label = Label(et,text="Description")
description_label.pack()
description_entry = Entry(et)
description_entry.pack()
description_entry.insert(0,"Enter description for expense")

#Category
category_label = Label(et,text="Category")
category_label.pack()

#list of categories
categories = ["Select category","Food","Transport","Entertainment","Utilities","Miscellaneous"]

#variable to select category
selected_category = StringVar()
selected_category.set(categories[0])

#Dropdown
category_option = OptionMenu(et,selected_category,*categories)
category_option.pack()

#add task
add_button = Button(et,text="Add Task",command=add_expense).pack()
delete_button = Button(et,text="Delete Button", command=delete_expense).pack()
exit_button = Button(et,text="Exit",command=et.destroy).pack()

et.mainloop()