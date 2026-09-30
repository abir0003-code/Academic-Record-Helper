# Academic Record Helper

**Author:** Abir Singh Pawar (26BAI10239)  
**Course:** Introduction To Problem Solving and Programming (CSE1021)  
**Faculty:** G. Prabhu Kannan

A small useful program in Python that keeps track of student marks for a class. You can add students, look them up, change their marks, delete them, and see simple class statistics like the average and the topper.

## Overview

I built this so a teacher (or a student helping a teacher) can manage marks without a spreadsheet. The program runs in the terminal and shows a menu with eight options. All records are stored in a Python dictionary while the program is running. But when it ends and someone exits it, the memory is lost.

The code is split into four files, 3 dictionaries (database, operations, analytics) and 1 Main File:

| File | What it does |
|------|--------------|
| `main.py` | Shows the menu and calls the right function |
| `operations.py` | Add, view, search, update and delete students |
| `analytics.py` | Class average and class topper |
| `database.py` | Holds the `db` dictionary used by everything else |

## Features

- Add a student with marks for two subjects
- View a report of all students with their personal averages
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
3. The screenshots further down show what the output looks like when i had run the code.

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

These were taken on my own laptop while running the program.

Start screen:

<img width="512" height="161" alt="Screenshot 2026-09-30 155603" src="https://github.com/user-attachments/assets/43795f31-1127-46b1-86c3-d866960a5e14" />


Adding students:

<img width="464" height="389" alt="Screenshot 2026-09-30 155700" src="https://github.com/user-attachments/assets/1688745c-cf5a-4521-8a20-077905d4ba27" />


Viewing all reports:

<img width="314" height="271" alt="Screenshot 2026-09-30 155733" src="https://github.com/user-attachments/assets/81ec5242-13d4-42db-b5e4-b84726a10b18" />


Class average and class topper:

<img width="323" height="267" alt="Screenshot 2026-09-30 155758" src="https://github.com/user-attachments/assets/76e1a394-9658-4bb2-9c8a-c90588b5c531" />


Search, update and delete:

<img width="335" height="650" alt="Screenshot 2026-09-30 155926" src="https://github.com/user-attachments/assets/776afdd8-4654-4538-b0ac-458b7c26fa64" />


Error handling:

<img width="280" height="477" alt="Screenshot 2026-09-30 160100" src="https://github.com/user-attachments/assets/7226c5fa-2d9f-44e6-9935-f10e95228267" />


Exiting the program:

<img width="260" height="170" alt="Screenshot 2026-09-30 160116" src="https://github.com/user-attachments/assets/a3748a04-170a-4e9f-9d8e-e1bffd2f6e81" />


## Known Limitations

- Data is not saved so when the program closes, all records are lost.
- Only two subjects are supported for now, I will increase the number of subjects later on.
- Names are case sensitive, so "amit" and "Amit" are treated as different students, so that might create a problem.
- The update option does not accept negative numbers.

## Future Improvements

Saving data to a file (CSV or JSON), supporting any number of subjects, grades, and sorting the report by marks. Furthermore, I will also try to add a cgpa and attendance calculator along with some other things also in the future.
