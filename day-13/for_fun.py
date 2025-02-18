import tkinter as tk
from tkinter import ttk
import time


def process_height():
    # Получаем значение из поля ввода
    height = entry.get()

    # Скрываем виджеты ввода
    entry_label.pack_forget()
    entry.pack_forget()
    send_button.pack_forget()

    # Показываем gif "обработки"
    processing_label.config(image=processing_img)
    processing_label.image = processing_img  # сохраняем ссылку
    processing_label.pack(pady=20)

    # После задержки (например, 3000 мс = 3 секунды) выводим результат
    root.after(3000, lambda: show_result(height))


def show_result(height):
    # Скрываем gif
    processing_label.pack_forget()

    # Выводим сообщение с результатом
    result_label.config(text=f"Ваш рост: {height}")
    result_label.pack(pady=20)


root = tk.Tk()
root.title("кАЛЬКУЛЯТОР РОСТА")
root.geometry("300x250")

# Метка и поле ввода для роста
entry_label = ttk.Label(root, text="Введите ваш рост:")
entry_label.pack(pady=10)
entry = ttk.Entry(root)
entry.pack()

# Кнопка отправки
send_button = ttk.Button(root, text="Отправить", command=process_height)
send_button.pack(pady=10)

# Метка для отображения gif "обработки"
processing_label = ttk.Label(root)

# Загружаем gif (убедитесь, что файл processing.gif существует)
processing_img = tk.PhotoImage(file="processing.gif")

# Метка для вывода результата
result_label = ttk.Label(root, font=("Arial", 14))

root.mainloop()
