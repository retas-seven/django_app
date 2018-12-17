from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}'.format(self.name, str(self.mail), str(self.gender), str(self.age), str(self.birthday))
