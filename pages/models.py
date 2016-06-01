from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture_url = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=40)
    job_description = models.TextField()
    join_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
