from django.conf import settings
from django.db import models
# Create your models here.


class UserContacts(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='User')
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 150)
    email_address = models.CharField(max_length = 150)
    street_address = models.CharField(max_length = 350)

    def __str__(self):

        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
        ordering=['owner','last_name','first_name']
