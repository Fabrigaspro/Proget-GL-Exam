from django.shortcuts import render, redirect
from SCOOLAPP.models import Classe, Type, Matiere, Professeur,Eleve
from django.http import JsonResponse,  HttpResponse

# Create your views here.

def acceuil(Request):
    CountE = Eleve.objects.all().count()
    CountClasses = Classe.objects.all().count()
    datas = {"CountE":CountE,"CountClasses":CountClasses}
    return render(Request, "SCOOLAPP/acceuil.html",datas)


#######################################################################################                                           
#####################################################                                              
#                VUES SUR LES CLASSES               #   
#####################################################  
def GetdatasClasses(Request):
    Classes = Classe.objects.all()
    datas = { "Classes": list(Classes.values()) }
    return JsonResponse(datas)

def GetdatasClassesbyidp(Request,idClass):
    Classes = Classe.objects.exclude(id= idClass)
    datas = { "Classes": list(Classes.values()) }
    return JsonResponse(datas)

def GestClasses(Request):
    data = {"infobuleConfirm": False}
    return render(Request, "SCOOLAPP/Gestions_classes.html",data)

def SelctDelClasses(Request):
    classes = Classe.objects.filter(state = True)
    for clas in classes:
        clas.state = False
        clas.save()
    return render(Request, "SCOOLAPP/SelectionSupp_class.html")

def validDelclasses(Request):
    classes = Classe.objects.filter(state = True)
    datas = { "classes": classes }
    return render(Request, "SCOOLAPP/validelclass.html",datas)

def ChangStatclass(Request):
    if Request.method == "GET":
        IDS = Request.GET["idC"]
        stat = Request.GET["stat"]
        if stat == "true":
            stat = True
        else:
            stat = False
    print("##########  ",IDS, "  ##################  ",stat)
    if IDS == "SelectAll":
        classes = Classe.objects.all()
        for classe in classes:
            print("#### BEFORE ######  ",classe.state, "  ##################")
            classe.state = stat
            classe.save()
            print("##### AFTER #####  ",classe.state, "  ##################")

    else:
        classe = Classe.objects.get(id=IDS)
        classe.state = stat
        classe.save()
    return render(Request, "SCOOLAPP/Gestions_classes.html")

def deleteClasses(Request):
    classes = Classe.objects.filter(state = True)
    classes.delete()
    data = {"infobuleConfirm": True}
    return render(Request, "SCOOLAPP/Gestions_classes.html", data)

def FormAddClasses(Request):
    types = Type.objects.all()
    datas = {"types": types}
    return render(Request, "SCOOLAPP/formAddclass.html",datas)

def AddnewClasse(Request):
    if Request.method == "POST":
        codeC = Request.POST["codeC"]
        nomC = Request.POST["nomC"]
        TypeC = Request.POST["TypeC"]
        descriptionC = Request.POST["descriptionC"]
    TypeC = Type.objects.get(nomTyp=TypeC)
    newClasse = Classe(codeClass=codeC, nomClass=nomC, typClass=TypeC, descrpClass=descriptionC)
    newClasse.save()
    data = {"infobuleConfirmCreat": True}
    return render(Request, "SCOOLAPP/Gestions_classes.html",data)

def details_Classe(Request, idClass):
    classe = Classe.objects.get(id= idClass)
    matieres = Matiere.objects.filter(ClassMat= classe)
    countMat = matieres.count()
    datas = {"classe":classe, "matieres":matieres,"countMat":countMat}
    return render(Request, "SCOOLAPP/Details_sur_classe.html",datas)

def ModifierClasse(Request, idClass):
    types = Type.objects.all()
    classe = Classe.objects.get(id= idClass)
    datas = {"classe":classe,"types": types}
    return render(Request, "SCOOLAPP/modifierClasse.html",datas)

def AddModifsClasse(Request,idClass):
    if Request.method == "POST":
        codeC = Request.POST["codeC"]
        nomC = Request.POST["nomC"]
        TypeC = Request.POST["TypeC"]
        descriptionC = Request.POST["descriptionC"]
    TypeC = Type.objects.get(nomTyp=TypeC)
    classe = Classe.objects.get(id= idClass)
    classe.codeClass = codeC
    classe.nomClass = nomC
    classe.typClass = TypeC
    classe.descrpClass = descriptionC
    classe.save()
    return details_Classe(Request, idClass)

#######################################################################################                                           
#####################################################                                         
#            VUES SUR LES PROFESSEURS               #    
#####################################################
def GetdatasProfs(Request):
    Profs = Professeur.objects.all()
    datas = { "Profs": list(Profs.values()) }
    return JsonResponse(datas)

def GetdatasProfsbyidp(Request, idProf):
    Profs = Professeur.objects.exclude(id = idProf)
    datas = { "Profs": list(Profs.values()) }
    return JsonResponse(datas)

def GestProfs(Request):
    data = {"infobuleConfirm": False}
    return render(Request, "SCOOLAPP/gestion_Professeurs.html",data)

def ChangStateProf(Request):
    if Request.method == "GET":
        IDS = Request.GET["idC"]
        stat = Request.GET["stat"]
        if stat == "true":
            stat = True
        else:
            stat = False
    print("##########  ",IDS, "  ##################  ",stat)
    if IDS == "SelectAll":
        Profs = Professeur.objects.all()
        for prof in Profs:
            prof.state = stat
            prof.save()
    else:
        prof = Professeur.objects.get(id=IDS)
        prof.state = stat
        prof.save()
    return render(Request, "SCOOLAPP/gestion_Professeurs.html")

