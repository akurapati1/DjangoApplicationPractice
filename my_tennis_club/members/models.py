from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, default="")
    joined_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["lastname", "firstname"]

    def __str__(self) -> str:
        return self.fullname

    @property
    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}".strip()
