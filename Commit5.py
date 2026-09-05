import tkinter as tk
import random

# ====== НАСТРОЙКИ ======
ROUND_TIME = 60
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река", "спиральная модель"
]

COLORS = ["red", "blue", "green", "orange", "purple"]


class AliasGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Alias")
        self.root.geometry("400x300")

        self.chip_color = "blue"
        self.score = 0
        self.time_left = ROUND_TIME

        self.show_menu()

    # ====== МЕНЮ ======
    def show_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Alias", font=("Arial", 26)).pack(pady=20)

        tk.Button(self.root, text="Начать игру", width=20,
                  command=self.choose_chip).pack(pady=5)

        tk.Button(self.root, text="Правила игры", width=20,
                  command=self.show_rules).pack(pady=5)

        tk.Button(self.root, text="Выход", width=20,
                  command=self.root.quit).pack(pady=5)

    # ====== ПРАВИЛА ======
    def show_rules(self):
        rules_window = tk.Toplevel(self.root)
        rules_window.title("Правила")
        rules_window.geometry("350x200")

        rules_text = (
            "Объясняй слово, не называя его.\n\n"
            "Если слово угадали — нажми «Угадали».\n"
            "Если сложно — нажми «Пропуск».\n\n"
            "За каждое угаданное слово +1 очко.\n"
            "Время ограничено!"
        )

        tk.Label(rules_window, text=rules_text,
                 font=("Arial", 12), justify="left").pack(padx=10, pady=10)

    # ====== ВЫБОР ФИШКИ ======
    def choose_chip(self):
        self.clear_window()

        tk.Label(self.root, text="Выбери фишку",
                 font=("Arial", 18)).pack(pady=10)

        for color in COLORS:
            tk.Button(
                self.root,
                text=color,
                bg=color,
                fg="white",
                width=15,
                command=lambda c=color: self.start_game(c)
            ).pack(pady=3)

    # ====== ИГРА ======
    def start_game(self, color):
        self.chip_color = color
        self.score = 0
        self.time_left = ROUND_TIME
        self.current_word = ""

        self.clear_window()
        self.create_widgets()
        self.next_word()
        self.update_timer()

    def create_widgets(self):
        self.word_label = tk.Label(
            self.root, text="", font=("Arial", 24),
            fg=self.chip_color
        )
        self.word_label.pack(pady=20)

        self.timer_label = tk.Label(
            self.root, text=f"Время: {self.time_left}",
            font=("Arial", 14)
        )
        self.timer_label.pack()

        self.score_label = tk.Label(
            self.root, text=f"Счёт: {self.score}",
            font=("Arial", 14)
        )
        self.score_label.pack(pady=10)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        self.correct_button = tk.Button(
            buttons_frame, text="Угадали",
            width=12, bg=self.chip_color, fg="white",
            command=self.correct
        )
        self.correct_button.pack(side=tk.LEFT, padx=10)

        self.skip_button = tk.Button(
            buttons_frame, text="Пропуск",
            width=12,
            command=self.skip
        )
        self.skip_button.pack(side=tk.RIGHT, padx=10)

    def next_word(self):
        self.current_word = random.choice(WORDS)
        self.word_label.config(text=self.current_word)

    def correct(self):
        self.score += 1
        self.score_label.config(text=f"Счёт: {self.score}")
        self.next_word()

    def skip(self):
        self.next_word()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Время: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.word_label.config(text="Время вышло!")
        self.correct_button.config(state=tk.DISABLED)
        self.skip_button.config(state=tk.DISABLED)

        tk.Button(self.root, text="В меню",
                  command=self.show_menu).pack(pady=10)

    # ====== УТИЛИТА ======
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = AliasGame(root)
    root.mainloop()