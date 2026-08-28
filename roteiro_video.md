# Roteiro do Vídeo e Registro do Processo com IA

> Material de apoio para o **vídeo de até 3 minutos** (Google Drive) — alinhado à apresentação `output/apresentacao_seazone_itapema.pptx` (7 slides).
> Tópicos exigidos pelo desafio: (1) recomendação e o raciocínio por trás dela, (2) como você usou a IA no processo, (3) o que você faria se tivesse mais uma semana. O roteiro também registra os momentos-chave do processo para a pasta `ai-log/`.

---

## 1 — Como a IA foi usada no processo

A IA (OpenCode + modelo DeepSeek) foi usada como **ferramenta de trabalho colaborativa**, não como substituta da decisão. O processo registrado reflete isso:

- **Curadoria e exploração de dados**: a IA gerou scripts para ler e inspecionar os 5 CSVs (estrutura, tipos, nulos, amostras) e produziu uma visualização HTML das bases brutas para revisão.
- **Explicitação de hipóteses**: a cada etapa, a IA propôs hipóteses (ex.: interpretação do `Price_AV`) e **aguardou validação do humano** antes de avançar — nenhum passo crítico foi tomado autonomamente.
- **Descoberta de inconsistências**: a IA identificou problemas — linhas duplicadas de owner, `min_nights` constante, bairro `none`, grupos com n pequeno — que foram tratados com o aval da equipe.
- **Ponto de virada no processo (Price_AV)**: ao questionar se as datas do `Price_AV` eram de ocupação ou de disponibilidade, a IA rodou um diagnóstico (distribuição por dia da semana, preenchimento do calendário) que mostrou padrão de **disponibilidade/precificação**, e não reserva. Isso levou à decisão coletiva de **modelar receita por cenários de ocupação** em vez de assumir dias ocupados — registrado no script `06_diagnostico_av.py`.
- **Análises estatísticas**: regressão múltipla (Q3) gerada e interpretada com apoio da IA, incluindo o tratamento de colinearidade e dos coeficientes negativos de ratings.
- **Auditoria crítica**: a IA atuou como revisor sênior, apontando fragilidades — sensibilidade do limiar de confiabilidade, nomenclatura financeira, falta de racional econômico — que foram corrigidas no `relatorio.md`.
- **Papel do humano**: decisões de critério (limiar de outlier R$ 3.000, taxas 40/55/70%, filtros do VivaReal, nomenclatura, tom da tese) foram **todas do analista**; a IA sugeriu e testou, o humano decidiu.

## 2 — O que faríamos se tivéssemos mais uma semana

1. **Dados de ano completo** (não só jan–abr/verão) para calibrar a sazonalidade real e estimar ocupação/renda de inverno — removendo a maior limitação da análise.
2. **Custos operacionais reais de short stay** (limpeza, energia, taxa da plataforma, vacância, gestão) para transformar o "retorno líquido de encargos" em um **NOI/cap rate completo**.
3. **Modelo preditivo de precificação e demanda** mais robusto (validação cruzada, VIF, árvores) + feature engineering (proximidade da praia, densidade de oferta).
4. **Análise qualitativa de liquidez imobiliária**: tempo de venda por bairro/tipo, dispersão de preços e de diária no mesmo bairro.
5. **Comparação com benchmarks de operação (Seazone)** e análise de **competição local** (nº de hosts profissionais por bairro-tipo).
6. **Validação com dados externos** (IBGE/setores censitários, IPTU, oferta de lançamentos) para testar a hipótese de renda da terra em Morretes.
7. **Análise de sensibilidade do limiar de confiabilidade** (5/10/15/20 listings) para apresentar a robustez da decisão 2Q.

## 3 — Roteiro do vídeo (até 3 minutos, alinhado aos 7 slides)

> Tempos sugeridos dentro do limite de 3 min. O deck tem 7 slides e cada bloco deste roteiro corresponde a ele.

### Slide 1 — Abertura (0:00–0:12)
> "Recomendação de investimento imobiliário em Itapema para a Seazone: apostar em apartamentos 2Q, começando por Morretes. Retorno líquido de encargos em torno de 10,8% ao ano — no cenário base de 55% de ocupação — com ticket acessível e alta confiabilidade estatística."

### Slide 2 — Raciocínio: o perfil (0:12–0:50)
> "Por que 2Q? Comparei três óticas. No faturamento bruto, 3Q e 4Q dominam, pois acomodam mais gente. Mas por metro quadrado, o imóvel de 1Q é o mais produtivo: R$ 1.807 por m². E sob o critério decisivo — retorno sobre o capital investido — o 2Q vence com 10,3%, enquanto o 4Q+ despenca para 5,7%. Ou seja, em investimento, eficiência de capital manda — e o 2Q é o equilíbrio entre retorno, liquidez e reprodutibilidade estatística."

### Slide 3 — Raciocínio: localização e drivers (0:50–1:25)
> "Onde? Meia Praia lidera a receita — R$ 118 mil por ano — e o Centro é a alternativa de maior volume. O que explica receita? São os atributos estruturais: número de quartos, banheiros e hóspedes — não os ratings. Sobre a tese interna dos compactos 1Q no Centro: os dados sustentam a intuição de que unidades pequenas são eficientes em capital, mas reposicionam a aposta — o ótimo é o 2Q e o melhor retorno está em Morretes."

### Slide 4 — A recomendação (1:25–2:00)
> "Se a Seazone investisse hoje: apartamento 2Q em Morretes (retorno líquido de encargos 10,8% e preço mediano de R$ 790 mil, com volume alto de dados — alta confiabilidade), depois Centro (9,2%) e Meia Praia (7,9%). Priorizei reprodutibilidade estatística e ticket acessível, e não simplesmente a maior taxa nominal."

### Slide 5 — Como a IA foi usada (2:00–2:30)
> "Em todo o processo, a IA foi ferramenta colaborativa, e o humano decidiu cada critério. Um momento decisivo: detectamos que o Price_AV mede disponibilidade, não ocupação — então modelamos a receita por cenários de ocupação, em vez de supor dias ocupados. A IA também apontou inconsistências e auditou o relatório como revisor sênior. Tudo registrado na pasta ai-log e nos scripts."

### Slide 6 — Com mais uma semana (2:30–2:50)
> "Com mais uma semana eu fecharia três frentes: dados de ano completo, para calibrar sazonalidade e ocupação de inverno; custos operacionais reais do short stay, para chegar a um NOI/cap rate completo; e validação externa da tese de Morretes, com dados censitários."

### Slide 7 — Fechamento (2:50–3:00)
> "Então, a resposta é clara: apartamentos 2Q, começando por Morretes. Obrigado. Os detalhes completos estão no relatório do repositório."

---

## Resumo dos slides (deck `output/apresentacao_seazone_itapema.pptx`)

| Slide | Tema | Tempo |
|---|---|---|
| 1 | Capa — recomendação sintética | 0:00–0:12 |
| 2 | Raciocínio 1 — perfil em 3 óticas | 0:12–0:50 |
| 3 | Raciocínio 2 — localização + drivers + tese | 0:50–1:25 |
| 4 | A recomendação (3 ativos + como calculamos) | 1:25–2:00 |
| 5 | Como a IA foi usada | 2:00–2:30 |
| 6 | O que faria com mais uma semana | 2:30–2:50 |
| 7 | Conclusão | 2:50–3:00 |

*Documento de apoio — análise completa em `relatorio.md`.*