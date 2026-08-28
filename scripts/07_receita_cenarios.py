import pandas as pd
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output")

# ------------------------------------------------------------------
# Estrita extração do Price_AV: diária + sazonalidade (sem "ocupação")
# ------------------------------------------------------------------
pri = pd.read_csv(os.path.join(DATA, "Price_AV_Itapema.csv"), encoding="utf-8", low_memory=False)
pri["date"] = pd.to_datetime(pri["date"])
pri["aquisition_date"] = pd.to_datetime(pri["aquisition_date"])
pri = (pri.sort_values("aquisition_date")
          .drop_duplicates(subset=["airbnb_listing_id", "date"], keep="last"))

# diária por listing (mediana central; media mantida p/ referencia)
price_agg = (pri.groupby("airbnb_listing_id")
                 .agg(diaria_media=("price", "mean"),
                      diaria_mediana=("price", "median"),
                      dias_observados_calendario=("date", "nunique"),
                      min_data=("date", "min"),
                      max_data=("date", "max"))
                 .reset_index())

# ------------------------------------------------------------------
# SAZONALIDADE: diária mediana por dia da semana e por sem~ segmentation
# ------------------------------------------------------------------
pri["dia_semana"] = pri["date"].dt.dayofweek          # 0=seg ... 6=dom
pri["mes"] = pri["date"].dt.month
saz_ds = (pri.groupby("dia_semana")["price"]
             .agg(["median", "mean", "size"])
             .rename(columns={"median":"diaria_mediana","mean":"diaria_media","size":"n_linhas"})
             .reset_index())
saz_mes = (pri.groupby("mes")["price"]
              .agg(diaria_mediana="median", diaria_media="mean", n_linhas="size")
              .reset_index())

# --------------------------------------------------------------------------
# BASE MASTER: reutiliza o join e aplica limpeza + receita por cenário
# --------------------------------------------------------------------------
master = pd.read_csv(os.path.join(OUT, "master_joined.csv"), encoding="utf-8", low_memory=False)

# renomeia a métrica de contagem de datas
master = master.rename(columns={"dias_ocupados": "dias_observados_calendario"})

# limpeza de bairro 'none'
master["suburb"] = master["suburb"].replace("none", pd.NA)

# outliers se mantêm na base geral, com flag
master["flag_outlier_diaria"] = (master["diaria_media"] > 3000).astype(bool)

# view com preço ok (diária > 0 e <= 3000)
preco_ok = master[(master["diaria_mediana"].notna()) & (master["diaria_media"] <= 3000)].copy()

# ---- Receita Anual Bruta por cenários de ocupação média ----
cenarios = {"conservador": 0.40, "base": 0.55, "otimista": 0.70}
for nome, tx in cenarios.items():
    preco_ok[f"receita_bruta_{nome}"] = preco_ok["diaria_mediana"] * 365 * tx

# salva
master.to_csv(os.path.join(OUT, "master_joined_limpo.csv"), index=False)
preco_ok.to_csv(os.path.join(OUT, "preco_ok.csv"), index=False)
saz_ds.to_csv(os.path.join(OUT, "sazonalidade_diaria_semana.csv"), index=False)
saz_mes.to_csv(os.path.join(OUT, "sazonalidade_mes.csv"), index=False)
price_agg.to_csv(os.path.join(OUT, "price_agregado_por_listing.csv"), index=False)

# ------------------ resumo ----------------
print("=== SAZONALIDADE por dia da semana (diária mediana) ===")
print(saz_ds.to_string(index=False))
print("\n=== SAZONALIDADE por mês (diária mediana) ===")
print(saz_mes.to_string(index=False))

print("\n=== preco_ok: nº de listings e receitas por cenário ===")
print("total preco_ok:", len(preco_ok))
cols = ["diaria_mediana"] + [f"receita_bruta_{t}" for t in cenarios]
print(preco_ok[cols].describe().to_string())

print("\nSalvos: master_joined_limpo.csv, preco_ok.csv, sazonalidade_*.csv, price_agregado_por_listing.csv")