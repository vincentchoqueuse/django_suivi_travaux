# Logiciel de Suivi de Travaux

## Installation

* Installation de Python > 3
* Installation de Django: `pip install django`
* Clonage du repo github

## Lancement du programme

* Creation d'un super-utilisateur: `python manage.py createsuperuser`
* Lancement du serveur: `python manage.py runserver`
* Ouverture de l'application dans votre navigateur
* Authentification en tant que super utilisateur
* Creation de deux nouveaux groupes d'utilisateur:
    * resp: responsable des travaux
    * chef: chef de travaux

## Création de nouveaux utilisateurs

> Tous les utilisateurs doivent pouvoir: 1) se loguer sur le site d'administration, et 2) deposer une nouvelle demande de travaux. 

* Creation d'un nouvel utilisateur
* Activation de l'attribut "is_staff" (possibilité d'accéder au menu d'administration)
* Affectation du groupe si besoin (resp et/ou chef)
* Ajout des droits d'édition pour les demandes de travaux

