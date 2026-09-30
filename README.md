# Academic Record Helper

**Author:** Abir Singh Pawar (26BAI10239)  
**Course:** Introduction To Problem Solving and Programming (CSE1021)  
**Faculty:** G. Prabhu Kannan

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
   git clone https://github.com/abir0003-code/Academic-Record-Helper.git
   cd Academic-Record-Helper
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
Academic-Record-Helper/
    main.py
    operations.py
    analytics.py
    database.py
    test_helper.py
    README.md
    statement.md
    Project_Report.pdf
    docs/            diagrams and screenshots
```

## Screenshots

These were taken on my own computer while running the program.

Start screen:

![Start screen](docs/real_01_start.png)

Adding students:

![Adding students](docs/real_02_add.png)

Viewing all reports:

![View reports](docs/real_03_view.png)

Class average and class topper:

![Class analytics](docs/real_04_analytics.png)

Search, update and delete:

![Search, update and delete](docs/real_05_search_update_delete.png)

Error handling:

![Error handling](docs/real_06_errors.png)

Exiting the program:

<img width="260" height="170" alt="Screenshot 2026-09-30 160116" src="https://github.com/user-attachments/assets/e7b5baa4-59fd-4807-80df-546c211ae5bb" />



## Known Limitations

- Data is not saved. When the program closes, all records are lost.
- Only two subjects are supported.
- Names are case sensitive, so "amit" and "Amit" are treated as different students.
- The update option does not accept negative numbers.

## Future Improvements

Saving data to a file (CSV or JSON), supporting any number of subjects, grades, and sorting the report by marks and moreover I will try to add some more things in it to calculate cgpa and attendance calculator and many more as i get the ideas.
