"""Model for account"""
from framework.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class Account(AbstractBaseModel):
    """Account of the connect application.
         Write schema below.
    """

    default_error_messages = {
        'invalid_id': _('Account does not exist')
    }

    class Meta:
        app_label = 'account'
        db_table = 'account'
