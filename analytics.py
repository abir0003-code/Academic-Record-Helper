from database import db


def cls_avg():
    # get class averages
    if not db:
        print("No data available.")
    else:
        ts1=0
        ts2=0
        cnt=0

        for k, v in db.items():
            ts1=ts1+v[0]
            ts2=ts2+v[1]
            cnt=cnt+1
        av1=ts1/cnt
        av2=ts2/cnt

        print("\n--- CLASS ANALYTICS ---")
        print("Total Students Registered:", cnt)
        print("Class Average for Subject 1:", av1)
        print("Class Average for Subject 2:", av2)


def topper():
    # find the topper
    if not db:
        print("No data available.")
    else:
        top=""
        max_tot=-1

        for k, v in db.items():
            tot=v[0]+v[1]
            if tot>max_tot:
                max_tot=tot
                top=k

        top_avg=max_tot/2
        print("\n--- CLASS TOPPER ---")
        print("Top Student:",top,"| Total Marks:",max_tot,"| Average:",top_avg)
