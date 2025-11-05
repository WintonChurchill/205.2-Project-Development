from flask import Flask, request, jsonify, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message #easy and simple method to send email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os

debug_value = True
app = Flask(__name__)

if debug_value == True:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/502-server'
else:
    # env var
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT', '5432')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Commented out for now (will update later)
#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USERNAME'] = 'florence.taele@gmail.com'
#app.config['MAIL_PASSWORD'] = 'oxwd hxux yiuj oshv'
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False 
#mail = Mail(app)

#@app.route("/")
#def index(): 
 #   msg = Message(
  #      subject="Hi, EasyBooking Team!",
   #     sender="florence.taele@gmail.com",
    #    recipients=['Easybooking74@gmail.com']
    #)
    #msg.body = "Hey, sending you this email from my flask app, let me know if it works!"
    #mail.send(msg)
    #return "Message sent succesfully!"


    
# talk to database using alcheme
db = SQLAlchemy(app)

# user table for db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #unique id 
    email = db.Column(db.String(120), unique=True, nullable=False) #email

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True) # booking number
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user that booked number
    start_time = db.Column(db.DateTime, nullable=False) #self explanatory
    end_time = db.Column(db.DateTime, nullable=False) #self explanatory
    created_at = db.Column(db.DateTime, default=datetime.utcnow) #gonna use this command as although its depreciated, i don't need time zone specific.
    user = db.relationship('User', backref='bookings')




@app.route('/api/bookings', methods=['GET']) # When requesting bookings, get args start and end
def get_bookings():
    """
    This gets a request, with 2 potential args, start_time and end_time. These are processed and queries the database.
    else, return all bookings made. then convert the information to json and return it.
    """
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time') 

    if start_time and end_time:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
        bookings = Booking.query.filter(
            Booking.start_time < end_dt,
            Booking.end_time > start_dt
        ).all()
    else:
        # Return all bookings if no range provided
        bookings = Booking.query.all()

    result = []
    for b in bookings:
        result.append({
            "id": b.id,
            "start_time": b.start_time.isoformat(),
            "end_time": b.end_time.isoformat(),
            "user": b.user.email
        })

    return jsonify(result)


# create a new booking
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """
    Reads data (Start and end times), converts them to py datetime format, queries the db to see if there are already bookings
    if not, send error in response. else create a new booking, send it over to the db, send success message.
    """
    data = request.json
    user_id = data.get('user_id')
    start_time = datetime.fromisoformat(data.get('start_time'))
    end_time = datetime.fromisoformat(data.get('end_time'))

    # Check for overlapping bookings
    overlap = Booking.query.filter(
        Booking.start_time < end_time,
        Booking.end_time > start_time
    ).first()
    if overlap:
        return jsonify({"error": "Time slot already booked"}), 409

    booking = Booking(user_id=user_id, start_time=start_time, end_time=end_time)
    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Booking created", "id": booking.id}), 201 # 201 = creating stuff




if __name__ == '__main__': 
    with app.app_context():
        db.create_all()
    app.run(debug=debug_value) # Using debug value to adjust db connectivity (either local or env vars)