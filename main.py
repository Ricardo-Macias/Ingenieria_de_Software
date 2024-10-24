import customtkinter
from tkinter import messagebox, ttk

import connection_SQL
import passwd
import files

class Menu:
    def __init__(self,windows,user,ID):
        self.windows = windows
        self.user = user
        self.ID = ID

        img_2 = files.open_image("Image\\Img_sala.jpg",(740, 450))
        lbl_fondo = customtkinter.CTkLabel(self.windows, image=img_2, text='',)
        lbl_fondo.place(x=0, y=0)

        frame_Menu = customtkinter.CTkFrame(self.windows, width=100, height=430)
        frame_Menu.place(x=10,y=10)

        img = files.open_image("Image\\user-login.png",(50,50))
        lbl_image = customtkinter.CTkLabel(frame_Menu, image=img, text='')
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

        self.employee_sql = connection_SQL.employee('localhost','root',passwd.passwd(),'3306','cine_paraiso')
        self.product_sql = connection_SQL.product('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
        self.membership_sql = connection_SQL.membership('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')

        self.font_title = customtkinter.CTkFont(family="Arial", size=30, weight="bold", slant="italic")
        self.font_id = customtkinter.CTkFont(family="Arial", size=16, weight="bold", slant="italic")
    
    def status_btn_Menu(self,status):
        self.btn_employee.configure(state=status)
        self.btn_membership.configure(state=status)
        self.btn_movie.configure(state=status)
        self.btn_product.configure(state=status)
        self.btn_showing.configure(state=status)
        self.btn_ticket.configure(state=status)

    
    def Employee(self):
        self.status_btn_Menu('disabled')
        frame_employee = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_employee.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_employee, width=580, height=80)
        frame_button.place(x=10, y=25)

        def table():
            global frame_table, table_Employee

            frame_table = customtkinter.CTkFrame(frame_employee, width=580, height=300)
            frame_table.place(x=10, y=120)

            table_Employee = ttk.Treeview(frame_table, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
            table_Employee.column('#0', width=50, anchor=customtkinter.CENTER)
            table_Employee.column('col1', width=100, anchor=customtkinter.CENTER)
            table_Employee.column('col2', width=140, anchor=customtkinter.CENTER)
            table_Employee.column('col3', width=120, anchor=customtkinter.CENTER)
            table_Employee.column('col4', width=120, anchor=customtkinter.CENTER)
            table_Employee.column('col5', width=100, anchor=customtkinter.CENTER)
            table_Employee.column('col6',width=50, anchor=customtkinter.CENTER)

            table_Employee.heading('#0', text='id')
            table_Employee.heading('col1', text='RFC')
            table_Employee.heading('col2', text='Nombre')
            table_Employee.heading('col3', text='Correo')
            table_Employee.heading('col4', text='Telefono')
            table_Employee.heading('col5', text='Direccion')
            table_Employee.heading('col6', text='Cargo')

            table_Employee.place(x=30, y=30, width=810, height=400)

            add_table()

        def form(id, option):
            global frame_form,txt_rfc, txt_name, txt_email, txt_address, txt_phone, cmb_post
            frame_table.destroy()

            frame_form = customtkinter.CTkFrame(frame_employee, width=580, height=300)
            frame_form.place(x=10, y=120)

            lbl_form = customtkinter.CTkLabel(frame_form, text=f"{option}", font=self.font_title)
            lbl_form.place(x=50, y=10)

            lbl_id = customtkinter.CTkLabel(frame_form, text=f"ID: {id}", font=self.font_id)
            lbl_id.place(x=50, y=50)

            lbl_rfc = customtkinter.CTkLabel(frame_form, text="RFC")
            lbl_rfc.place(x=50, y=85)
            txt_rfc = customtkinter.CTkEntry(frame_form, width=180)
            txt_rfc.place(x=110, y=85)

            lbl_name = customtkinter.CTkLabel(frame_form, text="Nombre")
            lbl_name.place(x=50, y=120)
            txt_name = customtkinter.CTkEntry(frame_form, width=240)
            txt_name.place(x=110, y=120)

            lbl_email = customtkinter.CTkLabel(frame_form, text="correo")
            lbl_email.place(x=50, y=155)
            txt_email = customtkinter.CTkEntry(frame_form, width=240)
            txt_email.place(x=110, y=155)

            lbl_address = customtkinter.CTkLabel(frame_form, text="Dir")
            lbl_address.place(x=50, y=190)
            txt_address = customtkinter.CTkEntry(frame_form, width=240)
            txt_address.place(x=110, y=190)

            lbl_phone = customtkinter.CTkLabel(frame_form, text="Tel")
            lbl_phone.place(x=50, y=225)
            txt_phone = customtkinter.CTkEntry(frame_form,width=150)
            txt_phone.place(x=110, y=225)
            
            lbl_post = customtkinter.CTkLabel(frame_form, text="Cargo")
            lbl_post.place(x=270, y=225)
            cmb_post = customtkinter.CTkComboBox(
                frame_form, values=["GRT", "GNL"], width=100)
            cmb_post.place(x=320, y=225)
            cmb_post.set("")

            btn_save = customtkinter.CTkButton(
                frame_form, text="Guardar", width=100, fg_color="GREEN", command=lambda: Save(id, option))
            btn_save.place(x=140, y=260)

            btn_cancel = customtkinter.CTkButton(
                frame_form, text="Cancelar", width=100, fg_color="RED", command=Cancel)
            btn_cancel.place(x=260, y=260)

            status_btn('disabled')

        def add_table():
            employee = self.employee_sql.Select_one('*', 'empleado', 'fecha_baja', 'NULL')
            for count in employee:
                table_Employee.insert("", customtkinter.END, text=count[0], values=[
                    count[1], count[2], count[3], count[4], count[5], count[6]])

        def status_btn(status):
            btn_add.configure(state=status)
            btn_modifier.configure(state=status)
            btn_leave.configure(state=status)

        def close():
            frame_employee.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.membership_sql.last_id('idempleado', 'empleado') + 1
            form(id, 'Agregar')

        def Modifier():
            select = table_Employee.focus()
            key = table_Employee.item(select, 'text')

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                value = table_Employee.item(select, 'values')
                form(key, 'Modificar')

                txt_rfc.insert(0, value[0])
                txt_name.insert(0, value[1])
                txt_email.insert(0, value[2])
                txt_phone.insert(0, value[3])
                txt_address.insert(0,value[4])
                cmb_post.set(value[5])

        def Leave():
            select = table_Employee.focus()
            key = table_Employee.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_Employee.item(select, 'values')
                option = messagebox.askquestion('Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.employee_sql.leave(key)
                    table_Employee.destroy()
                    table()

        def Save(id, option):
            if option == 'Agregar':
                self.employee_sql.Add(
                    id,txt_rfc.get(),txt_name.get(),txt_email.get(),txt_phone.get(),txt_address.get(),cmb_post.get())
                messagebox.showinfo("Agregar", "Nuevo membresia agregada")
            else:
                self.employee_sql.modifier(
                    id, txt_rfc.get(), txt_name.get(), txt_email.get(), txt_phone.get(), txt_address.get(), cmb_post.get())
                messagebox.showinfo(
                    'Modificar', 'Se modificaron los datos de la membresia')
            frame_form.destroy()
            status_btn('normal')
            table()

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                status_btn('normal')
                table()

        btn_close = customtkinter.CTkButton(frame_employee, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        lbl_title = customtkinter.CTkLabel(frame_button, text="Empleados", font=self.font_title)
        lbl_title.place(x=30, y=25)

        img_add = files.open_image("Image\\add.png", (20, 20))
        btn_add = customtkinter.CTkButton(frame_button, text="", image=img_add, width=30, height=30, fg_color="DARKBLUE", command=Add)
        btn_add.place(x=440, y=25)

        img_edit = files.open_image("Image\\edit.png", (20, 20))
        btn_modifier = customtkinter.CTkButton(frame_button, text="", image=img_edit, width=30, height=30, fg_color="DARKBLUE", command=Modifier)
        btn_modifier.place(x=480, y=25)

        img_delete = files.open_image("Image\\delete.png", (20, 20))
        btn_leave = customtkinter.CTkButton(frame_button, text="", image=img_delete, width=30, height=30, fg_color="DARKBLUE", command=Leave)
        btn_leave.place(x=520, y=25)

        table()

    def Membership(self):
        self.status_btn_Menu('disabled')
        frame_membership = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_membership.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_membership, width=580, height=80)
        frame_button.place(x=10, y=25)

        def table():
            global frame_table, table_Membership

            frame_table = customtkinter.CTkFrame(frame_membership, width=580, height=300)
            frame_table.place(x=10, y=120)
            
            table_Membership = ttk.Treeview(frame_table, columns=(
                'col1', 'col2', 'col3', 'col4'))
            table_Membership.column('#0', width=50, anchor=customtkinter.CENTER)
            table_Membership.column('col1', width=140, anchor=customtkinter.CENTER)
            table_Membership.column('col2', width=120, anchor=customtkinter.CENTER)
            table_Membership.column('col3', width=120, anchor=customtkinter.CENTER)
            table_Membership.column('col4', width=100, anchor=customtkinter.CENTER)

            table_Membership.heading('#0', text='ID')
            table_Membership.heading('col1', text='Nombre')
            table_Membership.heading('col2', text='Correo')
            table_Membership.heading('col3', text='Tipo')
            table_Membership.heading('col4', text='Fecha Alta')

            table_Membership.place(x=30, y=30, width=810, height=400)

            add_table()

        def form(id,option):
            global frame_form, txt_name, txt_email, cmb_type
            frame_table.destroy()

            frame_form = customtkinter.CTkFrame(
                frame_membership, width=580, height=300)
            frame_form.place(x=10, y=120)

            lbl_form = customtkinter.CTkLabel(frame_form, text=f"{option}", font=self.font_title)
            lbl_form.place(x=50, y=20)

            lbl_id = customtkinter.CTkLabel(frame_form, text=f"ID: {id}", font=self.font_id)
            lbl_id.place(x=50, y=80)

            lbl_name = customtkinter.CTkLabel(frame_form, text="Nombre")
            lbl_name.place(x=50, y=120)
            txt_name = customtkinter.CTkEntry(frame_form, width=140)
            txt_name.place(x=110, y=120)

            lbl_email = customtkinter.CTkLabel(frame_form, text="correo")
            lbl_email.place(x=50, y=160)
            txt_email = customtkinter.CTkEntry(frame_form, width=240)
            txt_email.place(x=110, y=160)

            lbl_type = customtkinter.CTkLabel(frame_form, text="Tipo")
            lbl_type.place(x=50, y=200)
            cmb_type = customtkinter.CTkComboBox(
                frame_form, values=["SLV", "GLD", "PLT"], width=100)
            cmb_type.place(x=110, y=200)
            cmb_type.set("")

            btn_save = customtkinter.CTkButton(
                frame_form, text="Guardar", width=100, fg_color="GREEN", command=lambda:Save(id,option))
            btn_save.place(x=140, y=240)

            btn_cancel = customtkinter.CTkButton(
                frame_form, text="Cancelar", width=100, fg_color="RED", command=Cancel)
            btn_cancel.place(x=260, y=240)

            status_btn('disabled')

        def add_table():
            membership = self.membership_sql.Select_one('*','membresia','fecha_baja','NULL')
            for count in membership:
                table_Membership.insert("", customtkinter.END, text=count[0], values=[
                    count[1], count[2], count[3], count[4]])

        def status_btn(status):
            btn_add.configure(state=status)
            btn_modifier.configure(state=status)
            btn_leave.configure(state=status)

        def close():
            frame_membership.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.membership_sql.last_id('idmembresia', 'membresia') + 1
            form(id,'Agregar')

        def Modifier():
            select = table_Membership.focus()
            key = table_Membership.item(select, 'text')

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                value = table_Membership.item(select, 'values')
                form(key, 'Modificar')

                txt_name.insert(0, value[0])
                txt_email.insert(0, value[1])
                cmb_type.set(value[2])

        def Leave():
            select = table_Membership.focus()
            key = table_Membership.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_Membership.item(select, 'values')
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.membership_sql.Leave(key)
                    table_Membership.destroy()
                    table()

        def Save(id, option):
            if option == 'Agregar':
                self.membership_sql.Add(id, txt_name.get(), txt_email.get(), cmb_type.get())
                messagebox.showinfo("Agregar", "Nuevo membresia agregada")
            else:
                self.membership_sql.Modifier(id, txt_name.get(), txt_email.get(), cmb_type.get())
                messagebox.showinfo('Modificar', 'Se modificaron los datos de la membresia')
            frame_form.destroy()
            status_btn('normal')
            table()

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                status_btn('normal')
                table()


        btn_close = customtkinter.CTkButton(
            frame_membership, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        lbl_title = customtkinter.CTkLabel(frame_button, text="Membresias", font=self.font_title)
        lbl_title.place(x=30, y=25)

        img_add = files.open_image("Image\\add.png",(20,20))
        btn_add = customtkinter.CTkButton(
            frame_button, text="",image=img_add ,width=30, height=30, fg_color="DARKBLUE", command=Add)
        btn_add.place(x=440, y=25)

        img_edit = files.open_image("Image\\edit.png",(20,20))
        btn_modifier = customtkinter.CTkButton(
            frame_button, text="", image=img_edit, width=30, height=30, fg_color="DARKBLUE", command=Modifier)
        btn_modifier.place(x=480, y=25)

        img_delete = files.open_image("Image\\delete.png",(20,20))
        btn_leave = customtkinter.CTkButton(
            frame_button, text="", image=img_delete, width=30, height=30, fg_color="DARKBLUE", command=Leave)
        btn_leave.place(x=520, y=25)
        
        table()

    def Movie(self):
        pass

    def Product(self):
        self.status_btn_Menu('disabled')
        frame_product = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_product.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_product, width=580, height=80)
        frame_button.place(x=10, y=25)

        def table():
            global frame_table, table_Product

            frame_table = customtkinter.CTkFrame(frame_product, width=580, height=300)
            frame_table.place(x=10, y=120)

            table_Product = ttk.Treeview(frame_table, columns=('col1', 'col2', 'col3'))
            table_Product.column('#0', width=50, anchor=customtkinter.CENTER)
            table_Product.column('col1', width=140, anchor=customtkinter.CENTER)
            table_Product.column('col2', width=120, anchor=customtkinter.CENTER)
            table_Product.column('col3', width=120, anchor=customtkinter.CENTER)

            table_Product.heading('#0', text='ID')
            table_Product.heading('col1', text='Nombre')
            table_Product.heading('col2', text='Precio')
            table_Product.heading('col3', text='Stock')

            table_Product.place(x=30, y=30, width=810, height=400)

            add_table()

        def form(id, option):
            global txt_name, txt_price, txt_stock, frame_form

            frame_table.destroy()

            frame_form = customtkinter.CTkFrame(frame_product, width=580, height=300)
            frame_form.place(x=10, y=120)

            lbl_form = customtkinter.CTkLabel(frame_form, text=f"{option}", font=self.font_title)
            lbl_form.place(x=50, y=20)

            lbl_id = customtkinter.CTkLabel(frame_form, text=f"ID: {id}", font=self.font_id)
            lbl_id.place(x=50, y=80)

            lbl_name = customtkinter.CTkLabel(frame_form, text="Nombre")
            lbl_name.place(x=50, y=120)
            txt_name = customtkinter.CTkEntry(frame_form, width=240)
            txt_name.place(x=110, y=120)

            lbl_price = customtkinter.CTkLabel(frame_form, text="Precio")
            lbl_price.place(x=50, y=160)
            txt_price = customtkinter.CTkEntry(frame_form, width=120)
            txt_price.place(x=110, y=160)

            lbl_stock = customtkinter.CTkLabel(frame_form, text="Stock")
            lbl_stock.place(x=50, y=200)
            txt_stock = customtkinter.CTkEntry(frame_form, width=120)
            txt_stock.place(x=110, y=200)

            btn_save = customtkinter.CTkButton(frame_form, text="Guardar", width=100, fg_color="GREEN", command=lambda: Save(id, option))
            btn_save.place(x=140, y=240)

            btn_cancel = customtkinter.CTkButton(frame_form, text="Cancelar", width=100, fg_color="RED", command=Cancel)
            btn_cancel.place(x=260, y=240)

            status_btn('disabled')

        def add_table():
            product = self.product_sql.Select_all('*','producto')
            for count in product:
                table_Product.insert("", customtkinter.END, text=count[0], values=[
                    count[1], count[2], count[3]])

        def status_btn(status):
            btn_add.configure(state=status)
            btn_modifier.configure(state=status)
            btn_leave.configure(state=status)

        def close():
            frame_product.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.product_sql.last_id('idproducto', 'producto') + 1
            form(id, 'Agregar')

        def Modifier():
            select = table_Product.focus()
            key = table_Product.item(select, 'text')

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                value = table_Product.item(select, 'values')
                form(key, 'Modificar')

                txt_name.insert(0, value[0])
                txt_price.insert(0, value[1])
                txt_stock.insert(0,value[2])

        def Leave():
            select = table_Product.focus()
            key = table_Product.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_Product.item(select, 'values')
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.product_sql.Delete(key)
                    table_Product.destroy()
                    table()

        def Save(id, option):
            if option == 'Agregar':
                self.product_sql.Add(id, txt_name.get(), txt_price.get(), txt_stock.get())
                messagebox.showinfo("Agregar", "Nuevo membresia agregada")
            else:
                self.product_sql.Modifier(id, txt_name.get(), txt_price.get(), txt_stock.get())
                messagebox.showinfo('Modificar', 'Se modificaron los datos de la membresia')
            frame_form.destroy()
            status_btn('normal')
            table()

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                status_btn('normal')
                table()

        btn_close = customtkinter.CTkButton(frame_product, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        lbl_title = customtkinter.CTkLabel(frame_button, text="Productos", font=self.font_title)
        lbl_title.place(x=30, y=25)

        img_add = files.open_image("Image\\add.png", (20, 20))
        btn_add = customtkinter.CTkButton(frame_button, text="", image=img_add, width=30, height=30, fg_color="DARKBLUE", command=Add)
        btn_add.place(x=440, y=25)

        img_edit = files.open_image("Image\\edit.png", (20, 20))
        btn_modifier = customtkinter.CTkButton(frame_button, text="", image=img_edit, width=30, height=30, fg_color="DARKBLUE", command=Modifier)
        btn_modifier.place(x=480, y=25)

        img_delete = files.open_image("Image\\delete.png", (20, 20))
        btn_leave = customtkinter.CTkButton(frame_button, text="", image=img_delete, width=30, height=30, fg_color="DARKBLUE", command=Leave)
        btn_leave.place(x=520, y=25)

        table()
        
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
    app.geometry('740x450')
    app.resizable(False,False)
    app.title('Cinema Paraiso')

    Menu(app,name,ID)

    app.mainloop()