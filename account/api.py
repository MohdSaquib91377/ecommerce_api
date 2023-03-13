from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from account import service as account_service

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            status, msg = account_service.AccountService.validate_registeration_payload(request.data)
            return Response({"status":status, "message":msg},status=status)
        except Exception as e:
            status, msg = 400, f"{e}"
            return Response({"status":status, "message":msg},status = status)
