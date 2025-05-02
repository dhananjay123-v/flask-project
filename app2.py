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
    msg = ''  # Initialize message variable
    if request.method == 'POST':
        try:
            name = request.form.get('user')
            password = request.form.get('password')
            
            # Execute the INSERT query
            mycorsor.execute("INSERT INTO login_tbl (username, pass1) VALUES (%s, %s)", (name, password))
            myconn.commit()
            
            msg = 'Data Inserted Successfully'
        except Exception as e:
            pass
    return render_template('index.html', msg=msg)
    
@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)








        # if name == "ABC" and password == "123":
        #     return render_template('about.html', msg1='LOGIN SUCCESSFUL')
        # else:
        #     return render_template('index.html', msg='Wrong User & Password')
       