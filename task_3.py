"""Ханойські вежі"""


class Stack:
    """
    Клас, що реалізує структуру даних стек.
    """

    def __init__(self):
        """Ініціалізує порожній стек."""
        self.items = []

    def push(self, item):
        """
        Додає елемент до вершини стеку.

        Args:
            item: Елемент для додавання до стеку.
        """
        self.items.append(item)

    def pop(self):
        """
        Видаляє та повертає елемент з вершини стеку.

        Returns:
            Елемент з вершини стеку або None, якщо стек порожній.
        """
        return self.items.pop() if self.items else None


def hanoi_tower(n, origin, extra, target):
    """
    Рекурсивна функція для вирішення задачі Ханойської вежі.

    Args:
        n (int): Кількість дисків
        origin (str): Початковий стрижень
        extra (str): Допоміжний стрижень
        target (str): Цільовий стрижень
    """
    def move_disk(from_peg, to_peg):
        """
        Переміщує один диск з одного стрижня на інший.

        Args:
            from_peg (str): Стрижень, з якого переміщується диск
            to_peg (str): Стрижень, на який переміщується диск
        """
        disk = towers[from_peg].pop()
        towers[to_peg].push(disk)
        print(f"Перемістити диск з {from_peg} на {to_peg}: {disk}")
        show_state()

    def show_state():
        """Виводить поточний стан всіх стрижнів."""
        state = {peg: stack.items for peg, stack in towers.items()}
        print(f"Проміжний стан: {state}")

    if n == 1:
        # Базовий випадок: переміщення одного диска
        move_disk(origin, target)
    else:
        # Рекурсивний випадок
        # 1. Перемістити n-1 дисків з початкового на допоміжний стрижень
        hanoi_tower(n - 1, origin, target, extra)
        # 2. Перемістити найбільший диск на цільовий стрижень
        move_disk(origin, target)
        # 3. Перемістити n-1 дисків з допоміжного на цільовий стрижень
        hanoi_tower(n - 1, extra, origin, target)


if __name__ == "__main__":
    # Отримання кількості дисків від користувача
    n = int(input("Введіть кількість дисків: "))

    # Ініціалізація трьох стрижнів (A, B, C) як стеків
    towers = {rod: Stack() for rod in 'ABC'}

    # Розміщення дисків на початковому стрижні (A)
    for i in range(n, 0, -1):
        towers['A'].push(i)

    # Виведення початкового стану
    print("Початковий стан:", {rod: stack.items for rod, stack in towers.items()})

    # Запуск алгоритму розв'язання
    hanoi_tower(n, 'A', 'B', 'C')

    # Виведення кінцевого стану
    print("Кінцевий стан:", {rod: stack.items for rod, stack in towers.items()})
