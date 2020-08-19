from flask import Flask, render_template
app = Flask(__name__)

@app.route('/templates/<user>')
def index(user):
    return render_template('templates.html', name = user)

@app.route('/hello/<int:score>')
def your_score(score):
    return render_template('templates.html', marks = score)

@app.route('/result')
def result():
    my_dict = {'Toan': 80, 'Van': 60, 'Ngoai Ngu': 80}
    return render_template('result.html', result = my_dict)

if __name__ == '__main__':
    app.run(debug=True)
