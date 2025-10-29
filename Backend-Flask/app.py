from flask import Flask #import flask library 
from flask_mail import Mail, Message #easy and simple method to send email
from flask import render_template, request, redirect, url_for, flash
import os 
import resend 

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'florence.taele@gmail.com'
app.config['MAIL_PASSWORD'] = 'oxwd hxux yiuj oshv'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False 
mail = Mail(app)

resend.api_key = os.environ['RESEND_API_KEY']
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']

#Contact Email HTML Body Message 
CONTACT_EMAIL = """
<!DOCTYPE html>
<html lang="en">
<head> 
    <meta charset="UTF-8">
    <met name="vieport" content="width=device-width, inital-scale=1.0">
    <title>New Message Notification from Customers!</title>
</head>
<body>
    <h2>New Message!</h2>
    <p><strong>Name:</strong>{name}</p>
    <p><strong>Message:<strong></p>
    <blockquote>
        {message}
</body>
</html>
"""

@app.route("/in")
def index(): 
    msg = Message(
        subject="Hi, EasyBooking Team!",
        sender="florence.taele@gmail.com",
        recipients=['Easybooking74@gmail.com']
    )
    msg.body = "Hey, sending you this email from my flask app, let me know if it works!"
    mail.send(msg)
    return "Message sent succesfully!"

@app.route('/', methods=['GET', 'POST'])
def contact(): 
    if request.method =="POST": 
        #loading data from form! 
        form_data = request.form.to_dict()

        #configuration of email fields! 
        params = {
            "from": "Your Flask App <onboarding@resend.dev>",
            "to": [ADMIN_EMAIL],
            "subject": f"New Message from {form_data['name']}!",
            "html": CONTACT_EMAIL.format(**form_data)
        }

        #Sending email and catching responses 
        response = resend.Emails.send(params)

        #Handle the response 
        if response.get("id"): 
            return redirect("/contact")
        else: 
            return {"message": "Something went wrong. Please try again."}
    else: 
        #return render template for contact form 
        return render_template("contact1.html")
    
if __name__ == '__main__': 
    app.run(debug=True)
    