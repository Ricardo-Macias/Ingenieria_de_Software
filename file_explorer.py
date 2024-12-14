import customtkinter
from tkinter import filedialog
from PIL import Image

class image_explorer:
    def __init__(self):
        self.poster = None

    def open_image(self,img, render=()):
        img = Image.open(img)
        if (render):
            return customtkinter.CTkImage(img, size=render)
        else:
            return img
        
    def setimage_explorer(self):
        self.poster = filedialog.askopenfilename(title="Buscar Imagen",filetypes=[("Archivos de imagen",("*.jpg","*.png","*.jpeg"))])
    
    def getimage_explorer(self):
        return self.poster
