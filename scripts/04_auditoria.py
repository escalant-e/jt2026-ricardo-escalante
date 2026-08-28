import pandas as pd
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "output", "dados")

master = pd.read_csv(os.path.join(OUT, "master_joined.csv"), encoding="utf-8", low_memory=False)

print("Linhas:", len(master), "| Colunas:", len(master.columns))
print("=" * 60)

# ---- 1. Nulos / vazios nos campos de integridade de join ----
print("\n[1] INTEGRIDADE DO JOIN (nulos / vazios)")

def describe_null(ser, label):
    total = ser.isna().sum()
    pct = total / len(master) * 100
    # também conta strings vazias
    if ser.dtype == "object":
        vazias = (ser.str.strip() == "").sum() if total < len(master) else 0
    else:
        vazias = 0
    print(f"  {label:<28} nulos={total:>5} ({pct:5.1f}%)  vazios={vazias}")

describe_null(master.get("suburb"), "suburb")
describe_null(master["owner"], "host owner (nome)")
describe_null(master["is_superhost"], "host is_superhost")
describe_null(master["number_of_reviews_host"], "host num_reviews")
describe_null(master["star_rating_host"], "host star_rating")
describe_null(master["diaria_media"], "diaria_media")
describe_null(master["dias_ocupados"], "dias_ocupados")

print("\n  -> Linhas onde suburb é nulo/vazio:")
mask_suburb = master["suburb"].isna() | (master["suburb"].astype(str).str.strip() == "")
print("    count:", mask_suburb.sum())

# ---- 2. Resumo estatístico das diárias + outliers ----
print("\n[2] RESUMO ESTATÍSTICO DIÁRIA MÉDIA (com preço, n=999)")
d = master["diaria_media"].dropna()
print("  describe:")
print(d.describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]).to_string())
print("  min:", d.min(), "| max:", d.max())
print("  n diárias <= 0:", (master["diaria_media"] <= 0).sum())
# outliers: valores acima do P99 e acima de certos limiares
p99 = d.quantile(0.99)
p999 = d.quantile(0.999) if 0.999 <= 1 else d.max()
print("  P99:", round(p99, 2))
print("  qnt acima de P99:", (d > p99).sum())

# diarias bem altas (ex: > 3000)
print("  diária > 3000:", (d > 3000).sum())
print("  diária > 5000:", (d > 5000).sum())
print("\n  amostra diárias top 10 (mais caras):")
print(d.sort_values(ascending=False).head(10).to_string())

# ---- 3. Listagem de bairros únicos ----
print("\n[3] BAIRROS ÚNICOS (grafia)")
print(master["suburb"].astype(str).value_counts(dropna=False).to_string())