from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField(max_length=140)

    def __str__(self):
        return f"Note title: {self.title} body: {self.body}"
