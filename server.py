from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from pickleshare import PickleShareDB

db = PickleShareDB('db')

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    from_number = request.values.get('From')
    body = request.values.get("Body")

    if body.lower()=="stop":
        del db[from_number]
        return str(MessagingResponse().message("Unregistered!"))

    db[from_number] = None
    # Could respond with SMS, but just calling will save money
    return str(MessagingResponse().message("Registered!"))

if __name__ == "__main__":
    app.run(debug=True)
