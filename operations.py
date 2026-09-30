from database import db


def add_st():
    # add student to dict
    nm=input("Enter student name: ").strip()
    if nm=="":
        print("Error: Name cannot be empty.")
        return
    if nm in db:
        print("Error: Student already registered.")
        return
    try:
        m1=float(input("Enter marks for Subject 1: "))
        m2=float(input("Enter marks for Subject 2: "))
        db[nm]=[m1, m2]
        print("Success: Student added!")
    except ValueError:
        print("Error: Please enter valid numbers for marks.")


def view_all():
    # view all records
    if not db:
        print("No records found.")
    else:
        print("\n--- STUDENT REPORTS ---")
        for k, v in db.items():
            tot=v[0]+v[1]
            avg=tot/2
            print("Student:",k,"| Marks:",v,"| Average:",avg)


def search_st():
    # search record
    key=input("Enter name to search: ").strip()
    if key in db:
        marks=db[key]
        avg=(marks[0]+marks[1])/2
        print("Found -> Name:",key,"| Marks:",marks,"| Average:",avg)
    else:
        print("Student not found.")


def upd_marks():
    # update marks
    key=input("Enter name to update: ").strip()
    if key in db:
        inp1=input("Enter new Subject 1 marks: ").strip()
        inp2=input("Enter new Subject 2 marks: ").strip()
        if inp1.replace(".","",1).isdigit() and inp2.replace(".","",1).isdigit():
            db[key]=[float(inp1), float(inp2)]
            print("Marks updated successfully!")
        else:
            print("Invalid mark format.")
    else:
        print("Student not found.")


def del_st():
    # delete student
    key=input("Enter the name to delete: ").strip()
    if key in db:
        db.pop(key)
        print("Record deleted successfully.")
    else:
        print("Student not found in the database.")
