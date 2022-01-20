from django.db import models


class Todo(models.Model):
    text      = models.CharField(max_length=250)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.text