# step 1: pip install flask-sqlalchemy
# step 2: from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'developementkey'

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(sefl, name, city, addr, pin):
        sefl.name = name
        sefl.city = city
        sefl.addr = addr
        sefl.pin = pin

@app.route('/')
def show_all():
    return render_template('sqlalchemy_show_all.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added!', 'info')
            return redirect(url_for('show_all'))
    return render_template('sql_alchemy_new.html')

if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run()
