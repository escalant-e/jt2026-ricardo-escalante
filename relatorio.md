# Relatório — Recomendação de Investimento Imobiliário em Itapema (SC)

> **Desafio**: Hackathon Jovens Talentos AI Builder 2026 — Seazone
> **Base**: Airbnb (Details, Hosts, Mesh, Price_AV) + VivaReal (venda)
> **Janela de preço observada**: 06/01/2025 – 20/04/2025 (verão) — *limitação descrita na Metodologia*

---

## Resumo executivo

Recomendação para a Seazone, respondendo as 4 perguntas do desafio e tomando posição sobre a tese interna dos "apartamentos compactos (studio/1Q) no Centro".

| # | Pergunta | Resposta-curta |
|---|---|---|
| 1 | Melhor perfil de imóvel | **2Q** (eficiência de capital); **3Q/4Q** lideram faturamento bruto |
| 2 | Melhor localização (receita) | **MEIA PRAIA** (receita consolidada); **CENTRO** relevante p/ retorno |
| 3 | Características que explicam receita | **Tamanho/capacidade** (quartos, banheiros, hóspedes); ratings pouco relevantes |
| 4 | O que comprar hoje | ver decisão + retorno abaixo |

---

## Q1 — Melhor perfil de imóvel (tipologia, nº de quartos, tipo de anúncio)

**Resposta em dois níveis** (o critério é aberto pelo desafio e depende do objetivo).

### Nível 1 — Faturamento bruto
| Tipologia | Diária mediana | Receita anual (cenário 55%) |
|---|---|---|
| 4Q+ | R$ 1.050 | R$ 210,8 mil |
| 3Q | R$ 650 | R$ 130,5 mil |
| 2Q | R$ 450 | R$ 90,3 mil |
| 1Q | R$ 385 | R$ 77,3 mil |

→ No faturamento bruto, **3Q e 4Q+ lideram** por acomodarem mais hóspedes.

### Nível 2 — Eficiência de capital (receita/m² e retorno)
| Tipologia | Receita/m² | Retorno bruto anual |
|---|---|---|
| 1Q | R$ 1.807/m² | 9,6% |
| **2Q** | R$ 1.202/m² | **10,3%** |
| 3Q | R$ 1.183/m² | 9,0% |
| 4Q+ | R$ 1.114/m² | 5,7% |

→ Sob ótica de investimento (capital eficiente), **as unidades menores (2Q, e 1Q em receita/m²) são o perfil ideal**; os imóveis grandes (4Q+) perdem eficiência de capital.

**Tipo de anúncio**: `apartamento` domina o mercado (908 de 994 listings com preço) e tem a maior receita por unidade (R$ 112 mil/ano); casas/hotéis têm volume irrelevante. Hosts profissionais têm receita mediana levemente superior (R$ 113,2 mil vs R$ 110,2 mil).

---

## Q2 — Melhor localização em termos de receita

| Bairro | n | Diária mediana | Receita anual (55%) |
|---|---|---|---|
| **MEIA PRAIA** | 630 | R$ 590 | **R$ 118,4 mil** |
| CANTO DA PRAIA | 8 | R$ 559 | R$ 112,2 mil |
| TABULEIRO DOS OLIVEIRAS | 20 | R$ 540 | R$ 108,4 mil |
| CENTRO | 205 | R$ 509 | R$ 102,2 mil |
| MORRETES | 82 | R$ 471 | R$ 94,5 mil |

→ **MEIA PRAIA é a melhor localização em receita consolidada** (diárias altas + maior oferta/demanda). CANTO DA PRAIA e AREAL mostram números altos, mas com volume mínimo (baixa confiabilidade). **CENTRO** aparece como alternativa relevante e de maior volume na região central.

---

## Q3 — Características que explicam as melhores receitas

Regressão múltipla sobre 994 listings (alvo: receita anual, cenário 55%), variáveis padronizadas. **R² = 0,45**.

**Drivers significativos (positivos):**
- Nº de quartos (+21,1) *** — o mais forte
- Nº de banheiros (+18,8) ***
- Nº de hóspedes (+13,6) ***
- Precisão do anúncio (accuracy_rating) (+22,8) *
- Satisfação geral (+8,8) *

**Não significativos / fracos**: star_rating global, cleanliness, location, nº de reviews, clean_fee, nº de fotos.

> **Conclusão**: a receita é explicada principalmente pela **estrutura e capacidade do imóvel** (tamanho), não pelas avaliações. Ratings global não têm poder explicativo relevante.

---

## Q4 — O que a Seazone compraria hoje

**Critério**: retorno bruto anual (receita ÷ preço de venda) com **confiabilidade ALTA/MÉDIA** (n_listings ≥ 5/15 e n_anuncios ≥ 10/30), avaliado em 3 cenários de ocupação (40/55/70%).

### Ranking de pares [Bairro + Tipologia] por retorno (ALTA confiabilidade, cenário base 55%)
**Retorno Bruto** = receita bruta anual ÷ preço de venda mediano.
**Retorno Líquido** = (receita bruta − condomínio_anual − IPTU) ÷ preço de venda mediano.

