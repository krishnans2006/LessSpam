from flask import Flask, render_template, redirect, url_for, request, session, g
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


import firebase_admin
from firebase_admin import credentials, firestore

import re

app = Flask(__name__)

account_sid = "AC347d2311e6c4e143683a712e24324db1"
auth_token = "5ff32eab5cc0619af6a728298a7cbf4b"
twilio = Client(account_sid, auth_token)

cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def index():
    return render_template("index.html", numbers=["3856886273", "8364759848"])

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if re.match(r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})', body):
        phone = body.strip().replace(" ", "").replace("-", "").replace(".", "").replace("+", "")
        print(phone)
        if db.collection("Numbers").document(phone).get().exists:
            db.collection("Numbers").document(phone).update({
                "Count": db.collection("Numbers").document(phone).get(["Count"]).to_dict()["Count"] + 1
            })
        else:
            db.collection("Numbers").document(phone).set({
                "Number": phone,
                "Count": 1
            })
        resp.message(f"- -\n\nYou have successfully reported:\n    {phone}\nas a spam number!\nYour input is helping people around the world stay safe from attackers and malicious deeds")
    else:
        resp.message("- -\n\nThat is not a valid phone number! Please make sure you entered it in correctly...\n\nA valid phone number is 10 digits, with an optional country code, and numbers separated by dots, dashes, or spaces.")
    print(str(resp))
    return str(resp)

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, True)
