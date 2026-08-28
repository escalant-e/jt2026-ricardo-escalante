import pandas as pd
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "output")

master = pd.read_csv(os.path.join(OUT, "master_joined.csv"), encoding="utf-8", low_memory=False)

n_antes = len(master)

# ---- 1. bairro 'none' -> NaN ----
n_none_antes = (master["suburb"].astype(str) == "none").sum()
master["suburb"] = master["suburb"].replace("none", pd.NA)

# ---- 2. outliers: diaria_media > 3000 -> marcar (nao remover da base geral) ----
n_outliers = (master["diaria_media"] > 3000).sum()
master["flag_outlier_diaria"] = (master["diaria_media"] > 3000).astype(bool)

# subview 'com preco ok' para agregações de diária/receita
preco_ok = master[(master["diaria_media"].notna()) & (master["diaria_media"] <= 3000)].copy()

print("Total linhas master geral:", len(master))
print("bairro 'none' convertidos a NaN:", n_none_antes)
print("outliers diaria>3000 (flag True):", n_outliers)
print("linhas 'com preco ok' (para agregacoes):", len(preco_ok))

# salva master geral (com flags) e a subview para agregacoes
master.to_csv(os.path.join(OUT, "master_joined_limpo.csv"), index=False)
preco_ok.to_csv(os.path.join(OUT, "preco_ok.csv"), index=False)

print("\nSalvos: master_joined_limpo.csv (geral) e preco_ok.csv (com preco ok)")