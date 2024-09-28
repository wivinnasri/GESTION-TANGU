from django.shortcuts import redirect,render,get_object_or_404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model, login as new_login, logout as new_logout, authenticate
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import logging
from django.db.models import Q,F
from datetime import datetime,date,timedelta
from django.utils import timezone

#Administrateur_g = get_user_model()
# Create your views here.
@login_required(login_url='login')
def index(request):
    user_d = request.user
    if Administrateur_g.objects.filter(user=user_d).exists():
        admin_i = Administrateur_g.objects.get(user=user_d)
        if admin_i.user.is_superuser:
            return redirect('login')
        else:
            formation = Formations.objects.count()
            client = Clients.objects.all().count()
            employe = Employes.objects.all().count()
            stagiaire = Stagiaires.objects.all().distinct().count()
            clients = Clients.objects.filter(id__lte=10)
            declients = Demande_client.objects.filter(id__lte=10)
            context = {
                'form': formation,
                'clie': client,
                'empl': employe,
                'stag': stagiaire,
                'client': clients,
                'de':declients,
            }
            return render(request, "index.html", context)
    else:
        return redirect('login')
    """user_d = request.user
    try:
        admin_i = Administrateur_g.objects.get(user=user_d)
        if admin_i.user.is_superuser:
            return redirect('login')
    except Administrateur_g.DoesNotExist:
        return redirect('login')

    formation = Formations.objects.count()
    client = Clients.objects.all().count()
    employe = Employes.objects.all().count()
    stagiaire = Stagiaires.objects.all().distinct().count()
    clients = Clients.objects.filter(id__lte=10)
    context = {
        'form': formation,
        'clie': client,
        'empl': employe,
        'stag': stagiaire,
        'client': clients,
    }
    return render(request, "index.html", context)
   user_d = request.user
   
    if user_d:
        admin_i=get_object_or_404(Administrateur_g,user=request.user)
    #admin_i=get_object_or_404(Administrateur_g,user=request.user)
        if admin_i.user.is_superuser:
            return redirect('login')
    else:
        admin_i=get_object_or_404(Administrateur_g,user=request.user)
        if admin_i.user.is_authenticated:
            formation = Formations.objects.count()
            client = Clients.objects.all().values_list('id', flat=True).count()
            employe = Employes.objects.all().values_list('id', flat=True).count()
            stagiaire = Stagiaires.objects.all().distinct().count()
            clients = Clients.objects.filter(id__lte=10)
            context ={
                'form':formation,
                'clie':client,
                'empl':employe,
                'stag':stagiaire,
                'client':clients,
            }
            return render(request,"index.html",context)
    return redirect('login')"""

def formations(request):
    admin_i=Formations.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        #admin_i = Employes.objects.filter(nom__icontains=item_name)
        admin_i = Formations.objects.filter(nom_formation__icontains=item_name)
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    return render(request,"formations.html",{'formation':admin_i})

def formationsadd(request):
    return render(request,"formationsadd.html")

