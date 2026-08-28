import pandas as pd
import unicodedata, os

OUT = os.path.join(os.path.dirname(__file__), "..", "output")

def norm_suburb(s):
    if pd.isna(s):
        return pd.NA
    s = "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn")
    s = s.upper().strip()
    if "MEIA PRAIA" in s:
        return "MEIA PRAIA"
    m = {"TABOLEIRO": "TABULEIRO DOS OLIVEIRAS", "TABULEIRO": "TABULEIRO DOS OLIVEIRAS"}
    return m.get(s, s)

def faixa_quartos(n):
    if pd.isna(n):
        return pd.NA
    n = int(n)
    if n <= 1:
        return "1Q"
    if n == 2:
        return "2Q"
    if n == 3:
        return "3Q"
    return "4Q+"

# Airbnb
air = pd.read_csv(os.path.join(OUT, "preco_ok.csv"), encoding="utf-8", low_memory=False)
air["suburb_norm"] = air["suburb"].apply(norm_suburb)
air["tipologia"] = air["number_of_bedrooms"].apply(faixa_quartos)
air = air[air["suburb_norm"].notna() & air["tipologia"].notna()].copy()

# VivaReal limpo (mesmas regras)
viva = pd.read_csv(os.path.join("data", "VivaReal_Itapema.csv"), encoding="utf-8", low_memory=False)
viva = viva[viva["listing_type"] == "apartamento"]
viva = viva[(viva["sale_price"] >= 100000) & (viva["usable_area"] >= 15)]
viva["suburb_norm"] = viva["suburb"].apply(norm_suburb)
viva["tipologia"] = viva["bedrooms"].apply(faixa_quartos)
viva = viva[viva["suburb_norm"].notna() & viva["tipologia"].notna()].copy()

air_g = (air.groupby(["suburb_norm", "tipologia"])
            .agg(receita_anual=("receita_bruta_base", "median"),
                 n_air=("airbnb_listing_id", "count"))
            .reset_index())
viva_g = (viva.groupby(["suburb_norm", "tipologia"])
              .agg(area_mediana=("usable_area", "median"),
                   preco_venda_mediano=("sale_price", "median"),
                   n_viva=("listing_id", "count"))
              .reset_index())

m = air_g.merge(viva_g, on=["suburb_norm", "tipologia"], how="inner")
m["receita_por_m2"] = m["receita_anual"] / m["area_mediana"]
m["retorno_bruto_pct"] = m["receita_anual"] / m["preco_venda_mediano"] * 100

print("Pares com área disponível:", len(m))

# ---- NÍVEL 1: faturamento bruto por tipologia (sobre todos os pares) ----
n1 = m.groupby("tipologia").agg(receita_anual_mediana=("receita_anual", "median"),
                                n_pares=("suburb_norm", "count")).sort_values("receita_anual_mediana", ascending=False)
print("\n===== NÍVEL 1 — FATURAMENTO BRUTO por tipologia =====")
print(n1.round(2).to_string())

# ---- NÍVEL 2: eficiência de capital (receita/m² e retorno) por tipologia ----
n2 = m.groupby("tipologia").agg(receita_por_m2_mediana=("receita_por_m2", "median"),
                                retorno_bruto_mediano=("retorno_bruto_pct", "median"),
                                n_pares=("suburb_norm", "count")).sort_values("retorno_bruto_mediano", ascending=False)
print("\n===== NÍVEL 2 — EFICIÊNCIA DE CAPITAL por tipologia =====")
print(n2.round(2).to_string())

# salvar
m.to_csv(os.path.join(OUT, "eficiencia_capital_tipologia.csv"), index=False)
print("\nSalvo: output/eficiencia_capital_tipologia.csv")