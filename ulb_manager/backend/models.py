from django.db import models


# Create your models here.

class bookInfo(models.Model):
    fromUser = models.CharField(max_length=30, default='WYS')
    fromSite = models.CharField(max_length=50)
    bookName = models.CharField(max_length=50)
    updateTime = models.DateTimeField()


class siteInfo(models.Model):
    siteName = models.CharField(max_length=50)
    bookName = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    updateTime = models.DateTimeField()
    lastChapter = models.CharField(max_length=100)
