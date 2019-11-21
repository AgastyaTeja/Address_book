from django.contrib import admin
from basic_app.models import UserContacts
# Register your models here.


class UserContactsAdmin(admin.ModelAdmin):
    list_display=['__str__', 'owner']
    list_filter=['owner']
    search_fields=['first_name', 'last_name']

    class Meta:
        model=UserContacts


#admin.site.register(UserProfileInfo)
admin.site.register(UserContacts, UserContactsAdmin)