# Hackathon Jovens Talentos AI Builder 2026 — Seazone

**Vídeo de apresentação (3 min):** _[cole aqui o link do Google Drive — compartilhamento "qualquer pessoa com o link"]_

---

## Recomendação de Investimento em Itapema (SC)

Análise completa e decisão de investimento no **`relatorio.md`** (resumo executivo, Q1–Q4, posição sobre a tese dos compactos e metodologia).

**Resumo da recomendação:** apartamentos **2Q** em **MORRETES**, **CENTRO** e **MEIA PRAIA** — com retorno líquido estimado (cenário 55% de ocupação) de **10,8%**, **9,2%** e **7,9%** ao ano, respectivamente. Os dados refutam a tese original dos "compactos 1Q no Centro": o eficiente é o **2Q**, e o melhor retorno está em **Morretes**.

---

## Como rodar

### Requisitos
- Python 3.14+ (testado no Windows)
- Dependências: `requirements.txt` (`pandas`, `numpy`, `statsmodels`)

### Setup
```bash
pip install -r requirements.txt
```

### Execução (pipeline em ordem)
```bash
python scripts/01_visualizar.py      # inspeção bruta das 5 bases
python scripts/02_dominio.py         # domínio de campos
python scripts/03_join_precos.py     # join + diária/dias observados
python scripts/04_auditoria.py       # integridade do join / outliers
python scripts/05_limpeza.py         # limpeza (bairro none, outlier)
python scripts/07_receita_cenarios.py# receita em 3 cenários de ocupação
python scripts/09_consolidado.py     # tabela consolidada [bairro+tipologia]
python scripts/11_confiabilidade.py  # classificação de confiabilidade
python scripts/12_respostas_q1q2q3.py# respostas Q1/Q2/Q3
python scripts/13_eficiencia_capital.py # receita/m² e retorno por tipologia
python scripts/14_regressao_q3.py    # regressão Q3
python scripts/15_retorno_liquido.py # retorno líquido dos 3 ativos
```

Cada script grava produtos em `output/` e imprime resumos no terminal.

---

## Estrutura do repositório

```
jt2026-ricardo-escalante/
├── README.md              # este arquivo (como rodar + onde está a resposta)
├── relatorio.md           # ★ RESPOSTA FINAL (recomendação e análise)
├── index.html             # enunciado do desafio (offline)
├── requirements.txt       # dependências Python
├── data/                  # 5 CSVs brutos (input)
├── scripts/               # pipeline numerado (01–15)
├── output/                # planilhas e relatórios intermediários
└── ai-log/                # conversas com a IA exportadas em texto
```

---

## Onde está a resposta

- **Recomendação e análise**: [`relatorio.md`](relatorio.md)
- **Registro do processo com IA**: pasta [`ai-log/`](ai-log/)
- **Pesquisas/planilhas**: `output/`
- **Código**: `scripts/`

---

## Sobre o desafio

- **Missão**: recomendar investimento imobiliário para a Seazone em Itapema (SC), a partir de dados de Airbnb (venda/curta estadia) e VivaReal (compra).
- **4 perguntas** (perfil de imóvel, localização, fatores de receita e o que comprar) — respondidas em `relatorio.md`.
- **Enunciado completo**: [seazone-tech.github.io/jovens-talentos-2026-hackathon-data](https://seazone-tech.github.io/jovens-talentos-2026-hackathon-data/) ou [`index.html`](index.html).

---

*Seazone — Jovens Talentos AI Builder 2026*