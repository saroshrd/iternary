from django.db import models

# Create your models here.

class City(models.Model):
  name = models.CharField(max_length=32)
  description = models.CharField(max_length=256)

  REQUIRED_FIELDS = ["name", "description"]

  class Meta:
    ordering = ["name"]
    unique_together = [["name"]]
    indexes = [
      models.Index(fields = ["name"], name ="city-db-name-idx")
    ]
    db_table = "m_city"


class Itinerary(models.Model):
  city = models.ForeignKey(City(), null=False, on_delete=models.CASCADE)
  day =  models.IntegerField(blank=True, null=True)
  itinerary = models.CharField(max_length=2048)

  REQUIRED_FIELDS = ["day", "itinerary"]

  class Meta:
    ordering = ["day"]
    # unique_together = [["name"]]
    indexes = [
      models.Index(fields = ["day"], name ="itinerary-db-name-idx")
    ]
    db_table = "m_itinerary"