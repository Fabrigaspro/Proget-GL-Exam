from django.contrib import admin

from .models import Type, Classe, Professeur, Matiere, Eleve
# Register your models here.
####################################################################################################
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id","CodeTyp", "nomTyp")
    search_fields = ["nomTyp"]

admin.site.register(Type, TypeAdmin)

####################################################################################################
class ClasseAdmin(admin.ModelAdmin):
    list_display = ("id","codeClass", "nomClass","descrpClass","typClass","state")
    search_fields = ["nomClass"]

admin.site.register(Classe, ClasseAdmin)

####################################################################################################
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ("id","MatriculeProf", "nomProf", "prenomProf","TelephoneProf","EmailProf","photoProf","state")
    search_fields = ["nomProf"]

admin.site.register(Professeur, ProfesseurAdmin)

####################################################################################################
class MatiereAdmin(admin.ModelAdmin):
    list_display = ("id","CodeMat", "nomMat","getClassMat","ProfMat","state")
    search_fields = ["nomMat"]

admin.site.register(Matiere, MatiereAdmin)

####################################################################################################
class EleveAdmin(admin.ModelAdmin):
    list_display = ("id","MatriculeElev", "nomElev", "prenomElev","ClassElev","genreElev","dateNaisElev","TelephoneElev","photoElev","state")
    search_fields = ["nomElev"]

admin.site.register(Eleve, EleveAdmin)