from db import acc_db, doctors_db
from tabulate import tabulate


def menu(username):
    print("\nLogged into ADMIN Client.")
    while True:
        print(
            "\nMain Menu \n1. User management \n2. Staff Management \n3. Department Management \n4. Exit"
        )
        try:
            user = int(input("Select an option by entering its number\n--> "))
        except:
            print("Wrong Option...")
        else:
            if user == 1:
                user_mngt()
            elif user == 2:
                staff_mngt()
            elif user == 3:
                dept_mgnt()
            elif user == 4:
                exit()
            else:
                print("Wrong Option...")


def dept_mgnt():
    while True:
        print(
            "\nDepartment Management\n1. List all Departments \n2. Add a department \n3. Delete a department \n4. Return to Main Menu"
        )
        try:
            user = int(input("--> "))
        except:
            print("Wrong Option")
        else:
            if user == 1:
                lst = doctors_db.get_all_dept()
                if not lst:
                    print("No Departments have been defined, add a few and try again.")
                    return
                table = tabulate(
                    lst, headers=["ID", "Department Name"]
                )
                print(table)
            elif user == 2:
                dname = input("Department Name: ")
                print(f"New department created with ID {doctors_db.add_dept(dname)}")
            elif user == 3:
                # show available  departments?
                did = int(input("Enter Department No. "))
                det = doctors_db.get_dept(did)
                if not det:
                    print(f"Patient with ID {did} not found.")
                    return
                if "y" in input(
                    f"Department is {det}. Do you want to delete this record? (y/n)"
                ):
                    doctors_db.delete_dept(did)
                    print(f"Deleted {det}'s records successfully")
            elif user == 4:
                break


def staff_mngt():
    while True:
        print(
            "\nStaff Management\n1. Add a Doctor \n2. Modify Doctor Details \n3. Delete Doctor \n4. Add a nurse \n5. Assign a nurse to a doctor \n6. Delete a Nurse \n7. Return to Main Menu"
        )
        try:
            user = int(input("--> "))
        except:
            print("Wrong Option")
        else:
            if user == 1:
                depts = doctors_db.get_all_dept()
                if not depts:
                    print(
                        "No Departments are defined, please add a department and try again."
                    )
                else:
                    name = input("Doctor's Name: ")
                    print("\n Available Departments: ")
                    print(tabulate(depts,headers=['ID','Department']))
                    dept = int(
                        input(
                            "Please Enter the ID of the Department of the doctor: "
                        )
                    )
                    spe = input("Doctor's Specialty? (Default: Consultant): ")
                    if spe:
                        did = doctors_db.add_doctor(name,dept,spe)
                        print(
                            f"Added Doctor {name} Successfully. His ID is {did}"
                        )
                    else:
                        did = doctors_db.add_doctor(name,dept)
                        print(
                            f"Added Doctor {name} Successfully. His ID is {did}"
                        )
                    usr=input('Make Dedicated account for doctor? (Y/n): ')
                    if usr in 'yY':
                        username = input('Username of Doctor: ')
                        password = input("Password of the Account: ")
                        acc_db.add_account(username,password,'doctor',name)
                        acc_db.link_account(username,did)
                        print(f"Added a Doctor Account {username} for {name}")
            elif user == 2:
                usr = int(input("Doctor ID: "))
                data = doctors_db.get_doc(usr)
                if data:
                    print(f"Currently {data[1]} is currently in {doctors_db.get_dept(data[2])} with specialty {data[3]}")
                    lst = doctors_db.get_all_dept()
                    if not lst:
                        print("No Departments have been defined, add a few and try again.")
                        return
                    print(tabulate(
                        lst, headers=["ID", "Department Name"]
                    ))
                    dep = int(input("Enter Department ID (press enter to skip): "))
                    if doctors_db.get_dept(dep):
                        if not dep: dep = data[2]
                        spe = input("Enter Specialty (press enter to skip): ")
                        if not spe: spe = data[3]
                        doctors_db.modify_doctor(usr,dep,spe)
                        print(f"Successfully Modifed details for Doctor {data[1]}")
                    else:
                        print("Invalid Department ID")
                else:
                    print('Invalid Doctor ID')
            elif user == 3:
                del_doc()
            elif user == 4:
                print('\nA new account will be created for the nurse.')
                user = input("Nurse's Name: ")
                username = input(f"Username for {user}'s account: ")
                password = input("Account Password: ")
                acc_db.add_account(username,password,'nurse',user)
                nsid = doctors_db.add_nurse(user,username)
                print(f"Nurse added with ID {nsid}. \nUsername is {username}.")
                usr = input("Assign Nurse to a doctor? (Y/n): ")
                if usr in 'Yy':
                    dcid = int(input("Doctor ID: "))
                    dct = doctors_db.get_doc(dcid)
                    if dct:
                        dept = dct[2]
                        acc_db.link_account(username,dcid)
                        doctors_db.link_nurse(nsid,dept,dcid)
                        print(f"Assigned {user} to {dct[1]} in department {doctors_db.get_dept(dept)}")
                    else: 
                        print('Invalid Doctor ID')
            elif user == 5:
                nsr = int(input("Nurse ID: "))
                data = doctors_db.get_nurse(nsr)
                if data:
                    if data[2] != None:
                        print(f"Nurse {data[1]} is currently assigned to {doctors_db.get_doc(data[2])[1]}")
                    else:
                        print(f"Nurse {data[1]} is currently assigned to nobody")
                    dcid = int(input("Doctor ID: "))
                    dct = doctors_db.get_doc(dcid)
                    if dct:
                        dept = dct[2]
                        username = data[4]
                        acc_db.link_account(username,dcid)
                        doctors_db.link_nurse(nsr,dept,dcid)
                        print(f"Assigned {user} to {dct[1]} in department {doctors_db.get_dept(dept)}")
                    else: 
                        print('Invalid Doctor ID')
                else:
                    print("Nurse not found with given ID")
            elif user == 6:
                del_nurse()
            elif user == 7:
                break


