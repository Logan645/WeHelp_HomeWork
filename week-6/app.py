from asyncore import read
from crypt import methods
from flask import Flask, render_template, redirect, request, session
import mysql.connector
import os
from dotenv import load_dotenv
# import tkinter as tk
load_dotenv()
PASSWORD=os.getenv('password')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="{}".format(PASSWORD),
  database="week6_DB"
)
# print(mydb) #連線完成
mycursor=mydb.cursor() #建立cursor物件
app=Flask(__name__,static_folder='public',static_url_path='/')
app.secret_key='12345678'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name=request.form['name']
    account=request.form['account']
    password=request.form['password']
    print(name, account,password)
    if name=="" or account=="" or password=="":
        return redirect('/error?message=任一欄位不可有空值')
    else:
        mycursor.execute("select account from member where account='{}'".format(account))
        result = mycursor.fetchall()
    if result!=[]:
        return redirect('/error?message=帳號已有人註冊')
    else:
        sql='insert into member(name, account,password) values (%s,%s,%s)'
        val=(name, account, password)
        mycursor.execute(sql,val)
        mydb.commit()
        # window=tk.Tk()
        # window.title('建立成功')
        # window.geometry("300x100+250+150")
        # backToHome=tk.Button(window,
        #            text="返回主畫面登入",
        #            command=redirect('/'))
        # backToHome.pack()
        # window.mainloop()
        return redirect('/')

@app.route('/signin', methods=['POST'] )
def signin():
    account=request.form['account']
    password=request.form['password']
    mycursor.execute("select * from member where account='{}' and password='{}'".format(account,password))
    result = mycursor.fetchone()
    if result!=None:
        session['name']=result[0]
        return redirect('/member')
    else:
        return redirect('/error?message=帳號或密碼輸入錯誤')

@app.route('/signout')
def signout():
    del session['name']
    return redirect('/')

@app.route('/member')
def member():
    if 'name' in session:
        return render_template('member.html',username=session['name'])
    else:
        return redirect('/')

@app.route('/error')
def error():
    message=request.args.get('message',"發生錯誤")
    return render_template('error.html',msg=message)


app.run(port=3000)