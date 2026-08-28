import pandas as pd
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "output", "dados")
os.makedirs(OUT, exist_ok=True)

ret = pd.read_csv(os.path.join(OUT, "retorno_financeiro.csv"), encoding="utf-8", low_memory=False)

# ---- Classificação de confiabilidade ----
def nivel_conf(n_listings, n_anuncios):
    if n_listings >= 15 and n_anuncios >= 30:
        return "ALTA"
    if n_listings >= 5 and n_anuncios >= 10:
        return "MEDIA"
    return "BAIXA"

ret["nivel_confiabilidade"] = [nivel_conf(a, b) for a, b in zip(ret["n_listings"], ret["n_anuncios"])]

# ---- Retornos por cenários de ocupação (40/55/70) ----
for tx, suf in [(0.40, "40"), (0.55, "55"), (0.70, "70")]:
    ret[f"receita_anual_{suf}"] = ret["diaria_mediana"] * 365 * tx
    ret[f"retorno_anual_{suf}_pct"] = ret[f"receita_anual_{suf}"] / ret["sale_price_mediana"] * 100

# salva classificada
ret.to_csv(os.path.join(OUT, "retorno_financeiro_classificado.csv"), index=False)

# ---- Tabela filtrada ALTA + MÉDIA ----
cols = ["suburb_norm", "tipologia", "nivel_confiabilidade", "diaria_mediana",
        "sale_price_mediana", "retorno_anual_40_pct", "retorno_anual_55_pct", "retorno_anual_70_pct"]
filt = ret[ret["nivel_confiabilidade"].isin(["ALTA", "MEDIA"])].copy()
filt = filt.sort_values("retorno_anual_55_pct", ascending=False).reset_index(drop=True)

print("===== PAres ALTA + MEDIA confiabilidade (ord. retorno base 55%) =====")
print(filt[cols].to_string(index=False))
print("\nn de pares ALTA/MEDIA:", len(filt))

print("\n===== RANKING TOP 3 (confiabilidade comprovada: ALTA) =====")
top3 = filt[filt["nivel_confiabilidade"] == "ALTA"].head(3)
print(top3[cols].to_string(index=False))