def del_doc():
    # TODO : delete account as well if linked
    from db import patient_db

    dtid = int(input("Enter Doctor ID: "))
    det = doctors_db.get_doc(dtid)
    if not det:
        print(f"Doctor with ID {dtid} not found.")
        return
    if "y" in input(
        f"Doctor's name is {det[1]}. Do you want to delete this record? (y/n)"
    ):
        doctors_db.delete_doctor(dtid)
    print(f"Deleted {det[1]}'s records successfully")

def del_nurse():
    from db import doctors_db, acc_db
    dtid = int(input("Enter Nurse ID: "))
    det = doctors_db.get_nurse(dtid)
    if not det:
        print(f"Nurse with ID {dtid} not found.")
        return
    if "y" in input(
        f"Nurse's name is {det[1]}. Do you want to delete this record? (y/n)"
    ):
        acc_db.delete_account(det[4])
        doctors_db.del_nurse(dtid)

    print(f"Deleted {det[1]}'s records successfully")


def user_mngt():
    while True:
        print(
            "\nUser Management\n1. Add a User \n2. Update User Information \n3. Delete a User \n4. Update User roles \n5. Return to Main Menu"
        )
        try:
            user = int(input("--> "))
        except:
            print("Wrong Option")
        else:
            if user == 1:
                name = input("User's Name: ")
                username = input("Enter Account's Username: ")
                password = input("Enter Password: ")
                add_user(username, password, name)
                print(f"Made a account for {name} with username {username}")
            elif user == 2:
                user = input("Username : ")
                data = acc_db.get_user(user)
                if data:
                    pwd = input("New Password: ")
                    if not pwd: pwd = data[1]
                    name = input(f"User's Name is {data[3]}. Enter New Name (press enter to skip): ")
                    if not name: name = data[3]
                    acc_db.modify_user(user,pwd,name)
                    print("Updated User details successfully")
                else:
                    print("Given Username doesn't exist")
            elif user == 3:
                acc_db.delete_account(input("Enter Username of the account to delete: "))
                print("Successfully Deleted Account.")
            elif user == 4:
                username = input("Enter Username: ")
                user_mod(username)
            elif user == 5:
                break


def add_user(username, password, name):
    print("Select which clients user should have access to:")
    lst = ["admin", "pharma", "doctor", "nurse", "emergency", "reception"]
    st = ""

    while True:
        for x in range(len(lst)):
            print(f"{x} :- {lst[x]} client.")
        print("\nSelect the number of the client you want to add, if you want to cancel, type 88:")
        print(f"User currently has access to: {st}")
        try:
            using = int(input("--> "))
            if using ==88:
                print("Confirming Accounts...")
            else:
                if not lst[using].isspace():
                    if st == "":
                        st = lst[using]
                    else:
                        st = st + "," + lst[using]
                    lst[using] = "    "
                else:
                    print("That option is unavailable")
        except:
            print("Wrong selection, please try again")
        if input("Done? Y/n: ") in "yY":
            acc_db.add_account(username,password,st,name)
            break

def user_mod(user):
    lst = ["admin", "pharma", "doctor", "nurse", "emergency", "reception"]
    data = acc_db.get_user(user)
    if not data:
        print("Given Username does not exist")
        return
    print("User currently has access to: ")
    for x in data[2].split(','): print(x)
    print("\nDefine New Roles: \n\n")
    st = ""
    while True:
        for x in range(len(lst)):
            print(f"{x} :- {lst[x]} client.")
        print("\nSelect the number of the client you want to add. To Cancel, type 88: ")
        print(f"User currently has access to: {st}")
        try:
            using = int(input("--> "))
            if using == 8:
                break
            else:
                if not lst[using].isspace():
                    if st == "":
                        st = lst[using]
                    else:
                        st = st + "," + lst[using]
                    lst[using] = "    "
                else:
                    print("That option is unavailable")
        except:
            print("Wrong selection, please try again")
        if input("Done? Y/n: ") in "yY":
            break
    if st: acc_db.modify_user_roles(user, st)
    print("Successfully Modified User Access Roles")
