import csv

def menu(username):
    while True:
        y = input("1. View archives \n2. Return to previous menu \nEnter your choice: ")
        if y == "1":
            lst = []
            with open("db/archives.csv") as f:
                robj = csv.reader(f)
                for x in robj:
                    lst.append(x)
                for x in range(1, len(lst)):
                    print(f"{x}. {lst[x][0]}")
            sel = int(input("Enter a number from the above selections: "))
            mk = lst[sel]
            with open("db/archives_data.txt") as f:
                chk = f.readlines()
                for x in range(int(mk[1]), int(mk[2])):
                    print(chk[x])
        if y == '2':
            return
        else:
            print("Invalid Choice:")


