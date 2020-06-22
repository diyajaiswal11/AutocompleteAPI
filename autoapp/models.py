from django.db import models



class Cities(models.Model):
    i_d=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    state_id=models.CharField(max_length=255)
    state_code=models.CharField(max_length=255)
    country_id=models.CharField(max_length=255)
    country_code=models.CharField(max_length=255)
    latitude=models.CharField(max_length=255)
    longitude=models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Countries(models.Model):
    i_d=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    iso3=models.CharField(max_length=255)
    iso2=models.CharField(max_length=255)
    phone_code=models.CharField(max_length=255)
    capital=models.CharField(max_length=255)
    currency=models.CharField(max_length=255)
    native=models.CharField(max_length=255)
    emoji=models.CharField(max_length=255)
    emojiU=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class States(models.Model):
    i_d=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    country_id=models.CharField(max_length=255)
    country_code=models.CharField(max_length=255)
    state_code=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name



