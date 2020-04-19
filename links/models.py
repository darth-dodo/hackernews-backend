from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Link(TimeStampedModel):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(
        to="hn_users.HNUser", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.url} | {self.description}"


class Vote(TimeStampedModel):
    user = models.ForeignKey(
        to="hn_users.HNUser", related_name="hn_user_votes", on_delete=models.CASCADE
    )
    link = models.ForeignKey(
        to="links.Link", related_name="link_votes", on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ("user", "link")

    def __str__(self):
        return f"{self.user} - {self.link}"
