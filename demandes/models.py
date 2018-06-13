from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
PERSONNEL_CHOIX = (
                  (1, "Technicien"),
                  (2, "Enseignant"),
                  (3, "Enseignant Chercheur"),
                  (4, "Autre"),
                  (5, "Exterieur")
                  )

NATURE_CHOIX = (
                   (1, "Débit matière 1ere"),
                   (2, "Décroupe Jet d'eau"),
                   (3, "Usinage Conventionnel"),
                   (4, "Usinage CN"),
                   (5, "Autre")
                   )

AFFECTATION_CHOIX = (
                (1, "Enseignement"),
                (2, "Projet"),
                (3, "Recherche"),
                (4, "Autre"),
                )

AVIS_CHOIX = (
              (1, "Favorable"),
              (2, "Défavorable"),
            )

class DemandeTravaux(models.Model):
    titre = models.CharField(max_length=200, null=True, blank=True)
    auteur = models.ForeignKey(User, null=True, blank=True,related_name= "auteur")
    date = models.DateField(default=datetime.now)
    type = models.IntegerField(choices=PERSONNEL_CHOIX, default=1)
    commentaire = models.CharField(max_length=200, null=True, blank=True)
    nature = models.IntegerField(choices=NATURE_CHOIX, default=1)
    affectation = models.IntegerField(choices=AFFECTATION_CHOIX, default=1)
    description = models.TextField()
    matiere = models.BooleanField(help_text="Matière disponible")
    commande = models.BooleanField(help_text="Commande à Prévoir")
    delai_fin = models.DateField(null=True, blank=True)
    dimensions = models.CharField(max_length=200)
    materiau = models.CharField(max_length=200)
    quantite = models.CharField(max_length=200)
    
    chef = models.ForeignKey(User, null=True, blank=True,related_name= "chef")
    chef_date = models.DateTimeField(auto_now=True)
    chef_avis = models.IntegerField(choices=AVIS_CHOIX,null=True, blank=True)
    chef_justification = models.TextField(null=True, blank=True)
    
    resp = models.ForeignKey(User, null=True, blank=True,related_name= "resp")
    resp_date = models.DateTimeField(auto_now=True)
    resp_avis = models.IntegerField(choices=AVIS_CHOIX,null=True, blank=True)
    resp_justification = models.TextField(null=True, blank=True)

    def val_chef(self):
        return self.chef_avis == 1

    def val_resp(self):
        return self.resp_avis == 1

    val_chef.boolean = True
    val_resp.boolean = True

    class Meta:
        verbose_name = "Travaux"
        verbose_name_plural = "Travaux"







