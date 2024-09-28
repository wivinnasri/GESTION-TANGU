from django.shortcuts import redirect,render,get_object_or_404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model, login as new_login, logout as new_logout, authenticate
from GESTION.models import *
from django.contrib import messages
#from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import logging
from django.db.models import Q
import requests
# Create your views here.
def home(request):
    admin_i = Formations.objects.filter(id__lte=5)
    return render(request, "accueil.html", {'admin_i': admin_i})

def service(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def team(request):
    return render(request,"team.html")

def develop(request):
    return render(request,"develop.html")

def profile(request):
    return render(request,"profile.html")

def suivi(request):
    """user_d = request.user
    user_i = get_object_or_404(Utilisateur, user=user_d)
    #user_i = Utilisateur.objects.get(user=user_d)
    demandes = Demande_stagiaire.objects.get(id_utilisateur=user_i)
    #demandes = get_object_or_404(Demande_stagiaire,id_utilisateur=user_i)
    #client=Demande_client.objects.filter(id_utilisateur=user_i)
    #client=get_object_or_404(Demande_client,id_utilisateur=user_i)
    if not demandes:
        message = "Aucune votre demande de formation n'a été trouvée."
    else:
        message = ""
    return render(request,"suivi.html",{'demande':demandes,'user_d':user_d,'message': message})
    """
    user_d = request.user
    user_i = get_object_or_404(Utilisateur, user=user_d)

    try:
        demande = Demande_stagiaire.objects.get(id_utilisateur=user_i)
        demandes = Demande_stagiaire.objects.filter(id_utilisateur=user_i)
    except Demande_stagiaire.DoesNotExist:
        demande = None
        demandes = []

    if demande is None and not demandes:
        message = "Aucune demande de formation n'a été trouvée."
    else:
        message = ""

    return render(request, "suivi.html", {'demande': demande, 'demandes': demandes, 'user_d': user_d, 'message': message})

def suivicl(request):
    """    now = datetime.now()
    date_locale = now.strftime("%Y-%m-%d")
    heure_locale = now.strftime("%H:%M:%S")
    
    # Votre code ici
    
    return render(request, 'votre_template.html', {'date_locale': date_locale, 'heure_locale': heure_locale})
    user_d = request.user
    #user_i = get_object_or_404(Utilisateur, user=user_d)
    user_i = Utilisateur.objects.get(user=user_d)
    #demandes = Demande_stagiaire.objects.filter(id_utilisateur=user_i)
    #demandes = get_object_or_404(Demande_stagiaire,id_utilisateur=user_i)
    #client=Demande_client.objects.get(id_utilisateur=user_i)
    client=get_object_or_404(Demande_client,id_utilisateur=user_i)
    if not client:
        message = "Aucune demande d'une audience n'a été trouvée."
    else:
        message = ""
    return render(request,"suivi.html",{'user_d':user_d,'client':client,'message': message})"""
    """user_d = request.user
    try:
        user_i = Utilisateur.objects.get(user=user_d)
        client = Demande_client.objects.filter(id_utilisateur=user_i)
        if not client:
            message = "Aucune votre demande de rendez-vous n'a été trouvée."
        else:
            message = ""
    except Utilisateur.DoesNotExist:
        user_i = None
        client = None
        message = "Utilisateur introuvable."

    return render(request, "suivicl.html", {'user_d': user_d, 'clients': client, 'message': message})
    """
    user_d = request.user
    user_i = get_object_or_404(Utilisateur, user=user_d)

    try:
        client = Demande_client.objects.get(id_utilisateur=user_i)
        clients = Demande_client.objects.filter(id_utilisateur=user_i)
    except Demande_client.DoesNotExist:
        client = None
        clients = []

    if client is None and not clients:
        message = "Aucune demande de rendez-vous n'a été trouvée."
    else:
        message = ""

    return render(request, "suivicl.html", {'client': client, 'clients': clients, 'user_d': user_d, 'message': message})

def suivie(request):
    user_d = request.user
    user_i = get_object_or_404(Utilisateur, user=user_d)

    try:
        demande = Stage.objects.get(id_utilisateur=user_i)
        demandes = Stage.objects.filter(id_utilisateur=user_i)
    except Stage.DoesNotExist:
        demande = None
        demandes = []

    if demande is None and not demandes:
        message = "Aucune demande de stage n'a été trouvée."
    else:
        message = ""

    return render(request, "sui.html", {'demande': demande, 'demandes': demandes, 'user_d': user_d, 'message': message})

def sui(request):
    user_d = request.user
    user_i = get_object_or_404(Utilisateur, user=user_d)

    try:
        demande = Stage.objects.get(id_utilisateur=user_i)
        demandes = Stage.objects.filter(id_utilisateur=user_i)
    except Stage.DoesNotExist:
        demande = None
        demandes = []

    if demande is None and not demandes:
        message = "Aucune demande de stage n'a été trouvée."
    else:
        message = ""

    return render(request, "sui.html", {'demande': demande, 'demandes': demandes, 'user_d': user_d, 'message': message})

def formation(request):
    admin_i = Formations.objects.filter(id__lte=5)
    item_name = request.GET.get('item_name')

    if item_name and item_name != '':
        admin_i = admin_i.filter(nom_formation__icontains=item_name)

    paginator = Paginator(admin_i, 5)
    page = request.GET.get('page')
    admin_i = paginator.get_page(page)

    context = {
        'admin_i': admin_i
    }

    return render(request, "formation.html", context)

def demande(request):
       if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        
        formation = request.POST.get('formation')

        admin_i = Formations.objects.get(id=formation)
        user_d = request.user
        user_i = get_object_or_404(Utilisateur, user=user_d)

        demande = Demande_stagiaire()
        demande.nom = nom
        demande.prenom = prenom
        demande.email = email
        demande.telephone = telephone
        demande.id_formation = admin_i
        demande.id_utilisateur = user_i
        demande.save()
        messages.success(request,'Vous avez faire un demande de Stage avec succes')
        return redirect('suivi')

        # Code pour sauvegarder la demande dans la base de données
       else:
        admin_i = Formations.objects.all()
        error=messages.error(request,'Impossible de demande un stage verifier bien vos donnees saisie!!')

        return render(request, "demande.html", {'admin_i': admin_i,'error':error})

def audience(request):
       if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        
        user_d = request.user
        user_i = get_object_or_404(Utilisateur, user=user_d)

        demande = Demande_client()
        demande.nom = nom
        demande.prenom = prenom
        demande.email = email
        demande.telephone = telephone
        demande.id_utilisateur = user_i
        demande.save()
        messages.success(request,'Vous avez faire un demande de rendez-vous avec succes')
        return redirect('suivicl')

        # Code pour sauvegarder la demande dans la base de données
       else:
        error=messages.error(request,'Impossible de demande un rendez-vous verifier bien vos donnees saisie!!')

        return render(request, "audience.html",{'error':error})

def stages(request):
       if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        type_stage = request.POST['type_stage']
        lettre = request.FILES['lettre']
        
        user_d = request.user
        user_i = get_object_or_404(Utilisateur, user=user_d)

        demande = Stage()
        demande.nom = nom
        demande.prenom = prenom
        demande.email = email
        demande.telephone = telephone
        demande.type_stage=type_stage
        demande.lettre_stage=lettre
        demande.id_utilisateur = user_i
        demande.save()
        messages.success(request,'Vous avez faire un demande de stage avec succes')
        return redirect('suivie')

        # Code pour sauvegarder la demande dans la base de données
       else:
        error=messages.error(request,'Impossible de demande un rendez-vous verifier bien vos donnees saisie!!')

        return render(request, "stages.html",{'error':error})

def inscrire(request):
    return render(request,"inscrire.html")

def inscrir(request):
	if request.method == 'POST':
		nom = request.POST.get('nom')
		prenom = request.POST.get('prenom')
		name = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')

		user=User.objects.create_user(first_name=nom,last_name=prenom,username=name,email=email,password=password)

		pade= Utilisateur(user=user)
		pade.save()
        
		new_login(request,user)
		return redirect('home')

	return render(request,"inscrire.html")
          
def connecte(request):
    """if request.method == 'POST':
        email = request.POST.get('email')
        passworde = request.POST.get('password')
       # donnee = (email1,password)
        #adm = get_object_or_404(Administrateur_g)
       # user = Administrateur_g.objects.filter(email=email).first()
        user = authenticate(request,email=email,password=passworde)
        if user is not None:
        # Comparaison des champs pour l'authentification
            authe=Utilisateur.objects.get(user=user)
            new_login(request,authe)
            messages.success(request,'Welcome back')
            return redirect('home')
        else:
            messages.error(request,'Username ou le Mot de passe n\'est pas correcte!!')
            return redirect('connecte')
            #return HttpResponse("Username ou le Mot de passe n'est pas correcte!!")
        #else:
           # return render(request,'login.html',{'error':'Invalid email ou mot de passe'})
    return render(request,"connecter.html")"""
    """if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Vérifier les informations d'identification de l'utilisateur
        try:
            utilisateur = Utilisateur.objects.get(user__email=email)
        except Utilisateur.DoesNotExist:
            utilisateur = None

        if utilisateur is not None:
            user = utilisateur.user

            # Authentifier l'utilisateur
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                # Connecter l'utilisateur
                new_login(request, user)
                messages.success(request, 'Welcome back')
                return redirect('home')

        messages.error(request, 'Email ou mot de passe incorrect!')
        return redirect('connecte')

    return render(request, 'connecter.html')"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authentifier l'utilisateur
        user = Utilisateur.objects.filter(user__email=email).first()
        if user is not None and user.user.check_password(password):
            # Connecter l'utilisateur
            auth_user = authenticate(request, username=user.user.username, password=password)
            if auth_user is not None:
                new_login(request, auth_user)
                messages.success(request, 'Welcome back')
                return redirect('home')

        messages.error(request, 'Email ou mot de passe incorrect!')
        return redirect('connecte')

    return render(request, 'connecter.html')

def log(request):
    new_logout(request)
    return redirect('connecte')