from django.urls import path
from SCOOLAPP.views import *

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [
    
    path('classes/GetdatasClassesbyidp/<int:idClass>', GetdatasClassesbyidp, name="GetdatasClassesbyidp"),
    path('classes/ModifierClasse/<int:idClass>', ModifierClasse, name="ModifierClasse"),
    path('classes/AddModifsClasse/<int:idClass>', AddModifsClasse, name="AddModifsClasse"),
    path('classes/deleteClasse/<int:idClass>', deleteClasse, name="deleteClasse"), 
    path('classes/details_Classe/<int:idClass>', details_Classe, name="details_Classe"),


    path('Professeur/GetdatasProfsbyidp/<int:idProf>', GetdatasProfsbyidp, name="GetdatasProfsbyidp"),
    path('Professeur/ModifierProf/<int:idProf>', ModifierProf, name="ModifierProf"),
    path('Professeur/AddModifsProf/<int:idProf>', AddModifsProf, name="AddModifsProf"),
    path('Professeur/deleteProf/<int:idProf>', deleteProf, name="deleteProf"), 
    path('Professeur/details_Prof/<int:idProf>', details_Prof, name="details_Prof"),

    path('Cours/ModifierCours/<int:idMat>', ModifierCours, name="ModifierCours"),
    path('Cours/AddModifsCours/<int:idMat>', AddModifsCours, name="AddModifsCours"),
    path('Cours/deleteCours/<int:idMat>', deleteCours, name="deleteCours"), 
    path('Cours/details_Cours/<int:idMat>', details_Cours, name="details_Cours"),

    path('Note/ChangeNoteElev/<int:idElev>,<int:idMat>,<int:ValNote>,<str:ValComt>', ChangeNoteElev, name="ChangeNoteElev"),
    path('Note/GetinfosPourc/<int:idMat>,<int:idClass>', GetinfosPourc, name="GetinfosPourc"),
    path('Note/GetinfosPourCM/<int:idMat>,<int:idClass>', GetinfosPourCM, name="GetinfosPourCM"),
    path('Bulletin/Bulletin_Eleve/<int:idElev>', Bulletin_Eleve, name="Bulletin_Eleve"), 
    

    path('Eleves/GetdatasElevesbyidE/<int:idElev>', GetdatasElevesbyidE, name="GetdatasElevesbyidE"),
    path('Eleves/ModifierEleves/<int:idElev>', ModifierElev, name="ModifierElev"),
    path('Eleves/AddModifsElev/<int:idElev>', AddModifsElev, name="AddModifsElev"),
    path('Eleves/deleteElev/<int:idElev>', deleteElev, name="deleteElev"), 
    path('Eleves/details_Eleve/<int:idElev>', details_Eleve, name="details_Eleve"), 

    path('EditModWordClass/<int:idClas>', EditModWordClass, name="EditModWordClass"), 
    path('CreateWordElev/<int:idE>', CreateWordElev, name="CreateWordElev"), 

    

    

]