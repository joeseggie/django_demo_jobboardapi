import uuid
from django.db import models


class Job(models.Model):

    class Meta:
        db_table = 'job'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField(max_length=60)
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=120)
    salary = models.FloatField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title
