# AirBnB - The Console

This project is a console-based implementation of a simple AirBnB clone. 
While not designed for user-friendliness, it provides a hint of the functionalities available.
class name = [BaseModel, User, City, Place, Review, State, Amenity]

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Credits](#credits)

## Installation

To run the project, clone the repository into a Python environment. As of now, it is not available in an executable format, only as the source code. It can be executed on any terminal with Python installed.

## Usage

To execute the code, run `./console.py` in your shell or cmd. In an IDE like VSCode, you can run it directly from the `console.py` file. The following commands are available:

- `(hbnb)`: The prompt that appears on the console.
- `quit`: Exits the prompt.
- `help`: Provides information on available commands.
- `create <class_name>`: Creates an instance of a class (e.g., `create BaseModel`, `create User`).
- `all` or `all <class_name>`: Displays all objects stored in `file.json` (e.g., `all`, `all BaseModel`).
- `destroy <class_name> <id>`: Deletes an object (e.g., `destroy BaseModel 1234-1234-1234`).
- `update <class_name> <id>`: Updates an object (e.g., `update BaseModel 1234-1234-1234`).
- `show <class_name> <id>`: Displays a specific object (e.g., `show BaseModel 1234-1234-1234`).
- `<class_name>.all()`: Views objects of a particular class.
- `<class_name>.count()`: Counts the number of instances of a class.
- `<class_name>.show("<id>")`: Displays a specific object of a class.
- `<class_name>.destroy("<id>")`: Deletes a specific object of a class.
- `<class_name>.update("<id>", attribute_name, attribute_value)`: Updates a specific object of a class.
- `<class_name>.update("<id>", {dictionary_representation})`: Updates a specific object of a class using dictionary representation.

## Contributors

- Asogwa Kingsantus
- Sean Gambanou

## License

ALX AFRICA HOLBERTON SCHOOL

## Credits

- Alx Instruction
- Alx Cohort 15 Mentor
- Ehoneah Obed
- Bright
- ALX Cohort 15
