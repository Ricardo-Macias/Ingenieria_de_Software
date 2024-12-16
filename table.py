import customtkinter
from tkinter import ttk

class tkinter_table(): 

    def __init__(self,frame,columns=(),heading=[]):
        self.frame = frame
        self.columns = columns
        self.heading = heading

    def create_table(self):
        self.frame_table = customtkinter.CTkFrame(self.frame, width=580, height=300)
        self.frame_table.place(x=10, y=120)

        self.table = ttk.Treeview(self.frame_table, columns=self.columns)

        for count_colums in range(len(self.columns)):

            if count_colums == 0:
                self.table.column('#0', width=50, anchor=customtkinter.CENTER)
                self.table.heading('#0', text=self.heading[count_colums])

            self.table.column(self.columns[count_colums],
                         width=100, anchor=customtkinter.CENTER)
            self.table.heading(self.columns[count_colums],
                          text=self.heading[count_colums+1])

        self.table.place(x=30, y=30, width=810, height=400)
    
    def add_content(self,content=[]):
        for count in content:
            count = list(count)
            self.table.insert("", customtkinter.END, text=count.pop(0), values=count)
    
    def clean_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def select_row(self):
        select = self.table.focus()
        key = self.table.item(select, 'text')
        value = self.table.item(select, 'value')
        return key, value
    
    def destroy_frame(self):
        self.table.destroy()
        self.frame_table.destroy()