from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class SubCategory(models.Model):
    Api = models.CharField(max_length=500, default=None)
    Description = models.CharField(max_length=500, default=None)
    Auth = models.CharField(max_length=500, default=None)
    HTTPS = models.CharField(max_length=500, default=None)
    Cors = models.CharField(max_length=100, default=None)
    Link = models.CharField(max_length=200, default=None)
    Category = models.CharField(max_length=100)

    def __dir__(self):
        return f"{self.Api} of {self.Category} category "
