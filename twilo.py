from twilio.rest import Client

account_sid = 'AC36144e43e00e773f8b72d33a0f417484'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='Some random text mesage',
    to='+61452613158'
)

print(message.sid)
