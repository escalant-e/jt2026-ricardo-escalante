import pandas as pd
import os, io, sys

pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

def load(fn):
    return pd.read_csv(os.path.join(DATA, fn), encoding="utf-8", low_memory=False)

files = [
    "Details_Itapema.csv",
    "Hosts_ids_Itapema.csv",
    "Mesh_Ids_Data_Itapema.csv",
    "Price_AV_Itapema.csv",
    "VivaReal_Itapema.csv",
]

buf = io.StringIO()
for fn in files:
    df = load(fn)
    print(f"===== {fn} =====", file=buf)
    print(f"Linhas: {len(df):,}    Colunas: {df.shape[1]}", file=buf)
    print("Colunas:", list(df.columns), file=buf)
    print("\n-- dtypes --", file=buf)
    print(df.dtypes.to_string(), file=buf)
    print("\n-- nulos (%) --", file=buf)
    na = df.isna().mean() * 100
    na = na[na > 0].sort_values(ascending=False)
    print(na.to_string() if len(na) else "sem nulos", file=buf)
    print("\n-- head --", file=buf)
    print(df.head(2).to_string(), file=buf)
    print("\n\n", file=buf)

print(buf.getvalue())