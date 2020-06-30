from django.db import models

class settings(models.Model):
    maximum_number = models.IntegerField(default=2)
    minimum_number = models.IntegerField(default=1)
    number_of_inputs = models.IntegerField(default=6)

    def __str__(self):
        return ('Change the settings here.')