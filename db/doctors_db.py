from db.constants import con, csr
from db import acc_db
# TODO : modify doctors table to have account username, so we can properly use nurse/doctors db. else add into login logic. Also increase len of dept name in dept table


def add_doctor(name, deptid, specialty="Consultant"):
    dcid = get_dcid() + 1
    qry = f"INSERT INTO doctors VALUES({dcid},'{name}',{deptid},'{specialty}');"
    csr.execute(qry)
    con.commit()
    return dcid

def modify_doctor(dcid, deptid, specialty):
    qry = f"update doctors set dept={deptid}, specialty='{specialty}' where id={dcid};"
    csr.execute(qry)
    con.commit()
    return

def delete_doctor(dcid):
    qry = f"DELETE FROM doctors WHERE id={dcid};"
    csr.execute(qry)
    con.commit()
    return


def delete_dept(dcid):
    qry = f"DELETE FROM dept WHERE id={dcid};"
    csr.execute(qry)
    con.commit()
    return


def add_dept(name):
    id = get_deptid() + 1
    qry = f"INSERT INTO dept VALUES({id},'{name}');"
    csr.execute(qry)
    con.commit()
    return id


def get_doc(id):
    qry = f"select * from doctors where id={id}"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False
    return data[0]

def get_nurse(id):
    qry = f"select * from nurses where id={id}"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == []:
        return False
    return data[0]


def get_dept(id):
    qry = f"select name from dept where id={id};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == None:
        return False
    return data[0][0]

def del_nurse(nsid):
    qry = f"delete from nurses where id={nsid};"
    csr.execute(qry)
    con.commit()
    return

def add_nurse(name,username,dept=None, assign=None):
    nsid = get_nsid() + 1
    if dept:
        qry = f'insert into nurses(id, name, dept, username) values({nsid},"{name}",{dept},"{username}");'
    elif dept and assign:
        qry = f'insert into nurses values({nsid},"{name}",{dept},{assign},"{username}");'
    else:
        qry = f'insert into nurses(id, name,username) values({nsid},"{name}", "{username}");'
    csr.execute(qry)
    con.commit()
    return nsid

def link_nurse(nsid, dept, assign):
    qry = f'update nurses set assigned_to={assign}, dept={dept} where id={nsid}'
    csr.execute(qry)
    con.commit()
    return

def get_all_dept():
    qry = f"select * from dept;"
    csr.execute(qry)
    data = csr.fetchall()
    if data == []:
        return False
    return data

def get_nsid():
    qry = "select max(id) from nurses;"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0] == None:
        return 0
    return data[0][0]


def get_dcid():
    qry = "select max(id) from doctors;"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0] == None:
        return 0
    return data[0][0]


def get_deptid():
    qry = "select max(id) from dept;"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data[0][0] == None:
        return 0
    return data[0][0]


def get_doc_dept(doct):
    qry = f"select dept from doctors where id={doct};"
    csr.execute(qry)
    data = csr.fetchall()
    con.commit()
    if data == None:
        return False
    return data[0][0]
