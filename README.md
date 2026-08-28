# Hackathon Jovens Talentos AI Builder 2026 — Seazone

**Vídeo de apresentação (3 min):** _[cole aqui o link do Google Drive — compartilhamento "qualquer pessoa com o link"]_

---

## Recomendação de Investimento em Itapema (SC)

Análise completa e decisão de investimento no **`relatorio.md`** (resumo executivo, Q1–Q4, posição sobre a tese dos compactos e metodologia).

**Resumo da recomendação:** apartamentos **2Q** em **MORRETES**, **CENTRO** e **MEIA PRAIA** — com retorno líquido de encargos imobiliários (cenário 55% de ocupação) de **10,8%**, **9,2%** e **7,9%** ao ano, respectivamente. Sobre a tese dos "compactos 1Q no Centro", a leitura é de **tese parcialmente validada e reposicionada**: unidades pequenas de fato têm alta eficiência de capital, mas o ótimo está no **2Q**, e o melhor retorno em **Morretes**.

---

## Como rodar

### Requisitos
- Python 3.14+ (testado no Windows)
- Dependências: [`requirements.txt`](requirements.txt) (`pandas`, `numpy`, `statsmodels`)

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
python scripts/06_diagnostico_av.py  # diagnóstico da natureza do Price_AV (disponibilidade vs ocupação)
python scripts/07_receita_cenarios.py# receita em 3 cenários de ocupação
python scripts/09_consolidado.py     # tabela consolidada [bairro+tipologia]
python scripts/11_confiabilidade.py  # classificação de confiabilidade
python scripts/12_respostas_q1q2q3.py# respostas Q1/Q2/Q3
python scripts/13_eficiencia_capital.py # receita/m² e retorno por tipologia
python scripts/14_regressao_q3.py    # regressão Q3
python scripts/15_retorno_liquido.py # retorno líquido de encargos dos 3 ativos
```

Cada script grava seus produtos na pasta `output/dados/` e imprime resumos no terminal.
Scripts exploratórios (01, 02, 06, 08) apenas imprimem análise/relatórios no terminal — o `06` é a evidência do processo analítico (a investigação de que o `Price_AV` = disponibilidade, não ocupação, o que motivou a modelagem por cenários de ocupação).

> **Nota**: os arquivos em `output/dados/*.csv` **já contêm os produtos finais** — não é preciso rodar o pipeline para ler a resposta (em `relatorio.md`). Os scripts existem para reprodutibilidade.

---

## Estrutura do repositório

```
jt2026-ricardo-escalante/
├── README.md              # este arquivo (como rodar + onde está a resposta)
├── relatorio.md           # ★ RESPOSTA FINAL (recomendação e análise)
├── index.html             # enunciado do desafio (offline)
├── requirements.txt       # dependências Python
├── data/                  # 5 CSVs brutos (input)
├── scripts/               # pipeline numerado (01–15) — código
├── output/
│   ├── dados/             # produtos: planilhas geradas pela análise
│   └── visualizacao_brutos.html  # inspeção visual da base bruta
└── ai-log/                # conversas com a IA exportadas em texto
```

---

## Onde está a resposta

- **Recomendação e análise**: [`relatorio.md`](relatorio.md)
- **Roteiro do vídeo + como a IA foi usada + próximos passos**: [`roteiro_video.md`](roteiro_video.md)
- **Registro do processo com IA**: pasta [`ai-log/`](ai-log/) *(a ser preenchida com as conversas exportadas)*
- **Pesquisas/planilhas**: [`output/dados/`](output/dados/)
- **Código**: [`scripts/`](scripts/)

---

## Sobre o desafio

- **Missão**: recomendar investimento imobiliário para a Seazone em Itapema (SC), a partir de dados de Airbnb (venda/curta estadia) e VivaReal (compra).
- **4 perguntas** (perfil de imóvel, localização, fatores de receita e o que comprar) — respondidas em `relatorio.md`.
- **Enunciado completo**: [seazone-tech.github.io/jovens-talentos-2026-hackathon-data](https://seazone-tech.github.io/jovens-talentos-2026-hackathon-data/) ou [`index.html`](index.html).

---

*Seazone — Jovens Talentos AI Builder 2026*