def formationsad(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        centre = request.POST.get('centre')
        domaine = request.POST.get('domaine')
        payer = request.POST.get('payer')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Formations()

        admin.nom_formation = nom
        admin.description = description
        admin.centre = centre
        admin.domaine = domaine
        admin.payer = payer
        admin.date_debut = date_debut
        admin.date_fin = date_fin
        admin.save()
        messages.success(request,'Vous avez ajouter un formation avec succes')
        
        return redirect('formations')
    else:
        messages.error(request,'Impossible d\'ajouter un\'formation verifier bien vos donnees saisie!!')
        return redirect('formationsadd')

def formate(request,id):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        centre = request.POST.get('centre')
        domaine = request.POST.get('domaine')
        payer = request.POST.get('payer')

        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Formations.objects.get(id=id)

        admin.nom_formation = nom
        admin.description = description
        admin.centre = centre
        admin.domaine = domaine
        admin.payer = payer
        if 'date_debut' in request.POST and request.POST['date_debut']:
            admin.date_debut = request.POST.get('date_debut')
        if 'date_fin' in request.POST and request.POST['date_fin']:
            admin.date_fin = request.POST.get('date_fin')
        admin.save()
        
        return redirect('formations')
    else:
        admin_i=Formations.objects.get(id=id)
        return render(request,"formate.html",{'admin_i':admin_i})
    
def formad(request,id):
    admin_i=Formations.objects.get(id=id)
    admin_i.delete()
    return redirect('formations')

def employes(request):  
    employe = Employes.objects.filter(id__lte=10)
    ca_form= Categories.objects.filter(nom_categories__in=["Formateur"]).values_list('id', flat=True)
    ca_ing= Categories.objects.filter(nom_categories__in=["ING en Logiciel"]).values_list('id', flat=True)
    ca_mai= Categories.objects.filter(nom_categories__in=["Maintenance"]).values_list('id', flat=True)
    ca_ingr= Categories.objects.filter(nom_categories__in=["ING en Reseaux"]).values_list('id', flat=True)
    somme_form = Employes.objects.filter(id_categories__in=ca_form).distinct().count()
    somme_ing = Employes.objects.filter(id_categories__in=ca_ing).distinct().count()
    somme_mai = Employes.objects.filter(id_categories__in=ca_mai).distinct().count()
    somme_ingr = Employes.objects.filter(id_categories__in=ca_ingr).distinct().count()
    context ={
        'empl':employe,
        'categorie':ca_form,
        's_form':somme_form,
        's_ing':somme_ing,
        's_mai':somme_mai,
        's_ingr':somme_ingr,
    }
    return render(request,"employes.html",context)

def employesv(request):
    admin_i=Employes.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        #admin_i = Employes.objects.filter(nom__icontains=item_name)
        admin_i = Employes.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name) | Q(ville__icontains=item_name) | Q(pays__icontains=item_name))
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    return render(request,"employesv.html",{'admin_i':admin_i})

def employesadd(request):
    user_d = request.user
    admin_i=Administrateur_g.objects.get(user=user_d)
    categories= Categories.objects.all()
    return render(request,"employesadd.html",{'categories':categories,'admin_i':admin_i})

def employesad(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quartier = request.POST.get('quartier')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        cni = request.POST.get('cni')
        passport = request.POST.get('passport')
        photo = request.FILES['photo']
        piece = request.FILES['piece']
        categorie = request.POST.get('categories')
        admin_id = request.POST.get('admin_id') 
        
        admin_i=get_object_or_404(Administrateur_g,user=request.user)
        categories=Categories.objects.get(id=categorie)

        admin=Employes()

        admin.nom = nom
        admin.prenom = prenom
        admin.email = email
        admin.telephone = telephone
        admin.quartier = quartier
        admin.ville = ville
        admin.pays = pays
        admin.CNI = cni
        admin.passport = passport
        admin.photo_profil = photo
        admin.piece_identite = piece
        admin.id_categories = categories
        admin.id_admin = admin_i
        admin.save()
        messages.success(request,'Vous avez ajouter un employe avec succes')
        
        return redirect('employesv')
    else:
        messages.error(request,'Impossible d\'ajouter un\'employe verifier bien vos donnees saisie!!')
        return redirect('employesadd')

def emplv(request,id):
    admin_i=Employes.objects.get(id=id)
    return render(request,"emplv.html",{'admin_i':admin_i})

def emple(request,id):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quartier = request.POST.get('quartier')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        cni = request.POST.get('cni')
        passport = request.POST.get('passport')
        selected_category_id = request.POST.get('categories')
        admin = Employes.objects.get(id=id) 
                
        user_d=request.user
        admin_i=get_object_or_404(Administrateur_g,user=user_d)
        #categories=Categories.objects.get(id=categorie)

        admin.nom = nom
        admin.prenom = prenom
        admin.email = email
        admin.telephone = telephone
        admin.quartier = quartier
        admin.ville = ville
        admin.pays = pays
        admin.CNI = cni
        admin.passport = passport
        if 'photo' in request.FILES and request.FILES['photo']:
            admin.photo_profil = request.FILES['photo']
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.piece_identite = request.FILES['piece']
        
        
        if selected_category_id:
           selected_category = Categories.objects.get(id=selected_category_id)
           admin.id_categories = selected_category
        admin.id_admin = admin_i
        admin.save()
        return redirect('employesv')
    else:
        admin_i=Employes.objects.get(id=id)
        categories= Categories.objects.all()
        return render(request,"emple.html",{'admin_i':admin_i,'categories':categories})

def empld(request,id):
    admin_i=Employes.objects.get(id=id)
    admin_i.delete()
    return redirect('employesv')

def clients(request):
    admin_i=Clients.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Clients.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name) | Q(nom_entreprise__icontains=item_name) | Q(cni__icontains=item_name) | Q(code_NIF__icontains=item_name))
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    return render(request,"clients.html",{'admin_i':admin_i})

