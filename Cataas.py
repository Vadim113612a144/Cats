from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)

        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()

        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)

        # Открываем изображение с помощью PIL
        img = Image.open(image_data)

        # Изменяем размер изображения
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)

        # функция вернет картинку в img
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


# def set_image():
#     # Вызываем функцию для загрузки изображения
#     img = load_image(url)
#
#     if img:
#         # Устанавливаем изображение в метку
#         label.config(image=img)
#         label.image = img


def open_new_window():
    tag = tag_entry.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)


    if img:
        # Создаем новое вторичное окно
        new_window = Toplevel()
        new_window.title("Картинка с котиком") # пропишем заголовок нового окна
        new_window.geometry("600x480") # размер изображения

        # Добавляем изображение в новое окно
        label = Label(new_window, image=img)  # !!!метка в новом окне
        label.image = img  # Сохраняем ссылку на изображение
        label.pack()


def exit():
    window.destroy()




window = Tk()
window.title("Cats!")
window.geometry("600x520")

# Поле ввода для тегов
tag_entry = Entry()
tag_entry.pack()

# Кнопка для загрузки изображения с тегом
load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()


# # Создаем метку без изображения
# label = Label()
# label.pack()

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)


# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

# file_menu1 = Menu(menu_bar)
# menu_bar.add_cascade(label="Файл1", menu=file_menu1)
# file_menu1.add_command(label="Загрузить фото", command=set_image)
# file_menu1.add_separator()
# file_menu1.add_command(label="Выход", command=exit)


# # Добавляем кнопку для обновления изображения
# update_button = Button(text="Обновить", command=set_image)
# update_button.pack()

url = 'https://cataas.com/cat'

# Вызываем функцию для установки изображения в метку
# set_image()


window.mainloop()


