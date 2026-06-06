# Коммит №1 - База: Структура приложения и главное меню.
import tkinter as tk
from tkinter import messagebox
import random
import os

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
        main_frame.pack(expand = True)
        tk.Label(main_frame, text = "ALIES", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Button(main_frame, text = "Одиночная игра", font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("solo")).pack(pady=10)

        tk.Button(main_frame, text = "Командная игра", font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("team")).pack(pady=10)

        tk.Button(main_frame, text="Правила игры", font=("Arial", 20), width=25,
                  command=self.show_rules).pack(pady=10)

        tk.Button(main_frame, text = "Выход", font=("Arial", 20), width=25,
                  command = self.root.quit).pack(pady=10)
    def show_rules(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Правила игры в разработке",
                 font=("Arial", 36, "bold")).pack(pady=10)

        tk.Button(main_frame, text="Назад в меню", font=("Arial", 18), command=self.show_menu).pack(pady=20)

    def start_settings(self,mode):
        self.mode = mode
        self.game_settings_menu()
    def game_settings_menu(self):
        self.clear_window()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Настройки игры в разработке", font=("Arial", 32, "bold")).pack(pady=30)
        tk.Button(main_frame, text="Назад в меню",font=("Arial", 18), bg="gray", fg="white",
                  command=self.show_menu).pack(pady=40)

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()