def clientsadd(request):
    return render(request,"clientsadd.html")

def clientsad(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        nom_entreprise = request.POST.get('nom_entreprise')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quartier = request.POST.get('quartier')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        cni = request.POST.get('cni')
        code_nif = request.POST.get('code_nif')
        photo = request.FILES['photo']
        piece = request.FILES['piece']
        #admin_id = request.POST.get('admin_id') 
        
        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Clients()

        admin.nom = nom
        admin.prenom = prenom
        admin.nom_entreprise = nom_entreprise
        admin.email = email
        admin.telephone = telephone
        admin.quartier = quartier
        admin.ville = ville
        admin.pays = pays
        admin.CNI = cni
        admin.code_NIF = code_nif
        admin.photo_profil = photo
        admin.piece_identite = piece
        #admin.id_categories = categories
        admin.id_admin = admin_i
        admin.save()
        messages.success(request,'Vous avez ajouter un client avec succes')
        
        return redirect('clients')
    else:
        messages.error(request,'Impossible d\'ajouter un\'client verifier bien vos donnees saisie!!')
        return redirect('clientsadd')

def clientv(request,id):
    admin_i=Clients.objects.get(id=id)
    return render(request,"clientsv.html",{'admin_i':admin_i})

def cliente(request,id):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        nom_e= request.POST.get('nom_entreprise')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quartier = request.POST.get('quartier')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        cni = request.POST.get('cni')
        passport = request.POST.get('code_nif')
        selected_category_id = request.POST.get('categories')
        admin = Clients.objects.get(id=id) 
                
        user_d=request.user
        admin_i=get_object_or_404(Administrateur_g,user=user_d)
        #categories=Categories.objects.get(id=categorie)

        admin.nom = nom
        admin.prenom = prenom
        admin.nom_entreprise = nom_e
        admin.email = email
        admin.telephone = telephone
        admin.quartier = quartier
        admin.ville = ville
        admin.pays = pays
        admin.CNI = cni
        admin.code_NIF = passport
        if 'photo' in request.FILES and request.FILES['photo']:
            admin.photo_profil = request.FILES['photo']
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.piece_identite = request.FILES['piece']

        admin.id_admin = admin_i
        admin.save()
        return redirect('clients')
    else:
        admin_i=Clients.objects.get(id=id)
        return render(request,"clientse.html",{'admin_i':admin_i})

def clientd(request,id):
    admin_i=Clients.objects.get(id=id)
    admin_i.delete()
    return redirect('clients')

def stagiaires(request):
    admin_i=Stagiaires.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Stagiaires.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name) | Q(email__icontains=item_name) | Q(telephone__icontains=item_name))
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    return render(request,"stagiaires.html",{'admin_i':admin_i})

def stagiairesadd(request):
    user_d = request.user
    admin_i=Administrateur_g.objects.get(user=user_d)
    formations= Formations.objects.all()
    return render(request,"stagiairesadd.html",{'formations':formations})

