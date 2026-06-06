import tkinter as tk
from tkinter import messagebox
import random
import os



def load_words_from_file(filename="words.txt"):
    words = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if word and not word.startswith("#"):
                    words.append(word)
    if not words:
        print(f"Предупреждение: файл {filename} не найден. Используются стандартные слова.")
        words = ["самолёт", "компьютер", "дерево", "кофе", "программист", "телефон", "книга", "школа"]
    return words


WORDS = load_words_from_file("words.txt")
COLORS = ["red", "blue", "green", "orange", "purple", "pink", "cyan", "brown", "yellow"]
COLOR_NAMES = {
    "red": "Красный", "blue": "Синий", "green": "Зеленый",
    "orange": "Оранжевый", "purple": "Фиолетовый", "pink": "Розовый",
    "cyan": "Голубой", "brown": "Коричневый", "yellow": "Желтый"
}
TIME_OPTIONS = [15, 30, 45, 60]
SCORE_OPTIONS = [25, 50, 75, 100]
SOLO_PLAYER_OPTIONS = [3, 4, 5, 6, 7]
TEAM_COUNT_OPTIONS = [2, 3, 4, 5]


class AliasGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Alies")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.mode = None
        self.team_scores = []
        self.team_names = []
        self.team_colors = []
        self.current_team = 0
        self.timer_id = None
        self.game_settings = {
            "round_time": 60,
            "win_score": 25,
            "player_count": 3,
            "team_count": 2
        }
        self.used_words = []
        self.current_word = ""

        self.show_menu()

    def show_menu(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        tk.Label(main_frame, text="ALIES", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Button(main_frame, text="Одиночная игра", font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("solo")).pack(pady=10)

        tk.Button(main_frame, text="Командная игра", font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("team")).pack(pady=10)

        tk.Button(main_frame, text="Правила игры", font=("Arial", 20), width=25,
                  command=self.show_rules).pack(pady=10)

        tk.Button(main_frame, text="Выход", font=("Arial", 20), width=25,
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

        tk.Label(main_frame, text="Правила игры", font=("Arial", 36, "bold")).pack(pady=20)
        tk.Label(main_frame, text=rules, font=("Arial", 20), justify="left").pack(pady=20)

        word_info = f"📚 В игре загружено слов: {len(WORDS)}"
        tk.Label(main_frame, text=word_info, font=("Arial", 14), fg="blue").pack(pady=5)

        tk.Button(main_frame, text="Назад в меню", font=("Arial", 18), command=self.show_menu).pack(pady=20)

    def show_game_turn(self):
        turn_window = tk.Toplevel(self.root)
        turn_window.title("Ход игры - ALIES")
        turn_window.geometry("700x550")
        turn_window.transient(self.root)
        turn_window.grab_set()

        turn_window.update_idletasks()
        x = (turn_window.winfo_screenwidth() // 2) - (700 // 2)
        y = (turn_window.winfo_screenheight() // 2) - (550 // 2)
        turn_window.geometry(f"+{x}+{y}")

        main_frame = tk.Frame(turn_window)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        tk.Label(main_frame, text="Ход игры", font=("Arial", 32, "bold")).pack(pady=20)

        turn_desc = (
            "📖 ОПИСАНИЕ ХОДА:\n\n"
            "1️⃣ Задача объясняющего — объяснить слово, не называя его напрямую\n"
            "2️⃣ Задача отгадывающих — угадать слово\n\n"
            "✅ Если слово угадано → нажимайте «УГАДАЛИ» (+1 балл)\n"
            "❌ Если слово сложное → нажимайте «ПРОПУСК» (-1 балл, но не ниже 0)\n"
            "⏱️ На ход даётся ограниченное время\n"
            "🎯 Побеждает тот, кто первым наберёт нужное количество слов\n\n"
            "💡 Советы:\n"
            "• Используйте синонимы, антонимы, ассоциации\n"
            "• Можно объяснять жестами и мимикой\n"
            "• Нельзя использовать однокоренные слова\n"
            "• Нельзя переводить слово на другой язык\n\n"
            f"📚 В игре {len(WORDS)} слов. Слова не повторяются в одной сессии"
        )

        text_widget = tk.Text(main_frame, font=("Arial", 14), wrap=tk.WORD, height=18)
        text_widget.insert("1.0", turn_desc)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH, pady=10)

        tk.Button(main_frame, text="Закрыть", font=("Arial", 14), command=turn_window.destroy).pack(pady=20)

    def start_settings(self, mode):
        self.mode = mode
        self.game_settings_menu()

    def game_settings_menu(self):
        self.clear_window()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Настройки игры в разработке", font=("Arial", 32, "bold")).pack(pady=30)
        tk.Button(main_frame, text="Назад в меню", font=("Arial", 18), bg="gray", fg="white",
                  command=self.show_menu).pack(pady=40)

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()