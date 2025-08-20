# Rotas de gráficos — gera imagens Matplotlib comparando antes/depois
from flask import Blueprint, render_template
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # backend sem janela (necessário em servidores)
import matplotlib.pyplot as plt

from app.utils.data_gen import generate_raw_data
from app.utils.cleaner import intelligent_clean

graph_bp = Blueprint("graph", __name__, template_folder='../../templates', static_folder='../../static')

# Pasta onde salvaremos as imagens
GRAPH_DIR = "app/static/graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

@graph_bp.route("/plot")
def plot():
    # Gera dados e limpa
    raw = generate_raw_data()
    clean, report = intelligent_clean(raw)

    # Gera histograma de 'idade' antes/depois (se existir)
    if "idade" in raw.columns:
        # Antes
        plt.figure()
        raw["idade"].dropna().plot.hist(alpha=0.5)
        plt.title("Distribuição de Idade - Antes")
        idade_before_path = os.path.join(GRAPH_DIR, "idade_antes.png")
        plt.savefig(idade_before_path, bbox_inches="tight")
        plt.close()

        # Depois
        plt.figure()
        clean["idade"].dropna().plot.hist(alpha=0.5)
        plt.title("Distribuição de Idade - Depois")
        idade_after_path = os.path.join(GRAPH_DIR, "idade_depois.png")
        plt.savefig(idade_after_path, bbox_inches="tight")
        plt.close()
    else:
        idade_before_path = idade_after_path = None

    # Histograma de salário (numérico) antes/depois (se existir)
    if "salario" in raw.columns:
        # Antes (converter para numérico para plot)
        plt.figure()
        pd.to_numeric(raw["salario"], errors="coerce").dropna().plot.hist(alpha=0.5)
        plt.title("Distribuição de Salário - Antes")
        sal_before_path = os.path.join(GRAPH_DIR, "salario_antes.png")
        plt.savefig(sal_before_path, bbox_inches="tight")
        plt.close()

        # Depois (já está numérico)
        plt.figure()
        pd.to_numeric(clean["salario"], errors="coerce").dropna().plot.hist(alpha=0.5)
        plt.title("Distribuição de Salário - Depois")
        sal_after_path = os.path.join(GRAPH_DIR, "salario_depois.png")
        plt.savefig(sal_after_path, bbox_inches="tight")
        plt.close()
    else:
        sal_before_path = sal_after_path = None

    # Renderiza a página do dashboard com as imagens
    return render_template(
        "dashboard.html",
        idade_before=os.path.basename(idade_before_path) if idade_before_path else None,
        idade_after=os.path.basename(idade_after_path) if idade_after_path else None,
        sal_before=os.path.basename(sal_before_path) if sal_before_path else None,
        sal_after=os.path.basename(sal_after_path) if sal_after_path else None,
    )
