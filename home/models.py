from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Gift(models.Model):
    image=models.FileField(upload_to="C:/Users/akanksha kulkarni/DjangoProjects/Christmas/media/")
    description=models.CharField(max_length=25)
    quantity=models.IntegerField()
    #quantity_remaining=models.IntegerField()

    def __str__(self):
        return self.description
    # def image_tag(self):
    #     return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    #     image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

class user(models.Model):
    username=models.CharField(max_length=25)
    mob_no=models.IntegerField()
    address=models.TextField()
    description=models.CharField(max_length=25)

    def __str__(self):
        return self.username