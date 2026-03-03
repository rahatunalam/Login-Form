from flask import Blueprint, render_template, request, redirect, flash, current_app

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        db = current_app.config['db']
        cursor = current_app.config['cursor']

        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return render_template('registration.html',
                                   error="Passwords do not match!")

        # 🔥 Store password directly (NO hashing)
        sql = "INSERT INTO registration (name, email, username, password) VALUES (%s, %s, %s, %s)"
        values = (name, email, username, password)

        cursor.execute(sql, values)
        db.commit()

        flash("Registration Successful! Please login.", "success")
        return redirect('/')

    return render_template('registration.html')