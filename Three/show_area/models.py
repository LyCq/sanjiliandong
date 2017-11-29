from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self',null=True,blank=True)

    class Meta:
        db_table= 'areas'