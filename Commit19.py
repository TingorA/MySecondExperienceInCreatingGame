# КОММИТ 2: Загрузка слов из файла и правила игры
# Сообщение: feat: add word loading from file and game rules screen

import tkinter as tk
from tkinter import messagebox
import random
import os


def load_words_from_file(filename="words.txt"):
    """Загружает список слов из текстового файла (по одному слову на строку)"""
    words = []

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if word and not word.startswith("#"):
                    words.append(word)

    if not words:
        print("Предупреждние: файл",filename,"не найден. Используются стандартные слова.")
        words = ["самолёт",'учёба',"кофе",'школа',"друг",'девушка','кроссовки',"рыба","лекарство","вода"]

    return words


WORDS = load_words_from_file("words.txt")


class AliasGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Alies")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.mode = None
        self.show_menu()

    def show_menu(self):
        self.clear_window()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="ALIES", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Button(main_frame, text="Одиночная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("solo")).pack(pady=10)

        tk.Button(main_frame, text="Командная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("team")).pack(pady=10)

        tk.Button(main_frame, text="Правила игры",
                  font=("Arial", 20), width=25,
                  command=self.show_rules).pack(pady=10)

        tk.Button(main_frame, text="Выход",
                  font=("Arial", 20), width=25,
                  command=self.root.quit).pack(pady=10)

    def show_rules(self):
        self.clear_window()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        rules = (
            "ALIES — объясни слово, не называя его напрямую.\n\n"
            "✔ Можно использовать синонимы\n"
            "✔ Можно описывать\n"
            "✖ Нельзя использовать однокоренные слова\n\n"
            "Одиночная игра:\n"
            "— каждый игрок играет за себя\n"
            "— игроки ходят по очереди\n"
            "— побеждает тот, кто первым наберет нужное количество слов\n\n"
            "Командная игра:\n"
            "— команды ходят по очереди\n"
            "— выигрывает команда с большим счётом\n\n"
            "Штрафы:\n"
            "— за пропуск слова снимается 1 балл (но не ниже 0)\n\n"
        )

        tk.Label(main_frame, text="Правила игры",
                 font=("Arial", 36, "bold")).pack(pady=20)

        tk.Label(main_frame, text=rules,
                 font=("Arial", 20), justify="left").pack(pady=20)

        word_info = f"📚 В игре загружено слов: {len(WORDS)}"
        tk.Label(main_frame, text=word_info,
                 font=("Arial", 14), fg="blue").pack(pady=5)

        tk.Button(main_frame, text="Назад в меню",
                  font=("Arial", 18),
                  command=self.show_menu).pack(pady=20)

    def start_settings(self, mode):
        self.mode = mode
        self.game_settings_menu()

    def game_settings_menu(self):
        self.clear_window()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="НАСТРОЙКИ ИГРЫ (в разработке)",
                 font=("Arial", 32, "bold")).pack(pady=30)

        tk.Button(main_frame, text="Назад в меню",
                  font=("Arial", 18), bg="gray", fg="white",
                  command=self.show_menu).pack(pady=40)

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()