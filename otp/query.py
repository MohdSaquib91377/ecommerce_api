
from otp import models as otp_models
from django.conf import settings
from datetime import datetime
class OTPHandler:

    @staticmethod
    def get_OTPHandler_class_instance():
        otp_ref = OTPHandler()
        return otp_ref
    
    def create_single_otp(self,email_or_mobile: str, otp_code: str) -> otp_models.OTP:
        """
        Creates a single OTP object with the given email or mobile and OTP code.

        :param email_or_mobile: A string representing the email or mobile number of the user.
        :type email_or_mobile: str
        :param otp_code: A string representing the OTP code to be associated with the email or mobile.
        :type otp_code: str
        :return: An OTP object representing the newly created OTP record.
        :rtype: otp_models.OTP

        """
        otp = otp_models.OTP.objects.create(email_or_mobile = email_or_mobile, otp = otp_code, expire_at =datetime.now() + settings.OTP["OTP_EXPIRATION_TIME"])
        return otp