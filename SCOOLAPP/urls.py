from django.urls import path
from SCOOLAPP.views import *

#baset,Ajouter_professeur_Enroll,Ajouter_professeur,Evoie_Et_Ajouter_session,Ajouter_session,search_EtatOF,Etat_val, Les_professeurs, search_prof,Search_NomorPlage_Session, les_sessions,Search_MatorPlage_prof


urlpatterns = [
    path('', acceuil, name="Acceuil"),

    path('Getdatasclasses/', GetdatasClasses, name="Getdatasclasses"),
    path('ChangStatclass/', ChangStatclass, name="ChangStatclass"),
    path('classes/validDelclasses/', validDelclasses, name="validDelclasses"),
    path('classes/', GestClasses, name="classes"),
    path('classes/SelctDelClasses/', SelctDelClasses, name="SelctDelClasses"),
    path('classes/deleteClasses/', deleteClasses, name="deleteClasses"),
    path('classes/FormAddClasses/', FormAddClasses, name="FormAddClasses"),
    path('classes/AddnewClasse/', AddnewClasse, name="AddnewClasse"),

    path('GetdatasProfs/', GetdatasProfs, name="GetdatasProfs"),
    path('Professeurs/', GestProfs, name="Professeurs"),
    path('ChangStateProf/', ChangStateProf, name="ChangStateProf"), 
    path('Professeurs/SelctDelProfs/', SelctDelProfs, name="SelctDelProfs"),
    path('Professeurs/validDelProfs/', validDelProfs, name="validDelProfs"),
    path('Professeurs/deleteProfs/', deleteProfs, name="deleteProfs"),    
    path('Professeurs/FormAddProfs/', FormAddProfs, name="FormAddProfs"),
    path('Professeurs/AddnewProf/', AddnewProf, name="AddnewProf"),

    path('GetdatasEleves/', GetdatasEleves, name="GetdatasEleves"),
    path('Eleves/', ViewsEleves, name="ViewsEleves"),
    path('ChangStateEleves/', ChangStateEleves, name="ChangStateEleves"), 
    path('Eleves/SelctDelEleves/', SelctDelEleves, name="SelctDelEleves"),
    path('Eleves/validDelEleves/', validDelEleves, name="validDelEleves"),
    path('Eleves/deleteEleves/', deleteEleves, name="deleteEleves"), 
    path('Eleves/FormAddEleve/', FormAddEleve, name="FormAddEleve"),
    path('Eleves/AddnewEleve/', AddnewEleve, name="AddnewEleve"),

    path('GetdatasMatieres/', GetdatasMatieres, name="GetdatasMatieres"),

]