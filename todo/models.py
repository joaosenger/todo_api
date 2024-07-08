from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=250)
    done = models.BooleanField()

    def __str__(self):
        return self.task
