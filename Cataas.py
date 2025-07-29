from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats!")
window.geometry("600x480")

# Создаем метку без изображения
label = Label()
label.pack()

# Создаем url адрес в интернете
url = 'https://cataas.com/cat'
img = load_image(url)   # после запроса картинка ляжет в img

# если лежит картинка в img:
if img:
    # Устанавливаем изображение в метку
    label.config(image=img)
    # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
    label.image = img

window.mainloop()


