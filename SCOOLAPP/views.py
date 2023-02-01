from django.shortcuts import render, redirect
from SCOOLAPP.models import Classe, Type, Matiere, Professeur,Eleve,Note, Groupe, BulletinDeNote,Administrateur
from django.http import JsonResponse,  HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

@login_required
def acceuilAdmin(Request):

    Admin = Administrateur.objects.get(Username=Request.user)
    CountE = Eleve.objects.all().count()
    CountP = Professeur.objects.all().count()
    CountClasses = Classe.objects.all().count()
    CountMats = Matiere.objects.all().count()
    datas = {"CountE":CountE,"CountP":CountP,"CountClasses":CountClasses,"CountMats":CountMats,"Admin":Admin}
    return render(Request, "SCOOLAPP/indexAdmin.html",datas)


#######################################################################################                                           
#####################################################                                              
#                VUES SUR LES CLASSES               #   
#####################################################  

@login_required
def GetdatasClasses(Request):
    Classes = Classe.objects.all()
    datas = { "Classes": list(Classes.values()) }
    return JsonResponse(datas)

@login_required
def GetdatasClassesbyidp(Request,idClass):
    Classes = Classe.objects.exclude(id= idClass)
    datas = { "Classes": list(Classes.values()) }
    return JsonResponse(datas)

