from django.db import models
from django.contrib.auth.models import User


TAG_TYPES = ("Blog Post Tag", "Song Tag")


# Create your models here.
class Tag(models.Model):
    pass
    # tag_name = models.CharField(max_length=20, primary_key=True)
    # tag_type = models.CharField(choices=TAG_TYPES)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL)
J7K58NYNA6DZ6U6