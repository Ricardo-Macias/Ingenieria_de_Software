import customtkinter
from tkinter import messagebox
from PIL import Image

import passwd
import connection_SQL

class log_in:

    def __init__(self,app):
        self.app = app
        self.frame = customtkinter.CTkFrame(self.app, height=300, width=300)
        self.frame.place(x=50, y=50)

        image = Image.open("Image\\user-login.png")
        login = customtkinter.CTkImage(image, size=(100,100))

        lbl_login = customtkinter.CTkLabel(self.frame, image=login, text="")
        lbl_login.place(x=100,y=10)

        lbl_users = customtkinter.CTkLabel(self.frame, text="Usuario ")
        lbl_users.place(x=50,y=130)
        self.txt_users = customtkinter.CTkEntry(self.frame,width=200)
        self.txt_users.place(x=50,y=160)

        lbl_password = customtkinter.CTkLabel(self.frame, text="ID")
        lbl_password.place(x=50,y=190)
        self.txt_password = customtkinter.CTkEntry(self.frame, width=200)
        self.txt_password.place(x=50,y=220)
        self.txt_password.configure(show="*")

        btn_log_in = customtkinter.CTkButton(self.frame, text="Iniciar secion", command=self.log)
        btn_log_in.place(x=75, y=260)

        self.select_database = connection_SQL.connect_DataBase('localhost','root',passwd.passwd(),'3306','cine_paraiso')
        
    def log(self):
        try:
            user = self.select_database.Select_one('nombre', 'empleado', 'idempleado', self.txt_password.get())
            if (self.txt_users.get() == user[0]):
                print("sesion iniciada")
                self.app.destroy()
            else:
                messagebox.showinfo('Login','Nombre incorrecto')
        except Exception as Ex:
            messagebox.showinfo('ID','ID vacio')


if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("400x400")

    img = Image.open("Image\\Fondo.jpg")
    render = customtkinter.CTkImage(img,size=(400,400))

    lbl_image = customtkinter.CTkLabel(app, image=render, text="")
    lbl_image.place(x=0,y=0)

    log_in(app)

    app.mainloop()