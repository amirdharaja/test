from django.db import models


class Test(models.Model):

    testdata = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.testdata

    class Meta:
        db_table = "test"