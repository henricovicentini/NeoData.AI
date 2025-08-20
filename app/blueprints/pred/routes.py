# Rotas de predição/limpeza — usam dados sintéticos e limpeza inteligente
from flask import Blueprint, render_template, send_file, jsonify
import os
import pandas as pd
from io import BytesIO

from app.utils.data_gen import generate_raw_data
from app.utils.cleaner import intelligent_clean, analyze

# Cria o blueprint
pred_bp = Blueprint("pred", __name__, template_folder="../../templates")

# Caminho para salvar o CSV limpo
CLEAN_DIR = "data/cleaned"
CLEAN_FILE = os.path.join(CLEAN_DIR, "dados_limpos.csv")

@pred_bp.route("/raw")
def raw():
    # Gera um DataFrame com erros simulados
    df = generate_raw_data()
    # Calcula estatísticas "antes"
    stats = analyze(df)
    # Renderiza a tabela e as estatísticas
    return render_template("raw.html",
                           table=df.to_html(classes="table table-striped", index=False),
                           stats=stats)

@pred_bp.route("/clean")
def clean():
    # Gera dados crus
    df_raw = generate_raw_data()
    # Aplica limpeza inteligente
    df_clean, report = intelligent_clean(df_raw)

    # Garante diretório de saída
    os.makedirs(CLEAN_DIR, exist_ok=True)
    # Salva CSV limpo
    df_clean.to_csv(CLEAN_FILE, index=False, encoding="utf-8")

    # Mostra tabela e relatório
    return render_template("clean.html",
                           table=df_clean.to_html(classes="table table-striped", index=False),
                           report=report,
                           download_path="/pred/download")

@pred_bp.route("/download")
def download():
    # Faz download do CSV limpo gerado em /clean
    if not os.path.exists(CLEAN_FILE):
        # Se ainda não foi limpo, faz agora para garantir a existência
        df_raw = generate_raw_data()
        df_clean, _ = intelligent_clean(df_raw)
        os.makedirs(CLEAN_DIR, exist_ok=True)
        df_clean.to_csv(CLEAN_FILE, index=False, encoding="utf-8")

    # Envia o arquivo como anexo
    return send_file(CLEAN_FILE, as_attachment=True, download_name="dados_limpos.csv")
