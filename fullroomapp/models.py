from django.db import models

class RoomData(models.Model):
    width = models.IntegerField()
    length = models.IntegerField()
    healthy = models.IntegerField()
    sick = models.IntegerField()

    def __str__(self):
        return self.width
    