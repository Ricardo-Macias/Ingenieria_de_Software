import customtkinter
from PIL import Image

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

        self.btn_employee = customtkinter.CTkButton(frame_Menu,text="Empledo", command=self.Employee, width=80,height=40)
        self.btn_employee.place(x=10,y=100)

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
    
    def status_btn_Menu(self,status):
        self.btn_employee.configure(state=status)
        self.btn_membership.configure(state=status)
        self.btn_movie.configure(state=status)
        self.btn_product.configure(state=status)
        self.btn_showing.configure(state=status)
        self.btn_ticket.configure(state=status)

    
    def Employee(self):
        self.status_btn_Menu('disabled')

    def Membership(self):
        pass

    def Movie(self):
        pass

    def Product(self):
        pass

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