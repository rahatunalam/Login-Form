from flask import Flask, render_template, request, redirect, flash
from registration import register_bp
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login_form"
)

cursor = db.cursor(dictionary=True)

app.config['db'] = db
app.config['cursor'] = cursor

app.register_blueprint(register_bp)


# 🔹 LOGIN ROUTE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        sql = "SELECT * FROM registration WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()

        # 🔥 Direct plain text comparison
        if user and user['password'] == password:
            flash("Login Successful!", "success")
            return f"Welcome {username}"
        else:
            return render_template('login.html',
                                   error="Invalid username or password!")

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)