from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    #additional

    def __str__(self):

        return self.user.usernname

class UserContacts(models.Model):

    current_user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 150)
    email_address = models.CharField(max_length = 150)
    street_address = models.CharField(max_length = 350)

    def __str__(self):

        return '{}'.format(self.first_name)
