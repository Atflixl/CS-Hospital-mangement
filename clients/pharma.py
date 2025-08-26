import csv
from tabulate import tabulate


def menu(pharma):

    while True:
        file = open("db\pharma_inventory.csv", "r+", newline="")
        y = input(
            "1. View inventory: \n2. Manage inventory \n3. Dispatch \n4. Add a new medicine \n5. Exit \nEnter your choice: ",
        )
        if y == "1":
            print("---------------------------")
            lst = []
            robj = csv.reader(file)
            next(robj)
            for p in robj:
                lst.append(p)
            print(tabulate(lst, headers=["Medicine Name", "Type", "Quantity"]))
            print()

        elif y == "2":
            with open("db\pharma_inventory.csv", "r+", newline="") as f:
                robj = csv.reader(f)
                wobj = csv.writer(f)
                lst = []
                for x in robj:
                    lst.append(x)
                for x in lst:
                    medicine_name = input("Enter the Name: ").lower()
                    if x[0].lower() == medicine_name:
                        print("For medicine", medicine_name, "quantity:", x[2])
                        new_quantity = int(input("Enter the Updated quantity: "))
                        x[2] = new_quantity
                        print(
                            "Quantity has been updated for :",
                            medicine_name,
                            "to amount",
                            new_quantity,
                        )
                    else:
                        print(medicine_name, "Not Found...Enter a valid medicine!")
            menu(pharma)

        elif y == "3":
            med = input("Medicine name: ").lower()
            with open("db\pharma_inventory.csv", "r+", newline="") as f:
                robj = csv.reader(f)
                wobj = csv.writer(f)
                lst = []
                for x in robj:
                    lst.append(x)
                for x in lst:
                    if x[0].lower() == med:
                        dis = int(input("How much to dispatch? : "))
                        x[2] -= dis
                wobj.writerows(lst)

        elif y == "4":
            med = input("Medicine name: ")
            medtype = input("Medicine type: ")
            medamt = int(input("Medicine Amount: "))
            with open("db\pharma_inventory.csv", "r", newline="") as f:
                robj = csv.reader(f)
                lst = []
                for x in robj:
                    lst.append(x)
            with open("db\pharma_inventory.csv", "w+", newline="") as f:
                wobj = csv.writer(f)
                lst.append([med, medtype, medamt])
                wobj.writerows(lst)

        elif y == "5":
            break

        else:
            menu(pharma)
