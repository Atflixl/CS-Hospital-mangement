from db.constants import con, csr


def add_patient(name, goid, dob, insurance, allergy):
    ptid = get_ptid() + 1
    qry = f"INSERT INTO patients VALUES({ptid},'{name}','{goid}',{dob},'{insurance}','{allergy}',NULL,NULL,NULL,NULL,NULL,NULL);"
    csr.execute(qry)
    con.commit()
    return ptid


def get_patient(ptid):
    qry = f"SELECT * FROM patients WHERE ptid={ptid};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False
    return data[0]


def delete_patient(ptid):
    qry = f"DELETE FROM patients WHERE ptid={ptid};"
    csr.execute(qry)
    con.commit()
    return


def get_ptid():
    qry = "select max(ptid) from patients;"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0] == None:
        return 0
    return data[0][0]
