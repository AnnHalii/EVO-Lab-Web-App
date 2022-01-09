from django.db import models


class AdditionalData(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254, db_index=True, unique=True)

    def __str__(self):
        return f"{self.email}: {self.first_name} {self.last_name}"

    @classmethod
    def get_or_none(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None
