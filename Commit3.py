import tkinter as tk
import random

# ====== НАСТРОЙКИ ======
ROUND_TIME = 60  # секунд
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река"
]


# ====== ГЛАВНОЕ МЕНЮ ======
class MainMenu:
    def __init__(self, root):
        self.root = root
        self.clear_window()

        root.title("Alias — Меню")
        root.geometry("400x350")

        tk.Label(
            root, text="Игра Alias",
            font=("Arial", 26)
        ).pack(pady=30)

        tk.Button(
            root, text="Начать игру",
            width=25,
            command=lambda: AliasGame(root)
        ).pack(pady=10)

        tk.Button(
            root, text="Правила",
            width=25,
            command=lambda: RulesScreen(root)
        ).pack(pady=10)

        tk.Button(
            root, text="Выход",
            width=25,
            command=root.quit
        ).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ====== ПРАВИЛА ======
class RulesScreen:
    def __init__(self, root):
        self.root = root
        self.clear_window()

        root.title("Alias — Правила")

        rules_text = (
            "Правила игры Alias:\n\n"
            "1. На экране появляется слово.\n"
            "2. Нужно объяснить его, не называя напрямую.\n"
            "3. Если слово угадали — нажми «Угадали».\n"
            "4. Можно пропускать слова.\n"
            "5. За каждое угаданное слово +1 очко.\n"
            "6. Раунд длится 60 секунд."
        )

        tk.Label(
            root, text=rules_text,
            font=("Arial", 12),
            justify="left"
        ).pack(padx=20, pady=20)

        tk.Button(
            root, text="Назад в меню",
            width=25,
            command=lambda: MainMenu(root)
        ).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ====== ИГРА ======
class AliasGame:
    def __init__(self, root):
        self.root = root
        self.clear_window()

        root.title("Alias — Игра")
        root.geometry("400x380")

        self.score = 0
        self.time_left = ROUND_TIME
        self.is_paused = False
        self.timer_id = None

        self.create_widgets()
        self.next_word()
        self.update_timer()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_widgets(self):
        self.word_label = tk.Label(
            self.root, text="", font=("Arial", 24)
        )
        self.word_label.pack(pady=15)

        self.timer_label = tk.Label(
            self.root, text=f"Время: {self.time_left}",
            font=("Arial", 14)
        )
        self.timer_label.pack()

        self.score_label = tk.Label(
            self.root, text=f"Счёт: {self.score}",
            font=("Arial", 14)
        )
        self.score_label.pack(pady=5)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=15)

        self.correct_button = tk.Button(
            buttons_frame, text="Угадали",
            width=12, command=self.correct
        )
        self.correct_button.grid(row=0, column=0, padx=5)

        self.skip_button = tk.Button(
            buttons_frame, text="Пропуск",
            width=12, command=self.skip
        )
        self.skip_button.grid(row=0, column=1, padx=5)

        self.pause_button = tk.Button(
            self.root, text="Пауза",
            width=25, command=self.toggle_pause
        )
        self.pause_button.pack(pady=5)

    def next_word(self):
        self.word_label.config(text=random.choice(WORDS))

    def correct(self):
        if not self.is_paused:
            self.score += 1
            self.score_label.config(text=f"Счёт: {self.score}")
            self.next_word()

    def skip(self):
        if not self.is_paused:
            self.next_word()

        def toggle_pause(self):
            self.is_paused = not self.is_paused

            if self.is_paused:
                if self.timer_id:
                    self.root.after_cancel(self.timer_id)
                self.word_label.config(text="Пауза")
                self.pause_button.config(text="Продолжить")
            else:
                self.pause_button.config(text="Пауза")
                self.next_word()
                self.update_timer()

        def update_timer(self):
            if self.is_paused:
                return

            if self.time_left > 0:
                self.time_left -= 1
                self.timer_label.config(text=f"Время: {self.time_left}")
                self.timer_id = self.root.after(1000, self.update_timer)
            else:
                self.end_game()

        def end_game(self):
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

            self.word_label.config(text="Время вышло!")
            self.correct_button.config(state=tk.DISABLED)
            self.skip_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.DISABLED)

            tk.Button(
                self.root, text="Играть ещё раз",
                width=25,
                command=lambda: AliasGame(self.root)
            ).pack(pady=5)

            tk.Button(
                self.root, text="В меню",
                width=25,
                command=lambda: MainMenu(self.root)
            ).pack(pady=5)

    # ====== ЗАПУСК ======
    if __name__ == "__main__":
        root = tk.Tk()
        MainMenu(root)
        root.mainloop()