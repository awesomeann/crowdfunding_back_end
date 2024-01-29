from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.db.models import Sum

def one_month_from_today():
    return datetime.now() + timedelta(days=30)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200) #pet name
    description = models.TextField()
    animal_choices = (
        ("CAT", "Cat"),
        ("DOG", "Dog"),
        ("BIRD", "Bird"),
        ("HORSE", "Horse")
    )
    animal = models.CharField(max_length=30, choices=animal_choices)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    is_successful = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now())
    deadline = models.DateTimeField(default=one_month_from_today)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

    @property
    def total_number_of_pledges(self):
        return self.pledges.count()

       
    @property
    def sum_of_pledges(self):
        sum = self.pledges.aggregate(Sum("amount", default=0))
        return sum
    


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField(default=False)
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supported_pledges'
    )