from django.db import models

class Genre(models.Model):
    valeur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genre'


class Salarie(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    email_personnel = models.CharField(max_length=250, blank=True, null=True)
    id_genre = models.ForeignKey(Genre, models.DO_NOTHING, db_column='id_genre')

    class Meta:
        managed = False
        db_table = 'salarie'
