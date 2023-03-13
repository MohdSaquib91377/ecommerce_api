from twilio.rest import Client

class OtpSms:
    def __init__(self,account_sid, auth_token,sender_phone_number,recipient_phone_number,otp):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.sender_phone_number = sender_phone_number
        self.recipient_phone_number = recipient_phone_number
        self.otp = otp

    def send(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Your OTP is: {self.otp}",
            from_=self.sender_phone_number,
            to=self.recipient_phone_number
        )
        return message.sid
    