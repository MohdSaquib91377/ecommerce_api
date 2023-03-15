
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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
    


class SerializerValidator:
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


