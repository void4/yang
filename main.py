from ConfigParser import RawConfigParser
from pickleshare import PickleShareDB
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
from random import random, choice
from time import time
import os

config = RawConfigParser()

if not config.read("credentials.ini"):
    print("Could not find credentials. Exiting.")
    exit(1)

account_sid = config.get("twilio", "account_sid")
auth_token = config.get("twilio", "auth_token")
call_number = config.get("twilio", "number")

client = Client(account_sid, auth_token)

db = PickleShareDB('db')

for number, nextcall in db.items():

    if nextcall is not None and nextcall>time():
        continue

    sample = choice([f for f in os.listdir("samples") if f.endswith(".mp3")])

    response = VoiceResponse()
    response.play("samples/" + sample)

    # Make the call
    call = client.api.account.calls.create(to=line[0], from_=call_number, url=response)

    print(call.sid)

    # Set next call time
    # Should not call at night?
    db["number"] = time()+random()*60*60*8
    print(number, nextcall, db["number"])
