from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Град"
        verbose_name_plural = "Градови"
        db_table = "city"


class Coords(models.Model):
    longitude = models.TextField()
    latitude = models.TextField()

    def __str__(self) -> str:
        return f"{self.longitude} - {self.latitude}"

    class Meta:
        verbose_name = "Координати"
        verbose_name_plural = "Координати"
        db_table = "coords"


class Winery(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField()
    phone = models.TextField()
    work = models.TextField(blank=True, null=True)
    coords = models.ForeignKey(Coords, on_delete=models.SET_NULL, blank=True, null=True)
    # reviews = models.ManyToManyField(Review)

    @property
    def rating(self):
        temp = [r.rating for r in self.reviews.all()]
        return round(sum(temp) / len(temp), 1) if temp else 0
    
    def __str__(self) -> str:
        return f"{self.name} - {self.city}"

    class Meta:
        verbose_name = "Винарија"
        verbose_name_plural = "Винарии"
        db_table = "winery"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="reviews")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    winery = models.ForeignKey(Winery, related_name="reviews", on_delete=models.CASCADE)    