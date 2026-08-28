import pandas as pd
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

pri = pd.read_csv(os.path.join(DATA, "Price_AV_Itapema.csv"), encoding="utf-8", low_memory=False)
pri["date"] = pd.to_datetime(pri["date"])
pri["aquisition_date"] = pd.to_datetime(pri["aquisition_date"])

print("Linhas:", len(pri), "| listings:", pri["airbnb_listing_id"].nunique())

# dedupe (listing,date)
pri2 = (pri.sort_values("aquisition_date")
            .drop_duplicates(subset=["airbnb_listing_id","date"], keep="last"))

print("Após dedupe (listing,date):", len(pri2), "linhas")

# eh a mesma data de chegada? Cada 'date' é uma noite. Vejamos padrão por listing.
# quantos listings têm preço no domingo vs dias úteis (se for disponibilidade, estatística)
pri2["dia_semana"] = pri2["date"].dt.dayofweek  # 0=seg ... 6=dom
prof = pri2.groupby("dia_semana").agg(
    n=("price","size"),
    preco_med=("price","median")).reset_index()
print("\nDistribuição por dia da semana (todas linhas com preço):")
print(prof.to_string())

# seriam os fins de semana com mais datas com 'disponibilidade'?
# para cada listing, o intervalo entre min e max data e qts dias preenchidos
g = pri2.groupby("airbnb_listing_id").agg(
    n_datas=("date","nunique"),
    min_data=("date","min"),
    max_data=("date","max")).reset_index()
g["janela"] = (g["max_data"]-g["min_data"]).dt.days+1
g["preenchimento"] = g["n_datas"]/g["janela"]
print("\nPreenchimento do calendário (n_datas / janela min->max):")
print(g["preenchimento"].describe().to_string())

# amostra de um listing específico: datas em ordem
one = pri2[pri2["airbnb_listing_id"]==pri2["airbnb_listing_id"].value_counts().index[0]]
print("\nExemplo listing", one["airbnb_listing_id"].iloc[0])
print("n_datas:", one["date"].nunique(), "| range:", one["date"].min(), "->", one["date"].max())
# mostra blocos: quais dias da semana estao preenchidos
c = one["date"].dt.dayofweek.value_counts().sort_index()
print("dias da semana do exemplo:\n", c.to_string())

# Contagem global: há datas vazias dentro da janela de cada listing? (furos)
# Se todo dia tiver preço = disponibilidade constante. Se tiver buracos, indica reserva.
full = pd.date_range("2025-01-06","2025-04-20")
all_dates = set(pd.to_datetime(pri2["date"]).dt.date)
print("\nDatas globalmente presentes:", len(all_dates), "de", len(full), "possíveis na janela 06jan-20abr")