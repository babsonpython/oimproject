from twilio.rest import Client
from credentials import WILSON_SID, WILSON_AUTH_TOKEN, NUMBERS

wilson_sid = WILSON_SID
wilson_auth = WILSON_AUTH_TOKEN
numbers = NUMBERS


account_sid = wilson_sid
auth_token = wilson_auth
client = Client(account_sid, auth_token)

def twilio_text():
    message = client.messages \
        .create(
            body='AS50 from Badminton Warehouse is now available for purchase!!!',
            from_='+18647320570',
            to= numbers
        )
    return message.sid

print(twilio_text())