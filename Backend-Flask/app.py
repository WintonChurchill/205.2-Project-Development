from flask import Flask #import flask library 
from flask_mail import Mail, Message 

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'florence.taele@gmail.com'
app.config['MAIL_PASSWORD'] = 'oxwd hxux yiuj oshv'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False 
mail = Mail(app)

@app.route("/")
def index(): 
    msg = Message(
        subject="Hi, EasyBooking Team!",
        sender="florence.taele@gmail.com",
        recipients=['Easybooking74@gmail.com']
    )
    msg.body = "Hey, sending you this email from my flask app, let me know if it works!"
    mail.send(msg)
    return "Message sent succesfully!"
    
if __name__ == '__main__': 
    app.run(debug=True)
    