from django.shortcuts import render
from django.http import HttpResponse

from .models import event

import mysql.connector
from mysql.connector import Error

import hashlib

#Global variables
email=None
pwd=None

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='stadium',
                                         user='root',
                                         password='j0keme0ut')
    if connection.is_connected():
        cursor = connection.cursor()
        
except Error as e:
    print("Error while connecting to MySQL", e)




def signin(request):
    return render(request, 'login.html', {'welcome1': '', 'welcome2': 'User Login'})


def verify_user(request):
    global email 
    email= request.POST['mail']
    global pwd 
    pwd= request.POST['pwd']
    cursor.execute("select email,password from customer")
    result = cursor.fetchall()
    cursor.execute("select email from customer")
    m=cursor.fetchall()
    mails=[]
    for i in  range(len(m)):
         mails.append(str(m[i][0]))
    if email not in mails:
        return render(request, 'login.html', {'welcome1': 'Incorrect Email or Password', 'welcome2': 'User Login'})
    cursor.execute("select name  from customer where email=%s",(email,))
    name=str(cursor.fetchall()[0][0])
    for x in result:
        if x[1] ==hashlib.md5(pwd.encode()).hexdigest():
            return render(request, 'index_login.html', {'name': name})  #the homepage again with the username specified
    else:
        return render(request, 'login.html', {'welcome1': 'Incorrect Email or Password', 'welcome2': 'User Login'})



def records(request):

    #SQL QUERY TO FETCH RECORDS OF  A PARTICULAR CUSTOMER
    cursor.execute('''select distinct (e.ev_id),e.ev_name,e.date,e.time,e.price,a.seat_id
               from event e,attends a
               where (e.ev_id ,a.seat_id) in
               (select a.ev_id,a.seat_id
               from attends a
               where a.cust_id in(
               (select c.cust_id
                from customer c
                where c.email = %s)))
                order by date
                desc limit 10''',(email,))


    e=cursor.fetchall()

    cursor.execute("select name  from customer where email=%s",(email,))
    name=str(cursor.fetchall()[0][0])

    objects = []

    #list of objects of class event 
    for i in range(len(e)):
         objects.append(event())



    for i in range(len(e)):
        objects[i].ev_id=e[i][0]
        objects[i].ev_name =e[i][1]
        objects[i].date =e[i][2]
        objects[i].time = e[i][3]
        objects[i].price=e[i][4]
        objects[i].seat=e[i][5]

    events=[]
    for i in range(len(objects)):
        events.append(objects[i])

    return render(request,'record.html',{'name':name,'events':events})



def signup(request):
    return render(request, 'signup_index.html',{'welcome1':'New Account ?', 'e1': "", 'e2': "", 'e3': "", 'e4': ""})


def store_user(request):
    name = request.POST['name']
    global email 
    email= request.POST['mail']
    phn = request.POST['phn']
    global pwd 
    pwd= request.POST['pwd']
    e1 = ""
    e2 = ""
    e3 = ""
    e4 = ""
    flag = 0

    if len(name) == 0:
        flag = 1
        e1 = "Enter Your Name"
    if len(phn) < 10:
        flag = 1
        e2 = "Enter Valid Phone Number"
    if len(email) == 0:
        flag = 1
        e3 = "Enter Valid Email"
    if len(pwd) < 8:
        flag = 1
        e4 = "Password should be greater than 8 chars"
    if flag == 1:
        return render(request, 'signup_index.html',
                      {'welcome1': 'New Account ?', 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4})

    cursor.execute("select email from customer")
    m=cursor.fetchall()
    mails=[]
    for i in range(len(m)):
         mails.append(str(m[i][0]))
    if email in mails:
        return render(request, 'signup_index.html', {'welcome1': 'User already exist. Please login with other email', 'e1': "", 'e2': "", 'e3': "", 'e4': ""})
    else:
        cursor.execute("insert into customer  (`Name`,`password`,email,contact_no) values (%s,%s,%s,%s)", (name, hashlib.md5(pwd.encode()).hexdigest(), email, phn))
        connection.commit()
        cursor.execute("select name  from customer where email=%s",(email,))
        name=str(cursor.fetchall()[0][0])
        return render(request,'index_login.html',{'name':name})
    
