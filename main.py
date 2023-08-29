import customtkinter
from tkinter import *
from PIL import Image, ImageTk

class log_in:

    def __init__(self,app):
        self.window = app

        lbl_users = customtkinter.CTkLabel(self.window, text="Usuario ")
        lbl_users.place(x=100,y=150)
        self.txt_users = customtkinter.CTkEntry(self.window,width=200)
        self.txt_users.place(x=100,y=180)

        lbl_password = customtkinter.CTkLabel(self.window, text="Password")
        lbl_password.place(x=100,y=210)
        self.txt_password = customtkinter.CTkEntry(self.window, width=200)
        self.txt_password.place(x=100, y=240)
        self.txt_password.configure(show="*")

        btn_log_in = customtkinter.CTkButton(self.window, text="Iniciar secion", command=self.log)
        btn_log_in.place(x=130,y=290)
        
    def log(self):
        if (self.txt_users.get() == "Rick" and self.txt_password.get() == "123"):
            print("sesion iniciada")
        else:
            print("contraseña incorrecta")



if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("400x400")

    img = Image.open("Fondo.jpg")
    img = img.resize((400,400))
    render = ImageTk.PhotoImage(img)
    lbl_image = customtkinter.CTkLabel(app, image=render, text="")
    lbl_image.place(x=0,y=0)

    log_in(app)

    app.mainloop()