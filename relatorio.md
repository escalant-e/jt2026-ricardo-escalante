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

**Resposta em dois níveis** (o critério é aberto pelo desafio e depende do objetivo). Mantemos a distinção entre **três métricas distintas** — nenhuma sozinha define o "melhor":

- **Máxima receita bruta** → tipologias grandes (3Q/4Q+) acomodam mais hóspedes.
- **Produtividade da área (receita/m²)** → unidades pequenas (1Q) extraem mais receita por metro quadrado.
- **Retorno sobre o capital (ROI/Cap Rate)** → medida de eficiência financeira do investimento; é o critério de decisão para a Seazone.

### Nível 1 — Faturamento bruto
| Tipologia | Diária mediana | Receita anual (cenário 55%) |
|---|---|---|
| 4Q+ | R$ 1.050 | R$ 210,8 mil |
| 3Q | R$ 650 | R$ 130,5 mil |
| 2Q | R$ 450 | R$ 90,3 mil |
| 1Q | R$ 385 | R$ 77,3 mil |

→ No faturamento bruto, **3Q e 4Q+ lideram** por acomodarem mais hóspedes.

### Nível 2 — Produtividade de área (receita/m²)
| Tipologia | Receita/m² |
|---|---|
| **1Q** | R$ 1.807/m² |
| 2Q | R$ 1.202/m² |
| 3Q | R$ 1.183/m² |
| 4Q+ | R$ 1.114/m² |

→ Sob produtividade de área, **1Q** é o mais eficiente (maximiza receita por metro quadrado).

### Nível 3 — Retorno sobre capital (ROI/Cap Rate)
| Tipologia | Retorno bruto anual |
|---|---|
| 1Q | 9,6% |
| **2Q** | **10,3%** |
| 3Q | 9,0% |
| 4Q+ | 5,7% |

→ Sob retorno sobre o capital investido, **2Q** tem o maior retorno (10,3%), e **4Q+** o menor (5,7%).

**Conclusão Q1**: o perfil recomendado é o **2Q** — ele **equilibra liquidez operacional (ticket intermediário), menor barreira de entrada vs 3Q/4Q+ e reprodutibilidade estatística** (volumes altos). O 1Q maximiza produtividade de área, mas o 2Q maximiza o retorno sobre capital com maior adaptação à demanda de famílias/grupos pequenos.

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

**Atenção à colinearidade do bloco de tamanho**: `quartos`, `banheiros`, `hóspedes` e `camas` são **altamente correlacionados entre si** (formam um "bloco de capacidade" do imóvel). Por isso, os coeficientes individuais desse bloco **não devem ser lidos isoladamente** como efeitos independentes — a leitura correta é que o **bloco agregado de tamanho/capacidade** é o maior determinante de receita. Os coeficientes **negativos** de `communication_rating` (−47,6) e `value_rating` (−32,4) também refletem esse fenômeno de mix de preço/multicolinearidade: unidades menores e mais baratas tendem a receber avaliações de valor/comunicação mais altas, o que vira correlação espúria com receita menor — **não** indicam que "pior comunicação gera mais receita".

> **Conclusão**: a receita é explicada principalmente pela **estrutura e capacidade do imóvel** (tamanho), não pelas avaliações. Ratings global não têm poder explicativo relevante.

---

## Q4 — O que a Seazone compraria hoje

**Critério**: retorno sobre capital (receita ÷ preço de venda) com **confiabilidade ALTA/MÉDIA** (n_listings ≥ 5/15 e n_anuncios ≥ 10/30), avaliado em 3 cenários de ocupação (40/55/70%). Distinguimos **Retorno Bruto** (receita bruta ÷ preço) de **Retorno Líquido de Encargos Imobiliários** (= receita bruta − condomínio_anual − IPTU, ÷ preço).

### Ranking de pares [Bairro + Tipologia] por retorno (ALTA confiabilidade, cenário base 55%)
| Bairro | Tipologia | Diária med | Preço venda | **Retorno Bruto 55%** | **Retorno Liq. Encargos 55%** |
|---|---|---|---|---|---|
| **MORRETES** | **2Q** | R$ 446 | R$ 790 mil | **11,3%** | **10,8%** |
| **CENTRO** | **2Q** | R$ 557 | R$ 1,145M | **9,8%** | **9,2%** |
| **MEIA PRAIA** | **2Q** | R$ 450 | R$ 1,065M | **8,5%** | **7,9%** |

> Pares como TABULEIRO 3Q, VARZEA 3Q e ILHOTA 1Q mostraram retornos maiores, porém com **volume mínimo** — baixa confiabilidade, não usados na decisão.

### Estimativa simples de retorno (cenários de ocupação)
A receita bruta anual estimada é `diária mediana × 365 × taxa_ocupação`. Para o retorno líquido de encargos, deduzimos condomínio (`monthly_condo_fee × 12`) e IPTU (`yearly_iptu`) medianos do VivaReal.

**Valores por ativo recomendado (cenário base 55%):**

