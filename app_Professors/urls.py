from django.urls import path
from app_Professors.views import *

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [

    path('acceuilProf/', acceuilProf, name="acceuilProf"),

    path('VoirMesEleves/', VoirMesEleves, name="VoirMesEleves"),

    path('VoirMesClasses/', VoirMesClasses, name="VoirMesClasses"),

    path('VoirMesCours/', VoirMesCours, name="VoirMesCours"),

    path('VoirProfile/', VoirProfile, name="VoirProfile"),

    path('api/details_Eleve_Prof<int:idElev>', details_Eleve_Prof, name="details_Eleve_Prof"),
    path('api/details_Cours_Prof<int:idMat>', details_Cours_Prof, name="details_Cours_Prof"),
    path('api/details_Classe_Prof<int:idClass>', details_Classe_Prof, name="details_Classe_Prof"),

    path('ModifProfileProf/', ModifProfileProf, name="ModifProfileProf"),
    path('ModifCompteProf/', ModifCompteProf, name="ModifCompteProf"),
]