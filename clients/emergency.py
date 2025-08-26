import csv
from tabulate import tabulate


def menu(user):
    while True:
        file = open("db\ER_DISPATCH.csv", "r+", newline="")
        y = input(
            "1. View available beds: \n2. Assign a bed \n3. Add beds\n4. Add Ambulances \n5. View Ambulances \n6. View Medical Archives \n7. Exit \nEnter your choice: ",
        )
        if y == "1":
            print("---------------------------")
            lst = []
            robj = csv.reader(file)
            next(robj)
            for p in robj:
                lst.append(p)
            print(tabulate(lst, headers=["Bed No", "Type", "status"]))
            print()

        elif y == "2":
            with open("db\ER_DISPATCH.csv", "r+", newline="") as f:
                robj = csv.reader(f)
                wobj = csv.writer(f)
                lst = []
                for x in robj:
                    lst.append(x)
                for x in lst:
                    BED_NO = input("Enter the BED NUMBER: ").lower()
                    PATIENT_NO= input("Enter the patient name: ")
                    if int(x[0]) == int(BED_NO):
                        print("For BED", PATIENT_NO, "Has been assigned",)

                        
                    else:
                        print(BED_NO, "Not Found...Enter a valid BED NUMBER!")
            menu('ER')

        elif y == "3":
            med = input("Medicine name: ").lower()
            with open("db\AMBULANCES.csv", "r+", newline="") as f:
                robj = csv.reader(f)
                wobj = csv.writer(f)
                lst = []
                for x in robj:
                    lst.append(x)
                for x in lst:
                    if x[0].lower() == med:
                        dis = int(input("Where to dispatch? : "))
                        x[2] -= dis
                wobj.writerows(lst)

        elif y == "4":
            AMBULANCE_NO = input("Bed no: ")
            AMBULANCE_TYPE = input("Bed type: ")
            STATUS = (input("ENTER THE STATUS: "))
            AREA_ASSIGNED = (input("Enter the area assigned: "))
            with open("db\AMBULANCES.csv", "w+", newline="") as f:
                robj = csv.reader(f)
                wobj = csv.writer(f)
                lst = []
                for x in robj:
                    lst.append(x)
                lst.append([AMBULANCE_NO, AMBULANCE_TYPE, STATUS, AREA_ASSIGNED])
                wobj.writerows(lst)

        elif y == "5":
            print("---------------------------")
            with open("db\AMBULANCES.csv", "w+", newline="") as f:
                lst = []
                robj = csv.reader(f)
                next(robj)
                for p in robj:
                    lst.append(p)
                print(tabulate(lst, headers=["AMBULANCE_NO", "AMBULANCE_TYPE", "STATUS", "AREA_ASSIGNED"]))
                print()
        elif y == '6':
            from clients import archives
            archives.menu(user)
        elif y == "7":
            break
        else:
            print("Invalid Option")


