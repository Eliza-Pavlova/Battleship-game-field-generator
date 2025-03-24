# Battleship Game Setup

This Python script generates and manages a simple version of the "Battleship" game. It allows random placement of ships on a game field, and supports saving and loading game states from files.

## Features

- Field Sizes: Supports 5x5, 6x6, 7x7, 8x8, 9x9, and 10x10 grids.
- Random Ship Placement: Ships are placed automatically, with no overlaps or adjacent ships.
- Save/Load: Save the field to a file and load it back later.
- Field Display: Prints the current game field with coordinates.

## Requirements

- Python 3.x

## How to Use

1. Run the Script: Launch the program, then choose a field size or load a field from a file.
2. Ship Placement: Ships are placed randomly on the selected grid.
3. Save/Load: Save the field to a file or load a previously saved field.

## Functions

- create_field(size): Creates an empty game field of the given size.
- print_field(field): Displays the game field with row and column coordinates.
- can_place_ship(field, start_row, start_col, end_row, end_col): Checks if a ship can be placed on the field at the specified coordinates.
- place_ship(field, start_row, start_col, end_row, end_col): Places a ship on the field at the specified coordinates.
- mark_surroundings(field, start_row, start_col, end_row, end_col): Marks surrounding cells as unavailable for placing ships.
- setup_ships(field, ships): Randomly places ships on the field based on the given configuration.
- save_field_to_file(field): Saves the current game field to a file (`game_field.txt`).
- load_field_from_file(filename="game_field.txt"): Loads a game field from the specified file.
- valid_input(prompt, min_value, max_value): Prompts the user for input until a valid number within the specified range is entered.
- main(): Main function that manages the game logic, including field selection, ship placement, saving, and loading.

## Example Output

Доступные размеры поля:
1. 5 x 5
2. 6 x 6
3. 7 x 7
4. 8 x 8
5. 9 x 9
6. 10 x 10
7. Загрузить поле из файла.

Выберите номер размера поля или загрузить поле (введите номер): 1

Результат расстановки кораблей:
   А Б В Г Д
1  ~ ~ ~ ~ ~
2  ~ ■ ■ ~ ~
3  ~ ~ ~ ~ ~
4  ■ ~ ~ ~ ~
5  ~ ~ ~ ~ ■

Хотите сохранить поле в файл? (да/нет): да
Поле сохранено в файл game_field.txt.
