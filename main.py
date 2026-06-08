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
        self.stop_timer()
        self.clear_window()
        self.used_words = []
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        tk.Label(main_frame, text="ALIES", font=("Arial", 48, "bold")).pack(pady=40)
        tk.Button(main_frame, text="Одиночная игра", font=("Arial", 20), width=25, command=lambda: self.start_settings("solo")).pack(pady=10)
        tk.Button(main_frame, text="Командная игра", font=("Arial", 20), width=25, command=lambda: self.start_settings("team")).pack(pady=10)
        tk.Button(main_frame, text="Правила игры", font=("Arial", 20), width=25, command=self.show_rules).pack(pady=10)
        tk.Button(main_frame, text="Выход", font=("Arial", 20), width=25, command=self.root.quit).pack(pady=10)

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
        tk.Label(main_frame, text=f"📚 В игре загружено слов: {len(WORDS)}", font=("Arial", 14), fg="blue").pack(pady=5)
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
        tk.Label(main_frame, text="НАСТРОЙКИ ИГРЫ", font=("Arial", 32, "bold")).pack(pady=30)
        time_frame = tk.Frame(main_frame)
        time_frame.pack(pady=15)
        tk.Label(time_frame, text="Время раунда:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.time_var = tk.IntVar(value=self.game_settings["round_time"])
        for t in TIME_OPTIONS:
            tk.Radiobutton(time_frame, text=f"{t} сек", font=("Arial", 16), variable=self.time_var, value=t).pack(side=tk.LEFT, padx=8)
        score_frame = tk.Frame(main_frame)
        score_frame.pack(pady=15)
        tk.Label(score_frame, text="Слов для победы:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
        self.score_var = tk.IntVar(value=self.game_settings["win_score"])
        for s in SCORE_OPTIONS:
            tk.Radiobutton(score_frame, text=str(s), font=("Arial", 16), variable=self.score_var, value=s).pack(side=tk.LEFT, padx=8)
        if self.mode == "solo":
            players_frame = tk.Frame(main_frame)
            players_frame.pack(pady=15)
            tk.Label(players_frame, text="Количество игроков:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.players_var = tk.IntVar(value=self.game_settings["player_count"])
            for p in SOLO_PLAYER_OPTIONS:
                tk.Radiobutton(players_frame, text=str(p), font=("Arial", 16), variable=self.players_var, value=p).pack(side=tk.LEFT, padx=8)
        else:
            teams_frame = tk.Frame(main_frame)
            teams_frame.pack(pady=15)
            tk.Label(teams_frame, text="Количество команд:", font=("Arial", 20)).pack(side=tk.LEFT, padx=15)
            self.teams_var = tk.IntVar(value=self.game_settings["team_count"])
            for t in TEAM_COUNT_OPTIONS:
                tk.Radiobutton(teams_frame, text=str(t), font=("Arial", 16), variable=self.teams_var, value=t).pack(side=tk.LEFT, padx=8)
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=40)
        tk.Button(buttons_frame, text="Назад в меню", font=("Arial", 18), bg="gray", fg="white", command=self.show_menu).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Далее", font=("Arial", 18), bg="green", fg="white", command=self.save_settings_and_continue).pack(side=tk.RIGHT, padx=10)

    def save_settings_and_continue(self):
        self.game_settings["round_time"] = self.time_var.get()
        self.game_settings["win_score"] = self.score_var.get()
        if self.mode == "solo":
            self.game_settings["player_count"] = self.players_var.get()
            self.enter_player_names()
        else:
            self.game_settings["team_count"] = self.teams_var.get()
            self.enter_team_names()

    def enter_player_names(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        tk.Label(main_frame, text="Введите имена игроков", font=("Arial", 32, "bold")).pack(pady=30)
        canvas_frame = tk.Frame(main_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        canvas = tk.Canvas(canvas_frame, height=400)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
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
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=20)
        tk.Button(buttons_frame, text="Назад", font=("Arial", 18), bg="gray", fg="white", command=self.game_settings_menu).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Далее", font=("Arial", 18), bg="green", fg="white", command=self.save_player_names).pack(side=tk.RIGHT, padx=10)

    def save_player_names(self):
        self.team_names = []
        for entry in self.name_entries:
            name = entry.get().strip()
            if not name: name = "Игрок"
            self.team_names.append(name)
        self.choose_colors_for_players()

    def enter_team_names(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        tk.Label(main_frame, text="Введите названия команд", font=("Arial", 32, "bold")).pack(pady=30)
        self.name_entries = []
        for i in range(self.game_settings["team_count"]):
            frame = tk.Frame(main_frame)
            frame.pack(pady=10)
            tk.Label(frame, text=f"Команда {i + 1}:", font=("Arial", 18)).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, font=("Arial", 18), width=25)
            entry.insert(0, f"Команда {i + 1}")
            entry.pack(side=tk.LEFT)
            self.name_entries.append(entry)
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=30)
        tk.Button(buttons_frame, text="Назад", font=("Arial", 18), bg="gray", fg="white", command=self.game_settings_menu).pack(side=tk.LEFT, padx=10)
        tk.Button(buttons_frame, text="Далее", font=("Arial", 18), bg="green", fg="white", command=self.save_team_names).pack(side=tk.RIGHT, padx=10)

    def save_team_names(self):
        self.team_names = []
        for entry in self.name_entries:
            name = entry.get().strip()
            if not name: name = "Команда"
            self.team_names.append(name)
        self.choose_colors_for_teams()

    def get_available_colors(self):
        used_colors = [color for color in self.team_colors if color is not None]
        return [color for color in COLORS if color not in used_colors]

    def choose_colors_for_players(self):
        self.team_colors = [None] * len(self.team_names)
        self.current_color_index = 0
        self.choose_next_player_color()

    def choose_next_player_color(self):
        if self.current_color_index >= len(self.team_colors):
            print("Ввод завершен. Переход к созданию игры в следующем коммите.")
            return
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        used_text = ""
        if self.current_color_index > 0:
            used = [COLOR_NAMES[color] for color in self.team_colors[:self.current_color_index] if color]
            used_text = f"\n\nУже выбраны: {', '.join(used)}"
        tk.Label(main_frame, text=f"{self.team_names[self.current_color_index]}, выберите цвет фишки{used_text}", font=("Arial", 28)).pack(pady=40)
        colors_frame = tk.Frame(main_frame)
        colors_frame.pack(pady=20)
        available = self.get_available_colors()
        row, col = 0, 0
        for color in available:
            if col == 3: row += 1; col = 0
            btn = tk.Button(colors_frame, text=COLOR_NAMES.get(color, color.upper()), font=("Arial", 14, "bold"), bg=color, fg="white", width=15, height=2, command=lambda c=color: self.set_player_color(c))
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
        tk.Button(main_frame, text="Назад к вводу имён", font=("Arial", 16), bg="gray", fg="white", command=self.enter_player_names).pack(pady=30)

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
            return
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)
        used_text = ""
        if self.current_color_index > 0:
            used = [COLOR_NAMES[color] for color in self.team_colors[:self.current_color_index] if color]
            used_text = f"\n\nУже выбраны: {', '.join(used)}"
        tk.Label(main_frame, text=f"{self.team_names[self.current_color_index]}, выберите цвет фишки{used_text}", font=("Arial", 28)).pack(pady=40)
        colors_frame = tk.Frame(main_frame)
        colors_frame.pack(pady=20)
        available = self.get_available_colors()
        row, col = 0, 0
        for color in available:
            if col == 3: row += 1; col = 0
            btn = tk.Button(colors_frame, text=COLOR_NAMES.get(color, color.upper()), font=("Arial", 14, "bold"), bg=color, fg="white", width=15, height=2, command=lambda c=color: self.set_team_color(c))
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
        tk.Button(main_frame, text="Назад к вводу названий", font=("Arial", 16), bg="gray", fg="white", command=self.enter_team_names).pack(pady=30)

    def set_team_color(self, color):
        self.team_colors[self.current_color_index] = color
        self.current_color_index += 1
        self.choose_next_team_color()

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def clear_window(self):
        for w in self.root.winfo_children(): w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    AliasGame(root)
    root.mainloop()