from django.shortcuts import render, redirect
from SCOOLAPP.models import Classe, Matiere, Professeur, Eleve,Administrateur
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

@login_required
def acceuilProf(Request):

    Prof = Professeur.objects.get(Username=Request.user)
    CountMats = Prof.AllMatsProf().count()
    CountE = len(Prof.AllElevesProf())
    CountClasses = len(Prof.AllClassesProf())
    datas = {"CountE":CountE,"CountClasses":CountClasses,"CountMats":CountMats,"Prof":Prof}
    return render(Request, "app_Professors/indexProf.html",datas)


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
def VoirMesClasses(Request):
    Prof = Professeur.objects.get(Username=Request.user)
    Classes = Prof.AllClassesProf()
    effClasses = [Eleve.objects.filter(ClassElev= clas).count() for clas in Classes]
    print(effClasses) 
    AllDatas = [{"clas":clas, "effClass":effClass} for clas,effClass in zip(Classes,effClasses)] 
    datas = {"AllDatas": AllDatas,"Prof":Prof}
    return render(Request, "app_Professors/all-Classes-Prof.html",datas)

@login_required
def details_Classe_Prof(Request, idClass):
    Prof = Professeur.objects.get(Username=Request.user)
    classe = Classe.objects.get(id= idClass)
    Totcoef = classe.TotcoeffClasseProf(Prof)
    pourNgivByC = classe.tot_note_givenAllClasProf(Prof)
    listelev = classe.AllEleve()
    listMat = classe.AllMatByProf(Prof)
    if classe.AllMat().count() ==0:
        fistMat = 0
    else:
        fistMat = listMat[0].nomMat

    listNotebyMat = [[elev.get_noteByMat(mat) for elev in listelev] for mat in listMat]
    PackBMat = []
    for lNote,mat in zip(listNotebyMat,listMat):
        ls = [{"Elev":elev,"note":note} for elev,note in zip(listelev,lNote)]
        PackBMat.append({"mat":mat,"datE":ls})

    TotElvByMats = [{"Mat":mat,"TEBM":mat.pourc_note_givenByMats(classe)} for mat in listMat]

    datas = {"classe":classe,"fistMat":fistMat,"PackBMat":PackBMat,"TotElvByMats":TotElvByMats,"Prof":Prof,
            "listMat":listMat,"TotcoefP":Totcoef,"pourNgivByC":pourNgivByC}
    return render(Request, "app_Professors/about-classe-Prof.html",datas)

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
def VoirMesCours(Request):
    Prof = Professeur.objects.get(Username=Request.user)
    Matieres = Prof.AllMatsProf()
    datas = {"Matieres": Matieres,"Prof":Prof}
    return render(Request, "app_Professors/all-courses-Prof.html",datas)

@login_required
def details_Cours_Prof(Request, idMat):
    Prof = Professeur.objects.get(Username=Request.user)
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
                "TotElvByClas":TotElvByClas,"PackBClas":PackBClas,"Prof":Prof}
    return render(Request, "app_Professors/about-courses-Prof.html",datas)

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
def VoirMesEleves(Request):
    Prof = Professeur.objects.get(Username=Request.user)
    Eleves = Prof.AllElevesProf()
    datas = { "Eleves": Eleves ,"Prof":Prof}
    return render(Request, "app_Professors/all-students-Prof.html",datas)

@login_required
def details_Eleve_Prof(Request, idElev):
    Prof = Professeur.objects.get(Username=Request.user)
    elev = Eleve.objects.get(id= idElev)
    jour_actuel = datetime.datetime.now().date()
    Annee_actu = jour_actuel.year
    AnneeDatNaiss = elev.dateNaisElev.year
    Age = Annee_actu - AnneeDatNaiss

    datas = {"elev":elev,"Age":Age,"Prof":Prof}
    return render(Request, "app_Professors/about-student-Prof.html",datas)


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
    return VoirMesEleves(Request)



#######################################################################################                                           
#####################################################                                              
#                SONE PROFILE PROFESSOR             #   
##################################################### 
def VoirProfile(Request):
    Prof = Professeur.objects.get(Username=Request.user)
    print(Prof)
    jour_actuel = datetime.datetime.now().date()
    Annee_actu = jour_actuel.year
    AnneeDatNaiss = Prof.dateNaisProf.year
    AnneeEntrance = Prof.DateJoinProf.year
    Age = Annee_actu - AnneeDatNaiss
    AnnExp = Annee_actu - AnneeEntrance
    Domaines = Prof.MatpossibProf.split(",")

    datas = {"Prof":Prof,"Age":Age,"AnnExp":AnnExp,"Domaines":Domaines}
    return render(Request, "app_Professors/profileProf.html",datas)

def ModifCompteProf(Request):
    if Request.method == "POST":
        Username = Request.POST["Username"]
        Password = Request.POST["Password"]
        Email = Request.POST["Email"]
    
    print(Username, Password, Email)
    Prof = Professeur.objects.get(Username=Request.user)
    Prof.Username = Username
    Prof.password = Password
    Prof.save()

    user = Request.user
    user.username = Username
    user.email = Email
    user.set_password(Password)
    user.save()

    return redirect("PageLogin")

def ModifProfileProf(Request):
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
            
    Prof = Professeur.objects.get(Username=Request.user)
    if Nom !="":
        Prof.nomProf = Nom
    if Prenom !="":
        Prof.prenomProf = Prenom
    if Telephone !="":
        Prof.TelephoneProf = Telephone
    if email !="":
        Prof.EmailProf = email
    if Adresse !="":
        Prof.AdresseProf = Adresse
    if Datnaiss !="":
        Prof.dateNaisProf = Datnaiss
    if Descrpt !="":
        Prof.DescrptProf = Descrpt
    if(Photo != ""):  
        Prof.photoProf=Photo
    Prof.save()

    user = Request.user
    user.first_name, user.last_name =  Nom, Prenom
    user.save()
    return VoirProfile(Request)
