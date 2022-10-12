from crypt import methods
from flask import Flask, render_template, request, session, redirect
import pymongo
import certifi

app=Flask(__name__,static_folder='public',static_url_path='/')
app.secret_key='12345678'
client = pymongo.MongoClient("mongodb+srv://Logan:19941217@mycluster.g4ddrju.mongodb.net/?retryWrites=true&w=majority",
tlsCAFile=certifi.where())
db = client.login_data #選擇要操作的database


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/member')
def member_page():
    if 'accountID' in session:
        return render_template('member.html')
    else:
        return redirect('/')

@app.route('/error')
def error():
    message=request.args.get('msg','發生問題，請聯繫客服')
    return render_template('error.html',error_msg=message)

@app.route('/signin', methods=["POST"])
def signin():
    account_ID=request.form['account_ID']
    print(account_ID)
    passwords=request.form['passwords']
    collecttion=db.member_data
    data=collecttion.find_one({
        "$and":[
            {"accountID":account_ID},
            {"passwords":passwords}
        ]
    })
    if account_ID == "" or passwords== "": #空字串用""，不是None，也不是Null
        return redirect('/error?msg=請輸入帳號、密碼')
    elif data==None:
        return redirect('/error?msg=帳號、或密碼輸入錯誤')
    else:
        session['accountID']=data['accountID']
        print('登入成功')
        return redirect('/member')
    # return redirect('/error?msg=請輸入帳號、密碼')
    # return redirect('/member')

@app.route('/signout')
def signout():
    del session['accountID']
    return redirect('/')
 
@app.route('/square')
def square():
    # number=request.args.get('number','')
    number=request.form.get('number')
    # print(number)
    # print(type(number))
    num=int(number) #一開始接收到的數字是字串
    square_number=num*num
    # return square_number
    return render_template('square.html',number=square_number)

app.run(port='3000')