# database connectivity project


import pymysql as p


def insert_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="insert into user(mobile,email,username,pinno,fname,lname,DOB) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,t)
    print("data inserted......")
    con.commit()
    con.close()
def update_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set u_m=%s,u_e=%s,u_un=%s,u_fn=%s,u_ln=%s,u_D=%s where u_pin=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def display_data():
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="select * from user"
    cur.execute(q)
    data=cur.fetchall()
    username=input("Enter your username:- ")
    pin=int(input("Enter your pin no:- "))
    for i in data:
        if username in i:
            print("mobile no=",i[0])
            print("email=",i[1])
            print("username=",i[2])
            print("pin no=",i[3])
            print("first name=",i[4])
            print("last name=",i[5])
            print("DOB=",i[6])
            print("------------x----------")
    con.commit()
    con.close()
def delete_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="delete from user where username=%s"
    cur.execute(q,t)
    print("Data removed")
    con.commit()
    con.close()
def insert_tr_table(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="insert into railtimetable(tr_id,tr_name,source,destination) values(%s,%s,%s,%s)"
    cur.execute(q,t)
    print("data inserted......")
    con.commit()
    con.close()
def display_tr_data():
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="select * from railtimetable"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        print("tr_id=",i[0])
        print("tr_name=",i[1])
        print("tr_source=",i[2])
        print("tr_destination=",i[3])
        print("------------x----------")
    con.commit()
    con.close()
def update_tr_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update railtimetable set tr_name=%s,source=%s,destination=%s, where tr_id=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def ticket_booking(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="insert into ticket_book(user_name,tr_id,departure,arrival,a_seats,m_seats,amount) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,t)
    print("data inserted......")
    con.commit()
    con.close()
def delete_ticket_booking(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="delete from ticket_book where user_name=%s"
    cur.execute(q,t)
    print("Data removed")
    con.commit()
    con.close()
def display_ticket_booking():
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="select * from ticket_book"
    cur.execute(q)
    data=cur.fetchall()
    u=input("Enter your username:- ")
    pin=int(input("Enter your pin no:- "))
    print("\n")
    for i in data:
        if u not in i:
            print("you aren't book tickets\n")
    for i in data:
        if u in i:
            print("user_name=",i[0])
            print("tr_id=",i[1])
            print("departure=",i[2])
            print("arrival=",i[3])
            print("a_seats=",i[4])
            print("m_seats=",i[5])
            print("amount=",i[6])
            print("------------x----------\n")
    con.commit()
    con.close()
def update_mobile_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set mobile=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def update_email_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set email=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def update_fname_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set fname=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def update_lname_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set lname=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def update_DOB_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set DOB=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()
def update_pinno_data(t):
    con=p.connect(user="root",host="localhost",database="travelbooking")
    cur=con.cursor()
    q="update user set pinno=%s where username=%s"
    cur.execute(q,t)
    print("data updated")
    con.commit()
    con.close()








while True:
    print("************  WELCOME TO FALCON RAILWAY BOOKING  ************")
    print('''
1-To admin access
2-To user registration(sign up)
3-To book a ticket
4-To cancel the booking
5-To view your booking
6-To update user records
7-To delete user account
8-To view your details
9-To quit the application\n''')
    choice=int(input("1-9: "))
    print("\n")

    
    if choice==1:
        a_name=input("Enter admin name:- ")
        a_pin=int(input("Enter admin pin:- "))
        if a_name=="Tejas" and a_pin==31101997:
                print('''1-to insert train data\n2-to show train records\n3-to update records\n''')
                n=int(input("1-3:- "))
                if n==1:
                    print("--TRAIN RECORDS--")
                    tr_id=int(input("Enter train id:- "))
                    tr_name=input("Enter train name:- ")
                    source=input("Enter train source name:- ")
                    destination=input("Enter train destination name:- ")
                    t=(tr_id,tr_name,source,destination)
                    insert_tr_table(t)
                elif n==2:
                    display_tr_data()
                elif n==3:
                    print("--UPDATE TRAIN RECORDS--")
                    tr_id=int(input("Enter train id:- "))
                    tr_name=input("Enter new train name:- ")
                    source=input("Enter new train source name:- ")
                    destination=input("Enter new train destination name:- ")
                    t=(tr_name,source,destination,tr_id)
                    update_tr_data(t)
                else:
                    print("invalid input")
        else:
            print("Incorrect admin inputs")


    elif choice==2:
        print("--USER REGISTRATION--")
        u_m=int(input("Enter your mobile number:- "))
        u_e=input("Enter your email id:- ")
        u_un=input("Enter Username:- ")
        u_pn=int(input("Enter security pin number:- "))
        u_fn=input("Enter your first name:- ")
        u_ln=input("Enter your last name:- ")
        u_D=input("Enter your date of birth:- ")
        t=(u_m,u_e,u_un,u_pn,u_fn,u_ln,u_D)
        insert_data(t)

        
    elif choice==3:
        print("--TRAIN DETAILS--")
        display_tr_data()
        u=input("Enter your user name:- ")
        p=int(input("Enter your pin no:- "))
        import pymysql as p
        con=p.connect(user="root",host="localhost",database="travelbooking")
        cur=con.cursor()
        q="select * from user"
        cur.execute(q)
        data=cur.fetchall()
        for i in data:
            if u not in i:
                print("You are not ragister the application,please register your account\n")
                break
        for i in data:
            if u in i:
                print("--%%%%%%%%%%%%%%%%%%%%%%%%--")
                print("--BOOK YOUR TICKET--")
                u=input("Enter your user name:- ")
                tr_id=int(input("Enter train id:- "))
                st=input("Enter departure location:- ")
                end=input("Enter arrival location:- ")
                a_seats=int(input("Enter adult no of seats:- "))
                m_seats=int(input("Enter minor no of seats:- "))
                if a_seats>0 or m_seats>0:
                    a_fair=a_seats*500
                    m_fair=m_seats*300
                    total_f=a_fair+m_fair
                    print("your total ticket fair is:-",total_f)
                    t=(u,tr_id,st,end,a_seats,m_seats,total_f)
                    ticket_booking(t)
                    con.commit()
                    con.close()
                print("THANK YOU FOR BOOKING TICKETS")
                break


            
    elif choice==4:
        print("--TO DELETE YOUR BOOKING--")
        user_name=input("Enter your username:- ")
        t=(user_name,)
        delete_ticket_booking(t)

        
    elif choice==5:
        print("--BOOKING DETAILS--")
        display_ticket_booking()

        
    elif choice==6:
        print('''---UPDATE YOUR PROFILE---
1-To update your mobile number
2-To update your email id
3-To update your first name
4-To update your last name
5-To update your date of birth
6-To update security pin\n''')
        n=int(input("1-6:- "))
        if n==1:
            u_un=input("Enter your Username:- ")
            u_mobile=int(input("Enter your new mobile number:- "))
            t=(u_mobile,u_un)
            update_mobile_data(t)
        elif n==2:
            u_un=input("Enter your Username:- ")
            u_email=input("Enter your new email id:- ")
            t=(u_email,u_un)
            update_email_data(t)
        elif n==3:
            u_un=input("Enter your Username:- ")
            u_fname=input("Enter your new first name:- ")
            t=(u_fname,u_un)
            update_fname_data(t)
        elif n==4:
            u_un=input("Enter your Username:- ")
            u_lname=input("Enter your new last name:- ")
            t=(u_lname,u_un)
            update_lname_data(t)
        elif n==5:
            u_un=input("Enter your Username:- ")
            u_DOB=input("Enter your new date of birth:- ")
            t=(u_DOB,u_un)
            update_DOB_data(t)
        elif n==6:
            u_un=input("Enter your Username:- ")
            u_pinno=input("Enter new security pin number:- ")
            t=(u_pinno,u_un)
            update_pin_data(t)
        else:
            print("Invaid input")

        
    elif choice==7:
        print("--TO DELETE YOUR ACCOUNT--")
        username=input("Enter your username:- ")
        t=(username,)
        delete_data(t)

        
    elif choice==8:
        display_data()

        
    elif choice==9:
        break

    elif choice>9 or choice<1:
        print("Invalid input")


        
            
            
            
            
        
























        
        
        



