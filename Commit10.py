import tkinter as tk
from tkinter import messagebox
import random

ROUND_TIME = 60

WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река", "спиральная модель"
]

COLORS = ["red", "blue", "green", "orange", "purple"]

TIME_OPTIONS = [15, 30, 45, 60]
SCORE_OPTIONS = [25, 50, 75, 100]
SOLO_PLAYER_OPTIONS = [3, 4, 5, 6, 7]
TEAM_COUNT_OPTIONS = [2, 3, 4, 5]


class AliasGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Alias")
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
            "player_count": 1,
            "team_count": 2
        }

        self.show_menu()

    # ====== МЕНЮ ======
    def show_menu(self):
        self.stop_timer()
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="ALIAS", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Button(main_frame, text="Одиночная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("solo")).pack(pady=10)

        tk.Button(main_frame, text="Командная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.choose_chip("team")).pack(pady=10)

        tk.Button(main_frame, text="Правила игры",
                  font=("Arial", 20), width=25,
                  command=self.show_rules).pack(pady=10)

        tk.Button(main_frame, text="Выход",
                  font=("Arial", 20), width=25,
                  command=self.root.quit).pack(pady=10)

    # ====== ПРАВИЛА ======
    def show_rules(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

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

        tk.Label(main_frame, text="Правила игры",
                 font=("Arial", 36, "bold")).pack(pady=20)

        tk.Label(main_frame, text=rules,
                 font=("Arial", 20), justify="left").pack(pady=20)

        tk.Button(main_frame, text="Назад",
                  font=("Arial", 18),
                  command=self.show_menu).pack(pady=20)

    # ====== НАСТРОЙКИ ИГРЫ ======
    def game_settings_menu(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="НАСТРОЙКИ ИГРЫ",
                 font=("Arial", 32, "bold")).pack(pady=30)

        # Настройка времени
        time_frame = tk.Frame(main_frame)
        time_frame.pack(pady=10)
        tk.Label(time_frame, text="Время раунда:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
        self.time_var = tk.IntVar(value=self.game_settings["round_time"])
        for t in TIME_OPTIONS:
            tk.Radiobutton(time_frame, text=f"{t} сек", font=("Arial", 14),
                           variable=self.time_var, value=t).pack(side=tk.LEFT, padx=5)

        # Настройка слов для победы
        score_frame = tk.Frame(main_frame)
        score_frame.pack(pady=10)
        tk.Label(score_frame, text="Слов для победы:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
        self.score_var = tk.IntVar(value=self.game_settings["win_score"])
        for s in SCORE_OPTIONS:
            tk.Radiobutton(score_frame, text=str(s), font=("Arial", 14),
                           variable=self.score_var, value=s).pack(side=tk.LEFT, padx=5)

        if self.mode == "solo":
            # Настройка количества игроков
            players_frame = tk.Frame(main_frame)
            players_frame.pack(pady=10)
            tk.Label(players_frame, text="Количество игроков:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
            self.players_var = tk.IntVar(value=self.game_settings["player_count"])
            for p in SOLO_PLAYER_OPTIONS:
                tk.Radiobutton(players_frame, text=str(p), font=("Arial", 14),
                               variable=self.players_var, value=p).pack(side=tk.LEFT, padx=5)
        else:
            # Настройка количества команд
            teams_frame = tk.Frame(main_frame)
            teams_frame.pack(pady=10)
            tk.Label(teams_frame, text="Количество команд:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
            self.teams_var = tk.IntVar(value=self.game_settings["team_count"])
            for t in TEAM_COUNT_OPTIONS:
                tk.Radiobutton(teams_frame, text=str(t), font=("Arial", 14),
                               variable=self.teams_var, value=t).pack(side=tk.LEFT, padx=5)

        tk.Button(main_frame, text="Далее", font=("Arial", 20),
                  command=self.save_settings_and_continue).pack(pady=30)

    def save_settings_and_continue(self):
        self.game_settings["round_time"] = self.time_var.get()
        self.game_settings["win_score"] = self.score_var.get()

        if self.mode == "solo":
            self.game_settings["player_count"] = self.players_var.get()
            self.choose_chip("solo")
        else:
            self.game_settings["team_count"] = self.teams_var.get()
            self.choose_chip("team")

    # ====== ВЫБОР ЦВЕТА ======
    def choose_chip(self, mode):
        self.mode = mode
        self.clear_window()

        if mode == "solo":
            self.team_colors = [None] * self.game_settings["player_count"]
            self.team_names = [f"Игрок {i + 1}" for i in range(self.game_settings["player_count"])]
            self.current_player_index = 0
            self.choose_color_for_player()
        else:
            self.team_colors = [None] * self.game_settings["team_count"]
            self.team_names = [f"Команда {i + 1}" for i in range(self.game_settings["team_count"])]
            self.current_team_index = 0
            self.choose_color_for_team()

    def choose_color_for_player(self):
        if self.current_player_index >= len(self.team_colors):
            self.start_game()
            return

        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text=f"{self.team_names[self.current_player_index]}, выберите цвет фишки",
                 font=("Arial", 32)).pack(pady=30)

        for color in COLORS:
            tk.Button(
                main_frame, text=color.upper(),
                font=("Arial", 18),
                bg=color, fg="white",
                width=20, height=2,
                command=lambda c=color: self.set_player_color(c)
            ).pack(pady=8)

    def set_player_color(self, color):
        self.team_colors[self.current_player_index] = color
        self.current_player_index += 1
        self.choose_color_for_player()

    def choose_color_for_team(self):
        if self.current_team_index >= len(self.team_colors):
            self.enter_team_names()
            return

        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text=f"{self.team_names[self.current_team_index]}, выберите цвет фишки",
                 font=("Arial", 32)).pack(pady=30)

        for color in COLORS:
            tk.Button(
                main_frame, text=color.upper(),
                font=("Arial", 18),
                bg=color, fg="white",
                width=20, height=2,
                command=lambda c=color: self.set_team_color(c)
            ).pack(pady=8)

    def set_team_color(self, color):
        self.team_colors[self.current_team_index] = color
        self.current_team_index += 1
        self.choose_color_for_team()

    def enter_team_names(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Введите названия команд",
                 font=("Arial", 32, "bold")).pack(pady=30)

        self.name_entries = []
        for i, name in enumerate(self.team_names):
            frame = tk.Frame(main_frame)
            frame.pack(pady=10)
            tk.Label(frame, text=f"Команда {i + 1}:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, font=("Arial", 18), width=20)
            entry.insert(0, name)
            entry.pack(side=tk.LEFT)
            self.name_entries.append(entry)

        tk.Button(main_frame, text="Начать игру", font=("Arial", 20),
                  command=self.save_team_names).pack(pady=30)

    def save_team_names(self):
        for i, entry in enumerate(self.name_entries):
            if entry.get().strip():
                self.team_names[i] = entry.get().strip()
        self.start_game()

    # ====== ИГРА ======
    def start_game(self):
        self.stop_timer()
        self.time_left = self.game_settings["round_time"]
        self.team_scores = [0] * len(self.team_colors)
        self.current_team = 0
        self.clear_window()
        self.create_widgets()
        self.next_word()
        self.update_timer()

    def create_widgets(self):
        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        # Информация о текущей команде/игроке
        if self.mode == "solo":
            info_text = f"Ходит {self.team_names[self.current_team]}"
        else:
            info_text = f"Ходит {self.team_names[self.current_team]}"

        self.info_label = tk.Label(
            main_frame,
            text=info_text,
            font=("Arial", 24)
        )
        self.info_label.pack(pady=10)

        self.word_label = tk.Label(
            main_frame,
            font=("Arial", 48),
            fg=self.team_colors[self.current_team]
        )
        self.word_label.pack(pady=40)

        self.timer_label = tk.Label(main_frame, font=("Arial", 24))
        self.timer_label.pack()

        # Отображение счетов
        score_text = self.get_score_text()
        self.score_label = tk.Label(
            main_frame,
            text=score_text,
            font=("Arial", 20)
        )
        self.score_label.pack(pady=20)

        btns = tk.Frame(main_frame)
        btns.pack(pady=20)

        tk.Button(btns, text="УГАДАЛИ", font=("Arial", 20),
                  width=12, command=self.correct).pack(side=tk.LEFT, padx=20)

        tk.Button(btns, text="ПРОПУСК", font=("Arial", 20),
                  width=12, command=self.next_word).pack(side=tk.RIGHT, padx=20)

        tk.Button(main_frame, text="В меню",
                  font=("Arial", 16),
                  command=self.show_menu).pack(pady=10)

        # Отображение цели игры
        tk.Label(main_frame,
                 text=f"Цель: {self.game_settings['win_score']} слов",
                 font=("Arial", 14)).pack(pady=5)

    def get_score_text(self):
        if self.mode == "solo":
            scores = []
            for i, score in enumerate(self.team_scores):
                scores.append(f"{self.team_names[i]}: {score}")
            return " | ".join(scores)
        else:
            scores = []
            for i, score in enumerate(self.team_scores):
                scores.append(f"{self.team_names[i]}: {score}")
            return " | ".join(scores)

    def next_word(self):
        self.word_label.config(text=random.choice(WORDS))

    def correct(self):
        self.team_scores[self.current_team] += 1
        self.score_label.config(text=self.get_score_text())

        # Проверка победы
        if self.team_scores[self.current_team] >= self.game_settings["win_score"]:
            self.end_game_winner()
        else:
            self.next_word()

    def update_timer(self):
        self.timer_label.config(text=f"Время: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def end_round(self):
        if self.mode == "solo":
            # В одиночном режиме просто показываем результат и возвращаемся в меню
            winner_name = self.team_names[self.current_team]
            winner_score = self.team_scores[self.current_team]
            messagebox.showinfo("Раунд окончен",
                                f"{winner_name} набрал {winner_score} слов!\n\nВозвращаемся в меню.")
            self.show_menu()
        else:
            # В командном режиме переключаем команду
            self.current_team = (self.current_team + 1) % len(self.team_colors)
            self.start_game()

    def end_game_winner(self):
        winner_name = self.team_names[self.current_team]
        winner_score = self.team_scores[self.current_team]

        self.stop_timer()
        messagebox.showinfo("ПОБЕДА!",
                            f"{winner_name} победил(а)!\nНабрано слов: {winner_score}")
        self.show_menu()

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