def stagiairesad(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        #date_debut = request.POST.get('date_debut')
        #date_fin = request.POST.get('date_fin')
        formation = request.POST.get('formation') 
        
        admin_i=get_object_or_404(Administrateur_g,user=request.user)
        formations=Formations.objects.get(id=formation)

        admin=Stagiaires()

        admin.nom = nom
        admin.prenom = prenom
        admin.email = email
        admin.telephone = telephone
        admin.date_debut = formations.date_debut
        admin.date_fin = formations.date_fin
        admin.nom_formation = formations
        admin.id_admin = admin_i
        admin.save()
        messages.success(request,'Vous avez ajouter un stagiaire avec succes')
        
        return redirect('stagiaires')
    else:
        messages.error(request,'Impossible d\'ajouter un\'stagiaire verifier bien vos donnees saisie!!')
        return redirect('stagiairesadd')

def archivres(request):
    contr = Contratclients.objects.count()
    contrat = Contratemployes.objects.all().values_list('id', flat=True).count()
    doc = Document_important.objects.all().values_list('id', flat=True).count()
    admin_i=Projet.objects.all()
    salaire = Salaire.objects.count()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Projet.objects.filter(nom_projet__icontains=item_name)
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    context ={
        'contrat':contr,
        'contrats':contrat,
        'document':doc,
        'admin_i':admin_i,
        'salaire':salaire,
    }
    return render(request,"archivres.html",context)

def salaire(request):
    employes = Employes.objects.all()
    salaires = Salaire.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        employes = Employes.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name))
    
    paginator = Paginator(employes, 5)
    page = request.GET.get('page')
    employes= paginator.get_page(page)
    context = {
        'employes': employes,
        'salaires': salaires
    }
    return render(request,"salaire.html",context)

def sj(request):
    employe=request.POST.get('employe')
    employes = Employes.objects.get(id=employe)
    salaires=Salaire(id_employe=employes, salaire=request.POST.get('salaire'))
    salaires.save()
    return redirect('salaire')

def se(request,id):
    if request.method == 'POST':
        #employe=request.POST.get('employe')
        salaire=request.POST.get('salaire')
        employes = Employes.objects.get(id=id)
        salaires=Salaire.objects.get(id_employe=employes)
        salaires.salaire=salaire
        salaires.save()
        return redirect('salaire')
    else:
        employes = Employes.objects.get(id=id)
        salaires = Salaire.objects.get(id_employe=employes)
        return render(request,"sj.html",{'salaire':salaires,'employe':employes})

def sd(request,id):
    employes = Employes.objects.get(id=id)
    salaires = Salaire.objects.get(id_employe=employes)
    salaires.delete()
    return redirect('salaire')

def projet(request):
    return render(request,"projet.html")

