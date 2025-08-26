# DEMO CODE DON'T DIRECTLY ADD

from db import acc_db

print("ADMIN : add a user to db")
user = input("Enter username: ")
password = input("Enter password: ")
name = input("what is the users name? : ")
print("select clients which user should have access to:")
lst = ["admin", "pharma", "doctor", "nurse", "emergency", "reception"]
st = ""

while True:
    for x in range(len(lst)):
        print(f"{x} :- {lst[x]} client.")
    print("\nSelect the number of the client you want to add, when done.:")
    print(f"User currently has access to: {st}")
    using = int(input("--> "))
    try:
        if not lst[using].isspace():
            if st == "":
                st = lst[using]
            else:
                st = st + "," + lst[using]
            lst[using] = "    "
        else:
            print("That option is unavailable")
    except:
        print("wrong selection, please try again")
    if input("Done? Y/n: ") in "yY":
        break
print(acc_db.add_account(user, password, st, name))
print("Added given account.")