def SelctDelProfs(Request):
    Profs = Professeur.objects.filter(state = True)
    for prof in Profs:
        prof.state = False
        prof.save()
    return render(Request, "SCOOLAPP/SelectionSupp_Prof.html")

def validDelProfs(Request):
    Profs = Professeur.objects.filter(state = True)
    datas = { "Profs": Profs }
    return render(Request, "SCOOLAPP/validelprof.html",datas) 

def deleteProfs(Request):
    Profs = Professeur.objects.filter(state = True)
    Profs.delete()
    data = {"infobuleConfirm": True}
    return render(Request, "SCOOLAPP/gestion_Professeurs.html", data)  

def FormAddProfs(Request):
    return render(Request, "SCOOLAPP/formAddprof.html")

def AddnewProf(Request):
    if Request.method == "POST":
        Matricule = Request.POST["Matricule"]
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        Telephone = Request.POST["Telephone"]
        email = Request.POST["email"]
        Photo = Request.FILES["Photo"]
    newProf = Professeur(MatriculeProf=Matricule, nomProf=Nom, prenomProf=Prenom, TelephoneProf=Telephone, EmailProf=email, photoProf=Photo)
    newProf.save()
    data = {"infobuleConfirmCreat": True}
    return render(Request, "SCOOLAPP/gestion_Professeurs.html",data)

def details_Prof(Request, idProf):
    prof = Professeur.objects.get(id= idProf)
    matieres = Matiere.objects.filter(ProfMat= prof)
    countMat = matieres.count()
    datas = {"prof":prof, "matieres":matieres,"countMat":countMat}
    return render(Request, "SCOOLAPP/Details_sur_Prof.html",datas)

def ModifierProf(Request, idProf):
    prof = Professeur.objects.get(id= idProf)
    datas = {"prof":prof}
    return render(Request, "SCOOLAPP/modifierProf.html",datas)

def AddModifsProf(Request,idProf):
    if Request.method == "POST":
        Matricule = Request.POST["Matricule"]
        Nom = Request.POST["Nom"]
        Prenom = Request.POST["Prenom"]
        Telephone = Request.POST["Telephone"]
        email = Request.POST["email"]
        try:
            Photo=Request.POST["Photo"]
        except:
            Photo = Request.FILES["Photo"]
            
    prof = Professeur.objects.get(id= idProf)
    prof.MatriculeProf=Matricule
    prof.nomProf=Nom
    prof.prenomProf=Prenom
    prof.TelephoneProf=Telephone
    prof.EmailProf=email
    if(Photo != ""):  
        prof.photoProf=Photo
    prof.save()
    return details_Prof(Request, idProf)

#######################################################################################                                           
#####################################################                                              
#                VUES SUR LES CLASSES               #   
##################################################### 

def GetdatasEleves(Request):
    eleves_Brt = Eleve.objects.all()
    eleves = eleves_Brt.values()
    databyelev = [{"elev":elev,"classe":elevb.ClassElev.nomClass} for elev,elevb in zip(eleves,eleves_Brt)]
    print(databyelev)
    datas = { "databyelev": databyelev }
    return JsonResponse(datas)

def GetdatasElevesbyidE(Request, iElev):
    eleves = Eleve.objects.exclude(id = iElev)
    datas = { "eleves": list(eleves.values()) }
    return JsonResponse(datas)

def ViewsEleves(Request):
    Eleves = Eleve.objects.all()
    datas = { "Eleves": Eleves }
    return render(Request, "SCOOLAPP/all-students.html",datas)

def FormAddEleve(Request):
    classes = Classe.objects.all()
    datas = {"classes":classes}
    return render(Request, "SCOOLAPP/Add-student.html",datas)

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

def ModifierElev(Request, idElev):
    classes = Classe.objects.all()
    elev = Eleve.objects.get(id= idElev)
    datas = {"elev":elev,"classes":classes}
    return render(Request, "SCOOLAPP/edit-student.html",datas)

def ChangStateEleves(Request):
    if Request.method == "GET":
        IDS = Request.GET["idE"]
        stat = Request.GET["stat"]
        if stat == "true":
            stat = True
        else:
            stat = False
    print("##########  ",IDS, "  ##################  ",stat)
    if IDS == "SelectAll":
        eleves = Eleve.objects.all()
        for elev in eleves:
            elev.state = stat
            elev.save()
    else:
        elev = Eleve.objects.get(id=IDS)
        elev.state = stat
        elev.save()
    return render(Request, "SCOOLAPP/gestion_Eleves.html")

def SelctDelEleves(Request):
    eleves = Eleve.objects.filter(state = True)
    for elev in eleves:
        elev.state = False
        elev.save()
    return render(Request, "SCOOLAPP/SelectionSupp_Eleve.html")

def validDelEleves(Request):
    eleves = Eleve.objects.filter(state = True)
    datas = { "eleves": eleves }
    return render(Request, "SCOOLAPP/validelEleves.html",datas) 

def deleteEleves(Request):
    eleves = Eleve.objects.filter(state = True)
    eleves.delete()
    data = {"infobuleConfirm": True}
    return render(Request, "SCOOLAPP/gestion_Eleves.html", data)  


#######################################################################################                                           
######################################################                                              
#                 VUES SUR LES MATIERE               #   
###################################################### 

def GetdatasMatieres(Request):
    matieres = Matiere.objects.all()
    datas = { "databyelev": matieres[0].ClassMat }
    return HttpResponse(matieres[0].getClassMat())