import os
from twilio.rest import Client
from dotenv import load_dotenv

class NotificationManager:
    def __init__(self):
        load_dotenv()
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)

    def send_message(self, flight):
        body = f"Low price alert! Only ${flight['price']} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']}" \
               f" to {flight['cityTo']}-{flight['cityCodeTo']}, from {flight['local_departure']} to" \
               f" {flight['local_departure_2']}"
        message = self.client.messages.create(
            from_=os.environ['TWILIO_PHONE_NO'],
            body=body,
            to=os.environ['MY_PHONE_NO']
        )
        print(message.sid)
