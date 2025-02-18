import tkinter as tk
from tkinter import ttk
import random


def process_height():
    height = entry.get()

    entry_label.pack_forget()
    entry.pack_forget()
    send_button.pack_forget()

    processing_label.config(image=processing_img)
    processing_label.image = processing_img
    processing_label.pack(pady=10)

    status_label.pack(pady=10)

    update_status()

    root.after(6000, lambda: show_result(height))


def update_status():
    status_label.config(text=random.choice(status_messages))
    root.after(1000, update_status)


def show_result(height):
    processing_label.pack_forget()
    status_label.pack_forget()

    result_label.config(text=f"Ваш рост: {height}")
    result_label.pack(pady=20)


root = tk.Tk()
root.title("кАЛЬКУЛЯТОР РОСТА")
root.geometry("300x250")

entry_label = ttk.Label(root, text="Введите ваш рост:")
entry_label.pack(pady=10)
entry = ttk.Entry(root)
entry.pack()

send_button = ttk.Button(root, text="Отправить", command=process_height)
send_button.pack(pady=10)

processing_label = ttk.Label(root)

processing_img = tk.PhotoImage(file="analyzing-solving.gif")

status_label = ttk.Label(root, text="", font=("Arial", 10))

status_messages = [
    "Запускаем сверхкомпьютер...",
    "Крутится, вертится, вычисляется...",
    "Уравниваем уравнения...",
    "Спрашиваем у ChatGPT...",
    "Калькулятор перегрелся... ждём...",
    "Проверяем по таблице умножения...",
    "Спрашиваем у Шелдона Купера...",
    "Танцы с бубном...",
]

result_label = ttk.Label(root, font=("Arial", 14))

root.mainloop()
