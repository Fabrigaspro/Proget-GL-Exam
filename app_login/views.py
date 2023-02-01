from django.shortcuts import render, redirect
from SCOOLAPP.models import Classe, Type, Matiere, Professeur,Eleve,Note, Groupe, BulletinDeNote, Administrateur
from django.http import JsonResponse,  HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app_Professors.views import *

# Create your views here.

def PageLogin(Request):
    return render(Request, "app_login/page-login.html")


def Login(Request):
    print(Request.method)
    if Request.method == "POST":
        username = Request.POST["username"]
        password = Request.POST["password"]

    else:
        return redirect('PageLogin')
    print("#######################")
    print(username, password)
    user = authenticate(username=username, password=password)

    if user is None :
        msg = "echec d'authentification. Le nom d'utilisateur ou le mot de passe est incorrect"
        return render (Request, "app_login/page-login.html",{"msg":msg,"UserN":username,"PWD":password})
    
    login(Request, user)
    try:
        Admin = Administrateur.objects.get(Username=username)
        return redirect("acceuilAdmin")
    except:
        professor = Professeur.objects.get(Username=username)
        return redirect("acceuilProf")

@login_required
def Logout(Request):
    logout(Request)
    return redirect('PageLogin')