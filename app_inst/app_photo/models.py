from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 1_000:
        raise ValidationError("Max size 1mb")
    else:
        return value


class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to="images", validators=[validate_file_size])

