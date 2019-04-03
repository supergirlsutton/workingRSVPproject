from flask import Flask, render_template, request
import os

app = Flask("MyApp")

port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/success", methods=['GET','POST'])
def success():
    formName=request.form['name']
    formGuests=request.form['guests']
    formEmail=request.form['email']
    send_simple_message(formName, formGuests, formEmail)
    return render_template('success.html', name=formName)

import requests

API_KEY = "1bba878437b3a947e2975697f59026c7-2416cf28-7183155c"
DOMAIN_NAME ="sandbox7a718bb475144a93ad6c7e282afbd66a.mailgun.org"

def send_simple_message(name, guests, email):
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_NAME+"/messages",
        auth=("api", API_KEY),
        data={"from": "Wedding planner <mailgun@"+DOMAIN_NAME+">",
              "to": ["catherineernx@gmail.com"],
              "subject": "New guests sign up",
              "text": name + " " + "Guests:" + " " + str(guests) + " " + "Email:" + " " + str(email)})

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=port, debug=False)
