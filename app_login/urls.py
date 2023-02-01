from django.urls import path
from app_login.views import *
from django.contrib.auth import views as auth_views

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [

    path('', PageLogin, name="PageLogin"),
    path('login/', Login, name="Login"),
    path('Logout/', Logout, name="Logout"),

]