from django.db import models


class Test(models.Model):

    testdata = models.TextField(null=False, unique=False)

    objects = models.Manager()

    def __str__(self):
        return self.testdata

    class Meta:
        db_table = "test"