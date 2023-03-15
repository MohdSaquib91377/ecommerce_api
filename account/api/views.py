from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from account import service as account_service

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            status, data = account_service.AccountService.validate_registeration_payload(request.data)
        except Exception as e:
            status, data = 400, f"{e}"
        finally:    
            return Response({"status":status, "data":data},status = status)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request, *args,**kwargs):
        try:
            status, data = account_service.AccountService.validate_login_payload(request.data)
        except Exception as e:
            status, data = 400, f"{e}"
        
        finally:
            return Response({"status":status,"data":data},status=status)
        
class SendOTpView(APIView):
    permission_classes = []

    def post(self,request, *args,**kwargs):
        try:
            status, data = account_service.AccountService.validate_send_otp_payload(request.data)
        except Exception as e:
            status, data = 400, f"{e}"
        
        finally:
            return Response({"status":status,"data":data},status=status)