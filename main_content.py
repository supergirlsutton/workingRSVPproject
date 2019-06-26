from flask import Flask, render_template, request
import os

app = Flask("MyApp")

port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=['GET', 'POST'])
#@app.route("/home", methods=['GET', 'POST']) - this is to call the link / at the end like you have evening below
def home():
    return render_template('daytime.html', when="daytime")

@app.route("/evening", methods=['GET', 'POST'])
def evening():
    return render_template('evening.html', when="evening")
    
@app.route("/success", methods=['GET','POST'])
def success():
    formName=request.form['name']
    formEmail=request.form['email']
    formFoodpreference=request.form['foodpreference']
    formRsvp=request.form['rsvp']
    formWhen=request.form['when']
    send_simple_message(formName, formEmail, formFoodpreference, formRsvp, formWhen)
    return render_template('success.html', name=formName)

import requests

API_KEY = os.environ.get('API_KEY', None)
DOMAIN_NAME = os.environ.get('DOMAIN_NAME', None)

def send_simple_message(name, email, foodpreference, rsvp, when):
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_NAME+"/messages",
        auth=("api", API_KEY),
        data={"from": "Wedding planner <mailgun@"+DOMAIN_NAME+">",
              "to": ["supergirlsutton@gmail.com"],
              "subject": "New Guest RSVP",
              "text": name + " " +  " " + " Email: " + " " + str(email) +  " "  +  " Food Preference: " + " " +
 				+ str(foodpreference) + " " +  "RSVP:"  + " "  + str(rsvp) + " " + "When:  " + " " + str(when)
 		})

#this below line allows you to make changes while it updates the local server - screen shot on desktop - CHANGE TO FALSE on deploy
app.run(host='0.0.0.0', port=port, debug=False)
