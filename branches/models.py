from django.db import models
from django.utils.text import slugify
import uuid
class Branch(models.Model):
    STATUS = (
        ("فعال", "فعال"),
        ("غیر فعال", "غیر فعال"),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)
    publish_date = models.DateField()
    status = models.CharField(choices=STATUS, default="فعال", max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super(Branch, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name