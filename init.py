from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector as mysql

db = mysql.connect(
    host = "database-my.caomyyms75ok.us-east-1.rds.amazonaws.com",
    user = "suriya",
    passwd = "suriya123"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS regform")
cursor.close()

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'database-my.caomyyms75ok.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'suriya'
app.config['MYSQL_PASSWORD'] = 'suriya123'
app.config['MYSQL_DB'] ='regform'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        age = details['age']
        email = details['email']
        mobile = details['mobile']
        location = details['location']
        cur = mysql.connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS userdata(name VARCHAR(150), age INT(3), email VARCHAR(150), mobile VARCHAR(10), location VARCHAR(100))") 
        cur.execute("INSERT INTO userdata(name, age, email, mobile, location) VALUES (%s, %s, %s, %s, %s)", (name, age, email, mobile, location))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
@app.route('/users')
def users():
    cur =mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM userdata")
    if resultValue > 0:
        usersDetails = cur.fetchall()
        return render_template('users.html',usersDetails=usersDetails)
