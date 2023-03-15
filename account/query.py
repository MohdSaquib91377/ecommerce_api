from account import models as account_models
from django.db.models import Q
class AccountHandler:

    @classmethod
    def get_user_by_email_or_mobile(cls,email_or_mobile):
        user = account_models.User.objects.filter(Q(email = email_or_mobile) | Q(mobile__icontains = email_or_mobile))
        return user