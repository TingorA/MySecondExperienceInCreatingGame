import os
import subprocess
import sys


def build_exe():
    print("Начинаю сборку AliasGame.exe...")

    # Проверка наличия pyinstaller
    try:
        import PyInstaller
    except ImportError:
        print("Устанавливаю PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Команда для сборки
    cmd = [
        "pyinstaller",
        "--onefile",  # Один файл
        "--windowed",  # Без консоли
        "--name=AliasGame",  # Имя файла
        "--clean",  # Очистка временных файлов
        "alias_game.py"  # Ваш файл с игрой
    ]

    # Запуск сборки
    subprocess.call(cmd)

    print("\n✅ Готово! Файл AliasGame.exe находится в папке dist")
    print("Вы можете скопировать его куда угодно и запускать!")


if __name__ == "__main__":
    build_exe()