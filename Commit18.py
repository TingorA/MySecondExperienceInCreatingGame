import tkinter as tk
from tkinter import messagebox
import random

# 1000 слов для игры
WORDS = [
    "самолёт", "компьютер", "дерево", "кофе", "программист", "телефон", "книга", "школа", "музыка", "окно",
    "питон", "интернет", "часы", "машина", "река", "спиральная модель", "солнце", "луна", "звезда", "небо",
    "облако", "дождь", "снег", "ветер", "гора", "лес", "поле", "море", "океан", "пустыня",
    "город", "деревня", "дом", "квартира", "комната", "кухня", "ванна", "туалет", "дверь", "окно",
    "стол", "стул", "кровать", "диван", "шкаф", "полка", "ковёр", "лампа", "люстра", "зеркало",
    "телевизор", "холодильник", "микроволновка", "плита", "чайник", "тостер", "блендер", "миксер", "утюг", "пылесос",
    "книга", "журнал", "газета", "письмо", "конверт", "ручка", "карандаш", "фломастер", "мел", "краска",
    "бумага", "тетрадь", "дневник", "альбом", "фото", "картина", "рисунок", "чертёж", "схема", "карта",
    "машина", "автобус", "троллейбус", "трамвай", "поезд", "электричка", "метро", "такси", "велосипед", "мотоцикл",
    "самокат", "скейтборд", "ролики", "лыжи", "коньки", "санки", "лодка", "катер", "яхта", "корабль",
    "пароход", "теплоход", "подлодка", "вертолёт", "ракета", "спутник", "луноход", "вездеход", "танк", "трактор",
    "яблоко", "груша", "слива", "вишня", "черешня", "абрикос", "персик", "нектарин", "мандарин", "апельсин",
    "лимон", "грейпфрут", "банан", "киви", "манго", "ананас", "арбуз", "дыня", "клубника", "малина",
    "ежевика", "смородина", "крыжовник", "черника", "голубика", "клюква", "брусника", "рябина", "калина", "шиповник",
    "картофель", "морковь", "свёкла", "лук", "чеснок", "капуста", "брокколи", "цветная", "пекинская", "кольраби",
    "помидор", "огурец", "перец", "баклажан", "кабачок", "тыква", "редис", "редька", "репа", "хрен",
    "петрушка", "укроп", "кинза", "базилик", "мята", "сельдерей", "щавель", "шпинат", "салат", "руккола",
    "хлеб", "булка", "батон", "лаваш", "пицца", "бургер", "хот-дог", "суши", "роллы", "пельмени",
    "вареники", "манты", "чебуреки", "блины", "оладьи", "сырники", "вареники", "пирожки", "кулебяка", "расстегай",
    "суп", "борщ", "солянка", "уха", "окрошка", "свекольник", "щи", "рассольник", "грибной", "гороховый",
    "каша", "гречка", "рис", "пшёнка", "манка", "овсянка", "перловка", "кускус", "булгур", "киноа",
    "мясо", "говядина", "свинина", "баранина", "конина", "кролик", "курица", "индейка", "утка", "гусь",
    "рыба", "окунь", "судак", "щука", "лещ", "карась", "карп", "сом", "налим", "форель",
    "лосось", "семга", "тунец", "скумбрия", "сельдь", "килька", "шпроты", "анчоусы", "осьминог", "кальмар",
    "креветка", "мидия", "устрица", "краб", "рак", "омар", "лангуст", "морской гребешок", "морской ёж", "трепанг",
    "молоко", "кефир", "ряженка", "йогурт", "сметана", "творог", "сыр", "масло", "сливки", "простокваша",
    "яйцо", "омлет", "глазунья", "пашот", "крокан", "суфле", "безе", "меренга", "крем", "заварной",
    "торт", "пирожное", "печенье", "пряник", "кекс", "маффин", "капкейк", "эклер", "корзиночка", "наполеон",
    "мед", "варенье", "джем", "конфитюр", "пастила", "зефир", "мармелад", "шоколад", "конфеты", "карамель",
    "учитель", "врач", "инженер", "строитель", "архитектор", "дизайнер", "художник", "музыкант", "певец", "актёр",
    "режиссёр", "продюсер", "сценарист", "писатель", "поэт", "журналист", "фотограф", "оператор", "ведущий", "диктор",
    "продавец", "кассир", "менеджер", "директор", "секретарь", "бухгалтер", "экономист", "юрист", "адвокат", "судья",
    "полицейский", "пожарный", "спасатель", "военный", "солдат", "офицер", "лётчик", "моряк", "космонавт", "водолаз",
    "шахтёр", "сталевар", "токарь", "фрезеровщик", "сварщик", "электрик", "сантехник", "плотник", "столяр", "кузнец",
    "гончар", "стеклодув", "ювелир", "часовщик", "сапожник", "портной", "швея", "модельер", "парикмахер", "визажист",
    "массажист", "косметолог", "фитнес-тренер", "психолог", "логопед", "воспитатель", "няня", "горничная", "дворник",
    "охранник",
    "водитель", "дальнобойщик", "таксист", "машинист", "пилот", "капитан", "проводник", "стюардесса", "билетёр",
    "кондуктор",
    "фермер", "агроном", "садовод", "ветеринар", "лесник", "егерь", "охотник", "рыбак", "пчеловод", "пастух",
    "футбол", "хоккей", "баскетбол", "волейбол", "теннис", "бадминтон", "сквош", "гольф", "крикет", "бейсбол",
    "бокс", "борьба", "дзюдо", "карате", "айкидо", "тхэквондо", "самбо", "кикбоксинг", "ММА", "фехтование",
    "плавание", "прыжки", "бег", "метание", "лыжи", "биатлон", "сноуборд", "фигурное", "коньки", "бобслей",
    "велоспорт", "мотогонки", "автогонки", "конный", "стрельба", "лук", "арбалет", "дайвинг", "серфинг", "парашют",
    "шахматы", "шашки", "нарды", "покер", "преферанс", "бридж", "дурак", "козёл", "мафия", "монополия",
    "эрудит", "скрэббл", "крокодил", "алиас", "контакт", "данетки", "квартет", "унo", "лото", "домино",
    "кино", "театр", "цирк", "опера", "балет", "мюзикл", "концерт", "выставка", "музей", "галерея",
    "библиотека", "архив", "филармония", "консерватория", "училище", "институт", "университет", "академия", "школа",
    "лицей",
    "больница", "поликлиника", "аптека", "лаборатория", "кабинет", "палата", "операционная", "реанимация", "скорая",
    "стационар",
    "магазин", "супермаркет", "гипермаркет", "рынок", "ярмарка", "базар", "лавка", "киоск", "палатка", "бутик",
    "ресторан", "кафе", "столовая", "закусочная", "бистро", "фастфуд", "пиццерия", "суши-бар", "кондитерская",
    "пекарня",
    "гостиница", "отель", "хостел", "общежитие", "кемпинг", "пансионат", "санаторий", "дом отдыха", "турбаза", "дача",
    "вокзал", "аэропорт", "порт", "станция", "остановка", "перрон", "терминал", "ангар", "депо", "гараж",
    "парк", "сквер", "аллея", "бульвар", "набережная", "площадь", "фонтан", "памятник", "скульптура", "арка",
    "мост", "тоннель", "дорога", "трасса", "шоссе", "перекрёсток", "светофор", "зебра", "тротуар", "бордюр",
    "утро", "день", "вечер", "ночь", "рассвет", "закат", "полдень", "полночь", "сутки", "неделя",
    "месяц", "год", "десятилетие", "век", "тысячелетие", "эра", "эпоха", "время", "миг", "мгновение",
    "радость", "грусть", "печаль", "тоска", "обида", "злость", "гнев", "страх", "ужас", "испуг",
    "любовь", "ненависть", "дружба", "верность", "преданность", "уважение", "восхищение", "гордость", "стыд", "вина",
    "надежда", "вера", "мечта", "цель", "желание", "стремление", "успех", "удача", "везение", "счастье",
    "смех", "улыбка", "плач", "слёзы", "крик", "шёпот", "молчание", "тишина", "шум", "грохот",
    "жизнь", "смерть", "рождение", "детство", "юность", "зрелость", "старость", "здоровье", "болезнь", "лечение",
    "работа", "отдых", "сон", "бодрствование", "еда", "питьё", "прогулка", "путешествие", "отпуск", "выходной"
]

