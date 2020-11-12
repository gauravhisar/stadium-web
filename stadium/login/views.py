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
        if x[0] == email and x[1] ==hashlib.md5(pwd.encode()).hexdigest():
            return render(request, 'index_login.html', {'name': name})  #the homepage again with the username specified
    else:
        return render(request, 'login.html', {'welcome1': 'Incorrect Email or Password', 'welcome2': 'User Login'})



def records(request):

    #SQL QUERY TO FETCH RECORDS OF  A PARTICULAR CUSTOMER
    cursor.execute('''select *
               from event e
               where e.ev_id in
               (select a.ev_id
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
        objects[i].price=e[i][6]

    events=[]
    for i in range(len(objects)):
        events.append(objects[i])

    return render(request,'record.html',{'name':name,'events':events})



def signup(request):
    return render(request, 'signup_index.html',{'welcome1':'New Account ?'})


def store_user(request):
    name = request.POST['name']
    email = request.POST['mail']
    phn = request.POST['phn']
    pwd = request.POST['pwd']
    cursor.execute("select email from customer")
    m=cursor.fetchall()
    mails=[]
    for i in  range(len(m)):
         mails.append(str(m[i][0]))
    if email in mails:
        return render(request,'signup_index.html',{'welcome1':'User already exist. Please login/enter another email.'})
    else:
        cursor.execute("insert into customer  (`Name`,`password`,email,contact_no) values (%s,%s,%s,%s)", (name, hashlib.md5(pwd.encode()).hexdigest(), email, phn))
        connection.commit()
        cursor.execute("select name  from customer where email=%s",(email,))
        name=str(cursor.fetchall()[0][0])
        return render(request,'index_login.html',{'name':name})
    