| Bairro | Tipologia | Diária med | Preço venda | **Retorno Bruto 55%** | **Retorno Líquido 55%** |
|---|---|---|---|---|---|
| **MORRETES** | **2Q** | R$ 446 | R$ 790 mil | **11,3%** | **10,8%** |
| **CENTRO** | **2Q** | R$ 557 | R$ 1,145M | **9,8%** | **9,2%** |
| **MEIA PRAIA** | **2Q** | R$ 450 | R$ 1,065M | **8,5%** | **7,9%** |

> Pares como TABULEIRO 3, VARZEA 3Q e ILHOTA 1Q mostraram retornos maiores, porém com **volume mínimo** — baixa confiabilidade, não usados na decisão.

### Estimativa simples de retorno (cenários de ocupação)
A receita bruta anual estimada é `diária mediana × 365 × taxa_ocupação`. Para o retorno líquido, deduzimos condomínio (`monthly_condo_fee × 12`) e IPTU (`yearly_iptu`) medianos do VivaReal.

**Valores por ativo recomendado (cenário base 55%):**

| Ativo | Receita bruta/ano | Condomínio+IPTU/ano | Receita líquida/ano | Retorno Bruto 55% | Retorno Líquido 55% |
|---|---|---|---|---|---|
| **MORRETES 2Q** | R$ 89.535 | R$ 4.035 | R$ 85.510 | 11,3% | **10,8%** |
| **CENTRO 2Q** | R$ 111.818 | R$ 6.346 | R$ 105.472 | 9,8% | **9,2%** |
| **MEIA PRAIA 2Q** | R$ 90.337 | R$ 6.050 | R$ 84.287 | 8,5% | **7,9%** |

**Recomendação de compra**:
1. **Apartamento 2Q em MORRETES** — melhor retorno (bruto 11,3% / líquido 10,8%), preço de compra acessível (R$ 790 mil) e confiabilidade ALTA (volumes grandes).
2. **Apartamento 2Q no CENTRO** — bom retorno (líquido 9,2%), região central de alto volume e demanda, alinhado a oferta consolidada.
3. **Apartamento 2Q em MEIA PRAIA** — receita consolidada maior, retorno moderado (líquido 7,9%), mas localização top com demanda robusta.

> Os retornos acima descontam condomínio e IPTU mas **não** consideram custos de operação/vacância do short stay (hospedagem, limpeza, energia), deságio de taxa da plataforma nem impostos sobre a renda — portanto são **retornos líquidos de custos imobiliários, não líquidos de operação**. A estimativa é uma **aproximação** do cap rate.

---

## Posição sobre a tese dos "compactos (studio/1Q) no Centro"

> **Os dados sustentam parcialmente, mas recomendam ajuste.**

- A tese acerta ao apontar que **unidades menores têm melhor eficiência de capital** (receita/m² e retorno) → confirmado no Nível 2 da Q1.
- Porém, **o melhor retorno não está no 1Q, e sim no 2Q** (10,3% vs 9,6% do 1Q em termos medianos), em todos os 3 cenários.
- E **o melhor retorno com confiabilidade alta está em MORRETES 2Q (11,3%)**, não no CENTRO 1Q. O CENTRO 2Q (9,8%) é a 2ª opção sólida.
- **1Q para short stay tende a ter menor receita bruta e ticket** e menor retorno/m² do que 2Q no mesmo capital.

**Conclusão**: recomendamos **potencializar a tese** — em vez de "compactos 1Q no Centro", investir em **2Q (não 1Q)** e priorizar **MORRETES e depois CENTRO**, mantendo MEIA PRAIA para receita consolidada.

---

## Metodologia e limitações

A análise foi conduzida segundo os princípios do ciclo **CRISP-DM** (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment), integrados a uma abordagem **Hypothesis-Driven Problem Solving**: partimos da tese interna sobre os compactos no Centro e a submetemos a **testes empíricos de falseamento** — confrontando-a com dados de receita por m², eficiência de capital e retorno por confiabilidade — em vez de buscar apenas confirmação. A modelagem de **unit economics** foi feita por **sensibilidade de ocupação**, estimando receita bruta e líquida em três cenários (40/55/70%) para quantificar o risco de premissa de ocupação sobre o retorno.

- **Receita** modelada com `Price_AV` (diária) × 365 × taxa de ocupação em **3 cenários (40/55/70%)**. `Price_AV` indica **preço por data**, não ocupação confirmada — por isso usamos cenários em vez de assumir dias ocupados.
- **Retorno líquido** deduz condomínio (`monthly_condo_fee × 12`) e IPTU (`yearly_iptu`) medianos do VivaReal, mas não descontam custos de operação.
- **Limitação da janela**: dados só cobrem **jan–abr 2025 (verão)**. As diárias de inverno provavelmente são menores; a anualização assume que a diária mediana observada se sustenta o ano todo — pode **superestimar** receita anual em todos os cenários.
- **Outliers/limpeza**: diárias > R$ 3.000 removidas (5); bairro 'none' → NaN; VivaReal filtrado para apartamentos, preço ≥ R$ 100 mil e área ≥ 15 m².
- **Confiabilidade**: pares com n_listings e n_anuncios baixos marcados como BAIXA e excluídos da decisão principal.

## Arquivos de apoio
- `scripts/` — pipeline numerado (01 a 14)
- `output/` — planilhas e relatórios intermediários
- `ai-log/` — registro das conversas com a IA (processo)
