from django.urls import path
from SCOOLAPP.views import *

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [

    path('acceuilAdmin/', acceuilAdmin, name="acceuilAdmin"),

    path('GetdatasClasses/', GetdatasClasses, name="GetdatasClasses"),
    path('classes/', ViewsClasses, name="ViewsClasses"),
    path('classes/FormAddClasses/', FormAddClasses, name="FormAddClasses"),
    path('classes/AddnewClasse/', AddnewClasse, name="AddnewClasse"),
    path('classes/SearchClassesToModif/', SearchClassesToModif, name="SearchClassesToModif"),
    path('classes/SearchClassesToDelete/', SearchClassesToDelete, name="SearchClassesToDelete"),
    path('classes/SearchClassesForAbout/', SearchClassesForAbout, name="SearchClassesForAbout"),

    path('GetdatasProfs/', GetdatasProfs, name="GetdatasProfs"),
    path('Professeurs/', ViewsProfs, name="ViewsProfs"),
    path('Professeurs/FormAddProfs/', FormAddProfs, name="FormAddProfs"),
    path('Professeurs/AddnewProf/', AddnewProf, name="AddnewProf"),
    path('Professeurs/SearchProfsToModif/', SearchProfsToModif, name="SearchProfsToModif"),
    path('Professeurs/SearchProfsToDelete/', SearchProfsToDelete, name="SearchProfsToDelete"),
    path('Professeurs/SearchProfsForAbout/', SearchProfsForAbout, name="SearchProfsForAbout"),


    path('GetdatasCours/', GetdatasCours, name="GetdatasCours"),
    path('cours/', ViewsCours, name="ViewsCours"),
    path('cours/FormAddCours/', FormAddCours, name="FormAddCours"),
    path('cours/AddnewCours/', AddnewCours, name="AddnewCours"),
    path('cours/SearchCoursToModif/', SearchCoursToModif, name="SearchCoursToModif"),
    path('cours/SearchCoursToDelete/', SearchCoursToDelete, name="SearchCoursToDelete"),
    path('cours/SearchCoursForAbout/', SearchCoursForAbout, name="SearchCoursForAbout"),


    path('GetdatasEleves/', GetdatasEleves, name="GetdatasEleves"),
    path('Eleves/', ViewsEleves, name="ViewsEleves"), 
    path('Eleves/FormAddEleve/', FormAddEleve, name="FormAddEleve"),
    path('Eleves/AddnewEleve/', AddnewEleve, name="AddnewEleve"),
    path('Eleves/SearchElevesToModif/', SearchElevesToModif, name="SearchElevesToModif"),
    path('Eleves/SearchElevesToDelete/', SearchElevesToDelete, name="SearchElevesToDelete"),
    path('Eleves/SearchElevesForAbout/', SearchElevesForAbout, name="SearchElevesForAbout"),


    path('VoirProfileAdmin/', VoirProfileAdmin, name="VoirProfileAdmin"),
    path('ModifProfileAdmin/', ModifProfileAdmin, name="ModifProfileAdmin"),
    path('ModifCompteAdmin/', ModifCompteAdmin, name="ModifCompteAdmin"),




]