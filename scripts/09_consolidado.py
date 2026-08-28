import pandas as pd
import unicodedata, os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

# ---------------------------------------------------------------
# Normalização de nomes de bairro
# ---------------------------------------------------------------
def norm_suburb(s):
    if pd.isna(s):
        return pd.NA
    s = str(s)
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    s = s.upper().strip()
    # unifica variações
    if "MEIA PRAIA" in s:
        return "MEIA PRAIA"
    m = {"TABOLEIRO": "TABULEIRO DOS OLIVEIRAS",
         "TABULEIRO": "TABULEIRO DOS OLIVEIRAS"}
    if s in m:
        return m[s]
    return s

# ---------------------------------------------------------------
# Faixas de quartos — IDÊNTICAS em ambas as bases
# 0 e 1 -> '1Q'(studio), 2 -> '2Q', 3 -> '3Q', >=4 -> '4Q+'
# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
# 1) VivaReal: limpeza + normalização + tipologia
# ---------------------------------------------------------------
viva = pd.read_csv(os.path.join(DATA, "VivaReal_Itapema.csv"), encoding="utf-8", low_memory=False)
print("VivaReal bruto:", len(viva))
viva = viva[viva["listing_type"] == "apartamento"].copy()
viva = viva[viva["sale_price"] >= 100000]
viva = viva[viva["usable_area"] >= 15]
print("VivaReal apartamento, preco>=100k, area>=15:", len(viva))

viva["suburb_norm"] = viva["suburb"].apply(norm_suburb)
viva["tipologia"] = viva["bedrooms"].apply(faixa_quartos)
viva_clean = viva[viva["suburb_norm"].notna() & viva["tipologia"].notna()].copy()

# ---------------------------------------------------------------
# 2) Airbnb (preco_ok): tipologia + por [bairro+tipologia]
# ---------------------------------------------------------------
air = pd.read_csv(os.path.join(OUT, "preco_ok.csv"), encoding="utf-8", low_memory=False)
air["suburb_norm"] = air["suburb"].apply(norm_suburb)
air["tipologia"] = air["number_of_bedrooms"].apply(faixa_quartos)
air_clean = air[air["suburb_norm"].notna() & air["tipologia"].notna()].copy()

# ---------------------------------------------------------------
# 3) Agregações
# ---------------------------------------------------------------
taxa_ocup_base = 0.55  # cenário base

air_g = (air_clean.groupby(["suburb_norm", "tipologia"])
                  .agg(diaria_mediana=("diaria_mediana", "median"),
                       n_listings=("airbnb_listing_id", "count"))
                  .reset_index())
air_g["receita_anual_projetada"] = air_g["diaria_mediana"] * 365 * taxa_ocup_base

viva_g = (viva_clean.groupby(["suburb_norm", "tipologia"])
                     .agg(sale_price_mediana=("sale_price", "median"),
                          n_anuncios=("listing_id", "count"))
                     .reset_index())

# ---------------------------------------------------------------
# 4) Tabela consolidada (todos os grupos)
# ---------------------------------------------------------------
consolidado = air_g.merge(viva_g, on=["suburb_norm", "tipologia"], how="outer",
                          suffixes=("_airbnb", "_vivareal"))
consolidado.to_csv(os.path.join(OUT, "consolidado_bairro_tipologia.csv"), index=False)

# ---------------------------------------------------------------
# 5) Tabela de retorno (apenas pares completos)
# ---------------------------------------------------------------
retorno = air_g.merge(viva_g, on=["suburb_norm", "tipologia"], how="inner")
retorno["retorno_bruto_anual_pct"] = retorno["receita_anual_projetada"] / retorno["sale_price_mediana"] * 100
retorno = retorno.sort_values("retorno_bruto_anual_pct", ascending=False).reset_index(drop=True)
retorno.to_csv(os.path.join(OUT, "retorno_financeiro.csv"), index=False)

print("\nConsolidado (todas as combinações):", len(consolidado))
print("Retorno financeiro (pares completos):", len(retorno))

print("\n===== TABELA DE RETORNO FINANCEIRO (ord. por retorno bruto anual) =====")
print(retorno[["suburb_norm", "tipologia", "n_listings", "diaria_mediana",
               "receita_anual_projetada", "n_anuncios", "sale_price_mediana",
               "retorno_bruto_anual_pct"]].to_string(index=False))

print("\nArquivos salvos:")
print("  output/consolidado_bairro_tipologia.csv")
print("  output/retorno_financeiro.csv")