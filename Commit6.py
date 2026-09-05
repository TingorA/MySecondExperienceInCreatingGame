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
        self.root.title("Alies")

        # Полный экран
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        self.root.bind("<F11>", lambda e: self.root.attributes("-fullscreen",
                                                             not self.root.attributes("-fullscreen")))

        self.mode = "solo"
        self.chip_color = "blue"

        self.team_scores = [0, 0]
        self.current_team = 0

        self.show_menu()

    # ====== МЕНЮ ======
    def show_menu(self):
        self.clear_window()

        tk.Label(self.root, text="ALIES",
                 font=("Arial", 48, "bold")).pack(pady=50)

        tk.Button(self.root, text="Одиночная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("solo")).pack(pady=10)

        tk.Button(self.root, text="Командная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("team")).pack(pady=10)

        tk.Button(self.root, text="Выход",
                  font=("Arial", 20), width=25,
                  command=self.root.quit).pack(pady=10)

    # ====== ВЫБОР ФИШКИ ======
    def choose_chip(self, mode):
        self.mode = mode
        self.clear_window()

        tk.Label(self.root, text="Выберите цвет фишки",
                 font=("Arial", 32)).pack(pady=30)

        for color in COLORS:
            tk.Button(
                self.root, text=color.upper(),
                font=("Arial", 18),
                bg=color, fg="white",
                width=20, height=2,
                command=lambda c=color: self.start_game(c)
            ).pack(pady=8)

    # ====== ИГРА ======
    def start_game(self, color):
        self.chip_color = color
        self.time_left = ROUND_TIME
        self.current_word = ""

        if self.mode == "solo":
            self.score = 0
        else:
            self.team_scores = [0, 0]
            self.current_team = 0

        self.clear_window()
        self.create_widgets()
        self.next_word()
        self.update_timer()

    def create_widgets(self):
        if self.mode == "team":
            self.team_label = tk.Label(
                self.root,
                text=f"Ходит команда {self.current_team + 1}",
                font=("Arial", 24)
            )
            self.team_label.pack(pady=10)

        self.word_label = tk.Label(
            self.root, text="",
            font=("Arial", 48),
            fg=self.chip_color
        )
        self.word_label.pack(pady=40)

        self.timer_label = tk.Label(
            self.root,
            text=f"Время: {self.time_left}",
            font=("Arial", 24)
        )
        self.timer_label.pack()

        if self.mode == "solo":
            self.score_label = tk.Label(
                self.root,
                text=f"Счёт: {self.score}",
                font=("Arial", 24)
            )
        else:
            self.score_label = tk.Label(
                self.root,
                text=f"Команда 1: {self.team_scores[0]}   "
                     f"Команда 2: {self.team_scores[1]}",
                font=("Arial", 24)
            )

        self.score_label.pack(pady=20)

        buttons = tk.Frame(self.root)
        buttons.pack(pady=30)

        tk.Button(
            buttons, text="УГАДАЛИ",
            font=("Arial", 20),
            bg=self.chip_color, fg="white",
            width=12, height=2,
            command=self.correct
        ).pack(side=tk.LEFT, padx=20)

        tk.Button(
            buttons, text="ПРОПУСК",
            font=("Arial", 20),width=12, height=2,
            command=self.skip
        ).pack(side=tk.RIGHT, padx=20)

    def next_word(self):
        self.current_word = random.choice(WORDS)
        self.word_label.config(text=self.current_word)

    def correct(self):
        if self.mode == "solo":
            self.score += 1
            self.score_label.config(text=f"Счёт: {self.score}")
        else:
            self.team_scores[self.current_team] += 1
            self.score_label.config(
                text=f"Команда 1: {self.team_scores[0]}   "
                     f"Команда 2: {self.team_scores[1]}"
            )
        self.next_word()

    def skip(self):
        self.next_word()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Время: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def end_round(self):
        if self.mode == "team":
            self.current_team = 1 - self.current_team
            self.start_game(self.chip_color)
        else:
            self.word_label.config(text="Время вышло!")
            tk.Button(self.root, text="В меню",
                      font=("Arial", 20),
                      command=self.show_menu).pack(pady=20)

    # ====== УТИЛИТА ======
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = AliasGame(root)
    root.mainloop()