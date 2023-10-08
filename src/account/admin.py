from django.contrib import admin

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    