import uuid
from django.db import models
from django.utils import timezone
#from TANGU.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User

# Create your models here.

class Administrateur_g(models.Model):
    #nom = models.CharField(max_length=25)
    #prenom = models.CharField(max_length=30)
    #email = models.EmailField(unique=True,default='guru@guruacademy.xyz')
    telephone = models.CharField(max_length=20)
    quartier = models.CharField(max_length=15)
    ville = models.CharField(max_length=16)
    pays = models.CharField(max_length=15)
    CNI  = models.CharField(max_length=50)
    passport = models.CharField(max_length=25,default='none')
    matricule = models.UUIDField(max_length=5,default=uuid.uuid4,editable=False,unique=True)
    #mot_de_passe = models.CharField(max_length=25,default='guru@2025')
    photo_profil = models.ImageField(upload_to='GESTION/static/img', null=True, blank=True)
    piece_identite  = models.FileField(upload_to='GESTION/static/document', null=True, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']
            

    def __str__(self):
        return str(self.user)

class Categories(models.Model):
    nom_categories = models.CharField(max_length=20)
    description = models.TextField()

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_categories)

class Employes(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True,default='employes@guruacademy.xyz')
    telephone = models.CharField(max_length=20)
    quartier = models.CharField(max_length=15)
    ville = models.CharField(max_length=16)
    pays = models.CharField(max_length=15)
    CNI  = models.CharField(max_length=50)
    passport = models.CharField(max_length=25,default='none')
    matricule = models.UUIDField(max_length=5,default=uuid.uuid4,editable=False,unique=True)
    #mot_de_passe = models.CharField(max_length=25,default='employes@2025')
    photo_profil = models.ImageField(upload_to='GESTION/static/img', null=True, blank=True)
    piece_identite  = models.FileField(upload_to='GESTION/static/document', null=True, blank=True)
    id_categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    id_admin = models.ForeignKey(Administrateur_g,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom)

class Clients(models.Model):
    nom = models.CharField(max_length=25,default='none',null=True)
    prenom = models.CharField(max_length=30,default='none',null=True)
    nom_entreprise = models.CharField(max_length=25,default='none',null=True)
    email = models.EmailField(unique=False)
    telephone = models.CharField(max_length=20)
    quartier = models.CharField(max_length=15)
    ville = models.CharField(max_length=16)
    pays = models.CharField(max_length=15)
    CNI = models.CharField(max_length=50,default='none',null=True)
    code_NIF = models.CharField(max_length=35,unique=True,default='none',null=True)
    photo_profil = models.ImageField(upload_to='GESTION/static/img', null=True, blank=True,default='none')
    piece_identite  = models.FileField(upload_to='GESTION/static/document', null=True, blank=True,default='none')
    id_admin = models.ForeignKey(Administrateur_g,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom)

class Contratclients(models.Model):
    nom_contrat = models.CharField(max_length=200)
    code_contrat = models.CharField(max_length=50,unique=True)
    lettre_commande  = models.FileField(upload_to='GESTION/static/document', null=True, blank=True)
    id_client = models.ForeignKey(Clients,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_contrat)

class Contratemployes(models.Model):
    nom_contrat = models.CharField(max_length=200)
    code_contrat = models.CharField(max_length=50,unique=True)
    lettre_commande  = models.FileField(upload_to='GESTION/static/document', null=True, blank=True)
    id_employe = models.ForeignKey(Employes,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_contrat)

class Formations(models.Model):
    nom_formation = models.CharField(max_length=35)
    description = models.TextField()
    payer=models.CharField(max_length=35,default='gratuit')
    centre=models.CharField(max_length=100,default='Kigobe')
    domaine=models.CharField(max_length=100,default='Informatique')
    #niveau=models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_formation)
     
class Stagiaires(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    nom_formation = models.CharField(max_length=20,default='PHP')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    #id_formation = models.ForeignKey(Formations,on_delete=models.CASCADE)
    id_admin = models.ForeignKey(Administrateur_g,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom)

class Utilisateur(models.Model):
    #username = models.CharField(max_length=35,unique=True)
    #email = models.EmailField()
    #password = models.CharField(max_length=15)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.user)

class Demande_stagiaire(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    #motif_stage = models.CharField(max_length=200)
    id_formation = models.ForeignKey(Formations,on_delete=models.CASCADE)
    validation = models.CharField(max_length=20,default='En attente')
    message = models.TextField(default='Pas de Reponse')
    id_utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    #id_admin = models.ForeignKey(Administrateur,on_delete=models.CASCADE)
    date_confirmation = models.DateTimeField(null=True, blank=True)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom)

class Document_important(models.Model):
    nom_document = models.CharField(max_length=100)
    piece_document = models.FileField(upload_to='GESTION/static/document', null=True, blank=True)
    id_admin = models.ForeignKey(Administrateur_g,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_document)

class Projet(models.Model):
    nom_projet = models.CharField(max_length=200)
    description = models.TextField()
    id_admin = models.ForeignKey(Administrateur_g,on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom_projet)

class Salaire(models.Model):
    salaire = models.CharField(max_length=20)
    id_employe = models.ForeignKey(Employes,on_delete=models.CASCADE)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.salaire)

class Demande_client(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    audience = models.DateField(null=True, blank=True)
    validation = models.CharField(max_length=20,default='En attente')
    message = models.TextField(default='Pas de Reponse')
    id_utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    #id_admin = models.ForeignKey(Administrateur,on_delete=models.CASCADE)
    date_confirmation = models.DateTimeField(null=True, blank=True)
    date_add = models.DateTimeField(auto_now=True)

    class Meta():
        """docstring for Meta"""
        ordering=['id']

    def __str__(self):
        return str(self.nom)

class Stage(models.Model):
    TYPE_STAGE_CHOICES = (
        ('academique', 'Stage académique'),
        ('professionnel', 'Stage professionnel'),
    )
    
    ETAT_CHOICES = (
        ('en_attente', 'En attente'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    )
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    type_stage = models.CharField(max_length=20, choices=TYPE_STAGE_CHOICES)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='en_attente')
    #message = models.TextField(default='Pas de Reponse')
    lettre_stage = models.FileField(upload_to='GESTION/static/document', null=True, blank=True ,default='Aucun Fichier a été Envoie')
    date_demande = models.DateTimeField(auto_now_add=True)
    date_confirmation = models.DateTimeField(null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    id_utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.type_stage}"