from numpy import empty
from HotelsDataBase import HotelsDataBase

import tkinter as tk
from hotel_analitic import hotel_analitic
import tkinter as tk
from tkinter import ttk

class Redact_hotel_form(object):
    def __init__(self, HotelsList):
        self.data_base = HotelsList
        self.listbox = None
    
    
    def delete_hotel(self):            
        row = self.listbox.selection()[0] + ' '
        i = 0
        for tmp_row in self.listbox.item(self.listbox.selection()[0], 'values'):
            row += tmp_row
            i += 1
            if i <= len(self.listbox.item(self.listbox.selection()[0], 'values')) - 1:
                row += ' '
                
        self.data_base.delete_hotel(row)
        self.refresh();
            
    def refresh(self):
        if(self.listbox != empty):
            self.listbox.delete(*self.listbox.get_children())
        for i in self.data_base.lines:
            words = i.split()
            item_id = words[0] 
            self.listbox.insert('', 'end', iid=item_id, text=words[0], values=(words[1], f'{words[2]} {words[3]}', words[4], words[5]))
    
        
    def create_form(self):
        def on_right_click(event):
            context_menu.post(event.x_root, event.y_root)
        
        root = tk.Tk()
        root.title("Hotel analitic")

        width = 1200
        height = 400
        root.geometry(f"{width}x{height}")
        
        # self.listbox = tk.Listbox(root, width=50, height=10)
        # self.listbox.grid(row=1, column=1, rowspan=5, padx=10, pady=10)
        
        self.listbox = ttk.Treeview(root, columns=('name', 'price', 'terotery', 'marks of clients', 'your mark'))

        self.listbox.heading('#0', text='name')
        self.listbox.heading('#1', text='price')
        self.listbox.heading('#2', text='terotery')
        self.listbox.heading('#3', text='mark of clients')
        self.listbox.heading('#4', text='your mark')

        
        

        self.listbox.grid(row=1, column=1, rowspan=5, padx=5, pady=5)
        
        self.listbox.bind("<Button-3>", on_right_click)
        # self.listbox.selection_set(0)


        
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Add hotel", command=self.create_add_form)
        context_menu.add_command(label="Update hotel", command=lambda: self.create_update_form(self.listbox.selection()[0]))
        context_menu.add_command(label="Delete hotel", command=self.delete_hotel)

        self.refresh();
        
        hotels_analitic = hotel_analitic(self.data_base)
        Predict_form = tk.Button(root, text="Check mark hotel for you", command=lambda: hotels_analitic.analitic_hotel_form())
        Predict_form.grid(row = 38, columnspan=2, pady=10)

        root.mainloop()
        
    
    def create_add_form(self):
        def add_hotel():
            self.data_base.add_hotel(entry_name.get(), entry_price.get(), entry_region.get(), entry_mark.get(), entry_my_mark.get())
            self.refresh()
            root.destroy()

        root = tk.Toplevel()
        
        width = 300
        height = 200
        root.geometry(f"{width}x{height}")
        
        label = tk.Label(root, text="Name: ")
        label.grid(row = 0, columnspan=1, pady=5)
        label = tk.Label(root, text="Price: ")
        label.grid(row = 1, columnspan=1, pady=5)
        label = tk.Label(root, text="Region: ")
        label.grid(row = 2, columnspan=1, pady=5)
        label = tk.Label(root, text="Mark: ")
        label.grid(row = 4, columnspan=1, pady=5)
        label = tk.Label(root, text="My mark: ")
        label.grid(row = 5, columnspan=1, pady=5)
        
        entry_name = tk.Entry(root, width=30)
        entry_price = tk.Entry(root, width=30)
        entry_country = tk.Entry(root, width=30)
        entry_region = tk.Entry(root, width=30)
        entry_mark = tk.Entry(root, width=30)
        entry_my_mark = tk.Entry(root, width=30)

        entry_name.grid(row=0, column=2, padx=10, pady=5)
        entry_price.grid(row=1, column=2, padx=10, pady=5)
        entry_region.grid(row=2, column=2, padx=10, pady=5)
        entry_mark.grid(row=4, column=2, padx=10, pady=5)
        entry_my_mark.grid(row=5, column=2, padx=10, pady=5)
        
        add_button = tk.Button(root, text="Add", command = add_hotel)
        add_button.grid(row = 30, columnspan=3, pady=10)

        root.mainloop()
        
    def create_update_form(self, name):
        def update_hotel_meth(old_name, updaterow):
            self.data_base.update_hotel(old_name, updaterow)
            self.refresh()
            new_root.destroy()
        
        new_root = tk.Toplevel()

        width = 300
        height = 200
        new_root.geometry(f"{width}x{height}")

        label_name = tk.Label(new_root, text="Name: ")
        label_name.grid(row=0, columnspan=1, pady=5)
        label_price = tk.Label(new_root, text="Price: ")
        label_price.grid(row=1, columnspan=1, pady=5)
        label_region = tk.Label(new_root, text="Region: ")
        label_region.grid(row=2, columnspan=1, pady=5)
        label_mark = tk.Label(new_root, text="Mark: ")
        label_mark.grid(row=4, columnspan=1, pady=5)
        label_my_mark = tk.Label(new_root, text="My mark: ")
        label_my_mark.grid(row=5, columnspan=1, pady=5)

        entry_name = tk.Entry(new_root, width=30)
        entry_price = tk.Entry(new_root, width=30)
        entry_region = tk.Entry(new_root, width=30)
        entry_mark = tk.Entry(new_root, width=30)
        entry_my_mark = tk.Entry(new_root, width=30)

        entry_name.grid(row=0, column=2, padx=10, pady=5)
        entry_price.grid(row=1, column=2, padx=10, pady=5)
        entry_region.grid(row=2, column=2, padx=10, pady=5)
        entry_mark.grid(row=4, column=2, padx=10, pady=5)
        entry_my_mark.grid(row=5, column=2, padx=10, pady=5)

        entry_name.insert(tk.END, name)
        entry_price.insert(tk.END, self.listbox.item(self.listbox.selection()[0], 'values')[0])
        entry_region.insert(tk.END, self.listbox.item(self.listbox.selection()[0], 'values')[1])
        entry_mark.insert(tk.END, self.listbox.item(self.listbox.selection()[0], 'values')[2])
        entry_my_mark.insert(tk.END, self.listbox.item(self.listbox.selection()[0], 'values')[3])

        update_button = tk.Button(new_root, text="Update", command=lambda: update_hotel_meth(name, f"{entry_name.get()} {entry_price.get()} {entry_region.get()} {entry_mark.get()} {entry_my_mark.get()}\n"))
        update_button.grid(row=30, columnspan=3, pady=10)

        new_root.mainloop()


    pass



