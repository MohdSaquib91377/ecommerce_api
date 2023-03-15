
from account.api import serializers as account_serializers
from otp import service as otp_service
from otp import query as otp_query
from services.email import TemplateEmail
from services import helpers as services_helpers
from account import query as account_query

class AccountService:
    

    @staticmethod
    def send_otp_email(email: str):
        '''
        1. validate email
        2. generate otp
        3.  create instance of OTPHandler
        5. create otp object
        6. send mail
        7. return status, data 
        '''
        if not services_helpers.EmailOrMobileValidator.is_email(email):
                return 400, "Invalid email"
                
        otp = otp_service.OTPService.generate_otp()
        otp_handler_ref = otp_query.OTPHandler()
        otp = otp_handler_ref.create_single_otp(email,otp)
        
        # TODO: send otp on email address
        email_ref = TemplateEmail("OTP",email, "account/one_time_password.html",context={"otp":otp.otp})
        email_ref.send()
        status, data = 200, {"message":f"otp sent successfully on {otp.email_or_mobile}","txn_id":otp.txn_id}
        return status, data


        


    @staticmethod
    def send_otp_mobile(mobile):
        '''
        1. validate email
        2. generate otp
        3.  create instance of OTPHandler
        5. create otp object
        6. send mail
        7. return status, data 
        '''

        if not services_helpers.EmailOrMobileValidator.is_mobile(mobile):
            return 400, "Invalid mobile number"
              
        otp = otp_service.OTPService.generate_otp()
        otp_handler_ref = otp_query.OTPHandler.get_OTPHandler_class_instance()
        otp = otp_handler_ref.create_single_otp(mobile,otp)
        # TODO: send otp on phone number

    @staticmethod
    def check_is_email_or_mobile(email_or_mobile):
        if "@" in email_or_mobile:
            status, data = AccountService.send_otp_email(email_or_mobile)

        else:
            status, data = AccountService.send_otp_mobile(email_or_mobile)
        
        return status, data

    @staticmethod
    def validate_registeration_payload(payload: dict):
        serializer = services_helpers.SerializerValidator(account_serializers.RegistrationLoginSerializer,payload)
        status, data = serializer.validate_input()
        if status == 400:
            return status, data
        
        status, data = AccountService.check_is_email_or_mobile(data["email_or_mobile"])
        return status, data
        
            

    @staticmethod
    def validate_login_payload(payload: dict):
        serializer = services_helpers.SerializerValidator(account_serializers.RegistrationLoginSerializer, payload)
        status, data = serializer.validate_input()
        if status == 400:
            return status, data

        status, data = AccountService.check_is_email_or_mobile(data["email_or_mobile"])
        return status, data
    
    @staticmethod
    def validate_send_otp_payload(payload: dict):
        serializer = services_helpers.SerializerValidator(account_serializers.RegistrationLoginSerializer, payload)
        status, data = serializer.validate_input()
        user = account_query.AccountHandler.get_user_by_email_or_mobile(payload["email_or_mobile"])
        if status == 400:
            return status, data
        
        elif len(user) == 0:
            return 400, {"message":f"invalid credentials"}
        else:
            status, data = AccountService.check_is_email_or_mobile(payload["email_or_mobile"])

        return status, data

