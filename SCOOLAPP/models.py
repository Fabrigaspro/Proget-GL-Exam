from django.db import models

# Create your models here.

############## Création de la table Type de classe ##############
class Type(models.Model):
    CodeTyp = models.CharField(max_length=100)
    nomTyp = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nomTyp)

    def __return__(self):
        return Type()

############## Création de la table professeur ##############
class Classe(models.Model):
    codeClass = models.CharField(max_length=100)
    nomClass = models.CharField(max_length=100)
    descrpClass = models.CharField(max_length=300)
    typClass = models.ForeignKey(Type, on_delete=models.CASCADE)
    state = models.BooleanField(default = False)

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
    MatriculeProf = models.CharField(max_length=200)
    TelephoneProf = models.CharField(max_length=20)
    EmailProf = models.CharField(max_length=100)
    photoProf = models.ImageField(upload_to = "photosProfs/")
    state = models.BooleanField(default = False)

    def __str__(self):
        return str(self.nomProf)

    def __return__(self):
        return Professeur()
    
    class Meta:
        ordering = ["nomProf","prenomProf"]

############## Création de la table professeur ##############
class Matiere(models.Model):
    CodeMat = models.CharField(max_length=200)
    nomMat = models.CharField(max_length=300)
    ClassMat = models.ManyToManyField(Classe)
    ProfMat = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    state = models.BooleanField(default = False)

    def getClassMat(self):
        return "["+",\n".join([c.nomClass for c in self.ClassMat.all()])+"]"

    def __str__(self):
        return str(self.nomMat)

    def __return__(self):
        return Matiere()
    
    class Meta:
        ordering = ["nomMat"]
    

############## Création de la table professeur ##############
class Eleve(models.Model):
    MatriculeElev = models.CharField(max_length=200)
    nomElev = models.CharField(max_length=300)
    prenomElev = models.CharField(max_length=300)
    TelephoneElev = models.CharField(max_length=20)
    photoElev = models.ImageField(upload_to = "photosEleves/")
    ClassElev = models.ForeignKey(Classe, on_delete=models.CASCADE)
    genreElev = models.CharField(max_length=200)
    dateNaisElev = models.DateField()
    state = models.BooleanField(default = False)

    def __str__(self):
        return str(self.nomElev)

    def __return__(self):
        return Eleve()
    
    class Meta:
        ordering = ["nomElev","prenomElev"]