# Módulo de usuário — placeholder para o futuro
from flask import Blueprint, render_template

# Cria o blueprint de usuário
user_bp = Blueprint("user", __name__, template_folder="../../templates")

@user_bp.route("/profile")
def profile():
    # Apenas uma página simples por enquanto
    return render_template("profile.html")
