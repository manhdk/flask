from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
app.secret_key = 'developerkey'


@app.route('/')
def home_page():
    return render_template('sqlite_home.html')

@app.route('/newstudent')
def newstudent():
    return render_template('sqlite_student.html')

@app.route('/addrecord', methods = ['GET', 'POST'])
def addrecord():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin_code = request.form['pin']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)', (name, address, city, pin_code))
                conn.commit()
                msg = 'Record successully added!'
        except:
            conn.rollback()
            msg = 'Error in insert operation!'
        
        finally:
            return render_template('sqlite_result.html', msg = msg)
            conn.close()

@app.route('/listrecord')
def listrecord():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('SELECT * from students')

    rows = cur.fetchall()
    return render_template('sqlite_list.html', rows = rows)

if __name__ == "__main__":
    app.debug = True
    app.run()
