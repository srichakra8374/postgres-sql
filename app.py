import os
from flask import Flask, render_template, request, redirect, url_for
##from flask_mysqldb import MySQL
import  psycopg2

app = Flask(__name__)

# Configure MySQL from environment variables
##app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
#app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
#app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
##mysql = MySQL(app)
conn = psycopg2.connect(database="achievers",
                        user=os.environ.get('DB_USER'),
                        password=os.environ.get('DB_USER_PWD'),
                        host=os.environ.get("DB_HOST"),
                        port="5432")

@app.route('/')
def hello():
    cur = conn.cursor()
    cur.execute('SELECT message FROM dbo.messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    ##cur = mysql.connection.cursor()
    cur = conn.cursor()
    cur.execute('INSERT INTO dbo.messages (message) VALUES (%s)', [new_message])
    ##mysql.connection.commit()
    conn.commit()
    cur.close()
    return redirect(url_for('hello'))


@app.route('/greeting')
def greeting():
    return "welcome to flask app"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

