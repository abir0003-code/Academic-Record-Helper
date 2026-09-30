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

The program is tested by running it and trying each menu option.

1. Run `python main.py`.
2. Go through the test cases below in order. Each one says what to type and what you should see.
3. The screenshots further down show what the output looks like.

| No. | Test case | What to type | Expected result |
|-----|-----------|--------------|-----------------|
| 1 | Add a student | Option 1, name `Amit`, marks `80` and `90` | Success: Student added! |
| 2 | Add a second student | Option 1, name `Riya`, marks `85` and `95` | Success: Student added! |
| 3 | View all reports | Option 2 | Amit average 85.0, Riya average 90.0 |
| 4 | Class average | Option 3 | 2 students, averages 82.5 and 92.5 |
| 5 | Class topper | Option 4 | Riya, total 180.0, average 90.0 |
| 6 | Search a student | Option 5, name `Amit` | Marks and average 85.0 are shown |
| 7 | Update marks | Option 6, name `Riya`, marks `86` and `92` | Marks updated successfully! |
| 8 | Delete, then search again | Option 7, name `Amit`, then option 5, name `Amit` | Record deleted, then Student not found. |
| 9 | Empty name | Option 1, press Enter | Error: Name cannot be empty. |
| 10 | Marks typed as text | Option 1, name `Abir`, marks `fifty` | Error: Please enter valid numbers for marks. |
| 11 | Duplicate name | Option 1, name `Riya` | Error: Student already registered. |
| 12 | Exit | Option 8 | Thank You!!! Have a nice day. |

Test cases 3 to 5 and 6 to 8 assume the earlier students have been added in the same run, because records are not saved between runs.

## Project Structure

```
Academic-Record-Helper/
    main.py
    operations.py
    analytics.py
    database.py
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

![Exit](docs/real_07_exit.png)

## Known Limitations

- Data is not saved. When the program closes, all records are lost.
- Only two subjects are supported.
- Names are case sensitive, so "amit" and "Amit" are treated as different students.
- The update option does not accept negative numbers.

## Future Improvements

Saving data to a file (CSV or JSON), supporting any number of subjects, grades, and sorting the report by marks.
