"""account URL Configuration

Add API endpoints urls here.
"""
from django.urls import path

from account.views import AccountView

routing_table_without_id = {

    "GET": "get_all_accounts",
    "POST": "create_account"
}
routing_table_with_id = {
    "GET": "get_single_account",
    "PUT": "update_account"
}

urlpatterns = [
    path(
        '',
        AccountView.as_view(
            routing_table=routing_table_without_id),
        name='account'),
    path(
        '/<resource_id>',
        AccountView.as_view(
            routing_table=routing_table_with_id),
        name='account-id')]
