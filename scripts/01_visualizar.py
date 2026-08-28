import pandas as pd
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

files = [
    "Details_Itapema.csv",
    "Hosts_ids_Itapema.csv",
    "Mesh_Ids_Data_Itapema.csv",
    "Price_AV_Itapema.csv",
    "VivaReal_Itapema.csv",
]

blocos = []

for fn in files:
    df = pd.read_csv(os.path.join(DATA, fn), encoding="utf-8", low_memory=False)
    n_linhas = len(df)
    n_cols = df.shape[1]

    # termina
    print(f"\n===== {fn} =====")
    print(f"Linhas: {n_linhas:,}  |  Colunas: {n_cols}")
    print("Tipos:")
    print(df.dtypes.to_string())
    print("Nulos por coluna:")
    print(df.isna().sum().to_string())
    print("Primeiras 5 linhas:")
    print(df.head(5).to_string())

    # HTML
    meta = pd.DataFrame({
        "coluna": df.columns,
        "tipo": [str(t) for t in df.dtypes],
        "nulos": df.isna().sum().values,
        "nao_nulos": df.notna().sum().values,
    })
    h = f"<h2>{fn} <small>({n_linhas:,} linhas | {n_cols} colunas)</small></h2>"
    h += "<p><b>Amostra (5 primeiras linhas):</b></p>"
    h += df.head(5).to_html(border=0, justify="left", index=True)
    h += "Nulos mais comuns por coluna: n/a (todas listadas abaixo)<p><b>Metadados (tipo e nulos por coluna):</b></p>"
    h += meta.to_html(border=0, index=False, justify="left")
    h += "<hr/>"

    blocos.append(h)

master = """<!DOCTYPE html>
<html lang="pt"><head><meta charset="utf-8">
<title>Inspecao das 5 bases - Hackathon Itapema</title>
<style>td,th{border:1px solid #ccc;padding:5px;font-size:12px}
table{border-collapse:collapse;margin-bottom:10px}
body{font-family:sans-serif;padding:20px} h2{color:#2c3e50}</style>
</head><body>
<h1>Inspecao dos dados brutos - 5 arquivos</h1>
"""
with open(os.path.join(OUT, "visualizacao_brutos.html"), "w", encoding="utf-8") as f:
    f.write(master)
    for b in blocos:
        f.write(b)
    f.write("</body></html>")

print("\n[OK] HTML salvo em", os.path.join(OUT, "visualizacao_brutos.html"))