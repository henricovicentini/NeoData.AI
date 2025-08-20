# Módulo de autenticação — placeholder para o futuro
from flask import Blueprint, render_template

# Cria o blueprint de auth (login/registro no futuro)
auth_bp = Blueprint("auth", __name__, template_folder="../../templates")

@auth_bp.route("/login")
def login():
    # Apenas uma página simples por enquanto
    return render_template("login.html")
