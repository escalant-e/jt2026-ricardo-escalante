# resumo-log — Resumo estruturado do processo (conversa completa em conversa-completa.md)

Este arquivo condensa os tópicos e decisões de cada fase do trabalho com a IA (OpenCode + DeepSeek).
**O registro completo, turno a turno, está em [`conversa-completa.md`](conversa-completa.md).**

---

## Fase 0 — Contexto e plano
- **Objetivo**: responder 4 perguntas de investimento imobiliário em Itapema (SC) para a Seazone e entregar repositório público + vídeo de 3 min.
- **Entregáveis obrigatórios (enunciado)**: `relatorio.md`/README com a resposta, pasta `ai-log/` com conversas em **texto** (print não vale), scripts/planilhas, e o **link do vídeo na 1ª linha do README**.
- **Tese a avaliar**: "apartamentos compactos (studio/1Q) no Centro seriam a aposta mais eficiente" — a resposta deve tomar posição.
- **Decisão**: trabalhar passo a passo, com validação do analista a cada etapa; nenhum marco avançado sem aval.

## Fase 1 — Exploração dos dados
- Inspeção bruta dos 5 CSVs (terminal + `output/visualizacao_brutos.html`).
- Esquemas: Details (4.441×35), Hosts (4.440×11), Mesh (4.441×8), Price_AV (118.839×4), VivaReal (8.329×22).
- Achados: `Price_AV` cobre 1.005 listings (jan 06/01–20/04/2025); VivaReal sem aluguel (só venda); host `response_rate_shown` 100% nulo; `owner_id` duplicados.
- **Decisão**: adotar "retorno ajustado por ocupação" como métrica central de investimento.

## Fase 2 — Join, consistência e limpeza
- Merge by `airbnb_listing_id` (Details+Mesh) e by `owner_id` (Hosts), deduplicando snapshots de owner (1.383 duplicados).
- Auditoria: 77,5% dos listings sem preço (cobertura do Price_AV, não problema de join); diárias sem valores ≤ 0; outliers em R$ 10.000.
- **Decisões de limpeza**: diária > R$ 3.000 removida da base de análise (mediana como métrica central); bairro `none` → NaN; nulos de preço mantidos na base geral (oferta), filtrados nas agregações.
- Outputs: `master_joined_limpo.csv`, `preco_ok.csv` (994 listings).

## Fase 3 — A natureza do Price_AV e modelagem de receita
- **Ponto de virada**: o analista questionou se as datas do `Price_AV` eram de ocupação ou de disponibilidade.
- IA rodou diagnóstico: preço **uniforme por dia da semana** e **preenchimento alto do calendário** → `Price_AV` = disponibilidade/precificação, **não ocupação**.
- **Decisões**: usar Price_AV só p/ diária (mediana) e sazonalidade; renomear `dias_ocupados` → `dias_observados_calendario`; modelar **Receita Anual = diária_mediana × 365 × taxa_ocupação** em 3 cenários: **40% / 55% / 70%**; documentar limitação da janela de verão.
- Sazonalidade: jan R$ 790 → abr R$ 480 (diária mediana).

## Fase 4 — Consolidação, retorno e eficiência de capital
- **VivaReal**: distribuição (percentis) antes de cortar; depois filtros: `apartamento`, `sale_price ≥ 100k`, `usable_area ≥ 15` → 7.474 anúncios.
- **Padronização**: bairros em maiúsculas/sem acento/unificados; faixas de quartos idênticas (1Q=0–1, 2Q, 3Q, 4Q+).
- Consolidação por `[bairro + tipologia]`: tabela principal só com **pares completos**; tabela secundária com todos os grupos.
- **Confiabilidade**: ALTA (n_listings ≥ 15 e n_anuncios ≥ 30), MÉDIA (≥5 e ≥10), BAIXA (demais).
- **Eficiência de capital (Q1 em níveis)**: faturamento bruto → 3Q/4Q+; receita/m² → 1Q; **retorno sobre capital → 2Q (10,3%)**; 4Q+ cai (5,7%).
- Top 3 retorno base 55% (ALTA): MORRETES 2Q 11,3% · CENTRO 2Q 9,8% · MEIA PRAIA 2Q 8,5%.

## Fase 5 — Respostas Q1–Q4
- **Q1**: recomendação de apartamento **2Q** (equilíbrio liquidez/ticket/reprodutibilidade); 3Q/4Q só em faturamento bruto; 1Q só em receita/m².
- **Q2**: **MEIA PRAIA** melhor receita consolidada (R$ 118,4 mil, n=630); CENTRO alternativa relevante; CANTO/AREAL altos mas n mínimo.
- **Q3**: regressão (R²=0,45) → tamanho/capacidade (quartos, banheiros, hóspedes) explica receita; ratings pouco relevantes; coeficientes negativos = colinearidade/mix de preço.
- **Q4**: comprar **2Q em MORRETES** (bruto 11,3% / liq. encargos 10,8%), depois **CENTRO** (9,8/9,2) e **MEIA PRAIA** (8,5/7,9). Retorno líquido = (receita − condomínio×12 − IPTU) ÷ preço.

## Fase 6 — Auditoria crítica e blindagem
- Auditoria (IA como revisor sênior) apontou 9 fragilidades; **analista aprovou as 9 correções**.
- Principais: sensibilidade do limiar de confiabilidade (se n_listings ≥ 10, MORRETES 3Q lidera), nomenclatura financeira ("Retorno Líquido de Encargos Imobiliários"), colinearidade no Q3, racional econômico (rendimentos decrescentes, renda da terra, superhosts).
- **Tese**: "parcialmente validada e reposicionada" (não refutada): ótimo é 2Q, melhor retorno em Morretes.

## Fase 7 — Entregáveis finais
- Reorganizou `output/dados/`, corrigiu links do README, criou `roteiro_video.md` (uso de IA + mais 1 semana + roteiro de vídeo).
- `relatorio.md` cita uso da IA e próximos passos.
- `ai-log/` com **resumo** (este) e **conversa completa** em texto.
- **Pendentes**: link real do vídeo na 1ª linha do README; push do repositório (público até 15/09).