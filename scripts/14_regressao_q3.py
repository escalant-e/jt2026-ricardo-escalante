import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "output")

air = pd.read_csv(os.path.join(OUT, "preco_ok.csv"), encoding="utf-8", low_memory=False)

# variáveis candidatas (características do imóvel/operacionais)
feats = ["number_of_bedrooms", "number_of_bathrooms", "number_of_beds",
         "number_of_guests", "cleaning_fee", "picture_count",
         "star_rating", "number_of_reviews", "guest_satisfaction_overall",
         "accuracy_rating", "checkin_rating", "cleanliness_rating",
         "communication_rating", "location_rating", "value_rating"]

# alvo: receita anual base (55%)
data = air[feats + ["receita_bruta_base"]].dropna().copy()

print("n observações:", len(data))

# padroniza variáveis p/ comparar importâncias
X = data[feats].astype(float)
y = (data["receita_bruta_base"] / 1000).astype(float)  # receita em milhares (R$ k) p/ escala

Xc = (X - X.mean()) / X.std()
Xc = sm.add_constant(Xc)

model = sm.OLS(y, Xc).fit()

print("\n===== REGRESSÃO MÚLTIPLA (alvo: receita anual em R$ mil, base 55%) =====")
print("R²:", round(model.rsquared, 4))
print("R² ajustado:", round(model.rsquared_adj, 4))
print("n:", int(model.nobs))

print("\nCoeficientes padronizados (beta): interpretação = +1 desvio-padrão na feature => +/- R$ mil na receita/ano")
coef = model.params.drop("const").sort_values(key=lambda s: abs(s), ascending=False)
tvals = model.tvalues.drop("const")
pvals = model.pvalues.drop("const")
for var in coef.index:
    sig = "***" if pvals[var] < 0.001 else ("**" if pvals[var] < 0.01 else ("*" if pvals[var] < 0.05 else "ns"))
    print(f"  {var:<30} beta={coef[var]:>9.2f}  t={tvals[var]:>7.2f}  p={pvals[var]:.4f} {sig}")

print("\nLegenda: *** p<0.001, ** p<0.01, * p<0.05, ns não-significante")