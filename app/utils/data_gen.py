# Geração de dados sintéticos (sem banco) para demonstrar ingestão
import pandas as pd
import numpy as np

def generate_raw_data(seed: int = 42) -> pd.DataFrame:
    # Define uma semente para reprodutibilidade
    rng = np.random.default_rng(seed)

    # Cria colunas com erros intencionais: NaN, duplicatas e outliers
    n = 60
    ids = np.arange(1, n + 1)

    # Idades com alguns NaN e um outlier
    idade = rng.integers(18, 65, size=n).astype(float)
    idade[rng.choice(n, size=5, replace=False)] = np.nan   # faltantes
    idade[rng.choice(n, size=1, replace=False)] = 180.0    # outlier

    # Salários como strings de moeda (para testar conversão)
    salario_num = rng.normal(4500, 1000, size=n).round(2)
    salario_num[salario_num < 0] = 1500  # evita valores negativos
    salario_str = [f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") for v in salario_num]

    # Datas como strings em formatos diversos
    datas = pd.date_range("2024-01-01", periods=n, freq="D").astype(str)
    datas = np.array(datas)
    # Introduz alguns formatos diferentes
    for i in rng.choice(n, size=5, replace=False):
        datas[i] = datas[i].replace("-", "/")
    for i in rng.choice(n, size=5, replace=False):
        y, m, d = datas[i].split("/") if "/" in datas[i] else datas[i].split("-")
        datas[i] = f"{d}/{m}/{y}"

    # Categoria com duplicatas e NaN
    categorias = rng.choice(["A", "B", "C"], size=n).astype(object)
    categorias[rng.choice(n, size=4, replace=False)] = None

    df = pd.DataFrame({
        "id": ids,
        "nome": rng.choice(["Ana", "Bruno", "Carla", "Diego", "Eva", None], size=n),
        "idade": idade,
        "salario": salario_str,   # string de moeda
        "data_compra": datas,     # datas em string de formatos variados
        "categoria": categorias
    })

    # Duplica algumas linhas de propósito
    dup_idx = rng.choice(n, size=5, replace=False)
    df = pd.concat([df, df.iloc[dup_idx]], ignore_index=True)

    return df