| Ativo | Receita bruta/ano | Condomínio+IPTU/ano | Receita liq. encargos | Retorno Bruto 55% | Retorno Liq. Encargos 55% |
|---|---|---|---|---|---|
| **MORRETES 2Q** | R$ 89.535 | R$ 4.035 | R$ 85.510 | 11,3% | **10,8%** |
| **CENTRO 2Q** | R$ 111.818 | R$ 6.346 | R$ 105.472 | 9,8% | **9,2%** |
| **MEIA PRAIA 2Q** | R$ 90.337 | R$ 6.050 | R$ 84.287 | 8,5% | **7,9%** |

**Recomendação de compra**:
1. **Apartamento 2Q em MORRETES** — melhor retorno (bruto 11,3% / liq. encargos 10,8%), preço de compra acessível (R$ 790 mil) e confiabilidade ALTA (volumes grandes: 59 listings Airbnb e 1.043 anúncios VivaReal).
2. **Apartamento 2Q no CENTRO** — bom retorno (liq. 9,2%), região central de alto volume e demanda, alinhado a oferta consolidada.
3. **Apartamento 2Q em MEIA PRAIA** — receita consolidada maior, retorno moderado (liq. 7,9%), mas localização top com demanda robusta.

**Por que Morretes 2Q é a escolha de equilíbrio (e não o de maior retorno bruto puro)?**
- **Liquidez operacional**: 2Q tem ticket intermediário e boa adaptação a famílias/grupos pequenos, com maior base de demanda que o 1Q.
- **Menor barreira de entrada**: preço de compra de R$ 790 mil vs R$ 2,1M+ (3Q do Centro) e R$ 3,7M (4Q) — menor capital em risco e mais fácil de escalar.
- **Reprodutibilidade estatística**: o MORRETES 2Q é ALTA confiabilidade com volumes expressivos (59 listings / 1.043 anúncios), o que torna o retorno de 10,8% muito mais robusto do que os de pares com n alto demais (TABULEIRO 3Q, VARZEA) ou grande demais (4Q+).
- Vale registrar: o **MORRETES 3Q** tem retorno bruto maior (14,3%), mas é MÉDIA confiabilidade (11 listings Airbnb) e exige ticket maior (R$ 845 mil) — a seleção prioriza **reprodutibilidade e liquidez**, não máxima taxa nominal.

> Os retornos acima descontam condomínio e IPTU (chamados de **Retorno Líquido de Encargos Imobiliários**), mas **não** consideram custos de operação/vacância do short stay (hospedagem, limpeza, energia), deságio de taxa da plataforma nem impostos sobre a renda — portanto **não são cap rate líquido de operação**. A estimativa aproxima um NOI imobiliário (antes de opex).

---

## Fundamentação econômica

A recomendação não repousa apenas em médias amostrais; há um racional econômico explícito por trás das escolhas:

**a) Rendimentos marginais decrescentes em tipologias grandes.** Os dados evidenciam uma curva de retorno marginal decrescente ao adicionar capacidade: o 2Q gera **10,3%** de retorno sobre capital, o 3Q **9,0%** e o 4Q+ despenca para **5,7%** — mesmo com receita bruta maior. A capacidade adicional de 3Q→4Q+ custa muito mais capital (preço/m² aumenta e o retorno colapsa) do que a receita marginal que produz. É o padrão econômico de **custo marginal crescente × utilidade marginal decrescente** aplicado a dormitórios.

**b) Renda da terra urbana em Morretes.** O retorno superior de MORRETES 2Q (10,8% líquido) não é anomalia; reflete a **teoria da renda da terra urbana (Ricardo/Alonso)**: bairros com preço de entrada menor (R$ 790 mil vs R$ 1,14M no Centro) e oferta de solo mais abundante podem oferecer o mesmo fluxo de receita a custo de aquisição inferior, capturando renda da terra relativamente subprecificada. É uma tese de **arbitragem de localização** — consolidada (não especulativa) dado o volume de transações.

**c) Sinalização de mercado em Superhosts.** Achado contra-intuitivo: hosts superhost têm receita mediana **menor** (R$ 103,8 mil vs R$ 115,4 mil). A interpretação econômica mais provável é **efeito de mix de portfólio** (superhosts concentram-se desproporcionalmente em 1Q/2Q e bairros de diária menor, onde há mais oferta administrada profissionalmente), não inferioridade de qualidade — ou **prêmio de risco/precificação** (hosts menores aceitam menos ocupação a preço maior). Esse sinal reforça que **tamanho/capacidade** (não avaliação) é o driver real, e deve ser objeto de validação com mais dados — nunca lido como "superhost é pior".

---

## Posição sobre a tese dos "compactos (studio/1Q) no Centro"

> **Os dados sustentam parcialmente e reposicionam a tese — não a refutam.**

