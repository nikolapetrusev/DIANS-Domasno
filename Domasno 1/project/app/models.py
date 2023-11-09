from django.db import models


class City(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Град"
        verbose_name_plural = "Градови"


class Coords(models.Model):
    longitude = models.TextField()
    latitude = models.TextField()

    def __str__(self) -> str:
        return f"{self.longitude} - {self.latitude}"

    class Meta:
        verbose_name = "Координати"
        verbose_name_plural = "Координати"


class Winery(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField()
    phone = models.TextField()
    work = models.TextField(blank=True, null=True)
    coords = models.ForeignKey(Coords, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.city}"

    class Meta:
        verbose_name = "Винарија"
        verbose_name_plural = "Винарии"
