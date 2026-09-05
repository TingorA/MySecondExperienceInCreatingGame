import tkinter as tk
from tkinter import messagebox
import random

WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист",
    "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река", "спиральная модель"
]

# Теперь 9 цветов
COLORS = [
    "red", "blue", "green", "orange", "purple",
    "pink", "cyan", "brown", "yellow"
]

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
            "player_count": 3,
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
                  command=lambda: self.start_settings("solo")).pack(pady=10)

        tk.Button(main_frame, text="Командная игра",
                  font=("Arial", 20), width=25,
                  command=lambda: self.start_settings("team")).pack(pady=10)

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
            "— каждый игрок играет за себя\n"
            "— игроки ходят по очереди\n"
            "— побеждает тот, кто первым наберет нужное количество слов\n\n"
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
    def start_settings(self, mode):
        self.mode = mode
        self.game_settings_menu()

    def game_settings_menu(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="НАСТРОЙКИ ИГРЫ",
                 font=("Arial", 32, "bold")).pack(pady=30)

        # Настройка времени
        time_frame = tk.Frame(main_frame)
        time_frame.pack(pady=15)
        tk.Label(time_frame, text="Время раунда:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.time_var = tk.IntVar(value=self.game_settings["round_time"])
        for t in TIME_OPTIONS:
            tk.Radiobutton(time_frame, text=f"{t} сек", font=("Arial", 16),
                           variable=self.time_var, value=t).pack(side=tk.LEFT, padx=8)

        # Настройка слов для победы
        score_frame = tk.Frame(main_frame)
        score_frame.pack(pady=15)
        tk.Label(score_frame, text="Слов для победы:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.score_var = tk.IntVar(value=self.game_settings["win_score"])
        for s in SCORE_OPTIONS:
            tk.Radiobutton(score_frame, text=str(s), font=("Arial", 16),
                           variable=self.score_var, value=s).pack(side=tk.LEFT, padx=8)

        if self.mode == "solo":
            # Настройка количества игроков
            players_frame = tk.Frame(main_frame)
            players_frame.pack(pady=15)
            tk.Label(players_frame, text="Количество игроков:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.players_var = tk.IntVar(value=self.game_settings["player_count"])
            for p in SOLO_PLAYER_OPTIONS:
                tk.Radiobutton(players_frame, text=str(p), font=("Arial", 16),
                               variable=self.players_var, value=p).pack(side=tk.LEFT, padx=8)
        else:
            # Настройка количества команд
            teams_frame = tk.Frame(main_frame)
            teams_frame.pack(pady=15)
            tk.Label(teams_frame, text="Количество команд:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.teams_var = tk.IntVar(value=self.game_settings["team_count"])
            for t in TEAM_COUNT_OPTIONS:
                tk.Radiobutton(teams_frame, text=str(t), font=("Arial", 16),
                               variable=self.teams_var, value=t).pack(side=tk.LEFT, padx=8)

        tk.Button(main_frame, text="Далее", font=("Arial", 20),
                  command=self.save_settings_and_continue).pack(pady=40)

    def save_settings_and_continue(self):
        self.game_settings["round_time"] = self.time_var.get()
        self.game_settings["win_score"] = self.score_var.get()

        if self.mode == "solo":
            self.game_settings["player_count"] = self.players_var.get()
            self.enter_player_names()
        else:
            self.game_settings["team_count"] = self.teams_var.get()
            self.enter_team_names()

    # ====== ВВОД ИМЕН ======
    def enter_player_names(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Введите имена игроков",
                 font=("Arial", 32, "bold")).pack(pady=30)

        # Создаем фрейм с прокруткой для большого количества игроков
        canvas_frame = tk.Frame(main_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        canvas = tk.Canvas(canvas_frame, height=400)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.name_entries = []
        for i in range(self.game_settings["player_count"]):
            frame = tk.Frame(scrollable_frame)
            frame.pack(pady=8)
            tk.Label(frame, text=f"Игрок {i + 1}:", font=("Arial", 16), width=12).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, font=("Arial", 16), width=25)
            entry.insert(0, f"Игрок {i + 1}")
            entry.pack(side=tk.LEFT)
            self.name_entries.append(entry)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Button(main_frame, text="Далее", font=("Arial", 20),
                  command=self.save_player_names).pack(pady=20)

    def save_player_names(self):
        self.team_names = []
        for entry in self.name_entries:
            name = entry.get().strip()
            if not name:
                name = "Игрок"
            self.team_names.append(name)

        self.choose_colors_for_players()

    def enter_team_names(self):
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="Введите названия команд",
                 font=("Arial", 32, "bold")).pack(pady=30)

        self.name_entries = []
        for i in range(self.game_settings["team_count"]):
            frame = tk.Frame(main_frame)
            frame.pack(pady=10)
            tk.Label(frame, text=f"Команда {i + 1}:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, font=("Arial", 18), width=25)
            entry.insert(0, f"Команда {i + 1}")
            entry.pack(side=tk.LEFT)
            self.name_entries.append(entry)

        tk.Button(main_frame, text="Далее", font=("Arial", 20),
                  command=self.save_team_names).pack(pady=30)

    def save_team_names(self):
        self.team_names = []
        for entry in self.name_entries:
            name = entry.get().strip()
            if not name:
                name = "Команда"
            self.team_names.append(name)

        self.choose_colors_for_teams()

    # ====== ВЫБОР ЦВЕТОВ ======
    def choose_colors_for_players(self):
        self.team_colors = [None] * len(self.team_names)
        self.current_color_index = 0
        self.choose_next_player_color()

    def choose_next_player_color(self):
        if self.current_color_index >= len(self.team_colors):
            self.start_game()
            return

        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text=f"{self.team_names[self.current_color_index]}, выберите цвет фишки",
                 font=("Arial", 28)).pack(pady=40)

        # Создаем сетку для цветов 3x3 (9 цветов)
        colors_frame = tk.Frame(main_frame)
        colors_frame.pack(pady=20)

        row, col = 0, 0
        for color in COLORS:
            if col == 3:
                row += 1
                col = 0

            # Названия цветов на русском для лучшего восприятия
            color_names = {
                "red": "КРАСНЫЙ", "blue": "СИНИЙ", "green": "ЗЕЛЕНЫЙ",
                "orange": "ОРАНЖЕВЫЙ", "purple": "ФИОЛЕТОВЫЙ", "pink": "РОЗОВЫЙ",
                "cyan": "ГОЛУБОЙ", "brown": "КОРИЧНЕВЫЙ", "yellow": "ЖЕЛТЫЙ"
            }

            btn = tk.Button(
                colors_frame, text=color_names.get(color, color.upper()),
                font=("Arial", 14, "bold"),
                bg=color, fg="white",
                width=15, height=2,
                command=lambda c=color: self.set_player_color(c)
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1

        # Добавляем информацию о том, сколько цветов осталось
        remaining_colors = len(COLORS) - self.current_color_index
        if remaining_colors < len(self.team_colors) - self.current_color_index:
            tk.Label(main_frame,
                     text=f"⚠️ Внимание: осталось {len(self.team_colors) - self.current_color_index} игроков, но доступно только {remaining_colors} цветов!",
                     font=("Arial", 12), fg="red").pack(pady=10)

    def set_player_color(self, color):
        self.team_colors[self.current_color_index] = color
        self.current_color_index += 1
        self.choose_next_player_color()

    def choose_colors_for_teams(self):
        self.team_colors = [None] * len(self.team_names)
        self.current_color_index = 0
        self.choose_next_team_color()

    def choose_next_team_color(self):
        if self.current_color_index >= len(self.team_colors):
            self.start_game()
            return

        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text=f"{self.team_names[self.current_color_index]}, выберите цвет фишки",
                 font=("Arial", 28)).pack(pady=40)

        # Создаем сетку для цветов 3x3 (9 цветов)
        colors_frame = tk.Frame(main_frame)
        colors_frame.pack(pady=20)

        row, col = 0, 0
        for color in COLORS:
            if col == 3:
                row += 1
                col = 0

            # Названия цветов на русском для лучшего восприятия
            color_names = {
                "red": "КРАСНЫЙ", "blue": "СИНИЙ", "green": "ЗЕЛЕНЫЙ",
                "orange": "ОРАНЖЕВЫЙ", "purple": "ФИОЛЕТОВЫЙ", "pink": "РОЗОВЫЙ",
                "cyan": "ГОЛУБОЙ", "brown": "КОРИЧНЕВЫЙ", "yellow": "ЖЕЛТЫЙ"
            }

            btn = tk.Button(
                colors_frame, text=color_names.get(color, color.upper()),
                font=("Arial", 14, "bold"),
                bg=color, fg="white",
                width=15, height=2,
                command=lambda c=color: self.set_team_color(c)
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1

    def set_team_color(self, color):
        self.team_colors[self.current_color_index] = color
        self.current_color_index += 1
        self.choose_next_team_color()

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
            info_text = f"Ходит: {self.team_names[self.current_team]}"
            turn_text = f"Очередь: {' → '.join(self.team_names)}"
        else:
            info_text = f"Ходит: {self.team_names[self.current_team]}"
            turn_text = f"Очередь: {' → '.join(self.team_names)}"

        self.info_label = tk.Label(
            main_frame,
            text=info_text,
            font=("Arial", 24),
            fg=self.team_colors[self.current_team]
        )
        self.info_label.pack(pady=10)

        # Показываем очередь ходов
        self.turn_label = tk.Label(
            main_frame,
            text=turn_text,
            font=("Arial", 14),
            fg="gray"
        )
        self.turn_label.pack(pady=5)

        self.word_label = tk.Label(
            main_frame,
            font=("Arial", 48, "bold"),
            fg=self.team_colors[self.current_team]
        )
        self.word_label.pack(pady=40)

        self.timer_label = tk.Label(main_frame, font=("Arial", 28))
        self.timer_label.pack(pady=10)

        # Отображение счетов
        score_text = self.get_score_text()
        self.score_label = tk.Label(
            main_frame,
            text=score_text,
            font=("Arial", 20),
            justify=tk.LEFT
        )
        self.score_label.pack(pady=20)

        btns = tk.Frame(main_frame)
        btns.pack(pady=30)

        tk.Button(btns, text="УГАДАЛИ ✓", font=("Arial", 20, "bold"),
                  width=12, bg="#4CAF50", fg="white",
                  command=self.correct).pack(side=tk.LEFT, padx=20)

        tk.Button(btns, text="ПРОПУСК ✗", font=("Arial", 20, "bold"),
                  width=12, bg="#FF5722", fg="white",
                  command=self.next_word).pack(side=tk.RIGHT, padx=20)

        tk.Button(main_frame, text="В меню", font=("Arial", 16),
                  command=self.show_menu).pack(pady=20)

        # Отображение цели игры
        tk.Label(main_frame,
                 text=f"Цель: {self.game_settings['win_score']} слов",
                 font=("Arial", 14)).pack(pady=5)

    def get_score_text(self):
        scores = []
        for i, (name, score) in enumerate(zip(self.team_names, self.team_scores)):
            if self.mode == "solo" and i == self.current_team:
                scores.append(f"👉 {name}: {score} 👈")
            else:
                scores.append(f"{name}: {score}")
        return "\n".join(scores)

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
        self.timer_label.config(text=f"⏱️ Время: {self.time_left} сек")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def end_round(self):
        self.stop_timer()

        if self.mode == "solo":
            # В одиночном режиме переключаем на следующего игрока
            self.current_team = (self.current_team + 1) % len(self.team_colors)

            # Проверяем, завершили ли все игроки свой ход
            all_played = True
            for score in self.team_scores:
                if score < self.game_settings["win_score"]:
                    all_played = False
                    break

            # Если кто-то уже достиг цели, игра должна была закончиться раньше
            # Просто переключаем ход и продолжаем игру
            self.start_game()
        else:
            # В командном режиме переключаем команду
            self.current_team = (self.current_team + 1) % len(self.team_colors)
            self.start_game()

    def end_game_winner(self):
        self.stop_timer()
        self.show_results("🏆 ПОБЕДА! 🏆")

    def show_results(self, title):
        """Показывает экран с результатами"""
        self.clear_window()

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        # Заголовок
        tk.Label(main_frame, text=title,
                 font=("Arial", 48, "bold"),
                 fg="gold").pack(pady=30)

        # Информация о победителе
        max_score = max(self.team_scores)
        winners = []
        for i, (name, score) in enumerate(zip(self.team_names, self.team_scores)):
            if score == max_score:
                winners.append((name, score, i))

        if len(winners) == 1:
            winner_text = f"Победитель: {winners[0][0]}!"
            tk.Label(main_frame, text=winner_text,
                     font=("Arial", 36, "bold"),
                     fg=self.team_colors[winners[0][2]]).pack(pady=20)
            tk.Label(main_frame, text=f"Набрано слов: {winners[0][1]}",
                     font=("Arial", 24)).pack()
        else:
            winner_text = "НИЧЬЯ!"
            tk.Label(main_frame, text=winner_text,
                     font=("Arial", 36, "bold"),
                     fg="orange").pack(pady=20)
            tk.Label(main_frame, text="Победители:",
                     font=("Arial", 28)).pack(pady=10)
            for name, score, i in winners:
                tk.Label(main_frame, text=f"{name} ({score} слов)",
                         font=("Arial", 24),
                         fg=self.team_colors[i]).pack()

        # Результаты всех игроков/команд
        tk.Label(main_frame, text="\nВсе результаты:",
                 font=("Arial", 28, "bold")).pack(pady=20)

        results_frame = tk.Frame(main_frame)
        results_frame.pack(pady=10)

        for i, (name, score) in enumerate(zip(self.team_names, self.team_scores)):
            result_text = f"{name}: {score} слов"
            color = self.team_colors[i]
            tk.Label(results_frame, text=result_text,
                     font=("Arial", 20),
                     fg=color).pack(pady=5)

        # Кнопка в меню
        tk.Button(main_frame, text="В главное меню",
                  font=("Arial", 20, "bold"),
                  bg="#4CAF50", fg="white",
                  width=20, height=2,
                  command=self.show_menu).pack(pady=40)

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