from django.shortcuts import render
import mysql.connector
stadiumDB = mysql.connector.connect(host="localhost", user="root", passwd="j0keme0ut", database="stadium")
mycursor = stadiumDB.cursor()


def signup(request):
    return render(request, 'signup_index.html')


def store_user(request):
    name = request.POST['name']
    email = request.POST['mail']
    phn = request.POST['phn']
    pwd = request.POST['pwd']
    mycursor.execute("insert into customer values (%s, %s,%s,%s,%s)", ('vt202',name, pwd, email, phn))
    stadiumDB.commit()
    return render(request, 'result.html', {'result': [name, email, phn, pwd]})
# Create your views here.
