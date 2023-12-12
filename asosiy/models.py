from django.db import models


class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    tugulgan_yil = models.DateField()
    davlat = models.CharField(max_length=30)

    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=50)
    sana = models.DateField(blank=True, null=True)
    rasm = models.FileField(upload_to="albom_rasmlar")
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(null=True, upload_to="qoshiqlar_mp3")
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
