# Limpeza Inteligente (IA + Regras) — sem banco, operando sobre DataFrames
import pandas as pd
import numpy as np
import re
from sklearn.impute import KNNImputer
from sklearn.ensemble import IsolationForest

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    # Converte strings de moeda (ex: 'R$ 1.234,56') para float
    def parse_money(x):
        if pd.isna(x):
            return np.nan
        s = str(x)
        # remove tudo que não for número, vírgula ou ponto
        s = re.sub(r"[^0-9,\.]", "", s)
        # se houver vírgula como decimal, troca por ponto
        if s.count(",") == 1 and (s.rfind(",") > s.rfind(".")):
            s = s.replace(".", "").replace(",", ".")
        return pd.to_numeric(s, errors="coerce")
    return series.map(parse_money)

def _to_datetime_flexible(series: pd.Series) -> pd.Series:
    # Tenta converter várias formatações de data para datetime
    return pd.to_datetime(series, errors="coerce", dayfirst=True, infer_datetime_format=True)

def analyze(df: pd.DataFrame) -> dict:
    # Calcula estatísticas descritivas úteis para relatório
    stats = {
        "rows": len(df),
        "cols": len(df.columns),
        "missing_total": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum())
    }
    # Conta outliers numéricos com Isolation Forest (sem remover ainda)
    num = df.select_dtypes(include=[np.number])
    if not num.empty:
        iso = IsolationForest(contamination=0.05, random_state=42)
        pred = iso.fit_predict(num.fillna(num.median()))
        stats["outliers_estimated"] = int((pred == -1).sum())
    else:
        stats["outliers_estimated"] = 0
    return stats

def intelligent_clean(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    report = {}

    # ===== 1) Conversões de tipo antes da imputação =====
    df = df.copy()

    # Tenta converter colunas suspeitas de moeda e data
    if "salario" in df.columns:
        df["salario"] = _to_numeric_currency(df["salario"])

    if "data_compra" in df.columns:
        df["data_compra"] = _to_datetime_flexible(df["data_compra"])

    # ===== 2) Análise antes =====
    report["before"] = analyze(df)

    # ===== 3) Imputação com KNN para numéricos =====
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        imputer = KNNImputer(n_neighbors=3)
        df[num_cols] = imputer.fit_transform(df[num_cols])

    # ===== 4) Strings: preenche faltantes com marcador =====
    obj_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
    for c in obj_cols:
        df[c] = df[c].fillna("Desconhecido")

    # ===== 5) Remoção de duplicatas =====
    report["duplicates_removed"] = int(df.duplicated().sum())
    df = df.drop_duplicates()

    # ===== 6) Detecção e remoção de outliers numéricos =====
    if num_cols:
        iso = IsolationForest(contamination=0.05, random_state=42)
        preds = iso.fit_predict(df[num_cols])
        outliers_mask = preds == -1
        report["outliers_removed"] = int(outliers_mask.sum())
        df = df.loc[~outliers_mask].reset_index(drop=True)
    else:
        report["outliers_removed"] = 0

    # ===== 7) Conversões finais / normalizações simples =====
    # Exemplo: garantir tipos consistentes
    if "data_compra" in df.columns:
        # Converte datetime de volta para string ISO para exportar facilmente
        df["data_compra"] = df["data_compra"].dt.strftime("%Y-%m-%d")

    # ===== 8) Análise depois =====
    report["after"] = analyze(df)

    return df, report
