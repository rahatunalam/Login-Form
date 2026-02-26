from flask import Flask,render_template,request 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password'] == '1234':
            return 'Welcome Admin!'
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)