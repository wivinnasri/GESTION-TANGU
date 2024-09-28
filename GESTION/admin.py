from django.contrib import admin
from .models import*

admin.site.site_header = "TANGANYIKA GURU"
admin.site.site_title = "TANGANYIKA GURU"
admin.site.index_title = "TANGU"
# Register your models here.

class Administrateur(admin.ModelAdmin):
    list_display = ('user','id','telephone','quartier','ville','pays','CNI','passport','matricule','date_add')
    search_fields=('telephone','quartier','ville','pays','CNI','passport',)

class Employees(admin.ModelAdmin):
    list_display = ('id','nom','prenom','email','telephone','quartier','ville','pays','CNI','passport','id_categories','matricule','id_admin','date_add')
    search_fields=('nom','prenom','email','telephone','quartier','ville','pays','CNI','passport',)

class Categoriese(admin.ModelAdmin):
    list_display = ('id','nom_categories','description')
    search_fields=('nom_categories',)   

class Clientes(admin.ModelAdmin):
    list_display = ('id','nom','prenom','email','telephone','quartier','ville','pays','CNI','id_admin','date_add')
    search_fields=('nom','prenom','email','telephone','quartier','ville','pays','CNI',)

class Stagiaire(admin.ModelAdmin):
    list_display = ('id','nom','prenom','email','telephone','nom_formation','date_debut','date_fin')
    search_fields=('nom','prenom','email','telephone',)

class Projets(admin.ModelAdmin):
    list_display = ('id','nom_projet','description','date_add')
    search_fields=('nom_projet',)

class Contratcl(admin.ModelAdmin):
    list_display = ('id','nom_contrat','code_contrat','lettre_commande','id_client','date_add')
    search_fields=('nom_contrat',)

class Contratempl(admin.ModelAdmin):
    list_display = ('id','nom_contrat','code_contrat','lettre_commande','date_add')
    search_fields=('nom_contrat',)

class Document(admin.ModelAdmin):
    list_display = ('id','nom_document','piece_document','id_admin','date_add')
    search_fields=('nom_document',)

class Formationse(admin.ModelAdmin):
    list_display = ('id','nom_formation','description','payer','centre','domaine','date_debut','date_fin')
    search_fields=('nom_formation',)

class Utilisateurs(admin.ModelAdmin):
    list_display = ('id','user','date_add')

class Demandest(admin.ModelAdmin):
    list_display = ('id','nom','prenom','id_utilisateur','email','telephone','id_formation','validation')
    search_fields=('nom','prenom','validation',)

class Demandecl(admin.ModelAdmin):
    list_display = ('id','nom','prenom','id_utilisateur','email','telephone','audience','message','validation')
    search_fields=('nom','prenom','validation',)

class Salaires(admin.ModelAdmin):
    list_display = ('id','salaire','id_employe')

class Stages(admin.ModelAdmin):
    list_display = ('id','nom','prenom','type_stage','email','telephone','date_demande','date_confirmation','date_debut','date_fin','etat')
    search_fields=('nom','prenom','etat',)

admin.site.register(Administrateur_g,Administrateur)
admin.site.register(Contratemployes,Contratempl)
admin.site.register(Contratclients,Contratcl)
admin.site.register(Clients,Clientes)
admin.site.register(Categories,Categoriese)
admin.site.register(Demande_stagiaire,Demandest)
admin.site.register(Demande_client,Demandecl)
admin.site.register(Document_important,Document)
admin.site.register(Employes,Employees)
admin.site.register(Formations,Formationse)
admin.site.register(Projet,Projets)
admin.site.register(Salaire,Salaires)
admin.site.register(Stagiaires,Stagiaire)
admin.site.register(Utilisateur,Utilisateurs)
admin.site.register(Stage,Stages)