from django.utils.crypto import get_random_string
from django.conf import settings
class OTPService:
  

    @staticmethod
    def generate_otp(otp_digit_length = 6) -> str:
        """
        Generates a random OTP (one-time password) of the specified length.

        :param length: The length of the OTP to be generated (default is 6).
        :type length: int
        :return: A string representing the randomly generated OTP.
        :rtype: str
        """
        
        otp = get_random_string(length = settings.OTP["OTP_DIGIT_LENGTH"], allowed_chars="1234567890")
        return otp
    
   