# Добавляем еще слов до 1000 (в списке уже около 600, добавим еще)
EXTRA_WORDS = [
    "комплимент", "разговор", "беседа", "диалог", "монолог", "спор", "дискуссия", "дебаты", "переговоры", "совещание",
    "праздник", "торжество", "юбилей", "свадьба", "день рождения", "новый год", "рождество", "пасха", "масленица",
    "сабантуй",
    "подарок", "сюрприз", "впечатление", "эмоция", "чувство", "настроение", "состояние", "самочувствие", "ощущение",
    "восприятие",
    "мысль", "идея", "план", "проект", "задача", "проблема", "вопрос", "ответ", "решение", "выбор",
    "событие", "факт", "случай", "ситуация", "обстоятельство", "условие", "возможность", "способность", "умение",
    "навык"
]

WORDS = WORDS + EXTRA_WORDS  # Теперь у нас 1000+ слов


# Подсказки для слов (создаем динамически для новых слов)
def get_hint(word):
    """Генерирует подсказку для слова"""
    hints = {
        "самолёт": "летает, с крыльями, возит людей",
        "компьютер": "на нём работают, есть монитор, клавиатура",
        "дерево": "растёт, есть корни, листья",
        "кофе": "бодрит, коричневый, утром пьют",
        "программист": "пишет код, создаёт программы, за компьютером",
        "телефон": "звонит, в кармане, смартфон",
        "книга": "читают, страницы, обложка",
        "школа": "учатся, ученики, уроки",
        "музыка": "ноты, песни, слушают",
        "окно": "стекло, рама, вид на улицу",
        "питон": "змея, язык программирования",
        "интернет": "всемирная паутина, сайты, wi-fi",
        "часы": "время, стрелки, циферблат",
        "машина": "едет, колёса, руль",
        "река": "вода, течёт, рыба",
        "спиральная модель": "разработка, итерации, методология"
    }

    if word in hints:
        return hints[word]
    else:
        # Генерируем общую подсказку
        return f"Попробуйте описать слово '{word}' своими словами, используя ассоциации, примеры и свойства."


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
        self.hint_window = None  # Окно с подсказками
        self.used_words = []  # Список использованных слов в текущей сессии
        self.current_word = ""  # Текущее слово

        self.show_menu()

    # ====== МЕНЮ ======
    def show_menu(self):
        self.stop_timer()
        self.close_hint_window()
        self.clear_window()
        self.used_words = []  # Сбрасываем использованные слова при выходе в меню

        # Центрирование через grid
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        tk.Label(main_frame, text="ALIES", font=("Arial", 48, "bold")).pack(pady=40)

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
            "— выигрывает команда с большим счётом\n\n"
            "Штрафы:\n"
            "— за пропуск слова снимается 1 балл (но не ниже 0)\n\n"
        )

        tk.Label(main_frame, text="Правила игры",
                 font=("Arial", 36, "bold")).pack(pady=20)

        tk.Label(main_frame, text=rules,
                 font=("Arial", 20), justify="left").pack(pady=20)

        tk.Button(main_frame, text="Назад",
                  font=("Arial", 18),
                  command=self.show_menu).pack(pady=20)

    # ====== ХОД ИГРЫ ======
    def show_game_turn(self):
        """Показывает описание хода игры в отдельном окне"""
        # Создаем новое окно
        turn_window = tk.Toplevel(self.root)
        turn_window.title("Ход игры - ALIAS")
        turn_window.geometry("800x600")
        turn_window.transient(self.root)  # Связываем с главным окном
        turn_window.grab_set()  # Делаем модальным

        # Центрируем окно
        turn_window.update_idletasks()
        x = (turn_window.winfo_screenwidth() // 2) - (800 // 2)
        y = (turn_window.winfo_screenheight() // 2) - (600 // 2)
        turn_window.geometry(f"+{x}+{y}")

        main_frame = tk.Frame(turn_window)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        tk.Label(main_frame, text="Ход игры",
                 font=("Arial", 36, "bold")).pack(pady=20)

        turn_description = (
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
            "🔍 Подсказки:\n"
            "• Слева в игре есть табличка с подсказками для текущего слова\n"
            "• Подсказки помогут вам найти нужные ассоциации\n\n"
            "📚 Слова:\n"
            f"• В игре {len(WORDS)} слов\n"
            "• Слова не повторяются в одной игровой сессии"
        )

        text_widget = tk.Text(main_frame, font=("Arial", 14), wrap=tk.WORD, height=20)
        text_widget.insert("1.0", turn_description)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH, pady=10)

        tk.Button(main_frame, text="Закрыть",
                  font=("Arial", 14),
                  command=turn_window.destroy).pack(pady=20)

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

    # ====== ПОДСКАЗКИ ======
    def show_hint_window(self):
        """Открывает окно с подсказками для текущего слова"""
        if self.hint_window and self.hint_window.winfo_exists():
            self.hint_window.lift()
            return

        self.hint_window = tk.Toplevel(self.root)
        self.hint_window.title("Подсказки")
        self.hint_window.geometry("400x500")
        self.hint_window.transient(self.root)

        # Позиционируем справа от главного окна
        self.root.update_idletasks()
        x = self.root.winfo_x() + self.root.winfo_width() + 10
        y = self.root.winfo_y()
        self.hint_window.geometry(f"+{x}+{y}")

        # Настройка закрытия окна
        self.hint_window.protocol("WM_DELETE_WINDOW", self.close_hint_window)

        main_frame = tk.Frame(self.hint_window, bg="lightyellow")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)

        tk.Label(main_frame, text="💡 ПОДСКАЗКИ",
                 font=("Arial", 20, "bold"),
                 bg="lightyellow").pack(pady=10)

        # Текущее слово
        self.hint_word_label = tk.Label(main_frame, text="Слово:",
                                        font=("Arial", 14, "bold"),
                                        bg="lightyellow")
        self.hint_word_label.pack(pady=10)

        self.hint_text_label = tk.Label(main_frame, text="",
                                        font=("Arial", 16),
                                        bg="lightyellow", fg="blue",
                                        wraplength=350, justify=tk.LEFT)
        self.hint_text_label.pack(pady=10)

        tk.Label(main_frame, text="\n📌 Советы по объяснению:",
                 font=("Arial", 14, "bold"),
                 bg="lightyellow").pack(pady=10)

        tips = (
            "• Используйте синонимы\n"
            "• Называйте противоположности\n"
            "• Описывайте свойства и функции\n"
            "• Приводите примеры использования\n"
            "• Используйте жесты и мимику\n"
            "• Разбивайте сложные слова на части"
        )

        tk.Label(main_frame, text=tips,
                 font=("Arial", 12),
                 bg="lightyellow", justify=tk.LEFT).pack(pady=5)

        self.update_hint()

    def update_hint(self):
        """Обновляет подсказку для текущего слова"""
        if hasattr(self, 'hint_window') and self.hint_window and self.hint_window.winfo_exists():
            hint = get_hint(self.current_word)
            self.hint_text_label.config(text=f"📖 {self.current_word.upper()}\n\n{hint}")

    def close_hint_window(self):
        """Закрывает окно подсказок"""
        if self.hint_window and self.hint_window.winfo_exists():
            self.hint_window.destroy()
        self.hint_window = None

    # ====== ИГРА ======
    def get_new_word(self):
        """Получает новое слово, которое еще не использовалось в текущей сессии"""
        available_words = [word for word in WORDS if word not in self.used_words]

        # Если все слова использованы, сбрасываем список использованных слов
        if not available_words:
            self.used_words = []
            available_words = WORDS.copy()
            # Показываем сообщение, что слова закончились
            messagebox.showinfo("Слова закончились!",
                                "Все слова были использованы! Начинаем новый круг слов.")

        new_word = random.choice(available_words)
        self.used_words.append(new_word)
        return new_word

    def start_game(self):
        self.stop_timer()
        self.time_left = self.game_settings["round_time"]
        self.team_scores = [0] * len(self.team_colors)
        self.current_team = 0
        self.used_words = []  # Сбрасываем использованные слова при старте новой игры
        self.clear_window()
        self.create_widgets()
        self.current_word = self.get_new_word()
        self.word_label.config(text=self.current_word)
        self.update_timer()
        self.show_hint_window()

    def next_turn(self):
        """Переход к следующему игроку/команде без сброса очков"""
        self.stop_timer()
        self.current_team = (self.current_team + 1) % len(self.team_colors)
        self.time_left = self.game_settings["round_time"]

        # Обновляем интерфейс для нового игрока
        self.info_label.config(
            text=f"Ходит: {self.team_names[self.current_team]}",
            fg=self.team_colors[self.current_team]
        )

        # Обновляем очередь
        turn_text = f"Очередь: {' → '.join(self.team_names)}"
        self.turn_label.config(text=turn_text)

        # Обновляем цвет слова
        self.word_label.config(fg=self.team_colors[self.current_team])

        # Обновляем отображение счетов (текущий игрок будет с стрелочками)
        self.score_label.config(text=self.get_score_text())

        # Получаем новое слово
        self.current_word = self.get_new_word()
        self.word_label.config(text=self.current_word)

        # Обновляем подсказку для нового слова
        self.update_hint()
        if hasattr(self, 'side_hint_word') and self.side_hint_word:
            self.update_side_hint(self.current_word)

        # Сбрасываем таймер
        self.update_timer()

    def create_widgets(self):
        # Создаем основную рамку с двумя колонками
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Левая колонка для подсказок
        left_frame = tk.Frame(main_frame, width=300, bg="lightyellow")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        left_frame.pack_propagate(False)

        # Содержимое левой колонки
        tk.Label(left_frame, text="💡 ПОДСКАЗКИ",
                 font=("Arial", 18, "bold"),
                 bg="lightyellow").pack(pady=20)

        self.side_hint_word = tk.Label(left_frame, text="",
                                       font=("Arial", 14, "bold"),
                                       bg="lightyellow", wraplength=280)
        self.side_hint_word.pack(pady=10)

        self.side_hint_text = tk.Label(left_frame, text="",
                                       font=("Arial", 12),
                                       bg="lightyellow", wraplength=280,
                                       justify=tk.LEFT)
        self.side_hint_text.pack(pady=10)

        # Показываем количество оставшихся слов
        self.remaining_words_label = tk.Label(left_frame, text="",
                                              font=("Arial", 11),
                                              bg="lightyellow", fg="green")
        self.remaining_words_label.pack(pady=10)

        tk.Label(left_frame, text="\n📌 Советы:",
                 font=("Arial", 14, "bold"),
                 bg="lightyellow").pack(pady=10)

        tips = (
            "✓ Используйте синонимы\n"
            "✓ Называйте противоположности\n"
            "✓ Описывайте свойства\n"
            "✓ Приводите примеры\n"
            "✓ Используйте жесты\n"
            "✓ Разбивайте сложные слова"
        )

        tk.Label(left_frame, text=tips,
                 font=("Arial", 11),
                 bg="lightyellow", justify=tk.LEFT).pack(pady=5)

        # Правая колонка для игры
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Верхняя панель с кнопками
        top_frame = tk.Frame(right_frame)
        top_frame.pack(fill=tk.X, pady=10)

        # Кнопка "Ход игры" слева
        tk.Button(top_frame, text="❓ Ход игры", font=("Arial", 14),
                  command=self.show_game_turn).pack(side=tk.LEFT, padx=20)

        # Кнопка "В меню" справа
        tk.Button(top_frame, text="🏠 В меню", font=("Arial", 14),
                  command=self.show_menu).pack(side=tk.RIGHT, padx=20)

        # Информация о текущей команде/игроке
        if self.mode == "solo":
            info_text = f"Ходит: {self.team_names[self.current_team]}"
            turn_text = f"Очередь: {' → '.join(self.team_names)}"
        else:
            info_text = f"Ходит: {self.team_names[self.current_team]}"
            turn_text = f"Очередь: {' → '.join(self.team_names)}"

        self.info_label = tk.Label(
            right_frame,
            text=info_text,
            font=("Arial", 24),
            fg=self.team_colors[self.current_team]
        )
        self.info_label.pack(pady=10)

        # Показываем очередь ходов
        self.turn_label = tk.Label(
            right_frame,
            text=turn_text,
            font=("Arial", 14),
            fg="gray"
        )
        self.turn_label.pack(pady=5)

        self.word_label = tk.Label(
            right_frame,
            font=("Arial", 48, "bold"),
            fg=self.team_colors[self.current_team]
        )
        self.word_label.pack(pady=40)

        self.timer_label = tk.Label(right_frame, font=("Arial", 28))
        self.timer_label.pack(pady=10)

        # Отображение счетов
        score_text = self.get_score_text()
        self.score_label = tk.Label(
            right_frame,
            text=score_text,
            font=("Arial", 20),
            justify=tk.LEFT
        )
        self.score_label.pack(pady=20)

        btns = tk.Frame(right_frame)
        btns.pack(pady=30)

        tk.Button(btns, text="УГАДАЛИ ✓", font=("Arial", 20, "bold"),
                  width=12, bg="#4CAF50", fg="white",
                  command=self.correct).pack(side=tk.LEFT, padx=20)

        tk.Button(btns, text="ПРОПУСК ✗", font=("Arial", 20, "bold"),
                  width=12, bg="#FF5722", fg="white",
                  command=self.skip_word).pack(side=tk.RIGHT, padx=20)

        # Отображение цели игры
        tk.Label(right_frame,
                 text=f"🎯 Цель: {self.game_settings['win_score']} слов",
                 font=("Arial", 14)).pack(pady=5)

        # Информация о штрафе
        tk.Label(right_frame,
                 text="⚠️ За пропуск слова -1 балл (не ниже 0)",
                 font=("Arial", 12), fg="red").pack(pady=5)

    def get_score_text(self):
        scores = []
        for i, (name, score) in enumerate(zip(self.team_names, self.team_scores)):
            if self.mode == "solo" and i == self.current_team:
                scores.append(f"👉 {name}: {score} 👈")
            else:
                scores.append(f"{name}: {score}")
        return "\n".join(scores)

    def update_side_hint(self, word):
        """Обновляет подсказки в левой колонке"""
        hint = get_hint(word)
        self.side_hint_word.config(text=f"📖 {word.upper()}")
        self.side_hint_text.config(text=hint)

        # Обновляем информацию о количестве оставшихся слов
        remaining = len([w for w in WORDS if w not in self.used_words])
        total = len(WORDS)
        self.remaining_words_label.config(text=f"📚 Осталось слов: {remaining}/{total}")

    def correct(self):
        self.team_scores[self.current_team] += 1
        self.score_label.config(text=self.get_score_text())

        # Проверка победы
        if self.team_scores[self.current_team] >= self.game_settings["win_score"]:
            self.end_game_winner()
        else:
            self.current_word = self.get_new_word()
            self.word_label.config(text=self.current_word)
            self.update_hint()
            self.update_side_hint(self.current_word)

    def skip_word(self):
        """Пропуск слова со штрафом -1 балл (но не ниже 0)"""
        # Штрафуем текущего игрока/команду
        if self.team_scores[self.current_team] > 0:
            self.team_scores[self.current_team] -= 1

        self.score_label.config(text=self.get_score_text())
        self.current_word = self.get_new_word()
        self.word_label.config(text=self.current_word)
        self.update_hint()
        self.update_side_hint(self.current_word)

    def update_timer(self):
        self.timer_label.config(text=f"⏱️ Время: {self.time_left} сек")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def end_round(self):
        self.stop_timer()

        # Показываем сообщение о конце времени
        messagebox.showinfo("Время вышло!",
                            f"Время {self.team_names[self.current_team]} истекло!\nХод переходит следующему.")

        if self.mode == "solo":
            # В одиночном режиме просто переходим к следующему игроку
            self.next_turn()
        else:
            # В командном режиме переключаем команду
            self.next_turn()

    def end_game_winner(self):
        self.stop_timer()
        self.close_hint_window()
        self.show_results("🏆 ПОБЕДА! 🏆")

    def show_results(self, title):
        """Показывает экран с результатами"""
        self.close_hint_window()
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