@login_required
def ViewsClasses(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Classes = Classe.objects.all()
    effClasses = [Eleve.objects.filter(ClassElev= clas).count() for clas in Classes]
    print(effClasses) 
    AllDatas = [{"clas":clas, "effClass":effClass} for clas,effClass in zip(Classes,effClasses)] 
    datas = {"AllDatas": AllDatas,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-Classes.html",datas)

@login_required
def SearchClassesForAbout(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Classes = Classe.objects.all()
    effClasses = [Eleve.objects.filter(ClassElev= clas).count() for clas in Classes]
    print(effClasses) 
    AllDatas = [{"clas":clas, "effClass":effClass} for clas,effClass in zip(Classes,effClasses)] 
    datas = {"AllDatas": AllDatas, "choix": "SelectAbout","Admin":Admin}
    return render(Request, "SCOOLAPP/all-Classes.html",datas)

@login_required
def details_Classe(Request, idClass):
    Admin = Administrateur.objects.get(Username=Request.user)
    classe = Classe.objects.get(id= idClass)
    if classe.AllMat().count() ==0:
        fistMat = 0
    else:
        fistMat = list(classe.AllMat())[0].nomMat
    listelev = classe.AllEleve()
    listMat = classe.AllMat()
    listNotebyMat = [[elev.get_noteByMat(mat) for elev in listelev] for mat in listMat]
    print(listNotebyMat)
    PackBMat = []
    for lNote,mat in zip(listNotebyMat,listMat):
        print("#############################################")
        ls = [{"Elev":elev,"note":note} for elev,note in zip(listelev,lNote)]
        PackBMat.append({"mat":mat,"datE":ls})
        print(mat,ls)  

    TotElvByMats = [{"Mat":mat,"TEBM":mat.pourc_note_givenByMats(classe)} for mat in listMat]

    datas = {"classe":classe,"fistMat":fistMat,"PackBMat":PackBMat,"TotElvByMats":TotElvByMats,"Admin":Admin}
    return render(Request, "SCOOLAPP/about-classe.html",datas)

@login_required
def FormAddClasses(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    types = Type.objects.all()
    datas = {"types": types,"Admin":Admin}
    return render(Request, "SCOOLAPP/Add-Classe.html",datas)

@login_required
def AddnewClasse(Request):
    if Request.method == "POST":
        codeC = Request.POST["Code"]
        nomC = Request.POST["Nom"]
        TypeC = Request.POST["Type"]
        descriptionC = Request.POST["Descrpt"]
    TypeC = Type.objects.get(nomTyp=TypeC)
    newClasse = Classe(codeClass=codeC, nomClass=nomC, typClass=TypeC, descrpClass=descriptionC)
    newClasse.save()
    return ViewsClasses(Request)

@login_required
def SearchClassesToModif(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Classes = Classe.objects.all()
    effClasses = [Eleve.objects.filter(ClassElev= clas).count() for clas in Classes]
    print(effClasses) 
    AllDatas = [{"clas":clas, "effClass":effClass} for clas,effClass in zip(Classes,effClasses)] 
    datas = {"AllDatas": AllDatas, "choix": "SelectEdit","Admin":Admin}
    return render(Request, "SCOOLAPP/all-Classes.html",datas)

@login_required
def ModifierClasse(Request, idClass):
    Admin = Administrateur.objects.get(Username=Request.user)
    Clas = Classe.objects.get(id= idClass)
    types = Type.objects.all()
    datas = {"Clas":Clas,"types": types,"Admin":Admin}
    return render(Request, "SCOOLAPP/edit-Classe.html",datas)

@login_required
def AddModifsClasse(Request,idClass):
    if Request.method == "POST":
        codeC = Request.POST["Code"]
        nomC = Request.POST["Nom"]
        TypeC = Request.POST["Type"]
        descriptionC = Request.POST["Descrpt"]
    TypeC = Type.objects.get(nomTyp=TypeC)

    Clas = Classe.objects.get(id= idClass)
    Clas.codeClass = codeC
    Clas.nomClass = nomC
    Clas.typClass = TypeC
    Clas.descrpClass = descriptionC
    Clas.save()
    return ViewsClasses(Request)

@login_required
def SearchClassesToDelete(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Classes = Classe.objects.all()
    effClasses = [Eleve.objects.filter(ClassElev= clas).count() for clas in Classes]
    print(effClasses) 
    AllDatas = [{"clas":clas, "effClass":effClass} for clas,effClass in zip(Classes,effClasses)] 
    datas = {"AllDatas": AllDatas, "choix": "SelectDel","Admin":Admin}
    return render(Request, "SCOOLAPP/all-Classes.html",datas)

@login_required
def deleteClasse(Request,idClass):
    classe = Classe.objects.get(id= idClass)
    classe.delete()
    return SearchClassesToDelete(Request)

#######################################################################################                                           
#####################################################                                              
#                 VUES SUR LES COURS                #   
#####################################################  
@login_required
def GetdatasCours(Request):
    Matieres = Matiere.objects.all()
    datas = { "Matieres": list(Matieres.values()) }
    return JsonResponse(datas)

@login_required
def GetdatasCoursbyidCrs(Request,idCrs):
    Matieres = Matiere.objects.exclude(id= idCrs)
    datas = { "Matieres": list(Matieres.values()) }
    return JsonResponse(datas)

@login_required
def ViewsCours(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Matieres = Matiere.objects.all()
    datas = {"Matieres": Matieres,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-courses.html",datas)

@login_required
def SearchCoursForAbout(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Matieres = Matiere.objects.all()
    datas = {"Matieres": Matieres, "choix": "SelectAbout","Admin":Admin}
    return render(Request, "SCOOLAPP/all-courses.html",datas)

@login_required
def details_Cours(Request, idMat):
    Admin = Administrateur.objects.get(Username=Request.user)
    matiere = Matiere.objects.get(id= idMat)
    classes = matiere.listClass()
    listElevbyClas = [clas.AllEleve() for clas in classes]
    
    listNotebyClass = [[elev.get_noteByMat(matiere) for elev in Lelev] for Lelev in listElevbyClas] 
    print(listNotebyClass)
    PackBClas = []
    K = 0
    for Lelev,LNote in zip(listElevbyClas,listNotebyClass):
        ls = [{"Elev":elev,"note":note} for elev,note in zip(Lelev,LNote)]
        PackBClas.append({"clas":classes[K],"datE":ls})
        K =+ 1
        
    TotElvByClas = [{"clas":clas,"TEBC":clas.pourc_note_givenByCls(matiere)} for clas in classes]
    print(TotElvByClas[0]["clas"]==PackBClas[0]["clas"])  

    datas = {"mat":matiere,"fistClass":list(matiere.listClass())[0].nomClass,
                "TotElvByClas":TotElvByClas,"PackBClas":PackBClas,"Admin":Admin}
    return render(Request, "SCOOLAPP/about-courses.html",datas)


@login_required
def FormAddCours(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Classes = Classe.objects.all()
    Professeurs = Professeur.objects.all()
    Groupes = Groupe.objects.all()
    datas = {"Professeurs": Professeurs, "Classes":Classes,"Groupes":Groupes,"Admin":Admin}
    return render(Request, "SCOOLAPP/Add-courses.html",datas)

@login_required
def AddnewCours(Request):
    if Request.method == "POST":
        codeC = Request.POST["code"]
        nomC = Request.POST["nom"]
        surnomC = Request.POST["surnom"]
        nomprof = Request.POST["prof"]
        nomgroup = Request.POST["group"]
        NomClass = dict(Request.POST)['classe']
        coeff = Request.POST["coef"]
        descriptionC = Request.POST["Descrpt"]

    idprof = int(nomprof.split("-")[0])
    Prof = Professeur.objects.get(id=idprof)
    group = Groupe.objects.get(nomGroup=nomgroup)
    ListClas = [Classe.objects.get(nomClass=clas) for clas in NomClass]

    print(ListClas)
    newCours = Matiere(CodeMat=codeC, nomMat=nomC, SurnomMat=surnomC, ProfMat=Prof, coeffMat=coeff,
                         DescrptMat=descriptionC, groupMat=group)
    newCours.save()
    for clas in ListClas:
        newCours.ClassMat.add(clas)
    return ViewsCours(Request)

@login_required
def SearchCoursToModif(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Matieres = Matiere.objects.all()
    datas = {"Matieres": Matieres, "choix": "SelectEdit","Admin":Admin}
    return render(Request, "SCOOLAPP/all-courses.html",datas)

@login_required
def ModifierCours(Request, idMat):
    Admin = Administrateur.objects.get(Username=Request.user)
    matiere = Matiere.objects.get(id= idMat)
    Classes = Classe.objects.all()
    Groupes = Groupe.objects.all()
    Professeurs = Professeur.objects.all()
    datas = {"mat":matiere,"Professeurs": Professeurs, "Classes":Classes,"Groupes":Groupes,"Admin":Admin}
    return render(Request, "SCOOLAPP/edit-courses.html",datas)

@login_required
def AddModifsCours(Request,idMat):
    if Request.method == "POST":
        code = Request.POST["code"]
        nom = Request.POST["nom"]
        surnom = Request.POST["surnom"]
        nomprof = Request.POST["prof"]
        NomClass = dict(Request.POST)['classe']
        nomgroup = Request.POST["group"]
        coeff = Request.POST["coef"]
        description = Request.POST["Descrpt"]

    idprof = int(nomprof.split("-")[0])
    Prof = Professeur.objects.get(id=idprof)
    group = Groupe.objects.get(nomGroup=nomgroup)
    ListClas = [Classe.objects.get(nomClass=clas) for clas in NomClass]

    matiere = Matiere.objects.get(id= idMat)
    matiere.CodeMat = code
    matiere.nomMat = nom
    matiere.SurnomMat = surnom
    matiere.ProfMat = Prof
    matiere.coeffMat = coeff
    matiere.groupMat = group
    matiere.DescrptMat = description
    matiere.save()
    listBDClass = matiere.ClassMat.all()
    for clas in listBDClass:
        if(clas not in ListClas):
            matiere.ClassMat.remove(clas)
    for clas in ListClas:
        if(clas not in listBDClass):
            matiere.ClassMat.add(clas)

    return ViewsCours(Request)


@login_required
def SearchCoursToDelete(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Matieres = Matiere.objects.all()
    datas = {"Matieres": Matieres, "choix": "SelectDel","Admin":Admin}
    return render(Request, "SCOOLAPP/all-courses.html",datas)

@login_required
def deleteCours(Request,idMat):
    matiere = Matiere.objects.get(id= idMat)
    matiere.delete()
    return SearchCoursToDelete(Request)

#######################################################################################                                           
#####################################################                                         
#            VUES SUR LES PROFESSEURS               #    
#####################################################
@login_required
def GetdatasProfs(Request):
    Profs = Professeur.objects.all()
    datas = { "Profs": list(Profs.values()) }
    return JsonResponse(datas)

@login_required
def GetdatasProfsbyidp(Request, idProf):
    Profs = Professeur.objects.exclude(id = idProf)
    datas = { "Profs": list(Profs.values()) }
    return JsonResponse(datas)

@login_required
def ViewsProfs(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Professeurs = Professeur.objects.all()
    data = {"Professeurs": Professeurs,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-professors.html",data)

@login_required
def SearchProfsForAbout(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Professeurs = Professeur.objects.all()
    datas = { "Professeurs": Professeurs,"choix": "SelectAbout" ,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-professors.html",datas)

@login_required
def details_Prof(Request, idProf):
    Admin = Administrateur.objects.get(Username=Request.user)
    Prof = Professeur.objects.get(id= idProf)
    jour_actuel = datetime.datetime.now().date()
    Annee_actu = jour_actuel.year
    AnneeDatNaiss = Prof.dateNaisProf.year
    AnneeEntrance = Prof.DateJoinProf.year
    Age = Annee_actu - AnneeDatNaiss
    AnnExp = Annee_actu - AnneeEntrance
    Domaines = Prof.MatpossibProf.split(",")

    datas = {"prof":Prof,"Age":Age,"AnnExp":AnnExp,"Domaines":Domaines,"Admin":Admin}
    return render(Request, "SCOOLAPP/professor-profile.html",datas)

@login_required
def FormAddProfs(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    return render(Request, "SCOOLAPP/Add-professor.html",{"Admin":Admin})

@login_required
def AddnewProf(Request):
    if Request.method == "POST":
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        email = Request.POST["Email"] 
        DateArriv = Request.POST["DateArriv_submit"]
        Password = Request.POST["Password"]
        Matricule = Request.POST["Matricule"]
        Genre = Request.POST["Genre"]
        Adresse = Request.POST["Adresse"]
        Telephone = Request.POST["Telephone"]
        Designation = Request.POST["Designation"]
        Datnaiss = Request.POST["Datnaiss_submit"]
        MatDomaine = Request.POST["MatDomaine"]
        Descrpt = Request.POST["Descrpt"]
        Photo = Request.FILES["Photo"]
        userName = Matricule
    newProf = Professeur(MatriculeProf=Matricule, nomProf=Nom, prenomProf=Prenom,DateJoinProf=DateArriv,
             TelephoneProf=Telephone, EmailProf=email, Username = userName,password=Password,
             genreProf=Genre,DesignationProf=Designation,MatpossibProf=MatDomaine,dateNaisProf=Datnaiss,
             AdresseProf= Adresse,DescrptProf=Descrpt, photoProf=Photo)
    newProf.save()
    newUser = User.objects.create_user(username=userName,email=email,password=Password)
    newUser.first_name = Nom
    newUser.last_name = Prenom
    newUser.save()
    return ViewsProfs(Request)

@login_required
def SearchProfsToModif(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Professeurs = Professeur.objects.all()
    datas = { "Professeurs": Professeurs,"choix": "SelectEdit","Admin":Admin }
    return render(Request, "SCOOLAPP/all-professors.html",datas)

@login_required
def ModifierProf(Request, idProf):
    Admin = Administrateur.objects.get(Username=Request.user)
    Prof = Professeur.objects.get(id= idProf)
    datas = {"prof":Prof,"Admin":Admin}
    return render(Request, "SCOOLAPP/edit-professor.html",datas)

@login_required
def AddModifsProf(Request,idProf):
    if Request.method == "POST":
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        OldUsername = Request.POST["OldUsername"]
        email = Request.POST["Email"] 
        DateArriv = Request.POST["DateArriv_submit"]
        Password = Request.POST["Password"]
        Matricule = Request.POST["Matricule"]
        Genre = Request.POST["Genre"]
        Adresse = Request.POST["Adresse"]
        Telephone = Request.POST["Telephone"]
        Designation = Request.POST["Designation"]
        Datnaiss = Request.POST["Datnaiss_submit"]
        MatDomaine = Request.POST["MatDomaine"]
        Descrpt = Request.POST["Descrpt"]
        userName = Matricule
        try:
            Photo = Request.POST["Photo"]
        except:
            Photo = Request.FILES["Photo"]
            
    Prof = Professeur.objects.get(id= idProf)
    
    Prof.nomProf, Prof.prenomProf, Prof.EmailProf = Nom, Prenom, email
    Prof.DateJoinProf, Prof.password, Prof.MatriculeProf = DateArriv, Password, Matricule
    Prof.genreProf, Prof.AdresseProf, Prof.TelephoneProf = Genre, Adresse, Telephone
    Prof.DesignationProf, Prof.dateNaisProf, Prof.MatpossibProf = Designation, Datnaiss, MatDomaine
    Prof.DescrptProf, Prof.Username = Descrpt, userName
    
    if(Photo != ""):  
        Prof.photoProf=Photo
    Prof.save()
    
    user = User.objects.get(username=OldUsername)
    user.username = userName
    user.first_name, user.last_name =  Nom, Prenom
    user.set_password(Password)
    user.save()
    return ViewsProfs(Request)


@login_required
def SearchProfsToDelete(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Professeurs = Professeur.objects.all()
    datas = { "Professeurs": Professeurs,"choix": "SelectDel" ,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-professors.html",datas)

@login_required
def deleteProf(Request,idProf):
    Prof = Professeur.objects.get(id= idProf)
    Prof.delete()
    return SearchProfsToDelete(Request)

#######################################################################################                                           
#####################################################                                              
#                VUES SUR LES ELEVES                #   
##################################################### 

@login_required
def GetdatasEleves(Request):
    eleves_Brt = Eleve.objects.all()
    eleves = eleves_Brt.values()
    databyelev = [{"elev":elev,"classe":elevb.ClassElev.nomClass} for elev,elevb in zip(eleves,eleves_Brt)]
    print(databyelev)
    datas = { "databyelev": databyelev }
    return JsonResponse(datas)

@login_required
def GetdatasElevesbyidE(Request, idElev):
    eleves = Eleve.objects.exclude(id = idElev)
    datas = { "eleves": list(eleves.values()) }
    return JsonResponse(datas)

@login_required
def ViewsEleves(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Eleves = Eleve.objects.all()
    datas = { "Eleves": Eleves ,"Admin":Admin}
    return render(Request, "SCOOLAPP/all-students.html",datas)

@login_required
def SearchElevesForAbout(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Eleves = Eleve.objects.all()
    datas = { "Eleves": Eleves,"choix": "SelectAbout","Admin":Admin }
    return render(Request, "SCOOLAPP/all-students.html",datas)

@login_required
def details_Eleve(Request, idElev):
    Admin = Administrateur.objects.get(Username=Request.user)
    elev = Eleve.objects.get(id= idElev)
    jour_actuel = datetime.datetime.now().date()
    Annee_actu = jour_actuel.year
    AnneeDatNaiss = elev.dateNaisElev.year
    Age = Annee_actu - AnneeDatNaiss

    datas = {"elev":elev,"Age":Age,"Admin":Admin}
    return render(Request, "SCOOLAPP/about-student.html",datas)


@login_required
def FormAddEleve(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    classes = Classe.objects.all()
    datas = {"classes":classes,"Admin":Admin}
    return render(Request, "SCOOLAPP/Add-student.html",datas)

@login_required
def AddnewEleve(Request):
    if Request.method == "POST":
        Matricule = Request.POST["Matricule"]
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        Telephone = Request.POST["Telephone"]
        nomclass = Request.POST["Classe"]
        Datnaiss = Request.POST["Datnaiss_submit"]
        Genre = Request.POST["Genre"]
        Photo = Request.FILES["Photo"]
    classe = Classe.objects.get(nomClass=nomclass)
    print(Datnaiss,"------",Genre)
    newEleve = Eleve(MatriculeElev=Matricule, nomElev=Nom, prenomElev=Prenom, dateNaisElev=Datnaiss, genreElev=Genre, TelephoneElev=Telephone, ClassElev=classe, photoElev=Photo)
    newEleve.save()
    data = {"infobuleConfirmCreat": True}
    return ViewsEleves(Request)


@login_required
def SearchElevesToModif(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Eleves = Eleve.objects.all()
    datas = { "Eleves": Eleves,"choix": "SelectEdit","Admin":Admin }
    return render(Request, "SCOOLAPP/all-students.html",datas)

@login_required
def ModifierElev(Request, idElev):
    Admin = Administrateur.objects.get(Username=Request.user)
    classes = Classe.objects.all()
    elev = Eleve.objects.get(id= idElev)
    datas = {"elev":elev,"classes":classes,"Admin":Admin}
    return render(Request, "SCOOLAPP/edit-student.html",datas)

@login_required
def AddModifsElev(Request,idElev):
    if Request.method == "POST":
        Matricule = Request.POST["Matricule"]
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        Telephone = Request.POST["Telephone"]
        nomclass = Request.POST["Classe"]
        Datnaiss = Request.POST["Datnaiss_submit"]
        Genre = Request.POST["Genre"]
        try:
            Photo=Request.POST["Photo"]
        except:
            Photo = Request.FILES["Photo"]
            
    elev = Eleve.objects.get(id= idElev)
    elev.MatriculeElev=Matricule
    elev.nomElev=Nom
    elev.prenomElev=Prenom
    elev.TelephoneElev=Telephone
    classe = Classe.objects.get(nomClass=nomclass)
    elev.ClassElev=classe
    elev.dateNaisElev=Datnaiss
    elev.genreElev=Genre
    if(Photo != ""):  
        elev.photoElev=Photo
    elev.save()
    return ViewsEleves(Request)

@login_required
def SearchElevesToDelete(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    Eleves = Eleve.objects.all()
    datas = { "Eleves": Eleves,"choix": "SelectDel" ,"Admin":Admin}
    print(datas)
    return render(Request, "SCOOLAPP/all-students.html",datas)

@login_required
def deleteElev(Request,idElev):
    print("###############",idElev, type(idElev))
    elev = Eleve.objects.get(id= idElev)
    elev.delete()
    return SearchElevesToDelete(Request)


#######################################################################################                                           
######################################################                                              
#                  VUES SUR LES NOTES                #   
###################################################### 
@login_required
def VoirProfileAdmin(Request):
    Admin = Administrateur.objects.get(Username=Request.user)
    jour_actuel = datetime.datetime.now().date()
    Annee_actu = jour_actuel.year
    AnneeDatNaiss = Admin.dateNaisAdmin.year
    Age = Annee_actu - AnneeDatNaiss

    datas = {"Admin":Admin,"Age":Age}
    return render(Request, "SCOOLAPP/Admin-profile.html",datas)

def ModifCompteAdmin(Request):
    if Request.method == "POST":
        Username = Request.POST["Username"]
        Password = Request.POST["Password"]
        Email = Request.POST["Email"]
    
    print(Username, Password, Email)
    Admin = Administrateur.objects.get(Username=Request.user)
    Admin.Username = Username
    Admin.password = Password
    Admin.save()

    user = Request.user
    user.username = Username
    user.email = Email
    user.set_password(Password)
    user.save()

    return redirect("PageLogin")

def ModifProfileAdmin(Request):
    if Request.method == "POST":
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        Telephone = Request.POST["Telephone"]
        email = Request.POST["Email"] 
        Adresse = Request.POST["Adresse"]
        try:
            Datnaiss = Request.POST["Datnaiss_submit"]
        except:
            Datnaiss = Request.POST["Datnaiss"]
        Descrpt = Request.POST["Descrpt"]
        try:
            Photo = Request.POST["Photo"]
        except:
            Photo = Request.FILES["Photo"]
            
    Admin = Administrateur.objects.get(Username=Request.user)
    if Nom !="":
        Admin.nomAdmin = Nom
    if Prenom !="":
        Admin.prenomAdmin = Prenom
    if Telephone !="":
        Admin.TelephoneAdmin = Telephone
    if email !="":
        Admin.EmailAdmin = email
    if Adresse !="":
        Admin.AdresseAdmin = Adresse
    if Datnaiss !="":
        Admin.dateNaisAdmin = Datnaiss
    if Descrpt !="":
        Admin.DescrptAdmin = Descrpt
    if(Photo != ""):  
        Admin.photoAdmin=Photo
    Admin.save()

    user = Request.user
    if Nom != "":
        user.first_name = Nom
    if Prenom != 0:
        user.last_name = Prenom
    user.save()
    return VoirProfileAdmin(Request)
#######################################################################################                                           
######################################################                                              
#                  VUES SUR LES NOTES                #   
###################################################### 

@login_required
def ChangeNoteElev(Request, idElev, idMat, ValNote,ValComt):
    eleve = Eleve.objects.get(id = idElev)
    Mat = Matiere.objects.get(id = idMat)
    try:
        note = Note.objects.get(eleveNote=eleve,matiereNote=Mat)
    except:
        newnote = Note(eleveNote=eleve, matiereNote=Mat, valeurNote=ValNote,CommentNote=ValComt)
        newnote.save()
    else:
        note.valeurNote = ValNote
        note.CommentNote = ValComt
        note.save()

    datas = { "databyelev": "databyelev" }
    return JsonResponse(datas)

@login_required
def GetinfosPourc(Request, idMat, idClass):
    Mat = Matiere.objects.get(id = idMat)
    classe = Classe.objects.get(id = idClass)

    print("################################")
    print(idMat, idClass)
    print("################################")

    datas = { "matPourc": Mat.pourc_note_given(),"matTewN": Mat.tot_note_given(),
            "matTe": Mat.get_TotElev_ClassMat(), "classePourc":classe.pourc_note_givenByCls(Mat)}
    return JsonResponse(datas)

@login_required
def GetinfosPourCM(Request, idMat, idClass):
    Mat = Matiere.objects.get(id = idMat)
    classe = Classe.objects.get(id = idClass)

    print("################################")
    print(idMat, idClass)
    print("################################")

    datas = { "classPourc": classe.tot_note_givenAllClas(),"matTewN": Mat.tot_note_given(),
            "matTe": Mat.get_TotElev_ClassMat(), "matPourc":Mat.pourc_note_givenByMats(classe)}
    return JsonResponse(datas)

def LESMESSAGES(Request):
    return render(Request, "SCOOLAPP/uc-sweetalert.html") 


@login_required
def Bulletin_Eleve(Request, idElev):
    Admin = Administrateur.objects.get(Username=Request.user)
    elev = Eleve.objects.get(id= idElev)

    Bulletin = BulletinDeNote.objects.get(eleve=elev)

    datas = {"elev":elev,"Bulletin":Bulletin,"modelBul":elev.ClassElev.ficheWordModel,"Admin":Admin}
    return render(Request, "SCOOLAPP/GenererBulletinStudent.html",datas)

@login_required
def EditModWordClass(Request, idClas):
    classe = Classe.objects.get(id= idClas)
    if Request.method == "POST":
        print(Request.FILES)
        Doc = Request.FILES["Moddocx"]
    
    classe.ficheWordModel = Doc
    classe.save()
    return HttpResponse("Yess")

@login_required
def CreateWordElev(Request, idE):
    elev = Eleve.objects.get(id= idE)
    classe = Classe.objects.get(id = elev.ClassElev.id)
    AllElevclass = classe.eleve_set.all()
    for Elv in AllElevclass:
        newbullletin = BulletinDeNote(eleve=Elv)
        newbullletin.save()
        
    Bulletin = BulletinDeNote.objects.get(eleve=elev)
    dicoMoyByGE = Bulletin.Get_AllMoybyGroupE()
    
    MoyG = Bulletin.MoyG
    MoyGA, MoyGB, MoyGC = dicoMoyByGE["MoyNotesGA"], dicoMoyByGE["MoyNotesGB"], dicoMoyByGE["MoyNotesGC"]

    Eff = AllElevclass.count()
    nomRangs = ["1er"]+[str(i)+"ème" for i in range(2,Eff+1)]
    MoyGAll = []
    AllMoyGA, AllMoyGB, AllMoyGC= [], [], []
    for Elv in AllElevclass:
        resu = Elv.bulletindenote_set.get()
        MoyGAll.append(resu.MoyG)
        dicoMoyByG = resu.Get_AllMoybyGroupE()
        AllMoyGA.append(dicoMoyByG["MoyNotesGA"])
        AllMoyGB.append(dicoMoyByG["MoyNotesGB"])
        AllMoyGC.append(dicoMoyByG["MoyNotesGC"])

    MoyGAll.sort(reverse=True)
    AllMoyGA.sort(reverse=True)
    AllMoyGB.sort(reverse=True)
    AllMoyGC.sort(reverse=True)
    
    Bulletin.Rang = nomRangs[MoyGAll.index(MoyG)]
    Bulletin.RangGA = nomRangs[AllMoyGA.index(MoyGA)]
    Bulletin.RangGB = nomRangs[AllMoyGB.index(MoyGB)]
    Bulletin.RangGC = nomRangs[AllMoyGC.index(MoyGC)]
    Bulletin.save()

    Bulletin.createBulletinWord()

    return HttpResponse("Yess")

