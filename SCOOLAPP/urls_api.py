from django.urls import path
from SCOOLAPP.views import *

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [
    path('Classe/<int:idClass>', details_Classe, name="details_Classe"),
    path('classes/ModifierClasse/<int:idClass>', ModifierClasse, name="ModifierClasse"),
    path('classes/GetdatasClassesbyidp/<int:idClass>', GetdatasClassesbyidp, name="GetdatasClassesbyidp"),
    path('classes/AddModifsClasse/<int:idClass>', AddModifsClasse, name="AddModifsClasse"),

    path('Professeur/<int:idProf>', details_Prof, name="details_Prof"),
    path('Professeur/ModifierProf/<int:idProf>', ModifierProf, name="ModifierProf"),
    path('Professeur/GetdatasProfsbyidp/<int:idProf>', GetdatasProfsbyidp, name="GetdatasProfsbyidp"),
    path('Professeur/AddModifsProf/<int:idProf>', AddModifsProf, name="AddModifsProf"),

    path('Eleves/ModifierEleves/<int:idElev>', ModifierElev, name="ModifierElev"),

    

]