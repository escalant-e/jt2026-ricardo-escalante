import pandas as pd
import unicodedata, os

OUT = os.path.join(os.path.dirname(__file__), "..", "output", "dados")
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

air = pd.read_csv(os.path.join(OUT, "preco_ok.csv"), encoding="utf-8", low_memory=False)
air["suburb_norm"] = air["suburb"].apply(norm_suburb)
air["tipologia"] = air["number_of_bedrooms"].apply(faixa_quartos)
air = air[air["suburb_norm"].notna() & air["tipologia"].notna()].copy()

# =====================================================================
# Q1 — MELHOR PERFIL DE IMÓVEL (tipologia, nº quartos, tipo de anúncio)
# Critério: receita/ano projetada (cenário base 55%) e diária mediana
# =====================================================================
print("=" * 70)
print("Q1 — MELHOR PERFIL DE IMÓVEL (tipologia / nº quartos / tipo anúncio)")
print("=" * 70)

# por tipologia
q1_tipo = (air.groupby("tipologia")
              .agg(n=("airbnb_listing_id", "count"),
                   diaria_mediana=("diaria_mediana", "median"),
                   receita_anual=("receita_bruta_base", "median"))
              .sort_values("receita_anual", ascending=False))
print("\n-- Por Tipologia (faixa de quartos) --")
print(q1_tipo.round(2).to_string())

# por listing_type
q1_list = (air.groupby("listing_type")
              .agg(n=("airbnb_listing_id", "count"),
                   diaria_mediana=("diaria_mediana", "median"),
                   receita_anual=("receita_bruta_base", "median"))
              .sort_values("receita_anual", ascending=False))
print("\n-- Por listing_type (tipo de anúncio) --")
print(q1_list.round(2).to_string())

# por tipo de host / profissional
q1_prof = (air.groupby("is_professional")
              .agg(n=("airbnb_listing_id", "count"),
                   diaria_mediana=("diaria_mediana", "median"),
                   receita_anual=("receita_bruta_base", "median")))
print("\n-- Por is_professional --")
print(q1_prof.round(2).to_string())

# =====================================================================
# Q2 — MELHOR LOCALIZAÇÃO EM TERMOS DE RECEITA
# =====================================================================
print("\n" + "=" * 70)
print("Q2 — MELHOR LOCALIZAÇÃO (bairro) em termos de receita")
print("=" * 70)
q2 = (air.groupby("suburb_norm")
         .agg(n=("airbnb_listing_id", "count"),
              diaria_mediana=("diaria_mediana", "median"),
              receita_anual=("receita_bruta_base", "median"))
         .sort_values("receita_anual", ascending=False))
print("\n-- Por bairro (receita/ano cenário base) --")
print(q2.round(2).to_string())

# =====================================================================
# Q3 — CARACTERÍSTICAS QUE EXPLICAM AS MELHORES RECEITAS
# =====================================================================
print("\n" + "=" * 70)
print("Q3 — CARACTERÍSTICAS QUE EXPLICAM AS MELHORES RECEITAS")
print("=" * 70)

# bivariado: correlação de características numéricas vs receita
nums = ["receita_bruta_base", "diaria_mediana", "number_of_bedrooms", "number_of_bathrooms",
        "number_of_beds", "number_of_guests", "cleaning_fee", "picture_count",
        "min_nights", "star_rating", "number_of_reviews", "guest_satisfaction_overall",
        "accuracy_rating", "cleanliness_rating", "communication_rating",
        "location_rating", "value_rating", "years_host", "number_of_reviews_host"]
sub = air[nums].dropna()
corr = sub.corr()["receita_bruta_base"].sort_values(ascending=False)
print("\n-- Correlação de características com receita/ano base --")
print(corr.to_string())

# por faixa de quartos x superhost
print("\n-- Receita mediana por superhost --")
print(air.groupby("is_superhost")["receita_bruta_base"].agg(["median", "count"]).round(2).to_string())

# save agregados
q1_tipo.to_csv(os.path.join(OUT, "q1_tipologia.csv"))
q2.to_csv(os.path.join(OUT, "q2_bairro.csv"))