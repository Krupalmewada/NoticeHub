from django.db import models

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()#no max length
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)#auto now can update more than once and auto now add is created

    class Meta:
        db_table = "notice"

