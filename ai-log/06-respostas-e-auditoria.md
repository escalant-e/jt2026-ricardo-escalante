# 06 — Respostas Q1–Q4, auditoria e blindagem

## Respostas construídas com os dados

**Q1 — Perfil de imóvel** (em dois/três níveis):
- Faturamento bruto: 3Q/4Q+ lideram (acomodam mais).
- Produtividade de área: 1Q lidera (R$ 1.807/m²).
- Retorno sobre capital: **2Q** lidera (10,3%), 4Q+ perde (5,7%).
- → Recomendação: **apartamento 2Q**, por equilíbrio de liquidez, ticket e reprodutibilidade estatística.

**Q2 — Localização (receita)**: **MEIA PRAIA** é a de maior receita consolidada (R$ 118,4 mil/ano, n=630); Can. Praia/Areal altos mas com n mínimo; CENTRO é alternativa relevante (R$ 102,2 mil, n=205).

**Q3 — Características que explicam receita** (`scripts/14_regressao_q3.py`, statsmodels):
- R² = 0,45; alvo = receita anual base 55%.
- Drivers positivos significativos: nº quartos (+21,1)***, banheiros (+18,8)***, hóspedes (+13,6)***, precisão (+22,8)*, satisfação (+8,8)*.
- Coeficientes negativos (communication/value_rating) interpretados como efeito de mix de preço/colinearidade — **não** como causalidade.
- `min_nights` era constante (só 0) → excluído.
- Conclusão: **tamanho/capacidade explica mais que ratings**.

**Q4 — O que comprar hoje** (`scripts/15_retorno_liquido.py`):

| Ativo | Retorno Bruto 55% | Retorno Liq. Encargos 55% |
|---|---|---|
| MORRETES 2Q | 11,3% | **10,8%** |
| CENTRO 2Q | 9,8% | **9,2%** |
| MEIA PRAIA 2Q | 8,5% | **7,9%** |

- Retorno líquido = (receita bruta − condomínio×12 − IPTU) ÷ preço de venda.
- Justificativa de Morretes 2Q: ticket acessível (R$ 790 mil), ALTA confiabilidade, equilíbrio liquidez × retorno.

## Auditoria crítica (IA como revisor sênior) — 9 pontos
A IA apontou (a pedido de uma auditoria rigorosa):
1. **Sensibilidade do limiar de confiabilidade**: com `n_listings ≥ 10`, MORRETES 3Q (14,3%) assumiria a 1ª posição — a decisão prioriza robustez, não máxima taxa.
2. Rótulo "Retorno Líquido" enganoso → **"Retorno Líquido de Encargos Imobiliários"**.
3. Coeficientes negativos de ratings = **colinearidade/mix de preço** (não causalidade).
4. Falta de racional econômico (rendimentos marginais decrescentes; renda da terra; superhosts).
5. Tom da tese superdimensionado: "refuta" → **"parcialmente validada e reposicionada"**.
6. Falta de "como a Seazone captura valor" (originação+fee) para fechar o CRISP-DM.
7–9. Documentação (ai-log, README links, outputs sincronizados).

## Decisões do analista
- **Aplicar as 9 correções** (todas validadas).
- Adotar nomenclatura sincronizada nos outputs: `retorno_bruto_*_pct` e `retorno_liq_encargos_55_pct`.

## Tom final sobre a tese
> "Os dados sustentam parcialmente e reposicionam a tese — **não a refutam**. A intuição original (compacidade = eficiência de capital) permanece correta; o que os dados ajustam é a **tipologia ótima (2Q)** e a **localização ótima (Morretes/Centro)**."

## Resultado
- `relatorio.md` blindado com fundamentação econômica, viés de cobertura, uso de IA e próximos passos.
- Scripts 11/15 regenerados com nomenclatura consistente.

## Lição registrada
A auditoria crítica transformou pontos fracos (escolha de limiar, nomeclatura, ausência de racional econômico) em argumentos de robustez — exatamente o que a banca pode testar.