from db import acc_db,appt_db,doctors_db,patient_db
from tabulate import tabulate

def menu(user):
    dctid = acc_db.get_user(user)[4]
    print(f"Appointments Scheduled to Doctor {doctors_db.get_doc(dctid)[1]}: \n")
    lst = appt_db.filter_appt(dctid)
    if not lst:
        print("No Appointments scheduled right now :)")
    else:
        lst = list(lst)
        for x in range(len(lst)):
            lst[x] = list(lst[x])
        for x in range(len(lst)):
            lst[x][1] = patient_db.get_patient(lst[x][1])[1]
        print(tabulate(lst, headers=["Appointment ID", "Patient Name", "Appointment Date", "Appointment Status"]))
    while True:
        print('\n\n1. Check Appointment Schedule \n2. Accept Appointment \n3. Add Vital Signs \n4. View Medical Archives \n5. Exit')
        user = int(input('---> '))
        if user == 1:
            print(f"Appointments Scheduled to Doctor {doctors_db.get_doc(dctid)[1]}: \n")
            lst = appt_db.filter_appt(dctid)
            if not lst:
                print("No Appointments scheduled right now :)")
            else:
                lst = list(lst)
                for x in range(len(lst)):
                    lst[x] = list(lst[x])
                for x in range(len(lst)):
                    lst[x][1] = patient_db.get_patient(lst[x][1])[1]
                print(tabulate(lst, headers=["Appointment ID", "Patient Name", "Appointment Date", "Appointment Status"]))
        elif user == 2:
            apptid = int(input("Appointment ID: "))
            data = appt_db.get_appt(apptid)
            if data:
                if appt_db.verify_appt(apptid,dctid):
                    print(f"Patient {patient_db.get_patient(data[1])[1]} -- Appointment {apptid}.")
                    if appt_db.check_status(apptid):
                        appt_menu(apptid)
                    else:
                        print("Appointment was already completed.")
                else:
                    print("Appointment not assigned to this doctor")
            else:
                print("Invalid Appointment ID")
        elif user == 3:
            apptid = int(input("Appointment ID: "))
            data = appt_db.get_appt(apptid)
            if data:
                print(f"Patient {patient_db.get_patient(data[1])[1]}. Appointment {apptid}.")
                if appt_db.verify_appt(apptid,dctid):
                    if appt_db.check_status(apptid):
                        if appt_db.check_vitals(apptid):
                            bp = input("Patient's Blood Pressure : ")
                            temp = input("Patient Temperature: ")
                            com = input("Additional Comments: ")
                            main = f"Blood Pressure: {bp} \nTemperature: {temp} \nAdditional Comments: {com}"
                            appt_db.add_vitals(apptid,main)
                            print('Done.')
                        else:
                            print("Vitals have already been taken for this appointment.")
                    else:
                        print("Vitals have already been taken for this appointment.")
                else:
                    print("Appointment not assigned to this doctor")
            else:
                print("Invalid Appointment ID.")
        elif user == 4:
            from clients import archives
            archives.menu(user)
        elif user == 5:
            break
        else:
            print('Wrong Option')

def appt_menu(apptid):
    appt_db.update_aptstatus(apptid,"Completed")
    diag = ""
    meds = ""
    while True:    
        print("1. Check Patient Vital Signs \n2. Add Patient Diagnosis \n3. Assign Medicine \n4. Export Patient Medical Diagnosis \n5. Return to the previous menu.")
        user = input('-->')
        if user == '1':
            data = appt_db.get_appt(apptid)
            print(data[5])
            print()
        elif user == '2':
            diag = input("Medical Diagnosis of the patient: ")
        elif user == '3':
            while True:
                usr = input("Medicine Name: ")
                amt = input("Amount To take: ")
                who = input("When to take: ")
                if meds == "":
                    meds = f"{usr},{amt},{who}"
                else:
                    meds = meds + f"|{usr},{amt},{who}"
                if input("Continue? (y/n): ") not in 'yY':
                    break
            print('Medicines Assigned: ')
            for x in meds.split('|'):
                print(x)
        elif user == '4':
            out = ['National Hospital \n',f'Appointment ID {apptid}\n', f'Patient Name : {patient_db.get_patient(appt_db.get_appt(apptid)[1])[1]}\n', f'Appointment Date: {appt_db.get_appt(apptid)[2]}\n',f'Doctor : {doctors_db.get_doc(appt_db.get_appt(apptid)[3])[1]}\n', f'Department {doctors_db.get_dept(appt_db.get_appt(apptid)[4])}\n', f'\n\nMedical Diagnosis : {diag}\n']
            out.append('\nMedicines Assigned \n')
            out.append('Medicine Name, Amount Give, When to take \n')
            for x in meds.split('|'):
                out.append(f'{x}\n')
            with open(f'APPOINTMENT_{apptid}.txt', 'w') as f:
                f.writelines(out)
            print(f'Successfully Exported Medical Diagnosis as APPOINTMENT_{apptid}.txt')
        elif user == '5':
            if diag!="" and meds!="":
                appt_db.appt_doctor(apptid,diag,meds)
                appt_db.confirm_appt(apptid)
                return
            else:
                if input("Certain Medical Fields are incomplete. Override? (y/n): ") in 'yY':
                    if diag!="":
                        appt_db.appt_doctor(apptid,diag,'NONE')
                    elif meds!="":
                        appt_db.appt_doctor(apptid,'NONE',meds)
                    else:
                        appt_db.appt_doctor(apptid,'NONE','NONE')
                    appt_db.confirm_appt(apptid)
                    return
        else:
            print("Invalid Option.")
