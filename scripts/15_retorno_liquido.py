import pandas as pd
import unicodedata, os

OUT = os.path.join(os.path.dirname(__file__), "..", "output", "dados")
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)

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

# Airbnb: receita por [bairro+tipologia]
air = pd.read_csv(os.path.join(OUT, "preco_ok.csv"), encoding="utf-8", low_memory=False)
air["suburb_norm"] = air["suburb"].apply(norm_suburb)
air["tipologia"] = air["number_of_bedrooms"].apply(faixa_quartos)
air = air[air["suburb_norm"].notna() & air["tipologia"].notna()].copy()

air_g = (air.groupby(["suburb_norm", "tipologia"])
            .agg(receita_55=("receita_bruta_base", "median"),
                 diaria_mediana=("diaria_mediana", "median"),
                 n_air=("airbnb_listing_id", "count"))
            .reset_index())

# VivaReal: preço + custos por [bairro+tipologia]
viva = pd.read_csv(os.path.join(DATA, "VivaReal_Itapema.csv"), encoding="utf-8", low_memory=False)
viva = viva[viva["listing_type"] == "apartamento"]
viva = viva[(viva["sale_price"] >= 100000) & (viva["usable_area"] >= 15)]
viva["suburb_norm"] = viva["suburb"].apply(norm_suburb)
viva["tipologia"] = viva["bedrooms"].apply(faixa_quartos)
viva = viva[viva["suburb_norm"].notna() & viva["tipologia"].notna()].copy()

viva_g = (viva.groupby(["suburb_norm", "tipologia"])
              .agg(preco_venda_mediano=("sale_price", "median"),
                   cond_mediana=("monthly_condo_fee", "median"),
                   iptu_mediana=("yearly_iptu", "median"),
                   n_viva=("listing_id", "count"))
              .reset_index())

m = air_g.merge(viva_g, on=["suburb_norm", "tipologia"], how="inner")

m["cond_anual_mediana"] = m["cond_mediana"] * 12
m["iptu_anual_mediana"] = m["iptu_mediana"]
m["receita_liq_encargos_55"] = m["receita_55"] - m["cond_anual_mediana"] - m["iptu_anual_mediana"]
m["retorno_bruto_55_pct"] = m["receita_55"] / m["preco_venda_mediano"] * 100
m["retorno_liq_encargos_55_pct"] = m["receita_liq_encargos_55"] / m["preco_venda_mediano"] * 100

# 3 ativos recomendados
ativos = [("MORRETES", "2Q"), ("CENTRO", "2Q"), ("MEIA PRAIA", "2Q")]
print("===== RETORNO LÍQUIDO DE ENCARGOS — 3 ATIVOS RECOMENDADOS (cenário base 55%) =====\n")
for b, t in ativos:
    r = m[(m["suburb_norm"] == b) & (m["tipologia"] == t)]
    if r.empty:
        print(f"{b} {t}: sem dados")
        continue
    r = r.iloc[0]
    print(f"{b} {t}")
    print(f"  receita bruta anual (55%): R$ {r['receita_55']:,.2f}")
    print(f"  condomínio anual (mediana {r['cond_mediana']}*12):  R$ {r['cond_anual_mediana']:,.2f}")
    print(f"  IPTU anual (mediana {r['iptu_mediana']}):           R$ {r['iptu_anual_mediana']:,.2f}")
    print(f"  receita líquida de encargos anual: R$ {r['receita_liq_encargos_55']:,.2f}")
    print(f"  preço venda mediano:         R$ {r['preco_venda_mediano']:,.2f}")
    print(f"  retorno BRUTO 55%: {r['retorno_bruto_55_pct']:.2f}%")
    print(f"  retorno LÍQUIDO DE ENCARGOS 55%: {r['retorno_liq_encargos_55_pct']:.2f}%")
    print()

m.to_csv(os.path.join(OUT, "retorno_liquido_ativos.csv"), index=False)
print("Salvo: output/retorno_liquido_ativos.csv")