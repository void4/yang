# yang
Calls people at random times.
Registration and unregistration through SMS.

Uses Twilio.

Start a cronjob to execute main.py every few minutes. This file loops through all registered numbers and calls them if enough time has passed. server.py is used for registration.
