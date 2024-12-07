import customtkinter
from tkinter import filedialog
from PIL import Image

def open_image(img, render=()):
    img = Image.open(img)
    if (render):
        return customtkinter.CTkImage(img, size=render)
    else:
        return img
    
def file_explore():
    poster = filedialog.askopenfilename(title="Buscar Poster",filetypes=[("Archivos de imagen",("*.jpg","*.png","*.jpeg"))])
    return poster
