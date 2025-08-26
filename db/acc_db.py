from db.constants import con,csr

def add_account(user,pwd,roles,name):
    qry=f'insert into users values("{user}","{pwd}","{roles}","{name}",null);'
    # roles acceptable: doctor, nurse, admin, pharma, emergency, reception
    csr.execute(qry)
    con.commit()
    return

def get_user(user):
    qry=f'select * from users where username="{user}";'
    # roles acceptable: doctor, nurse, admin, pharma, emergency, reception
    csr.execute(qry)
    data=csr.fetchall()
    if data == [] : return False
    return data[0]

def modify_user(username, pwd, name):
    qry =f"update users set pwd='{pwd}', name='{name}' where username='{username}';"
    csr.execute(qry)
    con.commit()
    return

def modify_user_roles(user,roles):
    qry =f"update users set access='{roles}' where username='{user}';"
    csr.execute(qry)
    con.commit()
    return

def delete_account(user):
    qry=f'delete from users where username="{user}";'
    csr.execute(qry)
    con.commit()
    return

def link_account(user,dcid):
    qry=f'update users set linked={dcid} where username="{user}";'
    csr.execute(qry)
    con.commit()
    return user
