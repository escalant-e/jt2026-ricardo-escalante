# ai-log — Registro das conversas com a IA

Esta pasta documenta o processo de trabalho com a IA (OpenCode + DeepSeek) durante o desafio, **exportado em texto** conforme exigido pela avaliação.

**Como ler:**
- Cada arquivo corresponde a uma fase do trabalho, na ordem cronológica.
- O formato é de **diálogo estruturado**: o que foi pedido, o que a IA propôs/gerou, as **decisões do analista** e os resultados numéricos de cada etapa.
- As decisões de critério (limiares, taxas, cortes, nomenclatura, tom) foram **sempre do analista**; a IA propôs hipóteses, gerou código e auditou.

**Ordem dos arquivos:**

| # | Arquivo | Fase |
|---|---|---|
| 0 | `README.md` (este) | índice |
| 1 | `01-contexto-e-plano.md` | Contexto do desafio, entregáveis, plano inicial |
| 2 | `02-exploracao-dos-dados.md` | Inspeção bruta dos 5 CSVs |
| 3 | `03-join-e-consistencia.md` | Joins, diagnósticos, limpeza e auditoria |
| 4 | `04-modelagem-receita-sazonalidade.md` | Natureza do `Price_AV` e receita por cenários |
| 5 | `05-consolidado-e-retorno.md` | Consolidação [bairro+tipologia], confiabilidade, eficiência de capital |
| 6 | `06-respostas-e-auditoria.md` | Respostas Q1–Q4, auditoria crítica, blindagem |
| 7 | `07-entregaveis-e-video.md` | README, relatório, roteiro do vídeo |

> O processo completo também é resumido no `relatorio.md` (seção "Uso de IA no processo") e no `roteiro_video.md`.