from django import views
from django.urls import path,include
from .views import *
#from account.views import login_user
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name="home"),
    path('TANGU/service',service,name="service"),
    path('TANGU/about',about,name="about"),
    path('TANGU/contact',contact,name="contact"),
    path('TANGU/team',team,name="team"), 
    path('TANGU/developpement',develop,name="develop"),
    path('TANGU/formation',formation,name="formation"), 
    path('TANGU/demande',demande,name="demande"), 
    path('TANGU/audience',audience,name="audience"), 
    path('TANGU/stage',stages,name="stages"),
    path('TANGU/suivi/formation',suivi,name="suivi"),
    path('TANGU/suivi/audience',suivicl,name="suivicl"),
    path('TANGU/suivi/stage',suivie,name="suivie"),
    path('TANGU/suivi/stage/st',sui,name="sui"),
    path('TANGU/profile',profile,name="profile"), 
    path('TANGU/inscrirer',inscrire,name="inscrire"),
    path('TANGU/inscrirer/add',inscrir,name="inscrir"), 
    path('TANGU/connecter',connecte,name="connecte"), 
    path('TANGU/logout',log,name="log"),
    path('TANGU/password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('TANGU/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('TANGU/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('TANGU/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)