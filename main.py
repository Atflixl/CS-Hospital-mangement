# Main Dashboard Code
# doctor, nurse, admin, pharma, emergency, reception
from db import acc_db

print("Welcome to Hospital Managament System")
print()
client = None
while client == None:
    user = input("Enter username: ") 
    if not acc_db.get_user(user):
        print("Username does not exist. Please try again.")
    else:
        client = acc_db.get_user(user)
else:
    tries = 3
    while tries != 0:
        password = input("Enter password: ")
        if password != client[1]:
            print("Wrong Password, Please try again.")
            tries -= 1
        else:
            print(f"\n Welcome {client[3]}! Logging in...")
            break
    else:
        print("You have exceeded the try limit. Try again after a few minutes.")
        exit()

access = client[2].replace('"', "").split(",")
print("You currently have access to the following clients: ")
for x in range(len(access)):
    print(f"{x} :- {access[x]} client.")
print("Please enter the number of the client you want to login to: ")
while True:
    try:
        user = int(input("--> "))
        access = access[user]
        break
    except:
        print("Wrong Option, please select again.")
if access == "admin":
    from clients import admin

    admin.menu(client[0])
elif access == "pharma":
    from clients import pharma

    pharma.menu(client[0])
elif access == "doctor":
    from clients import general
    try:
        general.menu(client[0])
    except:
        print("This account is not registered as a doctor.")
elif access == "nurse":
    from clients import general
    try:
        general.menu(client[0])
    except:
        print("This account is not linked to a doctor.")
elif access == "emergency":
    from clients import emergency

    emergency.menu(client[0])
elif access == "reception":
    from clients import reception

    reception.menu(client[0])
