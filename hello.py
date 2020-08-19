from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'Flask %s!' % name
# app.add_url_rule('/hello', 'hello', hello_world)

@app.route('/blog/<int:postID>/')
def show_blog(postID):
    return 'Blog number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run(debug=True)
