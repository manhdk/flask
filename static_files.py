from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def static_file():
    return render_template('static_files.html')

if __name__ == '__main__':
    app.run(debug=True)
