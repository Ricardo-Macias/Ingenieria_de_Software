import customtkinter
from tkinter import messagebox, ttk
from PIL import Image

import connection_SQL
import passwd

class Menu:
    def __init__(self,windows,user,ID):
        self.windows = windows
        self.user = user
        self.ID = ID

        img_2 = Image.open("Image\\Img_sala.jpg")
        render_2 = customtkinter.CTkImage(img_2, size=(800, 450))
        lbl_fondo = customtkinter.CTkLabel(self.windows, image=render_2, text='',)
        lbl_fondo.place(x=0, y=0)

        frame_Menu = customtkinter.CTkFrame(self.windows, width=100, height=430)
        frame_Menu.place(x=10,y=10)

        img = Image.open("Image\\user-login.png")
        render = customtkinter.CTkImage(img, size=(50, 50))
        lbl_image = customtkinter.CTkLabel(frame_Menu, image=render, text='')
        lbl_image.place(x=25, y=10)
        lbl_user = customtkinter.CTkLabel(frame_Menu,text=self.user,width=80)
        lbl_user.place(x=10,y=60)

        # --------> SOLO SI ES GERENTE
        self.btn_employee = customtkinter.CTkButton(frame_Menu,text="Empledo", command=self.Employee, width=80,height=40)
        self.btn_employee.place(x=10,y=100)
        #------------------------------

        self.btn_membership = customtkinter.CTkButton(frame_Menu, text="Membresia", command=self.Membership, width=80, height=40)
        self.btn_membership.place(x=10, y=150)

        self.btn_movie = customtkinter.CTkButton(frame_Menu, text="Pelicula", command=self.Movie, width=80, height=40)
        self.btn_movie.place(x=10, y=200)

        self.btn_product = customtkinter.CTkButton(frame_Menu, text="Producto", command=self.Product, width=80, height=40)
        self.btn_product.place(x=10, y=250)

        self.btn_showing = customtkinter.CTkButton(frame_Menu, text="Funcion", command=self.Showing, width=80, height=40)
        self.btn_showing.place(x=10, y=300)

        self.btn_ticket = customtkinter.CTkButton(frame_Menu, text="Ticket", command=self.Ticket, width=80, height=40)
        self.btn_ticket.place(x=10, y=350)

        self.employee = connection_SQL.employee('localhost','root',passwd.passwd(),'3306','cine_paraiso')
        self.product = connection_SQL.product('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
    
    def status_btn_Menu(self,status):
        self.btn_employee.configure(state=status)
        self.btn_membership.configure(state=status)
        self.btn_movie.configure(state=status)
        self.btn_product.configure(state=status)
        self.btn_showing.configure(state=status)
        self.btn_ticket.configure(state=status)

    
    def Employee(self):
        self.band_employee = True
        self.status_btn_Menu('disabled')
        frame_employee = customtkinter.CTkFrame(self.windows,width=670,height=430)
        frame_employee.place(x=120,y=10)

        def add_table():
            employee = self.employee.Select_all('*','empleado')
            for count in employee:
                table_Employee.insert("", customtkinter.END, text=count[1], values=[
                             count[2], count[3], count[4], count[5], count[6]])
        
        def clear_table():
            register = table_Employee.get_children()
            for count_register in register:
                table_Employee.delete(count_register)

        def clean_txt():
            txt_id.delete(0,customtkinter.END)
            txt_name.delete(0,customtkinter.END)
            txt_rfc.delete(0,customtkinter.END)
            txt_email.delete(0,customtkinter.END)
            txt_phone.delete(0,customtkinter.END)
            txt_adress.delete(0,customtkinter.END)
            cmb_post.set('')

        def status_txt(status):
            cmb_post.configure(state=status)
            txt_rfc.configure(state=status)
            txt_name.configure(state=status)
            txt_email.configure(state=status)
            txt_phone.configure(state=status)
            txt_adress.configure(state=status)

        def status_btn(status):
            btn_save.configure(state=status)
            btn_cancel.configure(state=status)

        def status_btn_add(status):
            btn_add.configure(state=status)
            btn_modifier.configure(state=status)
            btn_leave.configure(state=status)

        def close():
            frame_employee.destroy()
            self.status_btn_Menu('normal')
        
        def Add():
            self.band_employee = True
            id = len(self.employee.Select_all('*','empleado')) + 1

            txt_id.configure(state='normal')
            txt_id.insert(0,id)
            txt_id.configure(state='disabled')

            status_txt('normal')
            status_btn_add('disabled')
            status_btn('normal')
            cmb_post.set('GNL')

        def Modifier():
            self.band_employee = False
            select = table_Employee.focus()
            key = table_Employee.item(select, 'text')

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                status_txt('normal')
                value = table_Employee.item(select, 'values')

                txt_id.configure(state='normal')
                id = self.employee.Select_one('idempleado','empleado','rfc',f"'{key}'")

                txt_id.insert(0, id)
                txt_rfc.insert(0, key)
                txt_name.insert(0, value[0])
                txt_email.insert(0, value[1])
                txt_phone.insert(0, value[2])
                txt_adress.insert(0, value[3])
                cmb_post.set(value[4])

                txt_id.configure(state='disabled')
                status_btn_add('disabled')
                status_btn('normal')

        def Leave():
            select = table_Employee.focus()
            key = table_Employee.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_Employee.item(select, 'values')
                option = messagebox.askquestion('Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    id = self.employee.Select_one('idempleado','empleado','rfc',f"'{key}'")
                    self.employee.leave(int(id[0]))

        def Save():
            if self.band_employee:
                self.employee.Add(txt_id.get(),txt_rfc.get(),txt_name.get(),txt_email.get(),txt_phone.get(),txt_adress.get(),cmb_post.get())
                messagebox.showinfo("Agregar","Nuevo empleado agregado")
            else:
                self.employee.modifier(txt_id.get(), txt_rfc.get(), txt_name.get(), txt_email.get(), txt_phone.get(), txt_adress.get(), cmb_post.get())
                messagebox.showinfo('Modificar','Se modificaron los datos del empleado')
            txt_id.configure(state='normal')
            clean_txt()
            txt_id.configure(state='disabled')
            status_btn('disabled')
            status_btn_add('normal')
            status_txt('disabled')
            clear_table()
            add_table()

        def Cancel():
            option = messagebox.askokcancel('Cancelar','Seguro que quiere canccelar')
            if option:
                txt_id.configure(state='normal')
                clean_txt()
                txt_id.configure(state='disabled')
                status_btn('disabled')
                status_btn_add('normal')
                status_txt('disabled')

        lbl_id = customtkinter.CTkLabel(frame_employee,text="ID")
        lbl_id.place(x=30, y=40)
        txt_id = customtkinter.CTkEntry(frame_employee, width=50)
        txt_id.place(x=50,y=40)

        lbl_rfc = customtkinter.CTkLabel(frame_employee,text="RFC")
        lbl_rfc.place(x=30, y=80)
        txt_rfc = customtkinter.CTkEntry(frame_employee,width=140)
        txt_rfc.place(x=80,y=80)

        lbl_name = customtkinter.CTkLabel(frame_employee, text="Nombre")
        lbl_name.place(x=250,y=80)
        txt_name = customtkinter.CTkEntry(frame_employee,width=140)
        txt_name.place(x=305,y=80)

        lbl_email = customtkinter.CTkLabel(frame_employee,text="Correo")
        lbl_email.place(x=30, y=120)
        txt_email = customtkinter.CTkEntry(frame_employee, width=230)
        txt_email.place(x=80,y=120)

        lbl_phone = customtkinter.CTkLabel(frame_employee,text="Tel")
        lbl_phone.place(x=30, y=160)
        txt_phone = customtkinter.CTkEntry(frame_employee, width=140)
        txt_phone.place(x=80,y=160)

        lbl_adress = customtkinter.CTkLabel(frame_employee,text="Dir")
        lbl_adress.place(x=30, y=200)
        txt_adress = customtkinter.CTkEntry(frame_employee,width=140)
        txt_adress.place(x=80, y=200)

        lbl_post = customtkinter.CTkLabel(frame_employee,text="Cargo")
        lbl_post.place(x=150, y=40)
        cmb_post = customtkinter.CTkComboBox(frame_employee, values=["GRT","GNL"],width=70)
        cmb_post.place(x=200,y=40)
        cmb_post.set("")

        btn_close = customtkinter.CTkButton(frame_employee,width=10,height=10,text="X",fg_color="RED",command=close)
        btn_close.place(x=0,y=0)

        btn_add = customtkinter.CTkButton(frame_employee, text="Agregar", width=70, height=40, fg_color="DARKBLUE", command=Add)
        btn_add.place(x=500,y=80)

        btn_modifier = customtkinter.CTkButton(frame_employee, text="Modificar", width=70, height=40, fg_color="DARKBLUE", command=Modifier)
        btn_modifier.place(x=500,y=130)

        btn_leave = customtkinter.CTkButton(frame_employee, text="Baja",width=70, height=40,fg_color="DARKBLUE", command=Leave)
        btn_leave.place(x=500,y=180)

        btn_save = customtkinter.CTkButton(frame_employee,text="Guardar",width=100,fg_color="GREEN",command=Save)
        btn_save.place(x=290,y=160)

        btn_cancel = customtkinter.CTkButton(frame_employee,text="Cancelar",width=100,fg_color="RED",command=Cancel)
        btn_cancel.place(x=290,y=200)

        table_Employee = ttk.Treeview(frame_employee,columns=('col1','col2','col3','col4','col5'))
        table_Employee.column('#0',width=100)
        table_Employee.column('col1',width=90)
        table_Employee.column('col2',width=120)
        table_Employee.column('col3',width=120)
        table_Employee.column('col4',width=100)
        table_Employee.column('col5',width=140)

        table_Employee.heading('#0',text='RFC')
        table_Employee.heading('col1',text='Nombre')
        table_Employee.heading('col2', text='Correo')
        table_Employee.heading('col3',text='Telefono')
        table_Employee.heading('col4',text='Direccion')
        table_Employee.heading('col5', text='Cargo')

        table_Employee.place(x=50, y=380,width=800)

        add_table()

        txt_id.configure(state='disabled')
        status_txt('disabled')
        status_btn('disabled')

    def Membership(self):
        pass

    def Movie(self):
        pass

    def Product(self):
        self.band_product = True
        self.status_btn_Menu('disabled')
        frame_product = customtkinter.CTkFrame(self.windows,width=670,height=430)
        frame_product.place(x=120,y=10)

        def add_table():
            product = self.product.Select_all('*','producto')
            for count in product:
                table_product.insert("", customtkinter.END, text=count[0], values=[
                             count[1], count[2], count[3]])
        
        def clear_table():
            register = table_product.get_children()
            for count_register in register:
                table_product.delete(count_register)

        def clean_txt():
            txt_id.delete(0,customtkinter.END)
            txt_product.delete(0,customtkinter.END)
            txt_price.delete(0,customtkinter.END)
            txt_stock.delete(0,customtkinter.END)

        def status_txt(status):
            txt_product.configure(state=status)
            txt_price.configure(state=status)
            txt_stock.configure(state=status)

        def status_btn(status):
            btn_save.configure(state=status)
            btn_cancel.configure(state=status)

        def status_btn_add(status):
            btn_add.configure(state=status)
            btn_modifier.configure(state=status)
            btn_leave.configure(state=status)

        def close():
            frame_product.destroy()
            self.status_btn_Menu('normal')
        
        def Add():
            self.band_employee = True
            id = len(self.employee.Select_all('*','empleado')) + 1

            txt_id.configure(state='normal')
            txt_id.insert(0,id)
            txt_id.configure(state='disabled')

            status_txt('normal')
            status_btn_add('disabled')
            status_btn('normal')
            cmb_post.set('GNL')

        def Modifier():
            self.band_employee = False
            select = table_product.focus()
            key = table_product.item(select, 'text')

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                status_txt('normal')
                value = table_product.item(select, 'values')

                txt_id.configure(state='normal')
                id = self.employee.Select_one('idempleado','empleado','rfc',f"'{key}'")

                txt_id.insert(0, id)
                txt_rfc.insert(0, key)
                txt_name.insert(0, value[0])
                txt_email.insert(0, value[1])
                txt_phone.insert(0, value[2])
                txt_adress.insert(0, value[3])
                cmb_post.set(value[4])

                txt_id.configure(state='disabled')
                status_btn_add('disabled')
                status_btn('normal')

        def Leave():
            select = table_product.focus()
            key = table_product.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_product.item(select, 'values')
                option = messagebox.askquestion('Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    id = self.employee.Select_one('idempleado','empleado','rfc',f"'{key}'")
                    self.employee.leave(int(id[0]))

        def Save():
            if self.band_employee:
                self.employee.Add(txt_id.get(),txt_rfc.get(),txt_name.get(),txt_email.get(),txt_phone.get(),txt_adress.get(),cmb_post.get())
                messagebox.showinfo("Agregar","Nuevo empleado agregado")
            else:
                self.employee.modifier(txt_id.get(), txt_rfc.get(), txt_name.get(), txt_email.get(), txt_phone.get(), txt_adress.get(), cmb_post.get())
                messagebox.showinfo('Modificar','Se modificaron los datos del empleado')
            txt_id.configure(state='normal')
            clean_txt()
            txt_id.configure(state='disabled')
            status_btn('disabled')
            status_btn_add('normal')
            status_txt('disabled')
            clear_table()
            add_table()

        def Cancel():
            option = messagebox.askokcancel('Cancelar','Seguro que quiere canccelar')
            if option:
                txt_id.configure(state='normal')
                clean_txt()
                txt_id.configure(state='disabled')
                status_btn('disabled')
                status_btn_add('normal')
                status_txt('disabled')

        lbl_id = customtkinter.CTkLabel(frame_product,text="ID")
        lbl_id.place(x=30, y=40)
        txt_id = customtkinter.CTkEntry(frame_product, width=50)
        txt_id.place(x=50,y=40)

        lbl_product = customtkinter.CTkLabel(frame_product,text="Producto")
        lbl_product.place(x=30, y=80)
        txt_product = customtkinter.CTkEntry(frame_product,width=140)
        txt_product.place(x=80,y=80)

        lbl_price = customtkinter.CTkLabel(frame_product, text="Precio")
        lbl_price.place(x=250,y=80)
        txt_price = customtkinter.CTkEntry(frame_product,width=140)
        txt_price.place(x=305,y=80)

        lbl_stock = customtkinter.CTkLabel(frame_product,text="Stock")
        lbl_stock.place(x=30, y=120)
        txt_stock = customtkinter.CTkEntry(frame_product, width=230)
        txt_stock.place(x=80,y=120)

        btn_close = customtkinter.CTkButton(frame_product,width=10,height=10,text="X",fg_color="RED",command=close)
        btn_close.place(x=0,y=0)

        btn_add = customtkinter.CTkButton(frame_product, text="Agregar", width=70, height=40, fg_color="DARKBLUE", command=Add)
        btn_add.place(x=500,y=80)

        btn_modifier = customtkinter.CTkButton(frame_product, text="Modificar", width=70, height=40, fg_color="DARKBLUE", command=Modifier)
        btn_modifier.place(x=500,y=130)

        btn_leave = customtkinter.CTkButton(frame_product, text="Baja",width=70, height=40,fg_color="DARKBLUE", command=Leave)
        btn_leave.place(x=500,y=180)

        btn_save = customtkinter.CTkButton(frame_product,text="Guardar",width=100,fg_color="GREEN",command=Save)
        btn_save.place(x=290,y=160)

        btn_cancel = customtkinter.CTkButton(frame_product,text="Cancelar",width=100,fg_color="RED",command=Cancel)
        btn_cancel.place(x=290,y=200)

        table_product = ttk.Treeview(frame_product,columns=('col1','col2','col3'))
        table_product.column('#0',width=100)
        table_product.column('col1',width=90)
        table_product.column('col2',width=120)
        table_product.column('col3',width=120)

        table_product.heading('#0',text='ID')
        table_product.heading('col1',text='Producto')
        table_product.heading('col2', text='Precio')
        table_product.heading('col3',text='Stock')

        table_product.place(x=50, y=380,width=800)

        add_table()

        txt_id.configure(state='disabled')
        status_txt('disabled')
        status_btn('disabled')

    def Showing(self):
        pass

    def Ticket(self):
        pass
        
if __name__ == "__main__":
    # ----> Agregar el login

    # -----------------------

    name = "Ricardo"
    ID = 1

    app = customtkinter.CTk()
    app.geometry('800x450')
    app.title('Cinema Paraiso')

    Menu(app,name,ID)

    app.mainloop()