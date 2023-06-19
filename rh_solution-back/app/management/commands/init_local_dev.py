from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Genre, Salarie

import csv

ADMIN_ID = "admin"
ADMIN_PASSWORD = "admin"

class Command(BaseCommand):
    init_start_message = "Initialisation du projet pour un environnement local"
    database_delete_message = "Suppression du jeu de données existant..."
    superuser_create_message = "Création d'un super utilisateur..."
    genre_create_message = "Création des genres..."
    init_end_message = "Initialisation terminée !"

    genres = {
        "Male",
        "Female",
        "Agender"
    }

    def handle(self, *args, **options):

        self.stdout.write(self.style.MIGRATE_HEADING(self.init_start_message))

        self.stdout.write(self.style.WARNING(self.database_delete_message))
        User.objects.all().delete()
        Genre.objects.all().delete()
        Salarie.objects.all().delete()

        self.stdout.write(self.style.MIGRATE_HEADING(self.superuser_create_message))
        User.objects.create_superuser(ADMIN_ID, "admin@example.com", ADMIN_PASSWORD)

        self.stdout.write(self.style.MIGRATE_HEADING(self.genre_create_message))
        for genre in self.genres:
            Genre.objects.create(valeur=genre)

        with open("database.csv", newline="") as csvfile:
            database_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(database_reader, None)  # skip the headers
            for row in database_reader:
                prenom = row[1]
                nom = row[2]
                genre_en = row[3]
                telephone = row[4]
                email = row[5]
                email_personnel = row[6]
                genre_query_set =Genre.objects.get(valeur = genre_en)

                Salarie.objects.create(
                    prenom = prenom,
                    nom = nom,
                    telephone = telephone,
                    email = email,
                    email_personnel = email_personnel,
                    id_genre = genre_query_set
                )

        self.stdout.write(self.style.SUCCESS(self.init_end_message))
