import pandas as pd
import os, io

pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
pd.set_option("display.max_rows", 200)
DATA = os.path.join(os.path.dirname(__file__), "..", "data")

def load(fn):
    return pd.read_csv(os.path.join(DATA, fn), encoding="utf-8", low_memory=False)

buf = io.StringIO()

det = load("Details_Itapema.csv")
pri = load("Price_AV_Itapema.csv")
mesh = load("Mesh_Ids_Data_Itapema.csv")
hosts = load("Hosts_ids_Itapema.csv")
viva = load("VivaReal_Itapema.csv")

print("=== DETAILS: domínio de campos-chave ===", file=buf)
print("listing_type:", det["listing_type"].value_counts(dropna=False).to_dict(), file=buf)
print("number_of_bedrooms:", det["number_of_bedrooms"].value_counts(dropna=False).sort_index().to_dict(), file=buf)
print("number_of_guests quartis:", det["number_of_guests"].describe().to_dict(), file=buf)
print("is_professional:", det["is_professional"].value_counts(dropna=False).to_dict(), file=buf)
print("listing ids unicos:", det["airbnb_listing_id"].nunique(), file=buf)

print("\n=== MESH suburbs ===", file=buf)
print(mesh["suburb"].value_counts(dropna=False).to_dict(), file=buf)

print("\n=== PRICE_AV temporal ===", file=buf)
pri["date"] = pd.to_datetime(pri["date"])
print("range:", pri["date"].min(), "->", pri["date"].max(), file=buf)
print("n_listings no price:", pri["airbnb_listing_id"].nunique(), file=buf)
print("rows por listing:", pri.groupby("airbnb_listing_id").size().describe().to_dict(), file=buf)
print("price describe:", pri["price"].describe().to_dict(), file=buf)
# datas de captura
print("aquisition_date unicos (price):", pri["aquisition_date"].unique(), file=buf)
print("rows por captura:", pri.groupby("aquisition_date").size().to_dict(), file=buf)

print("\n=== VIVAREAL ===", file=buf)
print("business_types:", viva["business_types"].value_counts(dropna=False).to_dict(), file=buf)
print("listing_type:", viva["listing_type"].value_counts(dropna=False).to_dict(), file=buf)
print("property_type:", viva["property_type"].value_counts(dropna=False).to_dict(), file=buf)
print("bedrooms:", viva["bedrooms"].value_counts(dropna=False).sort_index().to_dict(), file=buf)
print("suburb:", viva["suburb"].value_counts(dropna=False).to_dict(), file=buf)
print("sale_price describe (nula?), na:", viva["sale_price"].isna().sum(), file=buf)
print("rental_price na:", viva["rental_price"].isna().sum(), file=buf)
print("portal:", viva["portal"].value_counts(dropna=False).to_dict(), file=buf)

print(buf.getvalue())