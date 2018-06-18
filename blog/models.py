from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=128)
    Email = models.CharField(max_length=128)
    Firstname = models.CharField(max_length=128)
    Lastname = models.CharField(max_length=128)
    def as_json(self):
        return dict(
            Username=self.Username,
            Password=self.Password,)
    class Meta:
        managed = False
        db_table = 'user'
