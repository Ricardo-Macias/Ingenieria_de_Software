import customtkinter
from tkinter import filedialog
from PIL import Image

class files:
    def __init__(self):
        self.poster = None

    def open_image(self,img, render=()):
        img = Image.open(img)
        if (render):
            return customtkinter.CTkImage(img, size=render)
        else:
            return img
        
    def setfile_explore(self):
        self.poster = filedialog.askopenfilename(title="Buscar Poster",filetypes=[("Archivos de imagen",("*.jpg","*.png","*.jpeg"))])
    
    def getfile_explore(self):
        return self.poster
