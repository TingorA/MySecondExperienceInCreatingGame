import tkinter as tk
import random

# ====== НАСТРОЙКИ ======
ROUND_TIME = 60  # секунд
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река", "спиральная модель"
]


class AliasGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Попробуй, объяснить")
        self.root.geometry("400x300")

        self.score = 0
        self.time_left = ROUND_TIME
        self.current_word = ""

        self.create_widgets()
        self.next_word()
        self.update_timer()

    def create_widgets(self):
        self.word_label = tk.Label(
            self.root, text="", font=("Arial", 24)
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
            width=12, command=self.correct
        )
        self.correct_button.pack(side=tk.LEFT, padx=10)

        self.skip_button = tk.Button(
            buttons_frame, text="Пропуск",
            width=12, command=self.skip
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


if __name__ == "__main__":
    root = tk.Tk()
    game = AliasGame(root)
    root.mainloop()