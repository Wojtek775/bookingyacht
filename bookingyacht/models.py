from django.db import models

from django.contrib.auth.models import User

YACHT_CATEGORY = (
    (1, "monohulls"),
    (2, "catamarans"),
    (3, "Motor Boat"),
    (4, "Trimaran")

)


#class YachtCategory(models.Model):
#    category = models.IntegerField(choices=YACHT_CATEGORY)
#
 #   def __str__(self):
 #       return f"{self.category}"


class Marina(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/marina_detail/{self.pk}/"


class CharterCompany(models.Model):
    name = models.CharField(max_length=64)
    marina = models.ManyToManyField('Marina')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/chartercompany_detail/{self.pk}/"


class Yacht(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    length = models.IntegerField()
    max_person = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.IntegerField(choices=YACHT_CATEGORY, null=False, blank=False)
    charter_company = models.ForeignKey(CharterCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/yacht_detail/{self.pk}/"


class YachtReservation(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)

