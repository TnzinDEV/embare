from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CadastroForm


def home_view(request):
    return render(request, "home.html")


def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect("perfil")

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Autentica automaticamente após cadastro válido.
            auth_login(request, user)

            messages.success(
                request,
                "Sua conta foi criada com sucesso. Bem-vindo à Embaré Kraft!",
            )

            return redirect("perfil")
    else:
        form = CadastroForm()

    return render(request, "cadastro.html", {"form": form})


@login_required(login_url="login")
def perfil_view(request):
    return render(
        request,
        "perfil.html",
        {"account_user": request.user},
    )