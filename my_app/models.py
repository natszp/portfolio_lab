from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

TYPES_OF_INSTITUTION = (
    ('fundacja', 'fundacja'),
    ('organizacja', 'organizacja pozarządowa'),
    ('zbiorka', 'zbiórka lokalna'),
)

class Institution(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    type = models.CharField(choices=TYPES_OF_INSTITUTION, default='fundacja', max_length=100)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.IntegerField()
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(auto_now=True)
    pick_up_time = models.TimeField(auto_now=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
