import tkinter as tk
import random

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
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.mode = None
        self.team_scores = [0, 0]
        self.team_colors = [None, None]
        self.current_team = 0
        self.timer_id = None

        self.show_menu()

    # ====== МЕНЮ ======
    def show_menu(self):
        self.stop_timer()
        self.clear_window()

        tk.Label(self.root, text="ALIAS", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Button(self.root, text="Одиночная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("solo")).pack(pady=10)

        tk.Button(self.root, text="Командная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("team")).pack(pady=10)

        tk.Button(self.root, text="Правила игры",
                  font=("Arial", 20), width=25,
                  command=self.show_rules).pack(pady=10)

        tk.Button(self.root, text="Выход",
                  font=("Arial", 20), width=25,
                  command=self.root.quit).pack(pady=10)

    # ====== ПРАВИЛА ======
    def show_rules(self):
        self.clear_window()

        rules = (
            "ALIAS — объясни слово, не называя его напрямую.\n\n"
            "✔ Можно использовать синонимы\n"
            "✔ Можно описывать\n"
            "✖ Нельзя использовать однокоренные слова\n\n"
            "Одиночная игра:\n"
            "— набери как можно больше слов за время\n\n"
            "Командная игра:\n"
            "— команды ходят по очереди\n"
            "— выигрывает команда с большим счётом"
        )

        tk.Label(self.root, text="Правила игры",
                 font=("Arial", 36, "bold")).pack(pady=20)

        tk.Label(self.root, text=rules,
                 font=("Arial", 20), justify="left").pack(pady=20)

        tk.Button(self.root, text="Назад",
                  font=("Arial", 18),
                  command=self.show_menu).pack(pady=20)

    # ====== ВЫБОР ЦВЕТА ======
    def choose_chip(self, mode):
        self.mode = mode
        self.clear_window()

        if mode == "team":
            text = f"Команда {len([c for c in self.team_colors if c]) + 1}, выберите цвет"
        else:
            text = "Выберите цвет фишки"

        tk.Label(self.root, text=text, font=("Arial", 32)).pack(pady=30)

        for color in COLORS:
            tk.Button(
                self.root, text=color.upper(),
                font=("Arial", 18),
                bg=color, fg="white",
                width=20, height=2,
                command=lambda c=color: self.color_chosen(c)
            ).pack(pady=8)

    def color_chosen(self, color):
        if self.mode == "solo":
            self.team_colors[0] = color
            self.start_game()
        else:
            index = 0 if self.team_colors[0] is None else 1
            self.team_colors[index] = color
            if None in self.team_colors:
                self.choose_chip("team")
            else:
                self.start_game()

    # ====== ИГРА ======
    def start_game(self):
        self.stop_timer()
        self.time_left = ROUND_TIME
        self.clear_window()

        if self.mode == "solo":
            self.team_scores = [0, 0]
            self.current_team = 0

        self.create_widgets()
        self.next_word()
        self.update_timer()

    def create_widgets(self):
        tk.Label(
            self.root,
            text=f"Ходит команда {self.current_team + 1}" if self.mode == "team" else "",
            font=("Arial", 24)
        ).pack(pady=10)

        self.word_label = tk.Label(
            self.root,
            font=("Arial", 48),
            fg=self.team_colors[self.current_team]
        )
        self.word_label.pack(pady=40)

        self.timer_label = tk.Label(self.root, font=("Arial", 24))
        self.timer_label.pack()

        self.score_label = tk.Label(
            self.root,
            text=f"Команда 1: {self.team_scores[0]}   Команда 2: {self.team_scores[1]}",
            font=("Arial", 24)
        )
        self.score_label.pack(pady=20)

        btns = tk.Frame(self.root)
        btns.pack(pady=20)

        tk.Button(btns, text="УГАДАЛИ", font=("Arial", 20),
                  width=12, command=self.correct).pack(side=tk.LEFT, padx=20)

        tk.Button(btns, text="ПРОПУСК", font=("Arial", 20),
                  width=12, command=self.next_word).pack(side=tk.RIGHT, padx=20)

        tk.Button(self.root, text="В меню",
                  font=("Arial", 16),
                  command=self.show_menu).pack(pady=10)

    def next_word(self):
        self.word_label.config(text=random.choice(WORDS))

    def correct(self):
        self.team_scores[self.current_team] += 1
        self.score_label.config(
            text=f"Команда 1: {self.team_scores[0]}   Команда 2: {self.team_scores[1]}"
        )
        self.next_word()

    def update_timer(self):
        self.timer_label.config(text=f"Время: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def end_round(self):
        self.current_team = 1 - self.current_team
        self.start_game()

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()