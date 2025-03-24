import random
import os

FIELD_SIZES = [(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

SHIPS = {
    (10, 10): {4: 1, 3: 2, 2: 3, 1: 4},
    (9, 9): {4: 1, 3: 2, 2: 2, 1: 4},
    (8, 8): {4: 1, 3: 2, 2: 2, 1: 3},
    (7, 7): {4: 1, 3: 1, 2: 2, 1: 3},
    (6, 6): {4: 0, 3: 2, 2: 2, 1: 2},
    (5, 5): {4: 0, 3: 1, 2: 1, 1: 2},
}

COORDINATES_LETTERS = 'АБВГДЕЖЗИК'

def create_field(size):
    field = []
    for row in range(size[0]):
        field_row = []
        for col in range(size[1]):
            field_row.append('~')
        field.append(field_row)
    return field

def print_field(field):
    print("    ", end="")
    for i in range(len(field[0])):
        print(f"{COORDINATES_LETTERS[i]} ", end="")
    print()

    for i in range(len(field)):
        print(f"{i + 1:2}  ", end="")
        for col in range(len(field[i])):
            print(field[i][col], end=" ")
        print()

def can_place_ship(field, start_row, start_col, end_row, end_col):
    rows = len(field)
    cols = len(field[0])

    if start_row == end_row:
        if start_col > end_col:
            start_col, end_col = end_col, start_col
        for row in range(max(0, start_row - 1), min(rows, start_row + 2)):
            for col in range(max(0, start_col - 1), min(cols, end_col + 2)):
                if field[row][col] not in ['~', 'O']:
                    return False
    elif start_col == end_col:
        if start_row > end_row:
            start_row, end_row = end_row, start_row
        for row in range(max(0, start_row - 1), min(rows, end_row + 2)):
            for col in range(max(0, start_col - 1), min(cols, start_col + 2)):
                if field[row][col] not in ['~', 'O']:
                    return False
    else:
        return False
    return True

def place_ship(field, start_row, start_col, end_row, end_col):
    if start_row == end_row:
        for col in range(start_col, end_col + 1):
            field[start_row][col] = '■'
    elif start_col == end_col:
        for row in range(start_row, end_row + 1):
            field[row][start_col] = '■'

    mark_surroundings(field, start_row, start_col, end_row, end_col)

def mark_surroundings(field, start_row, start_col, end_row, end_col):
    rows = len(field)
    cols = len(field[0])

    if start_row == end_row:
        if start_col > end_col:
            start_col, end_col = end_col, start_col
        for row in range(max(0, start_row - 1), min(rows, start_row + 2)):
            for col in range(max(0, start_col - 1), min(cols, end_col + 2)):
                if field[row][col] == '~':
                    field[row][col] = 'O'
    elif start_col == end_col:
        if start_row > end_row:
            start_row, end_row = end_row, start_row
        for row in range(max(0, start_row - 1), min(rows, end_row + 2)):
            for col in range(max(0, start_col - 1), min(cols, start_col + 2)):
                if field[row][col] == '~':
                    field[row][col] = 'O'

def setup_ships(field, ships):
    for length in ships:
        count = ships[length]
        for _ in range(count):
            placed = False
            attempts = 0
            while not placed and attempts < 500:
                attempts += 1
                orientation = random.choice(['горизонтально', 'вертикально'])
                if orientation == 'горизонтально':
                    start_row = random.randint(0, len(field) - 1)
                    start_col = random.randint(0, len(field[0]) - length)
                    end_row = start_row
                    end_col = start_col + length - 1
                else: # Вертикально
                    start_row = random.randint(0, len(field) - length)
                    start_col = random.randint(0, len(field[0]) - 1)
                    end_row = start_row + length - 1
                    end_col = start_col

                if can_place_ship(field, start_row, start_col, end_row, end_col):
                    place_ship(field, start_row, start_col, end_row, end_col)
                    placed = True

            if not placed:
                raise ValueError(f"Не удалось разместить {length}-палубный корабль.")

def save_field_to_file(field):
    filename = "game_field.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for row in field:
            line = ""
            for cell in row:
                line += cell + " "
            f.write(line.strip() + "\n")
    print(f"Поле сохранено в файл {filename}.")

def load_field_from_file(filename="game_field.txt"):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден!")

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    field = []
    for line in lines:
        field_row = line.strip().split()
        field.append(field_row)

    return field

def valid_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Введите число от {min_value} до {max_value}. Попробуйте снова.")
        except ValueError:
            print("Введите целое число.")

def main():
    while True:
        print("Доступные размеры поля:")
        for i in range(len(FIELD_SIZES)):
            size = FIELD_SIZES[i]
            print(f"{i + 1}. {size[0]} x {size[1]}")
        print(f"{len(FIELD_SIZES) + 1}. Загрузить поле из файла.")

        choice = valid_input("Выберите номер размера поля или загрузить поле (введите номер): ", 1, len(FIELD_SIZES) + 1) - 1

        if choice == len(FIELD_SIZES):
            try:
                field = load_field_from_file()
                print("\nИгровое поле:")
                print_field(field)
                print("Поле загружено.")
                return
            except FileNotFoundError as e:
                print(e)
                print("Попробуйте выбрать другой вариант.")
                continue

        field_size = FIELD_SIZES[choice]
        ships = SHIPS[field_size]
        field = create_field(field_size)

        try:
            setup_ships(field, ships)
            print("\nРезультат расстановки кораблей:")
            print_field(field)

            while True:
                save_choice = input("\nХотите сохранить поле в файл? (да/нет): ").strip().lower()
                if save_choice == "да":
                    save_field_to_file(field)
                    return
                elif save_choice == "нет":
                    print("\nПопробуйте выбрать другой размер поля или попросите бота расставить корабли еще раз.")
                    break
                else:
                    print("Пожалуйста, ответьте \"да\" или \"нет\".")

        except ValueError as e:
            print(e)
            print("Попробуйте выбрать другой размер поля или попросите бота расставить корабли еще раз.")

if __name__ == "__main__":
    main()
