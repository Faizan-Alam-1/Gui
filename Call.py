
from twilio.rest import Client
def make_call():
    account_sid = "ACc7d414df5a2772ddffae6e54f79f6756"
    auth_token = "28c73df22d8c9e3edc3a11aecc66dd02"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+918210410103',
                            from_='+19402919532')
    print(call.sid)
    

 
