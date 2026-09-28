# Student Management

Work in progress: a command-line application for managing students and classes. Data is stored in JSON files.

## Usage

From this directory, run:

```bash
python index.py
```

At the main menu, enter `OS` to manage students, `OC` to manage classes, or `salir` to exit. Follow the options shown in each menu. The program's prompts are currently in Spanish.

## Project Structure

- `index.py`: starts the application and displays the menus.
- `students.py`: adds, deletes, edits, searches, and lists students.
- `classes.py`: adds and deletes classes, renames and displays them, and adds student enrollments.
- `datos/datos.json`: stores students and their IDs, names, and ages.
- `datos/classes.json`: stores classes and their enrollments. Each enrollment maps an enrollment ID to a student ID.

Changes made in the application are saved to the corresponding JSON files.