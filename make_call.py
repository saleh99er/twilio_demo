# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

# credentials stored in environmental variables
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')

# to/from number also stored as environmental variables for privacy reasons
to_number = os.environ.get('MY_PHONE_NUMBER')
from_number = os.environ.get('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=to_number,
                        from_=from_number
                    )

print(call.sid)
