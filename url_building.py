# author: manhdk
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def admin_url():
    return 'Admin Page'

@app.route('/guest/<guest>')
def guest_url(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def user_url(name):
    if name == 'admin':
        return redirect(url_for('admin_url'))
    else:
        return redirect(url_for('guest_url', guest=name))

if __name__ == '__main__':
    app.run(debug=True)
