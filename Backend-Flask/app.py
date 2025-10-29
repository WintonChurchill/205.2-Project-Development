from flask import Flask #import flask library 
from flask_mail import Mail, Message #easy and simple method to send email
from flask import render_template, request, redirect, url_for, flash
import os 
import resend 

app = Flask(__name__)



if __name__ == '__main__': 
    app.run(debug=True)
    