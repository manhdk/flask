from flask import Flask, request, url_for, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('redirect_login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == "__main__":
    app.run(debug=False)
