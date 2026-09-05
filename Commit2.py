import tkinter as tk
import random

ROUND_TIME = 60  # секунд
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река"
]



class AliasGame:
    def __init__(self, root):
        self.root = root
        self.clear_window()

        self.root.title("Alias — Игра")
        self.root.geometry("400x350")

        self.score = 0
        self.time_left = ROUND_TIME
        self.current_word = ""
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
        self.current_word = random.choice(WORDS)
        self.word_label.config(text=self.current_word)

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
            self.pause_button.config(text="Продолжить")
            self.word_label.config(text="Пауза")
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

        restart_button = tk.Button(
            self.root, text="Играть ещё раз",
            width=25,
            command=self.restart_game
        )
        restart_button.pack(pady=5)



    def restart_game(self):
        AliasGame(self.root)