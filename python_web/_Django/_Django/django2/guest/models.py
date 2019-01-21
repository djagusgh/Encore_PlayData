from django.db import models

# Create your models here.
class Guest(models.Model):
    title = models.CharField(max_length=30) # DB에서 VARCHAR 개념
    content = models.CharField(max_length=1000)
    # auto_now_add : 수정할 때마다 적용!
    write_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

