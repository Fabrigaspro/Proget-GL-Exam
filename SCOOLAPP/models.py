from django.db import models
from docxtpl import DocxTemplate, InlineImage

# Create your models here.

############## Création de la table Type de classe ##############
class Type(models.Model):
    CodeTyp = models.CharField(max_length=100,default="TYP-", unique=True)
    nomTyp = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nomTyp)

    def __return__(self):
        return Type()

############## Création de la table Type de classe ##############
class Groupe(models.Model):
    nomGroup = models.CharField(max_length=10,default="GROUPE-", unique=True)
    
    def __str__(self):
        return str(self.nomGroup)

    def __return__(self):
        return Groupe()

############## Création de la table professeur ##############
class Classe(models.Model):
    codeClass = models.CharField(max_length=100,default="CLASS-", unique=True)
    nomClass = models.CharField(max_length=100)
    descrpClass = models.CharField(max_length=300)
    typClass = models.ForeignKey(Type, on_delete=models.SET_NULL,null=True)
    state = models.BooleanField(default = False)
    ficheWordModel = models.FileField(upload_to = "ModelBulletinsClasse/")




    def AllEleve(self):  
        return self.eleve_set.all()
    def AllMat(self): 
        return self.matiere_set.all()

    def countAllMat(self): 
        return self.matiere_set.all().count()

    def AllMatByProf(self,prof):
        return [mat for mat in self.matiere_set.all() if mat.ProfMat==prof]
    
    def countAllMatByProf(self, prof):
        return len(self.AllMatByProf(prof))

    def countAllProfs(self): 
        Tot_Mat = self.AllMat()
        Tot_Profs = []
        for mat in Tot_Mat:
            if mat.ProfMat not in Tot_Profs:
                Tot_Profs.append(mat.ProfMat)
        return len(Tot_Profs)

    def countAllEleve(self):
        return self.eleve_set.all().count()  
    
    def getAllNotes(self):
        Matieres = self.AllMat()
        resuAllNoteByMat = [Mat.note_set.filter(eleveNote__ClassElev__codeClass=self.codeClass) for Mat in Matieres if Mat.note_set.filter(eleveNote__ClassElev__codeClass=self.codeClass).count() != 0]
        resuAllNote = []
        for clas in resuAllNoteByMat:
            for note in clas:
                resuAllNote.append(note)
        
        return [{"matier":note.matiereNote.nomMat,"MatriElev":note.eleveNote.MatriculeElev,"valnote":note.valeurNote} for note in resuAllNote]

    def TotcoeffClasse(self): 
        return sum([mat.coeffMat for mat in self.matiere_set.all()])
    
    def TotcoeffClasseProf(self, prof): 
        return sum([mat.coeffMat for mat in self.matiere_set.all() if mat.ProfMat==prof])


    def tot_note_givenbyClas(self, mat):
        ListElev = self.AllEleve()
        cnt = 0
        for elev in ListElev:
            for note in elev.get_note():
                if note.matiereNote == mat:
                    cnt += 1
        return cnt
    
    def pourc_note_givenByCls(self, mat):
        if self.countAllEleve() == 0:
            return 0
        return round((self.tot_note_givenbyClas(mat)/self.countAllEleve()) * 100)

    def tot_note_givenAllClas(self):
        totNoteGiven = sum([mat.tot_note_givenByC(self.nomClass) for mat in self.matiere_set.all()])
        totElev = self.countAllEleve()
        totMat = self.countAllMat()
        if totElev == 0 or totMat==0:
            return 0
        return  round((totNoteGiven/(totElev*totMat))*100)
    
    def tot_note_givenAllClasProf(self, prof):
        totNoteGiven = sum([mat.tot_note_givenByC(self.nomClass) for mat in self.matiere_set.filter(ProfMat=prof)])
        totElev = self.countAllEleve()
        totMat = self.countAllMatByProf(prof)
        if totElev == 0 or totMat==0:
            return 0
        return  round((totNoteGiven/(totElev*totMat))*100)

    def __str__(self):
        return str(self.nomClass)

    def __return__(self):
        return Classe()
    
    class Meta:
        ordering = ["nomClass"]

