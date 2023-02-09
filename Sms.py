from twilio.rest import Client

def sms():
    # Your Account SID from twilio.com/console
    account_sid = "ACc7d414df5a2772ddffae6e54f79f6756"
    # Your Auth Token from twilio.com/console
    auth_token  = "28c73df22d8c9e3edc3a11aecc66dd02"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+918210410103", 
        from_="+19402919532",
        body="Help me ! i'm in danger")
    print(message.sid)