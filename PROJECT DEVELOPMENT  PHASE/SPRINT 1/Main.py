from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():

    return render_template('AdminLogin.html')


@app.route("/DonorLogin")
def DonorLogin():
    return render_template('DonorLogin.html')

@app.route("/NewDonor")
def NewDonor():
    return render_template('NewDonor.html')

@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')

@app.route("/PersonalInfo")
def PersonalInfo():
    return render_template('DonorPersonal.html')



@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')



@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html',data=data)




@app.route("/AdminDonorInfo")
def AdminDonorInfo():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM personltb  ")
    data = cur.fetchall()


    return render_template('AdminDonorInfo.html', data=data)









@app.route("/UserHome")
def UserHome():
    user = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + user + "'")
    data = cur.fetchall()
    return render_template('UserHome.html',data=data)


@app.route("/DonorHome")
def DonorHome():
    cuname = session['cname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM companytb where username='" + cuname + "'")
    data = cur.fetchall()
    return render_template('DonorHome.html', data=data)




@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM regtb ")
           data = cur.fetchall()
           return render_template('AdminHome.html' , data=data)

       else:
        return render_template('index.html', error=error)


@app.route("/donorlogin", methods=['GET', 'POST'])
def donorlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['dname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from donortb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM donortb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('DonorHome.html', data=data)








@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)



        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )




















@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'


    return render_template('UserLogin.html')



@app.route("/personal", methods=['GET', 'POST'])
def personal():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        blood = request.form['blood']
        health = request.form['health']
        dname = session['dname']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO personltb VALUES ('','" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + blood + "','" + health + "','"+ dname+"')")
        conn.commit()
        conn.close()


        alert = 'Record Saved'

        return render_template('goback.html', data=alert)



@app.route("/appr")
def appr():


    cid =  request.args.get('cid')
    dname = session['dname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from  personltb where id='" + str(cid) + "' ")
    conn.commit()
    conn.close()



    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM personltb where Username='"+ dname +"' ")
    data = cur.fetchall()



    return render_template('DonorPersonalInfo.html', data=data)


@app.route("/DonorPersonalInfo")
def DonorPersonalInfo():

    dname = session['dname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM personltb where Username='" + dname + "' ")
    data = cur.fetchall()

    return render_template('DonorPersonalInfo.html', data=data)



@app.route("/newdonor", methods=['GET', 'POST'])
def newdonor():
    if request.method == 'POST':

        name1 = request.form['name']

        phone = request.form['phone']

        email = request.form['email']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO donortb VALUES ('','" + name1 + "','" + phone + "','" + email + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()


    return render_template('DonorLogin.html')


@app.route("/Search")
def Search():


    return render_template('Search.html')


@app.route("/dsearch", methods=['GET', 'POST'])
def dsearch():



    blood = request.form['blood']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM personltb  where blood ='"+ blood +"'")
    data = cur.fetchall()
    return render_template('Search.html',data=data)


@app.route("/SendRequest")
def SendRequest():


    session['cid'] =  request.args.get('cid')


    return render_template('Notification.html')



@app.route("/noti", methods=['GET', 'POST'])
def noti():



    info = request.form['info']

    did = session['cid']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Plasmadb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  personltb where  id='" + did + "'")
    data = cursor.fetchone()

    if data:
        mail = data[4]
        print(mail)



    else:
        return 'Incorrect username / password !'





    alert = 'Send Notication'

    return render_template('goback.html', data=alert)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)