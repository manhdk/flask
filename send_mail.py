from flask import Flask
from flask_mail import Mail, Message
import smtplib, ssl

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app=app)

@app.route('/')
def index():
    msg = Message('Hello everyone!', sender='your-email@gmail.com', recipients=['your-email@gmail.com'])
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'send email successfully!'

if __name__ == "__main__":
    app.run(debug=True)
