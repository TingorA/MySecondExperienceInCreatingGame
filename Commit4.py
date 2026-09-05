import tkinter as tk
import random

ROUND_TIME = 60
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река"
]


# ====== МЕНЮ ======
class MainMenu:
    def __init__(self, root):
        self.root = root
        self.clear()

        root.title("Alias — Меню")
        root.geometry("400x350")

        tk.Label(root, text="Alias", font=("Arial", 26)).pack(pady=30)

        tk.Button(
            root, text="Начать игру", width=25,
            command=lambda: AliasGame(root)
        ).pack(pady=10)

        tk.Button(
            root, text="Правила", width=25,
            command=lambda: RulesScreen(root)
        ).pack(pady=10)

        tk.Button(
            root, text="Выход", width=25,
            command=root.quit
        ).pack(pady=10)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()


# ====== ПРАВИЛА ======
class RulesScreen:
    def __init__(self, root):
        self.root = root
        self.clear()

        text = (
            "Правила Alias:\n\n"
            "Объясняй слово,\n"
            "не называя его напрямую.\n\n"
            "Угадали — +1 очко\n"
            "Пропуск — без штрафа\n"
            "Время — 60 секунд"
        )

        tk.Label(root, text=text, font=("Arial", 12), justify="left").pack(pady=20)

        tk.Button(
            root, text="Назад в меню", width=25,
            command=lambda: MainMenu(root)
        ).pack(pady=10)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()


# ====== ИГРА ======
class AliasGame:
    def __init__(self, root):
        self.root = root
        self.clear()

        root.title("Alias — Игра")
        root.geometry("400x380")

        self.score = 0
        self.time_left = ROUND_TIME
        self.is_paused = False
        self.timer_id = None

        self.create_ui()
        self.next_word()
        self.update_timer()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def create_ui(self):
        self.word_label = tk.Label(self.root, font=("Arial", 24))
        self.word_label.pack(pady=15)

        self.timer_label = tk.Label(self.root, text="Время: 60", font=("Arial", 14))
        self.timer_label.pack()

        self.score_label = tk.Label(self.root, text="Счёт: 0", font=("Arial", 14))
        self.score_label.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=15)

        tk.Button(frame, text="Угадали", width=12, command=self.correct).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Пропуск", width=12, command=self.skip).grid(row=0, column=1, padx=5)

        self.pause_btn = tk.Button(
            self.root, text="Пауза", width=25, command=self.toggle_pause
        )
        self.pause_btn.pack()

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
            self.pause_btn.config(text="Продолжить")
        else:
            self.pause_btn.config(text="Пауза")
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
        self.pause_btn.config(state=tk.DISABLED)

        tk.Button(
            self.root, text="Играть ещё раз", width=25,
            command=lambda: AliasGame(self.root)
        ).pack(pady=5)

        tk.Button(
            self.root, text="В меню", width=25,
            command=lambda: MainMenu(self.root)
        ).pack(pady=5)

    # ====== ЗАПУСК ======
    if __name__ == "__main__":
        root = tk.Tk()
        MainMenu(root)
        root.mainloop()