from __future__ import unicode_literals

from PIL import Image as Img
import StringIO
from django.core.files import File

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ImageDetail(models.Model):
    image = models.ImageField(
        upload_to='pics/',
        default='pics/none/no-img.jpg'
    )
    name = models.CharField(blank=True, default='No Name', max_length=200)
    uploaded_by = models.ForeignKey(User)
    ssim = models.CharField(blank=True, null=True, max_length=100)
    mse = models.CharField(blank=True, null=True, max_length=100)

    def save(self, *args, **kwargs):
        if self.image:
            image = Img.open(StringIO.StringIO(self.image.read()))
            image.thumbnail((500, 500), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.image = File(output, self.image.name)
        super(ImageDetail, self).save(*args, **kwargs)
