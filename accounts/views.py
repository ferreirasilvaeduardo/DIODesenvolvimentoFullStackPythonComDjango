from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def authenticate_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("contacts:create"))
        else:
            # Return an 'invalid login' error message.
            context = {"message": "Usuário ou senha inválidos!"}
    return render(request, "accounts/login.html", context)


def logout_user(request):
    context = {}
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))
