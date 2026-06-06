import tkinter as tk
from tkinter import messagebox
import random
import os


def load_words_from_file(filename="words.txt"):
    words = []
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if word and not word.startswith('#'):
                    words.append(word)
    if not words:
        words = ["самолёт", 'учёба', "кофе", 'школа', "друг", 'девушка', 'кроссовки', "рыба", "лекарство", "вода"]
    return words


WORDS = load_words_from_file('words.txt')


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
        # Словарь для хранения выбранных настроек (Новое в Шаге 3)
        self.game_settings = {
            "round_time": 60,
            "win_score": 25,
            "player_count": 3,
            "team_count": 2
        }
        self.show_menu()

    def show_menu(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        tk.Label(main_frame, text="Добро пожаловать в ALIES 👽", font=("Arial", 48, "bold")).pack(pady=40)

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
        rules = ('ALIES — объясни слово, не называя его напрямую.\n\n'
                 '✔️ Можно использовать синонимы\n'
                 '✔️ Можно описывать\n'
                 '❌ Нельзя использовать однокоренные слова\n\n'
                 'Одиночная игра:\n'
                 '⤳ каждый игрок играет за себя\n'
                 '⤳ игроки ходят по очереди\n'
                 '⤳ побеждает тот, кто первым наберет нужное количество слов\n\n'
                 'Командная игра:\n'
                 '⤳ команды ходят по очереди\n'
                 '⤳ выигрывает команда с большим счётом\n\n'
                 '❌ Штрафы: ❌\n'
                 '⤳ за пропуск слова снимается 1 балл (но не ниже 0)\n\n'
                 )
        tk.Label(main_frame, text="💡 Правила игры 💡", font=("Arial", 36, "bold")).pack(pady=20)
        tk.Label(main_frame, text=rules, font=("Arial", 20), justify="left").pack(pady=20)
        word_info = f"📙 В игре загружено слов: {len(WORDS)}"
        tk.Label(main_frame, text=word_info, font=("Arial", 14), fg="blue").pack(pady=5)
        tk.Button(main_frame, text="Назад в меню", font=("Arial", 18), command=self.show_menu).pack(pady=20)

    def start_settings(self, mode):
        self.mode = mode
        self.game_settings_menu()

    # Окно настроек полностью переработано
    def game_settings_menu(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="⚙️ НАСТРОЙКИ ИГРЫ ⚙️", font=("Arial", 32, "bold")).pack(pady=30)

        # Выбор времени
        time_frame = tk.Frame(main_frame)
        time_frame.pack(pady=15)
        tk.Label(time_frame, text="⏱️ Время раунда:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.time_var = tk.IntVar(value=self.game_settings["round_time"])
        for t in TIME_OPTIONS:
            tk.Radiobutton(time_frame, text=f"{t} сек", font=("Arial", 16),
                           variable=self.time_var, value=t).pack(side=tk.LEFT, padx=8)

        # Выбор очков для победы
        score_frame = tk.Frame(main_frame)
        score_frame.pack(pady=15)
        tk.Label(score_frame, text="🎯 Слов для победы:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.score_var = tk.IntVar(value=self.game_settings["win_score"])
        for s in SCORE_OPTIONS:
            tk.Radiobutton(score_frame, text=str(s), font=("Arial", 16),
                           variable=self.score_var, value=s).pack(side=tk.LEFT, padx=8)

        # Выбор участников в зависимости от режима
        if self.mode == "solo":
            players_frame = tk.Frame(main_frame)
            players_frame.pack(pady=15)
            tk.Label(players_frame, text="👤 Количество игроков:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.players_var = tk.IntVar(value=self.game_settings["player_count"])
            for p in SOLO_PLAYER_OPTIONS:
                tk.Radiobutton(players_frame, text=str(p), font=("Arial", 16),
                               variable=self.players_var, value=p).pack(side=tk.LEFT, padx=8)
        else:
            teams_frame = tk.Frame(main_frame)
            teams_frame.pack(pady=15)
            tk.Label(teams_frame, text="👥 Количество команд:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.teams_var = tk.IntVar(value=self.game_settings["team_count"])
            for t in TEAM_COUNT_OPTIONS:
                tk.Radiobutton(teams_frame, text=str(t), font=("Arial", 16),
                               variable=self.teams_var, value=t).pack(side=tk.LEFT, padx=8)

        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=40)
        tk.Button(buttons_frame, text="Назад в меню", font=("Arial", 18), bg="gray", fg="white",
                  command=self.show_menu).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Далее ➔", font=("Arial", 18), bg="green", fg="white",
                  command=self.save_settings_and_continue).pack(side=tk.RIGHT, padx=10)

    def save_settings_and_continue(self):
        self.game_settings["round_time"] = self.time_var.get()
        self.game_settings["win_score"] = self.score_var.get()
        if self.mode == "solo":
            self.game_settings["player_count"] = self.players_var.get()
        else:
            self.game_settings["team_count"] = self.teams_var.get()

        # Переход к вводу имен (пока заглушка)
        messagebox.showinfo("Настройки", "Настройки сохранены успешно!")

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()