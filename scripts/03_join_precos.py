import pandas as pd
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(os.path.dirname(__file__), "..", "output", "dados")

# ---- carrega ----
det   = pd.read_csv(os.path.join(DATA, "Details_Itapema.csv"), encoding="utf-8", low_memory=False)
mesh  = pd.read_csv(os.path.join(DATA, "Mesh_Ids_Data_Itapema.csv"), encoding="utf-8", low_memory=False)
hosts = pd.read_csv(os.path.join(DATA, "Hosts_ids_Itapema.csv"), encoding="utf-8", low_memory=False)
pri   = pd.read_csv(os.path.join(DATA, "Price_AV_Itapema.csv"), encoding="utf-8", low_memory=False)

# ---- Price_AV: datas ----
pri["date"] = pd.to_datetime(pri["date"])
pri["aquisition_date"] = pd.to_datetime(pri["aquisition_date"])

# ---- 1. diária média por listing (dedupe (listing,date) mantendo captura mais recente) ----
pri_dedup = (pri.sort_values("aquisition_date")
                .drop_duplicates(subset=["airbnb_listing_id", "date"], keep="last"))

price_agg = (pri_dedup.groupby("airbnb_listing_id")
                      .agg(diaria_media=("price", "mean"),
                           diaria_mediana=("price", "median"),
                           dias_ocupados=("date", "nunique"),
                           min_data=("date", "min"),
                           max_data=("date", "max"),
                           qtd_linhas=("price", "size"))
                      .reset_index())

# ---- join Details + Mesh pelo airbnb_listing_id ----
det_mesh = det.merge(mesh[["airbnb_listing_id", "latitude", "longitude", "suburb"]],
                     on="airbnb_listing_id", how="left")

# ---- join Hosts pelo owner_id (mantém snapshot mais recente p/ owner duplicado) ----
hosts_clean = (hosts.sort_values("host_snapshot_date")
                    .drop_duplicates(subset=["owner_id"], keep="last"))
master = det_mesh.merge(hosts_clean[["owner_id", "owner", "is_superhost",
                                     "number_of_reviews_host", "is_verified",
                                     "star_rating_host", "years_host", "months_host",
                                     "host_snapshot_date"]],
                        on="owner_id", how="left")

# ---- juntar métricas de preço ----
master = master.merge(price_agg, on="airbnb_listing_id", how="left")

print("JOIN qtd linhas:", len(master))
print("colunas:", len(master.columns))

# salvando
os.makedirs(OUT, exist_ok=True)
master.to_csv(os.path.join(OUT, "master_joined.csv"), index=False)
price_agg.to_csv(os.path.join(OUT, "price_agregado_por_listing.csv"), index=False)

# resumo rapido
print("\n=== Diárias e ocupação (describe) ===")
sub = master[["diaria_media", "diaria_mediana", "dias_ocupados"]].describe()
print(sub.to_string())

print("\n=== Overlap: quantos listings tem preço? ===")
print("total listings:", len(master))
print("com preco:", master["diaria_media"].notna().sum())
print("sem preco:", master["diaria_media"].isna().sum())

print("\nArquivos salvos:")
print("  output/master_joined.csv")
print("  output/price_agregado_por_listing.csv")