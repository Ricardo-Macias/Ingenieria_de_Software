import customtkinter
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry

from file_explorer import image_explorer
from table import tkinter_table
import connection_SQL
import passwd

class Menu:
    def __init__(self,windows,user,ID):
        self.windows = windows
        self.user = user
        self.ID = ID

        self.image = image_explorer()

        self.employee_sql = connection_SQL.employee('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
        self.product_sql = connection_SQL.product('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
        self.membership_sql = connection_SQL.membership('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
        self.movie_sql = connection_SQL.movie('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')
        self.showing_sql = connection_SQL.showing('localhost', 'root', passwd.passwd(), '3306', 'cine_paraiso')

        self.font_title = customtkinter.CTkFont(
            family="Arial", size=30, weight="bold", slant="italic")
        self.font_id = customtkinter.CTkFont(
            family="Arial", size=16, weight="bold", slant="italic")

    def interface(self):
        img_2 = self.image.open_image("Image\\Img_sala.jpg",(740, 450))
        lbl_fondo = customtkinter.CTkLabel(self.windows, image=img_2, text='',)
        lbl_fondo.place(x=0, y=0)

        frame_Menu = customtkinter.CTkFrame(self.windows, width=100, height=430)
        frame_Menu.place(x=10,y=10)

        img = self.image.open_image("Image\\user-login.png",(50,50))
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

        self.btn_ticket = customtkinter.CTkButton(frame_Menu, text="Ticket", command=self.Sale, width=80, height=40)
        self.btn_ticket.place(x=10, y=350)
    
    def status_btn_Menu(self,status):
        self.btn_employee.configure(state=status)
        self.btn_membership.configure(state=status)
        self.btn_movie.configure(state=status)
        self.btn_product.configure(state=status)
        self.btn_showing.configure(state=status)
        self.btn_ticket.configure(state=status)

    def create_btn_add_edit_delete(self,frame,title,add_function, modifier_function, leave_function):
        lbl_title = customtkinter.CTkLabel(
            frame, text=f"{title}", font=self.font_title)
        lbl_title.place(x=30, y=25)

        img_add = self.image.open_image("Image\\add.png", (20, 20))
        self.btn_add = customtkinter.CTkButton(
            frame, text="", image=img_add, width=30, height=30, fg_color="DARKBLUE", command=add_function)
        self.btn_add.place(x=440, y=25)

        img_edit = self.image.open_image("Image\\edit.png", (20, 20))
        self.btn_modifier = customtkinter.CTkButton(
            frame, text="", image=img_edit, width=30, height=30, fg_color="DARKBLUE", command=modifier_function)
        self.btn_modifier.place(x=480, y=25)

        img_delete = self.image.open_image("Image\\delete.png", (20, 20))
        self.btn_leave = customtkinter.CTkButton(
            frame, text="", image=img_delete, width=30, height=30, fg_color="DARKBLUE", command=leave_function)
        self.btn_leave.place(x=520, y=25)

    def status_btn_add_modifier_delete(self,status):
        self.btn_add.configure(state=status)
        self.btn_modifier.configure(state=status)
        self.btn_leave.configure(state=status)
    
    def combobox_values(self,search, table, text=""):
        list_values = []
        values = self.movie_sql.Select_all(search, table)
        for count_values in range(len(values)):
            list_values.append(text + str(values[count_values][0]))
        return list_values

    def Employee(self):
        self.status_btn_Menu('disabled')
        frame_employee = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_employee.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_employee, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id, option):
            global frame_form,txt_rfc, txt_name, txt_email, txt_address, txt_phone, cmb_post

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

            self.status_btn_add_modifier_delete('disabled')

        def close():
            table_employee.destroy_frame()
            frame_employee.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.employee_sql.last_id('idempleado', 'empleado') + 1
            form(id, 'Agregar')

        def Modifier():
            key, value = table_employee.select_row()

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                form(key, 'Modificar')

                txt_rfc.insert(0, value[0])
                txt_name.insert(0, value[1])
                txt_email.insert(0, value[2])
                txt_phone.insert(0, value[3])
                txt_address.insert(0,value[4])
                cmb_post.set(value[5])

        def Leave():
            key, value = table_employee.select_row()

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                option = messagebox.askquestion('Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.employee_sql.leave('empleado','fecha_baja','idempleado',key)
                    content = self.employee_sql.Select_one('*','empleado','fecha_baja','NULL')
                    table_employee.clean_table()
                    table_employee.add_content(content)

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
            self.status_btn_add_modifier_delete('normal')
            content = self.employee_sql.Select_one('*', 'empleado', 'fecha_baja', 'NULL')
            table_employee.clean_table()
            table_employee.add_content(content)

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                self.status_btn_add_modifier_delete('normal')

        btn_close = customtkinter.CTkButton(frame_employee, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        self.create_btn_add_edit_delete(frame_button, "Empleado", Add, Modifier, Leave)
        table_employee = tkinter_table(frame_employee,('col1', 'col2', 'col3', 'col4', 'col5', 'col6'), ['ID', 'RFC', 'Nombre', 'Correo', 'Telefono', 'Direccion', 'Cargo'])
        table_employee.create_table()
        content = self.employee_sql.Select_one('*','empleado','fecha_baja','NULL')
        table_employee.add_content(content)

    def Membership(self):
        self.status_btn_Menu('disabled')
        frame_membership = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_membership.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_membership, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id,option):
            global frame_form, txt_name, txt_email, cmb_type

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

            self.status_btn_add_modifier_delete('disabled')

        def close():
            table_membership.destroy_frame()
            frame_membership.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.membership_sql.last_id('idmembresia', 'membresia') + 1
            form(id,'Agregar')

        def Modifier():
            key, value = table_membership.select_row()

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                form(key, 'Modificar')

                txt_name.insert(0, value[0])
                txt_email.insert(0, value[1])
                cmb_type.set(value[2])

        def Leave():
            key, value = table_membership.select_row()

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.membership_sql.leave('membresia','fecha_baja','idmembresia',key)
                    content = self.membership_sql.Select_one('*', 'membresia', 'fecha_baja', 'NULL')
                    table_membership.clean_table()
                    table_membership.add_content(content)

        def Save(id, option):
            if option == 'Agregar':
                self.membership_sql.Add(id, txt_name.get(), txt_email.get(), cmb_type.get())
                messagebox.showinfo("Agregar", "Nuevo membresia agregada")
            else:
                self.membership_sql.Modifier(id, txt_name.get(), txt_email.get(), cmb_type.get())
                messagebox.showinfo('Modificar', 'Se modificaron los datos de la membresia')

            frame_form.destroy()
            self.status_btn_add_modifier_delete('normal')
            content = self.membership_sql.Select_one('*', 'membresia', 'fecha_baja', 'NULL')
            table_membership.clean_table()
            table_membership.add_content(content)

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                self.status_btn_add_modifier_delete('normal')

        btn_close = customtkinter.CTkButton(
            frame_membership, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)
        
        self.create_btn_add_edit_delete(frame_button, "Membresias", Add, Modifier, Leave)
        content = self.membership_sql.Select_one('*','membresia','fecha_baja','NULL')
        table_membership = tkinter_table(frame_membership, ('col1','col2','col3','col4'),['ID','Nombre','Correo','Tipo','Fecha de Creacion'])
        table_membership.create_table()
        table_membership.add_content(content)

    def Movie(self):
        self.status_btn_Menu('disabled')
        frame_movie = customtkinter.CTkFrame(
            self.windows, width=600, height=430)
        frame_movie.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(
            frame_movie, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id, option):
            global frame_form, txt_title, cmb_languages, chk_subtitles, btn_poster, txt_duraction, txt_genres

            frame_form = customtkinter.CTkFrame(
                frame_movie, width=580, height=300)
            frame_form.place(x=10, y=120)

            lbl_form = customtkinter.CTkLabel(
                frame_form, text=f"{option}", font=self.font_title)
            lbl_form.place(x=50, y=10)

            lbl_id = customtkinter.CTkLabel(
                frame_form, text=f"ID: {id}", font=self.font_id)
            lbl_id.place(x=50, y=50)

            lbl_title = customtkinter.CTkLabel(frame_form, text="Titulo")
            lbl_title.place(x=50, y=85)
            txt_title = customtkinter.CTkEntry(frame_form, width=180)
            txt_title.place(x=110, y=85)

            lbl_languages = customtkinter.CTkLabel(frame_form, text="Idioma")
            lbl_languages.place(x=50, y=120)
            cmb_languages = customtkinter.CTkComboBox(frame_form, values=['ENG','ESP'],width=70)
            cmb_languages.place(x=110, y=120)

            chk_subtitles = customtkinter.CTkCheckBox(frame_form, text="Subtitulos")
            chk_subtitles.place(x=190, y=120)

            lbl_duration = customtkinter.CTkLabel(frame_form, text="Duracion")
            lbl_duration.place(x=50, y=155)
            entry_var = customtkinter.IntVar()
            txt_duraction = customtkinter.CTkEntry(frame_form,textvariable=entry_var ,width=100)
            txt_duraction.place(x=110, y=155)

            lbl_genres = customtkinter.CTkLabel(frame_form, text="Generos")
            lbl_genres.place(x=50,y=190)
            txt_genres = customtkinter.CTkEntry(frame_form, width=100)
            txt_genres.place(x=110,y=190)

            lbl_poster = customtkinter.CTkLabel(frame_form, text="Poster")
            lbl_poster.place(x=50, y=225)
            btn_poster = customtkinter.CTkButton(frame_form, text="Poster", command=self.image.setimage_explorer)
            btn_poster.place(x=110, y=225)

            btn_save = customtkinter.CTkButton(
                frame_form, text="Guardar", width=100, fg_color="GREEN", command=lambda: Save(id, option))
            btn_save.place(x=140, y=260)

            btn_cancel = customtkinter.CTkButton(
                frame_form, text="Cancelar", width=100, fg_color="RED", command=Cancel)
            btn_cancel.place(x=260, y=260)

            self.status_btn_add_modifier_delete('disabled')

        def close():
            table_movie.destroy_frame()
            frame_movie.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.movie_sql.last_id('idpelicula','pelicula') + 1
            form(id, 'Agregar')

        def Modifier():
            key, value = table_movie.select_row()

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                form(key, 'Modificar')

                txt_title.insert(0, value[0])
                cmb_languages.set( value[1])
                if value[2] == '1':
                    chk_subtitles.select(1)
                else:
                    chk_subtitles.deselect(0)
                #txt_synopsis.insert(0, value[3])
                #txt_cast.insert(0, value[4])
                #btn_poster.set(value[5])
                txt_duraction.insert(0,value[6])
                txt_genres.insert(0,value[7])

        def Leave():
            select = table_movie.focus()
            key = table_movie.item(select, 'text')

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                value = table_movie.item(select, 'values')
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.movie_sql.delete('plicula','idpelicula',key)
                    content = self.movie_sql.Select_all('*','pelicula')
                    table_movie.clean_table()
                    table_movie.add_content(content)

        def Save(id, option):
            if option == 'Agregar':
                self.movie_sql.Add(
                    id, txt_title.get(), cmb_languages.get(), chk_subtitles.get(),'NULL','NULL', self.image.getimage_explorer(),txt_duraction.get(),txt_genres.get())
                messagebox.showinfo("Agregar", "Nuevo pelicula agregada")
            else:
                self.movie_sql.Modifier(
                    id, txt_title.get(), cmb_languages.get(), chk_subtitles.get(), 'NULL', 'NULL', self.image.getimage_explorer(), txt_duraction.get(), txt_genres.get())
                messagebox.showinfo(
                    'Modificar', 'Se modificaron los datos de la Pelicula')
            frame_form.destroy()
            self.status_btn_add_modifier_delete('normal')
            content = self.movie_sql.Select_all('*','pelicula')
            table_movie.clean_table()
            table_movie.add_content(content)

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                self.status_btn_add_modifier_delete('normal')

        btn_close = customtkinter.CTkButton(
            frame_movie, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        self.create_btn_add_edit_delete(frame_button,"Pelicula", Add, Modifier, Leave)
        table_movie = tkinter_table(frame_movie, ('col1','col2','col3','col4','col5'), ['ID','Titulo','Idioma','Subtitulos','Duracion','Generos'])
        table_movie.create_table()
        content = self.movie_sql.Select_all('*','pelicula')
        table_movie.add_content(content)

    def Product(self):
        self.status_btn_Menu('disabled')
        frame_product = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_product.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_product, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id, option):
            global txt_name, txt_price, txt_stock, frame_form

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

            self.status_btn_add_modifier_delete('disabled')

        def close():
            table_product.destroy_frame()
            frame_product.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.product_sql.last_id('idproducto', 'producto') + 1
            form(id, 'Agregar')

        def Modifier():
            key, value = table_product.select_row()

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                form(key, 'Modificar')

                txt_name.insert(0, value[0])
                txt_price.insert(0, value[1])
                txt_stock.insert(0,value[2])

        def Leave():
            key, value = table_product.select_row()

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.product_sql.delete('producto','idproducto',key)
                    content = self.product_sql.Select_all('*','producto')
                    table_product.clean_table()
                    table_product.add_content(content)

        def Save(id, option):
            if option == 'Agregar':
                self.product_sql.Add(id, txt_name.get(), txt_price.get(), txt_stock.get())
                messagebox.showinfo("Agregar", "Nuevo membresia agregada")
            else:
                self.product_sql.Modifier(id, txt_name.get(), txt_price.get(), txt_stock.get())
                messagebox.showinfo('Modificar', 'Se modificaron los datos de la membresia')
    
            frame_form.destroy()
            self.status_btn_add_modifier_delete('normal')
            content = self.product_sql.Select_all('*', 'producto')
            table_product.clean_table()
            table_product.add_content(content)

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                self.status_btn_add_modifier_delete('normal')

        btn_close = customtkinter.CTkButton(frame_product, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        self.create_btn_add_edit_delete(frame_button, "Productos", Add, Modifier, Leave)
        table_product = tkinter_table(frame_product, ('col1','col2','col3'), ['ID','Nombre','precio','Stock'])
        table_product.create_table()
        content = self.product_sql.Select_all('*','producto')
        table_product.add_content(content)
        
    def Showing(self):
        self.status_btn_Menu('disabled')
        frame_showing = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_showing.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_showing, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id, option):
            global frame_form, cmb_movie, cmb_cinema_room, txt_date, txt_price

            frame_form = customtkinter.CTkFrame(
                frame_showing, width=580, height=300)
            frame_form.place(x=10, y=120)

            lbl_form = customtkinter.CTkLabel(
                frame_form, text=f"{option}", font=self.font_title)
            lbl_form.place(x=50, y=10)

            lbl_id = customtkinter.CTkLabel(
                frame_form, text=f"ID: {id}", font=self.font_id)
            lbl_id.place(x=50, y=50)

            lbl_movie = customtkinter.CTkLabel(frame_form, text="Pelicula")
            lbl_movie.place(x=50, y=85)

            values_movie = self.combobox_values("titulo","pelicula")
            cmb_movie = customtkinter.CTkComboBox(frame_form,values=values_movie ,width=200)
            cmb_movie.place(x=110, y=85)
            cmb_movie.set("")

            lbl_cinema_room= customtkinter.CTkLabel(frame_form, text="Sala")
            lbl_cinema_room.place(x=50, y=120)

            values_cinema_room = self.combobox_values("idsala", "sala", "Sala ")
            cmb_cinema_room = customtkinter.CTkComboBox(frame_form, values=values_cinema_room ,width=100)
            cmb_cinema_room.place(x=110, y=120)
            cmb_cinema_room.set("")

            lbl_date = customtkinter.CTkLabel(frame_form, text="Fecha")
            lbl_date.place(x=50, y=155)
            txt_date = customtkinter.CTkEntry(frame_form, width=100)
            txt_date.place(x=110, y=155)

            lbl_price = customtkinter.CTkLabel(frame_form, text="Precio")
            lbl_price.place(x=50, y=190)
            txt_price = customtkinter.CTkEntry(frame_form, width=100)
            txt_price.place(x=110, y=190)

            btn_save = customtkinter.CTkButton(
                frame_form, text="Guardar", width=100, fg_color="GREEN", command=lambda: Save(id, option))
            btn_save.place(x=140, y=240)

            btn_cancel = customtkinter.CTkButton(
                frame_form, text="Cancelar", width=100, fg_color="RED", command=Cancel)
            btn_cancel.place(x=260, y=240)

            self.status_btn_add_modifier_delete('disabled')

        def close():
            table_showing.destroy_frame()
            frame_showing.destroy()
            self.status_btn_Menu('normal')

        def Add():
            id = self.showing_sql.last_id('idfuncion', 'funcion') + 1
            form(id, 'Agregar')

        def Modifier():
            key, value = table_showing.select_row()

            if key == "":
                messagebox.showwarning("Modificar", "Selecciona un elemento")
            else:
                form(key, 'Modificar')

                cmb_movie.set( value[0])
                cmb_cinema_room.set( "Sala "+value[1])
                txt_date.insert(0, value[2])
                txt_price.insert(0, value[3])

        def Leave():
            key, value = table_showing.select_row()

            if key == "":
                messagebox.showwarning("Baja", "Selecciona un elemento")
            else:
                option = messagebox.askquestion(
                    'Baja', f'Dar de baja a {value[0]}')
                if option == 'yes':
                    self.showing_sql.delete('funcion','idfuncion',key)

                    content = self.showing_sql.Select_all('*', 'detalle_funcion')
                    table_showing.clean_table()
                    table_showing.add_content(content)

        def Save(id, option):
            idmovie = self.showing_sql.Select_one("idpelicula","pelicula","titulo",cmb_movie.get(),True)
            characters = "Sala "
            idroom = cmb_cinema_room.get()
            for x in range(len(characters)):
                idroom = idroom.replace(characters[x],"")
                
            if option == 'Agregar':
                self.showing_sql.Add(id,idmovie,idroom, txt_date.get(), txt_price.get())
                messagebox.showinfo("Agregar", "Nueva funcion registrada")
            else:
                self.showing_sql.Modifier(id, idmovie, idroom, txt_date.get(), txt_price.get())
                messagebox.showinfo(
                    'Modificar', 'Se modificaron los datos de la funcion')
                
            frame_form.destroy()
            self.status_btn_add_modifier_delete('normal')

            table_showing.clean_table()
            content = self.showing_sql.Select_all('*', 'detalle_funcion')
            table_showing.add_content(content)

        def Cancel():
            option = messagebox.askokcancel(
                'Cancelar', 'Seguro que quiere cancelar')
            if option:
                frame_form.destroy()
                self.status_btn_add_modifier_delete('normal')

        btn_close = customtkinter.CTkButton(
            frame_showing, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)

        self.create_btn_add_edit_delete(
            frame_button, "Funciones", Add, Modifier, Leave)
        
        table_showing = tkinter_table(frame_showing,('col1','col2','col3','col4'),['ID','Pelicula','Sala','Fecha y Hora', 'Precio'])
        table_showing.create_table()
        content = self.showing_sql.Select_all('*', 'detalle_funcion')
        table_showing.add_content(content)

    def Sale(self):
        self.status_btn_Menu('disabled')
        frame_sale = customtkinter.CTkFrame(self.windows, width=600, height=430)
        frame_sale.place(x=120, y=10)

        frame_button = customtkinter.CTkFrame(frame_sale, width=580, height=80)
        frame_button.place(x=10, y=25)

        def form(id, option):
            pass

        def close():
            frame_sale.destroy()
            self.status_btn_Menu('normal')

        def Add():
            pass

        def Modifier():
            pass

        def Leave():
            pass

        def Save(id, option):
            pass

        def Cancel():
            pass

        btn_close = customtkinter.CTkButton(
            frame_sale, width=10, height=10, text="X", fg_color="RED", command=close)
        btn_close.place(x=0, y=0)
        
if __name__ == "__main__":
    # ----> Agregar el login

    # -----------------------

    name = "Ricardo"
    ID = 1

    app = customtkinter.CTk()
    app.geometry('740x450')
    app.resizable(False,False)
    app.title('Cinema Paraiso')

    interface_cine = Menu(app,name,ID)
    interface_cine.interface()

    app.mainloop()