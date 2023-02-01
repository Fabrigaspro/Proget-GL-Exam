from django.contrib import admin

from .models import Type, Classe, Professeur, Matiere, Eleve,Note,Groupe, BulletinDeNote, Administrateur
# Register your models here.
####################################################################################################
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id","CodeTyp", "nomTyp")
    search_fields = ["nomTyp"]

admin.site.register(Type, TypeAdmin)
####################################################################################################
class GroupeAdmin(admin.ModelAdmin):
    list_display = ("id", "nomGroup")
    search_fields = ["nomGroup"]

admin.site.register(Groupe, GroupeAdmin)
####################################################################################################
class ClasseAdmin(admin.ModelAdmin):
    list_display = ("id","codeClass", "nomClass","ficheWordModel","AllEleve","getAllNotes","descrpClass","typClass")
    search_fields = ["nomClass"]

admin.site.register(Classe, ClasseAdmin)

####################################################################################################
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ("id","MatriculeProf", "nomProf", "prenomProf","AllMatsProf","AllClassesProf","AllElevesProf","genreProf","dateNaisProf","DesignationProf","MatpossibProf","TelephoneProf","EmailProf","AdresseProf","DateJoinProf","Username","password","photoProf")
    search_fields = ["nomProf"]

admin.site.register(Professeur, ProfesseurAdmin)

####################################################################################################
class MatiereAdmin(admin.ModelAdmin):
    list_display = ("id","CodeMat", "nomMat","SurnomMat","groupMat","coeffMat","getClassMat","tot_note_given","get_TotElev_ClassMat","ProfMat")
    search_fields = ["nomMat"]

admin.site.register(Matiere, MatiereAdmin)

####################################################################################################
class EleveAdmin(admin.ModelAdmin):
    list_display = ("id","MatriculeElev", "nomElev","get_MoyElev", "prenomElev","ClassElev","dateNaisElev","TelephoneElev","AdresseElev","photoElev")
    search_fields = ["nomElev"]

admin.site.register(Eleve, EleveAdmin)

####################################################################################################
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "valeurNote", "eleveNote","matiereNote","CommentNote")
    search_fields = ["eleveNote"]

admin.site.register(Note, NoteAdmin)

####################################################################################################
class BulletinDeNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "ficheWordE", "eleve","MoyG","Get_AllMoybyGroupE","Get_AllMoybyGroupC",)
    search_fields = ["eleve"]

admin.site.register(BulletinDeNote, BulletinDeNoteAdmin)

####################################################################################################
class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ("id","MatriculeAdmin", "nomAdmin", "prenomAdmin","TelephoneAdmin","EmailAdmin","Username","password", "genreAdmin", "dateNaisAdmin", "AdresseAdmin", "DescrptAdmin","photoAdmin")
    search_fields = ["eleve"]

admin.site.register(Administrateur, AdministrateurAdmin)
