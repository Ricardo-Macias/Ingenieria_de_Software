import customtkinter
from PIL import Image

def open_image(img, render=()):
    img = Image.open(img)
    if (render):
        return customtkinter.CTkImage(img, size=render)
    else:
        return img
