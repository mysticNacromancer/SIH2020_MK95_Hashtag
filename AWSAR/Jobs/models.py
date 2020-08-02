from django.db import models
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    vacancies = models.IntegerField(default=1)
    doc_url = models.URLField(blank=True)
    summary = models.CharField(max_length=500, blank=True)
    website = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                            related_name='applicants')
    applied_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()