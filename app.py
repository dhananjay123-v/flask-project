from flask import Flask, render_template, request
import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lpu_db"
)

mycorsor=myconn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    msg =''
    if request.method=='POST':
        try:
            name = request.form.get('user')
            password = request.form.get('password')
            mycorsor.execute("SELECT * FROM login_tbl WHERE username=%s AND pass1=%s", (name, password))
            result = mycorsor.fetchone()
            msg='Wrong User & Password'
            if result:
                if name == str(result[1]) and password == str(result[2]):
                    return render_template('about.html', msg1='LOGIN SUCCESSFUL')
                return render_template('index.html')
        except Exception as e:
            pass
    return render_template('index.html',msg=msg)
    

    
@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
