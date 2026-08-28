# 03 — Join, consistência e limpeza

## Pedido do analista
> "Faça o commit. Depois, vamos fazer o join entre Details, Mesh (via airbnb_listing_id) e Hosts (via owner_id). A partir do Price_AV, calcule por listing a diária média e o total de dias em que o airbnb estava ocupado. (Definições: dias ocupados = datas únicas; deduplicar por listing+date mantendo a captura mais recente.)"

## O que a IA fez
- `scripts/03_join_precos.py`: join + agregações de Price_AV (diária média/mediana, dias com preço).
- Identificou **problemas de consistência**:
  - Hosts: 1.383 `owner_id` duplicados (múltiplos snapshots) → inflavam o merge (4.441 → 30.822 linhas sem dedupe).
  - Price_AV: repetições de (listing,date) por capturas → precisavam de dedupe antes de somar.
- `scripts/04_auditoria.py` e `scripts/05_limpeza.py`: auditoria de nulos e limpeza.

## Auditoria (resultados)
- **Integridade do join**: `suburb`, dados do host e diária — nulos só nos 3.442 listings sem preço (77,5%) — não é problema de join, é cobertura do Price_AV.
- **Diárias**: sem valores ≤ 0. Mediana R$ 577,69; média R$ 682,54. Outliers: 10 acima do P99 (R$ 2.353); 3 em R$ 10.000 (suspeitos).
- **Bairros**: 16 valores únicos; `none` era na verdade missing.

## Decisões do analista (limpeza)
1. **Outliers**: diárias > R$ 3.000 filtradas nas análises; **mediana como métrica central**.
2. **Bairro `none`**: → NaN e ignorado nas análises geográficas.
3. **Nulos de preço**: mantidos na base geral (concorrência/oferta), filtrados nas agregações de diária/receita.

## Resultado
- `output/master_joined_limpo.csv` (base geral com flag de outlier) e `output/preco_ok.csv` (994 listings com preço ≤ R$ 3.000).
- Commit da limpeza registrado.

## Lição registrada
O join só funcionou corretamente após o tratamento dos duplicados de owner — sem isso, os números venceriam o sentido. A auditoria preveniu erros antes das agregações.