def projetadd(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')

        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Projet()

        admin.nom_projet = nom
        admin.description = description
        admin.id_admin = admin_i
        admin.save()
        messages.success(request,'Vous avez ajouter un projet avec succes')
        
        return redirect('archivres')
    else:
        messages.error(request,'Impossible d\'ajouter un\'projet verifier bien vos donnees saisie!!')
        return redirect('projetadd')
    
def projete(request,id):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('desc')
        admin = Projet.objects.get(id=id) 
                
        user_d=request.user
        admin_i=get_object_or_404(Administrateur_g,user=user_d)
        #categories=Categories.objects.get(id=categorie)

        admin.nom_projet = nom
        admin.description= prenom
 
        admin.id_admin = admin_i
        admin.save()
        return redirect('archivres')
    else:
        admin_i=Projet.objects.get(id=id)
        return render(request,"projete.html",{'admin_i':admin_i})

def projetd(request,id):
    admin_i=Projet.objects.get(id=id)
    admin_i.delete()
    return redirect('archivres')

def documents(request):
    admin_i=Document_important.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Document_important.objects.filter(nom_document__icontains=item_name)
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    context ={
        'admin_i':admin_i,
    }
    return render(request,"documents.html",context)

def document(request):
    return render(request,"documentsadd.html")

def documentsadd(request):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        description = request.FILES['piece']

        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Document_important()

        admin.nom_document = nom
        admin.piece_document = description
        admin.id_admin = admin_i
        admin.save()
        messages.success(request,'Vous avez ajouter un document avec succes')
        
        return redirect('documents')
    else:
        messages.error(request,'Impossible d\'ajouter un\'document verifier bien vos donnees saisie!!')
        return redirect('documentsadd')

def doc(request,id):

    user_d = request.user

    if request.method =='POST':
        nom = request.POST.get('nom')
        #description = request.FILES['piece']

        admin_i=get_object_or_404(Administrateur_g,user=request.user)

        admin=Document_important.objects.get(id=id)

        admin.nom_document = nom
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.piece_document = request.FILES['piece']
        admin.id_admin = admin_i
        admin.save()
        
        return redirect('documents')
    else:
        admin=Document_important.objects.get(id=id)
        return render(request,'doc.html',{'admin':admin})

def contratclients(request):
    admin_i = Contratclients.objects.all()
    client= Clients.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Contratclients.objects.filter(nom_contrat__icontains=item_name)
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    context ={
        'admin_i':admin_i,
        'client':client,
    }
    return render(request,"contratsclients.html",context)

def contratclientsadd(request):
    client= Clients.objects.all()
    return render(request,"contratsclientsadd.html",{'clients':client})

def contratclientsad(request):
    if request.method =='POST':
        nom = request.POST.get('nom')
        code = request.POST.get('code')
        piece = request.FILES['piece']
        nom_id = request.POST.get('client')

        admin_ir = Clients.objects.get(id=nom_id)

        admin=Contratclients()

        admin.nom_contrat = nom
        admin.code_contrat = code
        admin.lettre_commande = piece
        admin.id_client = admin_ir
        admin.save()
        messages.success(request,'Vous avez ajouter un Contrat du client avec succes')
        
        return redirect('contratclients')
    else:
        messages.error(request,'Impossible d\'ajouter un contrat du client verifier bien vos donnees saisie!!')
        return redirect('contratclientsadd')

def contrats(request,id):
    if request.method =='POST':
        nom = request.POST.get('nom')
        code = request.POST.get('code')
        nom_id = request.POST.get('employe')

        #admin_ir =Employes.objects.get(id=nom_id)

        admin=Contratclients.objects.get(id=id)

        admin.nom_contrat = nom
        admin.code_contrat = code
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.lettre_commande = request.FILES['piece']
        admin.save()
        
        return redirect('contratclients')
    else:
        admin=Contratclients.objects.get(id=id)
        return render(request,'contrats.html',{'admin':admin})

def contratemployes(request):
    admin_i = Contratemployes.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        admin_i = Contratemployes.objects.filter(nom_contrat__icontains=item_name)
    
    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i= paginator.get_page(page)
    context ={
        'admin_i':admin_i,
    }
    return render(request,"contratsemployes.html",context)

def contratemployesadd(request):
    employe= Employes.objects.all()
    return render(request,"contratsemployesadd.html",{'employes':employe})

def contratemployesad(request):
    if request.method =='POST':
        nom = request.POST.get('nom')
        code = request.POST.get('code')
        piece = request.FILES['piece']
        nom_id = request.POST.get('employe')

        admin_ir = Employes.objects.get(id=nom_id)

        admin=Contratemployes()

        admin.nom_contrat = nom
        admin.code_contrat = code
        admin.lettre_commande = piece
        admin.id_employe = admin_ir
        admin.save()
        messages.success(request,'Vous avez ajouter un Contrat d\'un employe avec succes')
        
        return redirect('contratemployes')
    else:
        messages.error(request,'Impossible d\'ajouter un contrat d\'un employe verifier bien vos donnees saisie!!')
        return redirect('contratemployesadd')

def contrate(request,id):
    if request.method =='POST':
        nom = request.POST.get('nom')
        code = request.POST.get('code')
        nom_id = request.POST.get('employe')

        #admin_ir =Employes.objects.get(id=nom_id)

        admin=Contratemployes.objects.get(id=id)

        admin.nom_contrat = nom
        admin.code_contrat = code
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.lettre_commande = request.FILES['piece']
        admin.save()
        
        return redirect('contratemployes')
    else:
        admin=Contratemployes.objects.get(id=id)
        return render(request,'contrate.html',{'admin':admin})
    
def demandes(request):
    demande = Demande_stagiaire.objects.filter(id__lte=10)
    dst = Demande_stagiaire.objects.all().values_list('id', flat=True).count()
    doc = Demande_client.objects.all().values_list('id', flat=True).count()
    doce = Stage.objects.all().values_list('id', flat=True).count()
    context ={
        'demandes':demande,
        'dsta':dst,
        'client':doc,
        'doce':doce,
    }
    return render(request,"demandes.html",context)

def demandest(request):
    demande = Demande_stagiaire.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        demande = Demande_stagiaire.objects.filter(nom__icontains=item_name)
    
    paginator = Paginator(demande, 5)
    page = request.GET.get('page')
    demande= paginator.get_page(page)
    context ={
        'demandes':demande,
    }
    return render(request,"demandesstagiaires.html",context)

def accepterst(request,id):
    demande = Demande_stagiaire.objects.get(id=id)
    formations=Formations.objects.get(nom_formation=demande.id_formation)

    demande.validation='Accepte'
    demande.date_confirmation = datetime.now()
    demande.message='Votre Demande a ete accepte.Et il faut que vous presentez a la siege de faire la formation et que vous devez payez le formation avant premier jour'
    demande.save()
     
    #date=demande.id_formation
    #formations=Formations.objects.get()
    user_d= request.user
    admin_i=get_object_or_404(Administrateur_g,user=request.user)

    admin=Stagiaires()
    admin.nom=demande.nom
    admin.prenom=demande.prenom
    admin.email=demande.email
    admin.telephone=demande.telephone
    admin.nom_formation=demande.id_formation
    admin.date_debut=formations.date_debut
    admin.date_fin=formations.date_fin
    admin.id_admin=admin_i
    admin.save()
    return redirect('demandest')

def refuserst(request,id):
    demande = Demande_stagiaire.objects.get(id=id)
    demande.validation='Refuse'
    demande.date_confirmation = datetime.now()
    demande.message='Votre Demande a ete refuse.Motif: Nous sommes desole pour vous informez que vous n\'avez pas accepter:Et qu\' il faut encore tente votre chance.'
    demande.save()
    return redirect('demandest')

def demandecl(request):
    demande = Demande_client.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        demande = Demande_client.objects.filter(nom__icontains=item_name)
    
    paginator = Paginator(demande, 5)
    page = request.GET.get('page')
    demande= paginator.get_page(page)
    context ={
        'demandes':demande,
    }
    return render(request,"demandesclients.html",context)

def acceptercl(request,id):
    demande = Demande_client.objects.get(id=id)
    
    period_start = timezone.now()
    period_end = period_start + timedelta(days=7, hours=3)
    demande.validation='Accepte'
    demande.audience=period_end
    demande.date_confirmation = datetime.now()
    demande.message='Votre Rendez-Vous a ete accepte.Et il faut que vous presentez a la siege dans la date donnee'
    demande.save()
     
    #date=demande.id_formation
    #formations=Formations.objects.get()
    """user_d= request.user
    admin_i=get_object_or_404(Administrateur_g,user=request.user)

    admin=()
    admin.nom=demande.nom
    admin.prenom=demande.prenom
    admin.email=demande.email
    admin.telephone=demande.telephone
    admin.id_formation=demande.id_formation
    admin.date_debut=formations.date_debut
    admin.date_fin=formations.date_fin
    admin.id_admin=admin_i
    admin.save()"""
    return redirect('demandecl')

def refusercl(request,id):
    demande = Demande_client.objects.get(id=id)
    demande.validation='Refuse'
    demande.date_confirmation = datetime.now()
    demande.message='Votre Demande de Rendez-vous a ete annulé.Nous sommes desole pour vous il faut encore demande le rendez vous'
    demande.save()
    return redirect('demandecl')

def demandesa(request):
    demande = Stage.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        demande = Stage.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name) | Q(etat__icontains=item_name) | Q(type_stage__icontains=item_name))
    
    paginator = Paginator(demande, 5)
    page = request.GET.get('page')
    demande= paginator.get_page(page)
    context ={
        'demandes':demande,
    }
    return render(request,"demandestage.html",context)

