from django.db import models
from account import models as account_models
import uuid
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class OTP(account_models.TimeStampModel):
    """
    1.The "txn_id" field is a UUIDField that stores the transaction ID (if any) associated with the OTP
    2. The "email_or_mobile" is a CharField that can store either an email or a mobile number.
    3. The "otp" field is a CharField that can store the OTP code.
    4. The "expire_at" field is a DateTimeField that stores the date and time the OTP was created.S et to 5 minutes after the OTP is created.
    5. The "is_verified" field is a BooleanField that stores whether the OTP has been verified or not.

    """

    txn_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    email_or_mobile = models.CharField(max_length=64)
    otp = models.CharField(unique=True, max_length=6)
    expire_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        db_table = "OTP"