############## Création de la table professeur ##############
class Professeur(models.Model):
    nomProf = models.CharField(max_length=300)
    prenomProf = models.CharField(max_length=300)
    MatriculeProf = models.CharField(max_length=200,default="PROF-", unique=True)
    DateJoinProf = models.DateField()
    TelephoneProf = models.CharField(max_length=20)
    EmailProf = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    genreProf = models.CharField(max_length=200)
    DesignationProf = models.CharField(max_length=100)
    MatpossibProf = models.CharField(max_length=200)
    dateNaisProf = models.DateField()
    AdresseProf = models.CharField(max_length=200,default="rue 445, Douala")
    DescrptProf = models.CharField(max_length=400,default="Rien par rapport !")
    photoProf = models.ImageField(upload_to = "photosProfs/")

    def AllMatsProf(self):  
        return self.matiere_set.all()
    
    def CountAllMatsProf(self):  
        return self.matiere_set.all().count()
    
    def AllClassesProf(self): 
        AllMat = self.AllMatsProf()
        resu = []
        for mat in AllMat:
            for clas in mat.getClassMatObj():
                if clas not in resu:
                    resu.append(clas)
        return resu

    def AllElevesProf(self): 
        AllClass = self.AllClassesProf()
        print(AllClass)
        resu = []
        for clas in AllClass:
            lis = [elev for elev in clas.AllEleve()]
            resu += lis
        return resu

    def __str__(self):
        return str(self.nomProf)

    def __return__(self):
        return Professeur()
    
    class Meta:
        ordering = ["nomProf","prenomProf"]

############## Création de la table professeur ##############
class Administrateur(models.Model):
    nomAdmin = models.CharField(max_length=300)
    prenomAdmin = models.CharField(max_length=300)
    MatriculeAdmin = models.CharField(max_length=200,default="ADMIN-", unique=True)
    TelephoneAdmin = models.CharField(max_length=20)
    EmailAdmin = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    genreAdmin = models.CharField(max_length=200)
    dateNaisAdmin = models.DateField()
    AdresseAdmin = models.CharField(max_length=200,default="rue 445, Douala")
    DescrptAdmin = models.CharField(max_length=400,default="Rien par rapport !")
    photoAdmin = models.ImageField(upload_to = "photosProfs/")

    def __str__(self):
        return str(self.nomAdmin)

    def __return__(self):
        return Administrateur()
    
    class Meta:
        ordering = ["nomAdmin","prenomAdmin"]

