"""
Цей модуль містить функції для рекурсивного копіювання файлів з вихідної директорії
до нової директорії, сортуючи їх у піддиректорії за розширеннями файлів.

Використання:
python file_sorter.py <вихідна_директорія> [цільова_директорія]

Якщо цільова директорія не вказана, використовується 'dist' у поточній директорії.
"""


import shutil
from pathlib import Path
import sys


def parse_folder(path: Path) -> dict:
    """
    Рекурсивно обходить директорію та повертає словник файлів з їх розширеннями.

    Args:
        path (Path): Шлях до директорії для парсингу.

    Returns:
        dict: Словник, де ключі - абсолютні шляхи до файлів, значення - розширення файлів.
    """
    file_dict = {}
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            file_dict.update(parse_folder(element))
        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")
            file_dict[element.absolute()] = element.suffix.lstrip('.')
    return file_dict

def copy_files_to_folder(files: dict, dist_dir: Path) -> None:
    """
    Копіює файли в відповідні піддиректорії, базуючись на їх розширеннях.

    Args:
        files (dict): Словник файлів для копіювання.
        dist_dir (Path): Шлях до директорії призначення.
    """
    dest_path = Path(dist_dir)
    dest_path.mkdir(parents=True, exist_ok=True)

    for file, folder in files.items():
        subfolder_path = dest_path / folder
        subfolder_path.mkdir(exist_ok=True)
        try:
            shutil.copy2(file, subfolder_path)
            print(f"Скопійовано: {file.name} до {subfolder_path}")
        except shutil.SameFileError:
            print(f"Пропущено: {file.name} (файл вже існує в папці призначення)")
        except PermissionError:
            print(f"Помилка: Немає прав для копіювання {file.name}")
        except Exception as e:
            print(f"Помилка при копіюванні {file.name}: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <вихідна_директорія> [цільова_директорія]")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    if not source_dir.is_dir():
        print(f"Помилка: {source_dir} не є директорією або не існує.")
        sys.exit(1)

    if len(sys.argv) > 2:
        dest_dir = Path(sys.argv[2])
    else:
        dest_dir = Path("dist")

    copy_files_to_folder(parse_folder(source_dir), dest_dir)

if __name__ == "__main__":
    main()