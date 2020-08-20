from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def cookies():
    return render_template('cookies.html')

@app.route('/setcookies', methods = ['POST', 'GET'])
def setcookies():
    if request.method == "POST":
        user = request.form['name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookies')
def getcookies():
    name = request.cookies.get('userID')
    return '<h2>Welcome '+name+'</h2>'

if __name__ == '__main__':
    app.run(debug=True)
