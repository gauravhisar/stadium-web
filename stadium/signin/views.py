from django.shortcuts import render
import mysql.connector
import hashlib
stadiumDB = mysql.connector.connect(host="localhost", user="root", passwd="j0keme0ut", database="stadium")
mycursor = stadiumDB.cursor()


def signin(request):
    return render(request, 'signin_index.html', {'welcome1': '', 'welcome2': 'User Login'})


def verify_user(request):
    email = request.POST['mail']
    pwd = request.POST['pwd']
    mycursor.execute("select email,password from customer")
    result = mycursor.fetchall()
    for x in result:
        if x[0] == email and x[1] == hashlib.md5(pwd.encode()).hexdigest():
            return render(request, 'result.html', {'result': result})  #the homepage again with the username specified

    return render(request, 'signin_index.html', {'welcome1': 'Incorrect Email or Password', 'welcome2': 'User Login'})
# Create your views here.
