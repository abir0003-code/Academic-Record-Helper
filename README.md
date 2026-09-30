# Academic Record Helper

A small console program in Python that keeps track of student marks for a class. You can add students, look them up, change their marks, delete them, and see simple class statistics like the average and the topper.

## Overview

I built this so a teacher (or a student helping a teacher) can manage marks without a spreadsheet. The program runs in the terminal and shows a menu with eight options. All records are stored in a Python dictionary while the program is running.

The code is split into four files so each file has one job:

| File | What it does |
|------|--------------|
| `main.py` | Shows the menu and calls the right function |
| `operations.py` | Add, view, search, update and delete students |
| `analytics.py` | Class average and class topper |
| `database.py` | Holds the `db` dictionary used by everything else |

There is also `test_helper.py` with unit tests.

## Features

- Add a student with marks for two subjects
- View a report of all students with their average
- Class average for each subject
- Find the class topper
- Search for a student by name
- Update marks
- Delete a student
- Input checks for empty names, duplicate names and wrong mark formats

## Technologies Used

- Python 3 (no external libraries needed)
- `unittest` and `unittest.mock` for testing
- Git and GitHub for version control

## How to Install and Run

1. Install Python 3.8 or newer.
2. Clone the repository:
   ```
   git clone <your-repository-link>
   cd academic_record_helper
   ```
3. Run the program:
   ```
   python main.py
   ```
4. Type a number from 1 to 8 and press Enter. Choose 8 to exit.

## How to Test

From the project folder run:

```
python -m unittest test_helper -v
```

There are 12 tests. They cover adding students (valid, empty name, duplicate, bad marks), searching, updating, deleting, the class average, the topper, and what happens when the database is empty. The tests replace `input()` with fake answers so nothing has to be typed.

## Project Structure

```
academic_record_helper/
    main.py
    operations.py
    analytics.py
    database.py
    test_helper.py
    README.md
    statement.md
    docs/            diagrams and screenshots
```

## Screenshots

Adding students and viewing reports:

![Add and view](docs/shot_add_view.png)

Class average and topper:

![Analytics](docs/shot_analytics.png)

Error handling:

![Errors](docs/shot_errors.png)

## Known Limitations

- Data is not saved. When the program closes, all records are lost.
- Only two subjects are supported.
- Names are case sensitive, so "amit" and "Amit" are treated as different students.
- The update option does not accept negative numbers.

## Future Improvements

Saving data to a file (CSV or JSON), supporting any number of subjects, grades, and sorting the report by marks.
