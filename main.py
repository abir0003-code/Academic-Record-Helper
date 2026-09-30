from database import a
from operations import add_st, view_all, search_st, upd_marks, del_st
from analytics import cls_avg, topper

print("\n")
print(a.center(80,"-"))

def run_system():
    running=True
    while running:
        print("\n--- MENU ---")
        print("1.Add Student                   5.Search Student ")
        print("2.View All Student Reports      6.Update Marks")
        print("3.View Class Average            7.Delete Student")
        print("4.Find Class Topper             8.Exit")

        print("\n","\n")
        ch=input("Enter choice (1-8): ").strip()

        if ch=="1":
            add_st()
        if ch=="2":
            view_all()
        if ch=="3":
            cls_avg()
        if ch=="4":
            topper()
        if ch=="5":
            search_st()
        if ch=="6":
            upd_marks()
        if ch=="7":
            del_st()
        if ch=="8":
            # exit app
            print("Thank You!!!\nHave a nice day.")
            running=False

if __name__=="__main__":
    run_system()

# THANK YOU
# Hope you find it useful.
