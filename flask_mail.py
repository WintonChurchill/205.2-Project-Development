#import Libraries 
from flask import Flask 
from flask_mail import Mail, Message 

app = Flask(__name__)

from app import index 
#this helps in support of notifying Flask that if app.index is relying on 
#20/10/25 - Error when trying to test! 
#Note: Will be working in other github repo and here when completed fully!  
#but will be regularly updating 

app.config['MAIL_SERVER']  = 'create_new_gmail@gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_gmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'xiue oust nuqz cdru' 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index(): 
    msg = Message(
        subject = 'Hi there, it is Easybooking here! ', 
        sender = 'florence.taele@gmail.com', #Must match MAIL_USERNAME #will add later once created new Gmail
        recipients = ['new_gmail@gmail.com'] #ACUTAL customer email 
    )

    msg.body = "Hi, send you this email from Flask app, let me know if you need anything!"
    mail.send(msg)
    return "Message sent!"

@app.route("/send_html_email")
def send_html_email(): 
    msg = Message(subject='HTML Email from Flask', 
                  sender='florence.taele@gmail.com',
                  recipients=['recipient@gmail.com'])#add other gmail!
    
    #HTML Body-Content 
    msg.html = """
    <html>
        <body> 
            <h1>HI! from Flask-Mail</h1>
            <p>This is an example of an <strong>HTML</strong> email</p>
        </body>
    <html>
    """

    mail.send(msg)

    return "HTML email sent"

if __name__ == '__main__': 
    app.run(debug=True)