############## Création de la table professeur ##############
class Matiere(models.Model):
    CodeMat = models.CharField(max_length=200, unique=True)
    nomMat = models.CharField(max_length=300)
    SurnomMat = models.CharField(max_length=300)
    ClassMat = models.ManyToManyField(Classe, blank=True)
    ProfMat = models.ForeignKey(Professeur, on_delete=models.SET_NULL,null=True, blank=True)
    state = models.BooleanField(default = False)
    coeffMat = models.IntegerField(default=1)
    groupMat = models.ForeignKey(Groupe, on_delete=models.SET_NULL,null=True)
    DescrptMat = models.CharField(max_length=400,default="Rien par rapport !")


    def getClassMat(self):
        return "-&-".join([c.nomClass for c in self.ClassMat.all()])  

    def getClassMatObj(self):

        return [c for c in self.ClassMat.all()] 

    def count_ClassMat(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        return len([c.nomClass for c in self.ClassMat.all()])   
    
    def listClass(self):
        return self.ClassMat.all()  

    def get_TotElev_ClassMat(self):
        listTot = [c.eleve_set.all().count() for c in self.ClassMat.all()]
        return sum(listTot)
    
    def tot_note_given(self):
        return self.note_set.all().count()
    
    def tot_note_givenByC(self,classe):
        return self.note_set.filter(eleveNote__ClassElev__nomClass=classe).count()

    def pourc_note_given(self):
        if self.get_TotElev_ClassMat() == 0:
            return 0
        return round((self.tot_note_given()/self.get_TotElev_ClassMat()) * 100)
    
    def pourc_note_givenByMats(self, clas):
        if clas.countAllEleve() == 0:
            return 0
        return round((self.tot_note_givenByC(clas)/clas.countAllEleve()) * 100)


    def __str__(self):
        return str(self.nomMat)

    def __return__(self):
        return Matiere()
    
    class Meta:
        ordering = ["nomMat"]
    

############## Création de la table professeur ##############
class Eleve(models.Model):
    MatriculeElev = models.CharField(max_length=200,default="ELEV-", unique=True)
    nomElev = models.CharField(max_length=300)
    prenomElev = models.CharField(max_length=300)
    TelephoneElev = models.CharField(max_length=20)
    photoElev = models.ImageField(upload_to = "photosEleves/")
    ClassElev = models.ForeignKey(Classe, on_delete=models.CASCADE)  # Maitre
    genreElev = models.CharField(max_length=200)
    dateNaisElev = models.DateField()
    AdresseElev = models.CharField(max_length=200,default="rue 445, Douala")

    def get_note(self):
        return self.note_set.all()

    def countAllnotes(self):
        return self.get_note().count()
    
    def get_MoyElev(self):
        return self.bulletindenote_set.get().MoyG
    
    def get_PourcMoyElev(self):
        return round((self.get_MoyElev()/20)*100, 2)
    
    def get_noteByMat(self,mat):
        resu = self.note_set.filter(matiereNote=mat)
        if resu.count()==0:
            return 0
        return resu[0]
    
    def __str__(self):
        return str(self.nomElev)

    def __return__(self):
        return Eleve()
    
    class Meta:
        ordering = ["nomElev","prenomElev"]


############## Création de la table professeur ##############
class Note(models.Model):
    valeurNote = models.IntegerField()
    eleveNote = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiereNote = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    CommentNote = models.CharField(max_length=200,default="Pas de commentaires à faire")

    def __str__(self):
        return self.eleveNote.nomElev+"-"+self.matiereNote.SurnomMat+"-"+str(self.valeurNote)

    def __return__(self):
        return Note()
    
    class Meta:
        ordering = ["eleveNote"]


############## Création de la table professeur ##############
class BulletinDeNote(models.Model):
    eleve = models.OneToOneField(Eleve, on_delete=models.CASCADE)
    ficheWordE = models.FileField(upload_to = "BulletinsEleves/", editable=False)
    MoyG = models.FloatField(default=0.0,editable=False)     
    Rang = models.CharField(max_length=10, default="not defined", editable=False)  
    RangGA = models.CharField(max_length=10, default="not defined", editable=False)   
    RangGB = models.CharField(max_length=10, default="not defined", editable=False)   
    RangGC = models.CharField(max_length=10, default="not defined", editable=False)
    
    def Get_All_Notes(self): # recherche de toutes les Objets Notes de l'eleve dans sa classe 
        return self.eleve.note_set.all()

    def Get_All_NoteCoef(self): # recherche de toutes les notes et coefficients de l'elève
        Notes = self.Get_All_Notes()
        ValNotesE = {}  # listes des notes et coefficients de l'elève
        for note in Notes:
            ValNotesE["Coef"+note.matiereNote.SurnomMat] = note.matiereNote.coeffMat
            ValNotesE["Note"+note.matiereNote.SurnomMat] = note.valeurNote
            ValNotesE["Coment"+note.matiereNote.SurnomMat] = note.CommentNote
        return ValNotesE

    def Set_MoyGE(self): # (SET MoyG) Reglage de la moyenne generale de l'elève
        Notes = self.Get_All_Notes()
        if Notes.count() == 0:
            return 0
        TotCoef = self.eleve.ClassElev.TotcoeffClasse()
        if TotCoef == 0:
            return 0
        Moy = 0
        for note in Notes:
            Moy += note.valeurNote * note.matiereNote.coeffMat
        Moy = round(Moy / TotCoef,2)
        self.MoyG = Moy
        self.save()
        return Moy
    
    def pourcReuiss(self):
        moy = self.Set_MoyGE()
        return round((moy/20)*100, 2)
    
    def pourcReuissC(self):
        moyGClass = self.MoyGeneraleC()
        return round((moyGClass/20)*100, 2)
    
    def Get_AllMoybyGroupE(self): # calcul de la moyenne generale et du total coefficients de l'elève par groupe
        # Reglage de toutes ses notes par matiere
        Notes = self.Get_All_Notes()
        Lgroupes = ["GA","GB","GC"]
        # Recuperation des notes de l'etudiant par Groupe de matieres
        LGA, LGB, LGC = [], [], []
        for note in Notes:
            lTemp = []
            if note.matiereNote.groupMat.nomGroup == "GROUPE A":
                LGA.append(note)
            elif note.matiereNote.groupMat.nomGroup == "GROUPE B":
                LGB.append(note)
            else:
                LGC.append(note)
        ListMatNotesByG = [LGA, LGB, LGC]

        # Extration des donnees pour chaque groupe de matieres de l'etudiant:
            # Total coefficients par groupe
            # moyenne de l'eleve par groupe
            #
        dico = {}
        for listNGrp, gp in zip(ListMatNotesByG, Lgroupes):
            Totcoef = self.Calcul_TotCoef_Lnotes(listNGrp)
            MoyGrpE = self.Calcul_MoyFGroupNotes(listNGrp)
            dico["TotCoef"+gp] = Totcoef
            dico["MoyNotes"+gp] = MoyGrpE

        return dico

    def Get_AllMoybyGroupC(self): # Calcul de la moyenne generale et du total coefficients de l'elève par groupe
        # Recuperation de toutes les moyennes par matiere
        ListAllMoyByMat = self.Get_Set_AllMoyByMat()[1]

        # Recuperation de toutes les moyennes par matiere par Groupe de matieres
        LGA, LGB, LGC = [], [], []
        for elt in ListAllMoyByMat:
            temp = [elt["mat"].coeffMat, elt["MoyM"]]
            if elt["mat"].groupMat.nomGroup == "GROUPE A":
                LGA.append(temp)
            elif elt["mat"].groupMat.nomGroup == "GROUPE B":
                LGB.append(temp)
            else:
                LGC.append(temp)
        ListMatMoyByG = [LGA, LGB, LGC]

        # Extration des donnees pour chaque groupe de matieres de la classe:
            # moyenne de la classe par groupe de matieres
        Lgroupes = ["GA","GB","GC"]
        dico = {}
        for listMoyGrp, gp in zip(ListMatMoyByG,Lgroupes):
            # Somme des coefficients du groupe
            sumCoeff = sum([lMMG[0] for lMMG in listMoyGrp])
            if sumCoeff == 0 :
                return 0
            # Moyenne du groupe
            moy = sum([lMMG[0]*lMMG[1] for lMMG in listMoyGrp])/sumCoeff
            dico["MoyC"+gp] = round(moy,2)
            dico["TOTcoefC"+gp] = sumCoeff

        return dico
  
    def Get_AllNotesByMat(self): #Recherche de toutes les notes de la classe par matiere
        # Obtention de toutes les matieres de la classe
        AllMats = self.eleve.ClassElev.AllMat()
        # Retour de la liste de toutes les notes de la classe par matiere
        return [Mat.note_set.filter(eleveNote__ClassElev=self.eleve.ClassElev) for Mat in AllMats ]

    def Get_Set_AllMoyByMat(self): # Recherche et reglage (SET MoybyMatC) de toutes les moyennes de la classe par matiere
        # Obtention de toutes les matieres de la classe
        AllMats = self.eleve.ClassElev.AllMat()
        # Obtention de toutes les moyennes de la classe par matiere
        ListAllNotesByMat = self.Get_AllNotesByMat()
        Eff = len(ListAllNotesByMat[0])
        nomRangs = ["1er"]+[str(i)+"ème" for i in range(2,Eff+1)]
        Notes = self.Get_All_Notes()
        dicoNotes={note.matiereNote.SurnomMat:note.valeurNote for note in Notes}
        MoybyMatC = {}
        for mat, LNotesmat in zip(AllMats,ListAllNotesByMat):
            MoybyMatC["MoyC"+mat.SurnomMat] = self.Calcul_MoyFGroupNotes(LNotesmat)
            notes = [elt["valeurNote"] for elt in LNotesmat.values("valeurNote")]

            trieCnotes = sorted(notes,reverse=True)

            rang = nomRangs[trieCnotes.index(dicoNotes[mat.SurnomMat])]
            MoybyMatC["NoteMin"+mat.SurnomMat] = min(notes)
            MoybyMatC["NoteMax"+mat.SurnomMat] = max(notes)
            MoybyMatC["Rang"+mat.SurnomMat] = rang

        return MoybyMatC, [{"mat":mat,"MoyM":self.Calcul_MoyFGroupNotes(LNotesmat)} for mat, LNotesmat in zip(AllMats,ListAllNotesByMat)]

    def MoyGeneraleC(self):
        dicoMoyGpes = self.Get_AllMoybyGroupC()
        sum = 0
        totcoef = 0
        Lgroupes = ["GA","GB","GC"]
        for gp in Lgroupes:
            sum += dicoMoyGpes["MoyC"+gp] * dicoMoyGpes["TOTcoefC"+gp]
            totcoef += dicoMoyGpes["TOTcoefC"+gp]
        if totcoef == 0:
            return 0
        return round(sum/totcoef,2)

    def DatasbyGroup(self):
        Notes = self.Get_All_Notes()
        Notes = self.Get_All_Notes()
        Lgroupes = ["GA","GB","GC"]
        # Recuperation des notes de l'etudiant par Groupe de matieres
        LGA, LGB, LGC = [], [], []
        for note in Notes:
            lTemp = []
            if note.matiereNote.groupMat.nomGroup == "GROUPE A":
                LGA.append(note)
            elif note.matiereNote.groupMat.nomGroup == "GROUPE B":
                LGB.append(note)
            else:
                LGC.append(note)
        ListMatNotesByG = [LGA, LGB, LGC]
        ValNotesE = self.Get_All_NoteCoef()
        MoybyMatC = self.Get_Set_AllMoyByMat()[0]
        MoybyGrpE = self.Get_AllMoybyGroupE()
        MoybyGrpC = self.Get_AllMoybyGroupC()
        
        datGroup = []
        for listNGrp, gp in zip(ListMatNotesByG, Lgroupes):
            dico = [{"nomMat":note.matiereNote.nomMat,"Coeff":note.matiereNote.coeffMat,"noteE":ValNotesE["Note"+note.matiereNote.SurnomMat],
                        "min":MoybyMatC["NoteMin"+note.matiereNote.SurnomMat],"max":MoybyMatC["NoteMax"+note.matiereNote.SurnomMat],
                        "moyM":MoybyMatC["MoyC"+note.matiereNote.SurnomMat],"comment":note.CommentNote,
                    } for note in listNGrp]
            datGen = {"nom":"Moyenne "+gp,"TotcoefG":MoybyGrpE["TotCoef"+gp],"moyE":MoybyGrpE["MoyNotes"+gp],"moyC":MoybyGrpC["MoyC"+gp]}
            
            datGroup.append({"datGen":datGen,"dico":dico})
        
        return datGroup

    def createBulletinWord(self):
        # Ouverture du fichier model de la classe
        doc = DocxTemplate(self.eleve.ClassElev.ficheWordModel)

        moyGclass = self.MoyGeneraleC()
        print(moyGclass)
        # Dictionnaire du contennu a completer sur le ficier word
        context = {"MoyNotesG":self.MoyG,"TotCoefG":self.eleve.ClassElev.TotcoeffClasse(),
                    "NonElev":self.eleve.nomElev+" "+self.eleve.prenomElev,
                    "nomClasse":self.eleve.ClassElev.nomClass,"MoyCG":moyGclass,
                    "RangG":self.Rang,"RangGA":self.RangGA,"RangGB":self.RangGB,"RangGC":self.RangGC}

        # Ajout des variables dans le dictionnaire
        ALlNotCef = self.Get_All_NoteCoef()  # Donnees sur les matieres et les notes de l'eleve sur ces matieres
        ListItem_ALlNotCef =  list(ALlNotCef.keys())
        for item in ListItem_ALlNotCef:
            context[item] = ALlNotCef[item]

        ALlMOYBYGROUPE = self.Get_AllMoybyGroupE()  # Donnees sur ses moyennes par groupe de matieres et du total coef par groupe
        ListItem_ALlMOYBYGROUPE =  list(ALlMOYBYGROUPE.keys())
        for item in ListItem_ALlMOYBYGROUPE:
            context[item] = ALlMOYBYGROUPE[item]
        
        ALlMOYBYGROUPC = self.Get_AllMoybyGroupC()
        ListItem_ALlMOYBYGROUPC =  list(ALlMOYBYGROUPC.keys())
        for item in ListItem_ALlMOYBYGROUPC:
            context[item] = ALlMOYBYGROUPC[item]

        ALLMOYBYMAT = self.Get_Set_AllMoyByMat()[0]
        ListItem_ALLMOYBYMAT =  list(ALLMOYBYMAT.keys())
        for item in ListItem_ALLMOYBYMAT:
            context[item] = ALLMOYBYMAT[item]

        doc.render(context)
        print(self.ficheWordE.url)
        path = "media/BulletinsEleves/"+self.eleve.nomElev+" "+self.eleve.prenomElev+".docx"
        doc.save(path)
        self.ficheWordE = path[5:]
        self.save()

    def Calcul_TotCoef_Lnotes(self,LNotesmat):
        TotCoef = [note.matiereNote.coeffMat for note in LNotesmat]
        return sum(TotCoef)

    def Calcul_MoyFGroupNotes(self,LNotesmat):
        TotCoef = self.Calcul_TotCoef_Lnotes(LNotesmat)
        if TotCoef == 0:
            return 0
        Moy = 0
        for note in LNotesmat:
            Moy += note.valeurNote * note.matiereNote.coeffMat
        
        return round(Moy / TotCoef,2)

    def __str__(self):
        return str(self.eleve.nomElev)

    def __return__(self):
        return BulletinDeNote()
    
    class Meta:
        ordering = ["eleve"]