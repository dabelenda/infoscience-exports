from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    sciper = models.PositiveIntegerField(null=True, blank=True)
    where = models.CharField(max_length=100, null=True, blank=True)
    units = models.CharField(max_length=300, null=True, blank=True)
    group = models.CharField(max_length=150, null=True, blank=True)
    classe = models.CharField(max_length=100, null=True, blank=True)
    statut = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email

    def __unicode__(self):
        return """  Sciper:    %s
                        where:     %s
                        units:     %s
                        group:     %s
                        classe:    %s
                        statut:    %s
                    """ % (self.sciper,
                           self.where,
                           self.units,
                           self.group,
                           self.classe,
                           self.statut)
