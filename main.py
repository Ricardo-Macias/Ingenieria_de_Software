import customtkinter
from PIL import Image

class log_in:

    def __init__(self,app):
        self.frame = customtkinter.CTkFrame(app, height=300, width=300)
        self.frame.place(x=50, y=50)

        image = Image.open("Image\\user-login.png")
        login = customtkinter.CTkImage(image, size=(100,100))

        lbl_login = customtkinter.CTkLabel(self.frame, image=login, text="")
        lbl_login.place(x=100,y=10)

        lbl_users = customtkinter.CTkLabel(self.frame, text="Usuario ")
        lbl_users.place(x=50,y=130)
        self.txt_users = customtkinter.CTkEntry(self.frame,width=200)
        self.txt_users.place(x=50,y=160)

        lbl_password = customtkinter.CTkLabel(self.frame, text="Password")
        lbl_password.place(x=50,y=190)
        self.txt_password = customtkinter.CTkEntry(self.frame, width=200)
        self.txt_password.place(x=50,y=220)
        self.txt_password.configure(show="*")

        btn_log_in = customtkinter.CTkButton(self.frame, text="Iniciar secion", command=self.log)
        btn_log_in.place(x=75, y=260)
        
    def log(self):
        if (self.txt_users.get() == "Rick" and self.txt_password.get() == "123"):
            print("sesion iniciada")
        else:
            print("contraseña incorrecta")



if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("400x400")

    img = Image.open("Image\\Fondo.jpg")
    render = customtkinter.CTkImage(img,size=(400,400))

    lbl_image = customtkinter.CTkLabel(app, image=render, text="")
    lbl_image.place(x=0,y=0)

    log_in(app)

    app.mainloop()