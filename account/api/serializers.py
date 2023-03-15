from rest_framework import serializers
from account import models as account_models

class RegistrationLoginSerializer(serializers.Serializer):
    """
    Serializer class for user registration.
    
    This serializer validates and serializes the input data for user registration, and defines the 'email_or_mobile'
    field, which represents the email or mobile number of the user being registered.
    
    Attributes:
    -----------
    email_or_mobile : serializers.CharField(max_length=64)
        A required field that represents the email or mobile number of the user being registered.
        The maximum length of this field is 64 characters.
    """
    email_or_mobile = serializers.CharField(max_length=64)


