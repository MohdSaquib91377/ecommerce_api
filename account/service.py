
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from account import serializers as account_serializers
from otp import service as otp_service
from otp import query as otp_query
from services.email import TemplateEmail

class InputValidator:
    def __init__(self, serializer_class, payload):

        """
        Initializes the InputValidator with a serializer class and payload.
        """

        self.serializer_class = serializer_class
        self.payload = payload

    def validate_input(self):
        """
        Validates the payload using the serializer class.

        Returns:
            dict: The validated payload data.
            
        """
        serializer = self.serializer_class(data=self.payload)
        if serializer.is_valid():
            status, msg = 200, serializer.validated_data
            return status, msg
        
        status, msg = 400, serializer.errors
        return status, msg


class EmailOrMobileValidator:
    @staticmethod
    def is_email(value: str) -> bool:
        """
        Returns True if the given value is a valid email address, otherwise False.

        Args:
            value (str): The value to check.

        Returns:
            bool
        """

        try:
            validate_email(value)
            return True
        except ValidationError as err:
            return False

    @staticmethod
    def is_mobile(value):
        """
        Returns True if the given value is a valid mobile phone number, otherwise False.

        Args:
            value (str): The value to check.

        Returns:
            bool
        """

        # Check that the value contains only digits
        if not value.isdigit():
            return False
        
        # Check that the value has the correct length for a mobile phone number
        elif len(value) != 10:
            return False

        return True



class AccountService:
    
    @staticmethod
    def validate_registeration_payload(payload: dict):
        validator = InputValidator(account_serializers.UserRegistrationSerializer,payload)
        
        otp = otp_service.OTPService.generate_otp()
        otp_handler_ref = otp_query.OTPHandler.get_OTPHandler_class_instance()
        
        status, data = validator.validate_input()
        if status == 400:
            return status, data
        
        elif "@" in data["email_or_mobile"]:
            if not EmailOrMobileValidator.is_email(data["email_or_mobile"]):
                status, data = 400, "Invalid email"
                return status, data
            
            otp = otp_handler_ref.create_single_otp(data["email_or_mobile"],otp)
            # TODO: send otp on email address
            email_ref = TemplateEmail("OTP",data["email_or_mobile"], "account/one_time_password.html",context={"otp":otp})
            email_ref.send()
            status, data = 200, f"otp sent successfully on {otp.email_or_mobile}"
            return status, data

        else:
            if not EmailOrMobileValidator.is_mobile(data["email_or_mobile"]):
                status, data = 400, "Invalid mobile number"
                return status, data
            
            otp = otp_handler_ref.create_single_otp(data["email_or_mobile"],otp)
            # TODO: send otp on phone number
        
            
        
        

    @staticmethod
    def validate_login_payload(payload: dict):
        pass