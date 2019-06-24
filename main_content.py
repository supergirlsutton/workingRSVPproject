from flask import Flask, render_template, request
import os

app = Flask("MyApp")

port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('daytime.html', when="daytime")

@app.route("/evening", methods=['GET', 'POST'])
def evening():
    return render_template('evening.html', when="evening")
    
@app.route("/success", methods=['GET','POST'])
def success():
    formName=request.form['name']
    formGuests=request.form['guests']
    formEmail=request.form['email']
    formVegetarian=request.form['foodpreference']
    formWhen=request.form['when']
    send_simple_message(formName, formGuests, formEmail, formVegetarian, formWhen)
    return render_template('success.html', name=formName)

import requests

API_KEY = "cc1be912ad91e420f327101bb5d096b5-7bce17e5-c201b125"
DOMAIN_NAME ="sandbox58c29f7f76574b62a838d23116825fa6.mailgun.org"

def send_simple_message(name, guests, email, foodpreference, when):
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_NAME+"/messages",
        auth=("api", API_KEY),
        data={"from": "Wedding planner <mailgun@"+DOMAIN_NAME+">",
              "to": ["supergirlsutton@gmail.com"],
              "subject": "New guests sign up",
              "text": name + " " + " Guests: " + " " + str(guests) + " " + " Email: " + " " + str(email) + " " + " Food Preference: "
 				+ str(foodpreference) + " When: " + str(when)
 		})
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=port, debug=False)
