# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from credentials import WILSON_SID, WILSON_AUTH_TOKEN, WILSON_NUMBER

wilson_sid = WILSON_SID
wilson_auth = WILSON_AUTH_TOKEN
wilson_number = WILSON_NUMBER

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = wilson_sid
auth_token = wilson_auth
client = Client(account_sid, auth_token)

def twilio_text():
    message = client.messages \
        .create(
            body='AS50 from Badminton Warehouse is now available for purchase!!!',
            from_='+18647320570',
            to= wilson_number
        )
    return message.sid

print(twilio_text())