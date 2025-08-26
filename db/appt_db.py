from db.constants import con, csr
from db import doctors_db

def filter_appt(dctid):
    qry = f"select id,ptid,appt_date,appt_status from apptdb where doctor={dctid} and appt_status='scheduled';"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False    
    return data

def filter_appt_all(dctid):
    qry = f"select id,ptid,appt_date,appt_status from apptdb where doctor={dctid};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False    
    return data

def add_vitals(apptid, vitals):
    qry = f"UPDATE apptdb set vital_signs='{vitals}' where id={apptid};"
    csr.execute(qry)
    con.commit()
    return apptid


def add_appt(ptid, doctor, doa):
    # change appt to rec in doctor's side after confirming.
    dept = doctors_db.get_doc_dept(doctor)
    qry = f"UPDATE patients set upc_appt_date={doa}, upc_appt_doctor={doctor}, upc_appt_dept={dept} where ptid={ptid};"
    csr.execute(qry)
    apptid = get_apptid() + 1
    qry = f"INSERT INTO apptdb VALUES({apptid}, {ptid}, {doa}, {doctor}, {dept}, null, 'scheduled',null,null);"
    csr.execute(qry)
    con.commit()
    return apptid

def update_aptdate(apptid,date):
    qry = f"UPDATE apptdb set appt_date={date} where id={apptid};"
    csr.execute(qry)
    con.commit()
    return apptid

def update_aptstatus(apptid, status):
    qry = f"UPDATE apptdb set appt_status='{status}' where id={apptid};"
    csr.execute(qry)
    con.commit()
    return apptid

def check_status(apptid):
    qry = f"select appt_status from apptdb where id={apptid} and appt_status='scheduled';"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if not data:
        return False
    return True

def appt_doctor(apptid, diag, meds):
    qry = f"UPDATE apptdb set diagnosis='{diag}', meds='{meds}' where id={apptid};"
    csr.execute(qry)
    con.commit()
    return apptid

def get_appt(apptid):
    qry = f"select * from apptdb where id={apptid};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False
    return data[0]

def check_vitals(apptid):
    qry = f"select vital_signs from apptdb where id={apptid};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0]!=None:
        return False
    return True

def verify_appt(appt,dctid):
    qry = f"select * from apptdb where id={appt} and doctor={dctid};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False
    return True


def get_apptid():
    qry = "select max(id) from apptdb;"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0] == None:
        return 0
    return data[0][0]

def confirm_appt(apptid):
    data = get_appt(apptid)
    qry = f"update patients set upc_appt_date=null,upc_appt_doctor=null,upc_appt_dept=null,rec_appt_date={data[2]},rec_appt_doctor={data[3]},rec_appt_dept={data[4]} where ptID={data[1]};"
    csr.execute(qry)
    con.commit()
    return