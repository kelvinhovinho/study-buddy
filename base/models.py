from django.db import models

# Create your models here.
class Room(models.Model):
    # host 
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # prticipants
    updated = models.DateTimeField(auto_now=True) #changes everytime it is saved
    created = models.DateTimeField(auto_now_add=True) #save the first time and dosenr change

    def __str__(self):
        return self.name