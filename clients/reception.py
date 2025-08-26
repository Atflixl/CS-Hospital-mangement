from db import appt_db, doctors_db, patient_db


def menu(user):
    print("\nLogged into RECEPTION Client.")
    while True:
        print("\nMain Menu \n1. Patient Management \n2. Appointment Booking \n3. Exit")
        try:
            user = int(input("Select an option by entering its number\n--> "))
        except:
            print("Wrong Option...")
        else:
            if user == 1:
                pt_mgmt()
            elif user == 2:
                appt_mgmt()
            elif user == 3:
                exit()
            else:
                print("Wrong Option...")


def appt_mgmt():
    while True:
        print(
            "\nAppointment Management \n1. Create an appointment \n2. Cancel an appointment \n3. Update Appointment \n4. Check Appointment Status \n5. Return to previous menu"
        )
        try:
            user = int(input("Select an option by entering its number\n--> "))
        except:
            print("Wrong Option...")
        else:
            if user == 1:
                add_appt()
            elif user == 2:
                apptid = int(input("Appointment ID : "))
                res = appt_db.get_appt(apptid)
                if res:
                    if appt_db.check_status(apptid):
                        appt_db.update_aptstatus(apptid,'cancelled')
                        print(f"Successfully Cancelled Appointment ID {apptid}")
                    else:
                        print('Appointment was already Completed')
                else:
                    print("Invalid Appointment ID")
            elif user == 3:
                apptid = int(input("Appointment ID : "))
                res = appt_db.get_appt(apptid)
                if res:
                    if appt_db.check_status(apptid):
                        print(f"Current Appointment Date is : {res[2]}")
                        us = int(input("Enter New Date (YYYYMMDD): "))
                        appt_db.update_aptdate(apptid,us)
                        print(f"Successfully Updated Appointment {res[0]} from {res[2]} to {us}")
                    else:
                        print("Appointment already completed.")
                else:
                    print("Invalid Appointment ID")
            elif user == 4:
                chk_appt()
            elif user == 5:
                break


def chk_appt():
    apptid = int(input("Enter Appointment ID: "))
    data = appt_db.get_appt(apptid)
    if not data:
        print("Appointment with the given ID doesn not exist")
        return
    doc = doctors_db.get_doc(data[3])[1]
    dept = doctors_db.get_dept(data[4])
    print(
        f"\n\nAppointment Status for ID {apptid} \nAppointment is Scheduled for {patient_db.get_patient(data[1])[1]} (Patient ID {data[1]}) on {data[2]}  \nAppointment is Scheduled with {doc} of {dept} department \nAppointment is currently, {data[6]}"
    )


def add_appt():
    ptid = int(input("Enter patient ID: "))
    if not patient_db.get_patient(ptid):
        print("Invalid Patient ID")
        return
    doct = int(input("Enter Doctor's ID: "))
    if not doctors_db.get_doc(doct):
        print("Invalid Doctor ID")
        return
    doa = int(input("Date of appointment (YYYYMMDD): "))
    print(f"Appointment ID is {appt_db.add_appt(ptid,doct,doa)}")


def pt_mgmt():
    while True:
        print(
            "\nPatient Management \n1. Create a new patient file \n2. Delete a patient file \n3. Retrieve a patient file \n4. Return to previous menu."
        )
        try:
            user = int(input("Select an option by entering its number\n--> "))
        except:
            print("Wrong Option...")
        else:
            if user == 1:
                add_pt()
            elif user == 2:
                del_pt()
            elif user == 3:
                get_pt()
            elif user == 4:
                break
            else:
                print("Wrong Option...")


def add_pt():
    name = input("Patient's Full Name: ")
    if len(name) > 30:
        print("Name should not be more than 30 characters.")
        return
    goid = input("Patient's GovernmentID: ")
    if len(goid) > 10:
        print("GovernmentID should not be more than 10 characters.")
        return
    dob = int(input("Patient's Date of Birth (in YYYYMMDD format): "))
    insurance = input("Patient's Insurance Type: ")
    if len(insurance) > 20:
        print("Insurance type should not be more than 20 characters.")
        return
    alleg = input("Known Patient's Allergies: ")
    if len(alleg) > 100:
        print("Allergies should not be more than 100 characters.")
        return
    from db import patient_db

    print(
        f"Done! Patient ID is {patient_db.add_patient(name,goid,dob,insurance,alleg)}"
    )


def del_pt():
    from db import patient_db

    ptid = int(input("Enter Patient ID: "))
    det = patient_db.get_patient(ptid)
    if not det:
        print(f"Patient with ID {ptid} not found.")
        return
    if "y" in input(
        f"Patient's name is {det[1]}. Do you want to delete this record? (y/n)"
    ):
        patient_db.delete_patient(ptid)
    print(f"Deleted {det[1]}'s records successfully")


def get_pt():
    from db import patient_db

    ptid = int(input("Enter Patient ID: "))
    det = patient_db.get_patient(ptid)
    if not det:
        print(f"Patient with ID {ptid} not found.")
        return
    print()
    lst = [
        f"Patient ID is {det[0]}",
        f"Patient Name is {det[1]}",
        f"GovtID of the patient is {det[2]}",
        f"The date of birth is {det[3]}",
        f"Patient's Insurance is {det[4]}",
        f"Known allergies of the patient are {det[5]}",
        f"Patient's Upcoming Appointment is on {det[6]} with {det[7]} in department {det[8]}",
        f"The Patient had a recent Appointment is on {det[8]} with {det[9]} in department {det[10]}",
    ]
    for x in lst:
        print(x)
    if "y" in input("\n\n Export data to text file? (y/n): "):
        mn = []
        for x in lst:
            mn.append(x + "\n")
        with open(f"PATIENTDATA_{ptid}.txt", "w") as f:
            f.writelines(lst)
        print(f"Successfully exported as text file with filename : PATIENTDATA_{ptid}")
