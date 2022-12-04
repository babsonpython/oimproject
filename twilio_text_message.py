from twilio.rest import Client
from credentials import WILSON_SID, WILSON_AUTH_TOKEN, NUMBERS

wilson_sid = WILSON_SID
wilson_auth = WILSON_AUTH_TOKEN


account_sid = wilson_sid
auth_token = wilson_auth
client = Client(account_sid, auth_token)

def twilio_text():
    for number in NUMBERS:
        message = client.messages \
            .create(
                body='AS50 from Badminton Warehouse is now available for purchase!!!',
                from_='+18647320570',
                to= number
            )
    return message.sid
