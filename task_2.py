"""Скрипт для малювання сніжинки Коха."""


import turtle


def koch_curve(t: turtle, order: int, size: float) -> None:
    """
    Рекурсивна функція для малювання кривої Коха.

    Args:
        t (turtle): Об'єкт Turtle для малювання.
        order (int): Рівень рекурсії.
        size (float): Довжина сегмента.

    Returns:
        None
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t: turtle, order: int, size: float) -> None:
    """
    Функція для малювання сніжинки Коха.

    Args:
        t (turtle): Об'єкт Turtle для малювання.
        order (int): Рівень рекурсії.
        size (float): Довжина сторони сніжинки.

    Returns:
        None
    """
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    """
    Основна функція для малювання сніжинки Коха.

    Запитує у користувача рівень рекурсії, налаштовує вікно та об'єкт Turtle,
    і малює сніжинку Коха.

    Returns:
        None
    """
    # Отримуємо рівень рекурсії від користувача
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (ціле число від 0 до 5): "))
            if 0 <= order <= 5:
                break
            else:
                print("Будь ласка, введіть число від 0 до 5.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Налаштування вікна та черепашки
    window = turtle.Screen()
    window.setup(800, 600)
    window.title(f"Сніжинка Коха (Рівень рекурсії: {order})")
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість
    t.penup()
    t.goto(-200, 100)  # Початкова позиція
    t.pendown()

    # Малювання сніжинки
    koch_snowflake(t, order, 400)

    # Приховуємо черепашку після завершення
    t.hideturtle()

    # Утримуємо вікно відкритим
    window.mainloop()

if __name__ == "__main__":
    main()