- A tese acerta ao apontar que **unidades menores têm melhor eficiência de capital** (receita/m² e retorno) → confirmado no Nível 2/3 da Q1.
- Porém, **o melhor retorno não está no 1Q, e sim no 2Q** (10,3% vs 9,6% do 1Q em termos medianos), em todos os 3 cenários.
- E **o melhor retorno com confiabilidade alta está em MORRETES 2Q (11,3%)**, não no CENTRO 1Q. O CENTRO 2Q (9,8%) é a 2ª opção sólida.
- **1Q para short stay tende a ter menor receita bruta e ticket** e menor retorno do que o 2Q no mesmo capital; o 1Q só **vence em receita/m²**, mas com menor robustez na capitalização.

**Conclusão**: recomendamos **potencializar a tese (parcialmente validada e reposicionada)** — em vez de "compactos 1Q no Centro", investir em **2Q (não 1Q)** e priorizar **MORRETES e depois CENTRO**, mantendo MEIA PRAIA para receita consolidada. A intuição original (compacidade = eficiência de capital) permanece correta; o que os dados ajustam é **a tipologia ótima (2Q) e a localização ótima (Morretes/Centro)**.

---

## Metodologia e limitações

A análise foi conduzida segundo os princípios do ciclo **CRISP-DM** (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment), integrados a uma abordagem **Hypothesis-Driven Problem Solving**: partimos da tese interna sobre os compactos no Centro e a submetemos a **testes empíricos de falseamento** — confrontando-a com dados de receita por m², eficiência de capital e retorno por confiabilidade — em vez de buscar apenas confirmação. A modelagem de **unit economics** foi feita por **sensibilidade de ocupação**, estimando receita bruta e líquida em três cenários (40/55/70%) para quantificar o risco de premissa de ocupação sobre o retorno.

- **Receita** modelada com `Price_AV` (diária) × 365 × taxa de ocupação em **3 cenários (40/55/70%)**. `Price_AV` indica **preço por data**, não ocupação confirmada — por isso usamos cenários em vez de assumir dias ocupados.
- **Retorno líquido de encargos imobiliários** deduz condomínio (`monthly_condo_fee × 12`) e IPTU (`yearly_iptu`) medianos do VivaReal, mas não desconta custos de operação (limpeza, energia, taxa de plataforma, vacância). <sup>Definição de nomenclatura sincronizada com os outputs (`retorno_bruto_55_pct`, `retorno_liq_encargos_55_pct`).</sup>
- **Limitação da janela**: dados só cobrem **jan–abr 2025 (verão)**. As diárias de inverno provavelmente são menores; a anualização assume que a diária mediana observada se sustenta o ano todo — pode **superestimar** receita anual em todos os cenários.
- **Outliers/limpeza**: diárias > R$ 3.000 removidas (5); bairro 'none' → NaN; VivaReal filtrado para apartamentos, preço ≥ R$ 100 mil e área ≥ 15 m².
- **Confiabilidade**: pares com n_listings e n_anuncios baixos marcados como BAIXA e excluídos da decisão principal.

### Viés de Cobertura da Amostra

O `Price_AV` cobre **22,4% do universo total de listings** (994 de 4.441 anúncios) — e essa cobertura é **desigual por bairro**, o que pode enviesar as estimativas de diária e receita por localização:

| Bairro | Listings total | Com preço | Cobertura |
|---|---|---|---|
| CENTRO | 657 | 205 | 31,2% |
| CANTO DA PRAIA | 28 | 8 | 28,6% |
| SERTAOZINHO | 21 | 5 | 23,8% |
| MEIA PRAIA | 2.860 | 630 | 22,0% |
| AREAL | 5 | 1 | 20,0% |
| MORRETES | 441 | 82 | 18,6% |
| ILHOTA | 56 | 10 | 17,9% |
| CASA BRANCA | 88 | 15 | 17,0% |
| TABULEIRO DOS OLIVEIRAS | 129 | 20 | 15,5% |
| SERTAO DO TROMBUDO | 22 | 3 | 13,6% |
| VARZEA | 43 | 5 | 11,6% |
| ALTO SAO BENTO | 62 | 5 | 8,1% |
| LEOPOLDO ZARLING | 18 | 1 | 5,6% |

**Implicações**: (i) bairros com cobertura alta (CENTRO, CANTO DA PRAIA) têm estimativas de diária/receita mais robustas; (ii) bairros de baixa cobertura (ALTO SAO BENTO, LEOPOLDO ZARLING e outros com ≤5 listings) são pouco representados e tiveram menos peso na decisão; (iii) como o `Price_AV` só cobre a janela de verão, esse viés soma-se à limitação sazonal já descrita. Usamos a **mediana** (robusta a isso) e excluímos da decisão pares com volume mínimo.

## Arquivos de apoio
- `scripts/` — pipeline numerado (01 a 15), incluindo `06_diagnostico_av.py` (evidência da investigação sobre a natureza do `Price_AV`)
- `output/dados/` — planilhas finais sincronizadas com este relatório (nomenclatura `retorno_bruto_*` e `retorno_liq_encargos_*`)
- `output/visualizacao_brutos.html` — inspeção visual da base bruta
- `roteiro_video.md` — como a IA foi usada, o que faria com mais uma semana e o roteiro do vídeo
- `ai-log/` — registro das conversas com a IA (processo)
