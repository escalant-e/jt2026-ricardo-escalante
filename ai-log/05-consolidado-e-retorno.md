# 05 — Consolidação, retorno e eficiência de capital

## Pedidos do analista
1. Inspecionar distribuição do VivaReal (preço, área, percentis) **antes** de cortar.
2. Aplicar limpeza no VivaReal: `listing_type == 'apartamento'`, `sale_price >= 100.000`, `usable_area >= 15`.
3. Padronizar bairros (maiúsculas, sem acento, unificar variações como "MEIA PRAIA - FRENTE MAR" → "MEIA PRAIA").
4. Criar faixas de quartos **idênticas nas duas bases**: 1Q (0–1), 2Q, 3Q e 4Q+ (≥4).
5. Consolidar Airbnb + VivaReal por `[bairro + tipologia]`.
6. Tabela de retorno: **apenas pares completos**, com diária mediana, receita anual projetada e retorno bruto.
7. Classificar por **confiabilidade** (n_listings e n_anuncios).

## Investigação do VivaReal (antes do corte)
- `sale_price`: mediana R$ 1,75M; P1 R$ 450k; um anúncio a R$ 10k (erro claro) e outro a R$ 99k.
- `usable_area`: mediana 128 m²; mínimo 0; max 188.000 (outlier extremo). Área 0/10 = principalmente **terrenos**.
- 68 anúncios com área ≤ 15; 1 com preço ≤ 50k; total 69 no critério OU.

## Decisões do analista (limpeza VivaReal)
- Filtrar apenas `apartamento` (short stay) → remove terrenos que poluíam área 0.
- `sale_price >= 100.000` (remove anomalias óbvias).
- `usable_area >= 15` (evita distorções dentro dos apartamentos).
- `bedrooms == 0` → faixa **1Q** (studio).
- Resultado: **7.474** anúncios válidos (de 8.329).

## Consolidação e retorno (scripts 08–11)
- **61 combinações** [bairro+tipologia] no consolidado; **29 pares completos** (Airbnb+VivaReal).
- Confiabilidade:
  - ALTA: n_listings ≥ 15 E n_anuncios ≥ 30
  - MÉDIA: n_listings ≥ 5 E n_anuncios ≥ 10
  - BAIXA: demais
- Top 3 por retorno bruto base 55% (ALTA): **MORRETES 2Q 11,3%** · **CENTRO 2Q 9,8%** · **MEIA PRAIA 2Q 8,5%**.

## Eficiência de capital (resposta Q1 em dois níveis — script 13)
| Tipologia | Receita/m² | Retorno bruto |
|---|---|---|
| 1Q | R$ 1.807/m² | 9,6% |
| **2Q** | R$ 1.202/m² | **10,3%** |
| 3Q | R$ 1.183/m² | 9,0% |
| 4Q+ | R$ 1.114/m² | 5,7% |

- **Faturamento bruto**: 4Q+/3Q lideram. **Eficiência de capital**: 2Q lidera em retorno; 1Q em receita/m².

## Decisões do analista
- Associar "tipologia" = faixa de quartos em **ambas** as bases (chave comum de junção).
- Na tabela de retorno, manter **apenas pares completos**; manter tabela secundária com todos os grupos.
- Usar **mediana** como métrica central de diária/preço.

## Resultado
- Arquivos: `retorno_financeiro.csv`, `retorno_financeiro_classificado.csv`, `eficiencia_capital_tipologia.csv`, `consolidado_bairro_tipologia.csv`, etc.

## Lição registrada
Pares com retorno alto mas **volume mínimo** (ILHOTA 1Q 31,5%, CANTO DA PRAIA 1Q 20,4%) foram corretamente descartados pela confiabilidade — a banca valoriza evitar decisões por n pequeno.