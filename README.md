# Battleship Game Field Generator

This Python script generates fields for the "Battleship" game. It allows random placement of ships on a game field and supports saving and loading game fields from files.

## Features

- Field Sizes: supports 5x5, 6x6, 7x7, 8x8, 9x9 and 10x10 grids.
- Random Ship Placement: ships are placed automatically by progrsm with no overlaps or adjacent ships.
- Save/Load: save the field to a file and load it back later.
- Field Display: prints the current game field with coordinates.

## Requirements

- Python 3.x

## How to Use

1. Run the Script: launch the program, then choose a field size or load a field from a file.
2. Ship Placement: ships are placed randomly on the selected grid.
3. Save/Load: save the field to a file or load a previously saved field.

## Functions

- create_field(size): creates an empty game field of the given size.
- print_field(field): Ddsplays the game field with row and column coordinates.
- can_place_ship(field, start_row, start_col, end_row, end_col): checks if a ship can be placed on the field at the specified coordinates.
- place_ship(field, start_row, start_col, end_row, end_col): places a ship on the field at the specified coordinates.
- mark_surroundings(field, start_row, start_col, end_row, end_col): marks surrounding cells as unavailable for placing ships.
- setup_ships(field, ships): randomly places ships on the field based on the given configuration.
- save_field_to_file(field): saves the current game field to a file (`game_field.txt`).
- load_field_from_file(filename="game_field.txt"): loads a game field from the specified file.
- valid_input(prompt, min_value, max_value): prompts the user for input until a valid number within the specified range is entered.
- main(): main function that manages the game logic, including field selection, ship placement, saving, and loading.