def acceptersa(request,id):
    demande = Stage.objects.get(id=id)
    #formations=Formations.objects.get(nom_formation=demande.id_formation)
    demande.etat='accepte'
    demande.date_confirmation = datetime.now()
    if demande.type_stage == 'professionnel':
       period = timezone.now()
       period_start = period + timedelta(days=15)
       period_end = period_start + timedelta(days=186)
       demande.date_debut=period_start
       demande.date_fin=period_end
    else:
       period = timezone.now()
       period_start = period + timedelta(days=16)
       period_end = period_start + timedelta(days=31)
       demande.date_debut=period_start
       demande.date_fin=period_end
    
    #demande.message='Votre Demande a ete accepte.Et il faut que vous presentez a la siege de faire la formation'
    demande.save()
     
    #date=demande.id_formation
    #formations=Formations.objects.get()
    user_d= request.user
    admin_i=get_object_or_404(Administrateur_g,user=request.user)
    return redirect('demandesa')

def refusersa(request,id):
    demande = Stage.objects.get(id=id)
    demande.etat='refuse'
    demande.date_confirmation = datetime.now()
    #demande.message='Votre Demande de Rendez-vous a ete annulé.Nous sommes desole pour vous il faut encore demande le rendez vous'
    demande.save()
    return redirect('demandesa')

