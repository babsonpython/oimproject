from twilio.rest import Client
from credentials import MY_SID, MY_AUTH_TOKEN, NUMBERS #credentials.py is hidden due to sensitive information
# NUMBERS is stored as a list of numbers that we want to send messages to. Format: [+0123XXXX890, +1234XXXX901,etc]

my_sid = MY_SID
my_auth = MY_AUTH_TOKEN

account_sid = my_sid
auth_token = my_auth
client = Client(account_sid, auth_token)

def twilio_text():
    """Uses the twilio API to send messages to users who sign up"""
    for number in NUMBERS:
        message = client.messages \
            .create(
                body='AS50 from Badminton Warehouse is now available for purchase!!!',
                from_='+18647320570',
                to= number
            )
    return message.sid

def main():
    twilio_text()

if __name__ == '__main__':
    main()