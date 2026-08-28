import pandas as pd
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

viva = pd.read_csv(os.path.join(DATA, "VivaReal_Itapema.csv"), encoding="utf-8", low_memory=False)

print("Total anúncios VivaReal:", len(viva))

# ---- 1. Percentis + 10 menores valores de sale_price e usable_area ----
print("\n[1a] SALE_PRICE —— percentis")
sp = viva["sale_price"].dropna()
print(sp.describe(percentiles=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]).to_string())
print("\n10 MENORES sale_price:")
print(sp.sort_values().head(10).to_string())

print("\n[1b] USABLE_AREA —— percentis")
ua = viva["usable_area"].dropna()
print(ua.describe(percentiles=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]).to_string())
print("\n10 MENORES usable_area:")
print(ua.sort_values().head(10).to_string())

# ---- 2. Quantos anúncios com area <=15 ou preço <=50000 ----
print("\n[2] CORTES CANDIDATOS")
m_area = viva["usable_area"] <= 15
m_preco = viva["sale_price"] <= 50000
print("anúncios com area <= 15 m²:", int(m_area.sum()), f"({m_area.mean()*100:.2f}%)")
print("anúncios com preço <= R$ 50.000:", int(m_preco.sum()), f"({m_preco.mean()*100:.2f}%)")
print("anúncios que atendem AMBOS:", int((m_area & m_preco).sum()))
print("anúncios que atendem área<=15 OU preço<=50k:", int((m_area | m_preco).sum()))
print("área <= 15 (indep. preço):", int(m_area.sum()))
print("preço <= 50k (indep. área):", int(m_preco.sum()))

# amostra do que seria cortado
cortados = viva[m_area | m_preco][["listing_id", "sale_price", "usable_area", "bedrooms", "listing_type", "suburb"]]
print("\nAmostra dos anúncios que cairiam no corte (área<=15 ou preço<=50k):")
print(cortados.head(20).to_string())
print("\nTotal a cortar:", len(cortados))