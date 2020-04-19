from django.db import models


# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(
        to="hn_users.HNUser", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.url} | {self.description}"
