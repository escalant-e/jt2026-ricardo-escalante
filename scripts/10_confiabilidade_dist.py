import pandas as pd
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "output", "dados")

ret = pd.read_csv(os.path.join(OUT, "retorno_financeiro.csv"), encoding="utf-8", low_memory=False)

print("Pares completos:", len(ret))
print("\n===== Distribuição de volumes =====")
print("n_listings (Airbnb):")
print(ret["n_listings"].describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9]).to_string())
print("\nn_anuncios (VivaReal):")
print(ret["n_anuncios"].describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9]).to_string())

print("\n===== Pares por faixa de n_listings (Airbnb) =====")
print(ret.groupby(pd.cut(ret["n_listings"], bins=[0, 4, 9, 19, 200])).size().to_string())
print("\n===== Pares por faixa de n_anuncios (VivaReal) =====")
print(ret.groupby(pd.cut(ret["n_anuncios"], bins=[0, 9, 29, 99, 2000])).size().to_string())

# Densidade conjunta
print("\n===== Matriz: n_listings vs n_anuncios =====")
print(pd.crosstab(
    pd.cut(ret["n_listings"], bins=[0, 4, 9, 19, 200], labels=["1-4", "5-9", "10-19", "20+"]),
    pd.cut(ret["n_anuncios"], bins=[0, 9, 29, 99, 2000], labels=["1-9", "10-29", "30-99", "100+"])
).to_string())