def stage(request):
    demande = Stage.objects.filter(etat='accepte')
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        demande = Stage.objects.filter(Q(nom__icontains=item_name) | Q(prenom__icontains=item_name) | Q(etat__icontains=item_name) | Q(type_stage__icontains=item_name))
    
    paginator = Paginator(demande, 5)
    page = request.GET.get('page')
    demande= paginator.get_page(page)
    context ={
        'demandes':demande,
    }
    return render(request,"stage.html",context)

def comptes(request):
    user_d= request.user
    admin=Administrateur_g.objects.get(user=user_d)
    user= admin.user
    context = {
        'user':user,
        'admin':admin,
    }
    return render(request,'comptes.html',context)

def visualiserc(request,id):
    
    user_d= request.user
    #u= User.objects.get(pk=id)
    admin=Administrateur_g.objects.get(user=user_d)
    user= admin.user
    context = {
        'user':user,
        'admin':admin,
        #'administrateur': 'administateur',
    }
    return render(request,'visualiser.html',context)

def editerc(request,id):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        username = request.POST.get('username')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quartier = request.POST.get('quartier')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        cni = request.POST.get('cni')
        passport = request.POST.get('passport')
        #photo = request.FILES['photo']
        #ph = request.FILES['photo1']
        #piece = request.FILES['piece']
        #p = request.FILES['piece1']
        #user_i = User(username=username,email=email,first_name=nom,last_name=prenom)
        #admin_i = Administrateur_g(telephone=telephone,quartier=quartier,ville=ville,pays=pays,CNI=cni,passport=passport,photo_profil=photo,piece_identite=piece,user=user_d)
        user = User.objects.get(id=id) 
        #user_d = request.user
        admin=Administrateur_g.objects.get(user=user)
        #user= admin.user

        user.username = username
        user.email = email
        user.first_name = nom
        user.last_name = prenom

        user.save()

        admin.telephone = telephone
        admin.quartier = quartier
        admin.ville = ville
        admin.pays = pays
        admin.CNI = cni
        admin.passport = passport
        if 'photo' in request.FILES and request.FILES['photo']:
            admin.photo_profil = request.FILES['photo']
        if 'piece' in request.FILES and request.FILES['piece']:
            admin.piece_identite = request.FILES['piece']
        
        admin.user = request.user

        admin.save()
        return redirect('comptes')
    else:
        user_d= request.user
        #u= User.objects.get(pk=id)
        admin=Administrateur_g.objects.get(user=user_d)
        user= admin.user
        context = {
            'user':user,
            'admin':admin,
        #'administrateur': 'administateur',
        }
    return render(request,'editc.html',context)
    
#def editerci(request,id):
   
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passworde = request.POST.get('password')
       # donnee = (email1,password)
        #adm = get_object_or_404(Administrateur_g)
       # user = Administrateur_g.objects.filter(email=email).first()
        user = authenticate(request,username=email,password=passworde)
        if user is not None:
        # Comparaison des champs pour l'authentification
            new_login(request,user)
            messages.success(request,'Welcome back')
            return redirect('index')
        else:
            messages.error(request,'Username ou le Mot de passe n\'est pas correcte!!')
            return redirect('index')
            #return HttpResponse("Username ou le Mot de passe n'est pas correcte!!")
        #else:
           # return render(request,'login.html',{'error':'Invalid email ou mot de passe'})
        
    return render(request,'login.html')

def logout(request):
    new_logout(request)
    return redirect('login')