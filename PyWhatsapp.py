# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

# Start Flask Server
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/sms", methods=["POST"])
def sms_reply():
    # Fetch the message
    msg = request.form.get("Body")
    sender = request.form.get("From")
    num_media = int(request.values.get("NumMedia"))
    media_url = request.form.get("MediaUrl0")
    media_type = request.form.get("MediaContentType0")
    print("Sender" + sender)
    print("Message: " + msg)
    print("Number of media items: " + format(num_media))
    print("Media location: " + format(media_url))
    print("Media type: " + format(media_type))

    # Create reply
    resp = MessagingResponse()
    
    # Welcome Mr. XXX
    if sender == "whatsapp:+XXXXXXXXXXXX":
        if msg.strip().lower() == "hey":
            resp.message("Hello Mr. XXX! How may I help you today. You may choose to perform below operations for a quick start. Please reply with the option #:\n1. Add a new machine")
        elif msg.strip().lower() == "1":
            resp.message("Ok Mr. XXX, please tell me the machine name?")
        elif msg.strip().lower() == "mname":
            resp.message("Thank you, please provide some additional description?")
        elif msg.strip().lower() == "mdesc":
            resp.message("Thank you, please provide a main image?")
        else:
            resp.message("Thank you for messaging me Mr. XXX, I will get back to you ASAP - YYY.")

    else:
        resp.message("Thank you for messaging me, I will get back to you ASAP - YYY.")
    return str(resp)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+XXXXXXXXXXX',
#                               to='whatsapp:+XXXXXXXXXXXX'
#                           )

# print(message.sid)

if __name__ == "__main__":
  app.run()
