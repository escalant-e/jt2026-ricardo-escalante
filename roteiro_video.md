# Roteiro do Vídeo e Registro do Processo com IA

> Material de apoio para o **vídeo de até 3 minutos** (Google Drive) e para a pasta `ai-log/`.
> Tópicos exigidos pelo desafio: (1) como a IA foi usada no processo, (2) o que faria com mais uma semana, (3) roteiro da apresentação.

---

## 1 — Como a IA foi usada no processo

A IA (OpenCode + modelo DeepSeek) foi usada como **ferramenta de trabalho colaborativa**, não como substituta da decisão. O processo registrado reflete isso:

- **Curadoria e exploração de dados**: a IA gerou scripts para ler e inspecionar os 5 CSVs (estrutura, tipos, nulos, amostras) e produziu uma visualização HTML das bases brutas para revisão.
- **Explicitação de hipóteses**: a cada etapa, a IA propôs hipóteses (ex.: interpretação do `Price_AV`) e **aguardou validação do humano** antes de avançar — nenhum passo crítico foi tomado autonomamente.
- **Descoberta de inconsistências**: a IA identificou problemas — linhas duplicadas de owner, `min_nights` constante, bairro `none`, grupos com n pequeno — que foram tratados com o aval da equipe.
- **Ponto de virada no processo (Price_AV)**: ao questionar se as datas do `Price_AV` eram de ocupação ou de disponibilidade, a IA rodou um diagnóstico (distribuição por dia da semana, preenchimento do calendário) que mostrou padrão de **disponibilidade/precificação**, e não reserva. Isso levou à decisão coletiva de **modelar receita por cenários de ocupação** em vez de assumir dias ocupados — registrado no script `06_diagnostico_av.py`.
- **Análises estatísticas**: regressão múltipla (Q3) gerada e interpretada com apoio da IA, incluindo o tratamento de colinearidade e dos coeficientes negativos de ratings.
- **Auditoria crítica**: a IA atuou como revisor sênior (deadline), apontando fragilidades — sensibilidade do limiar de confiabilidade, nomeclatura financeira, falta de racional econômico — que foram corrigidas no `relatorio.md`.
- **Papel do humano**: decisões de critério (limiar de outlier R$ 3.000, taxas 40/55/70%, filtros do VivaReal, nomenclatura, tom da tese) foram **todas do analista**; a IA sugeriu e testou, o humano decidiu.

## 2 — O que faríamos se tivéssemos mais uma semana

1. **Dados de ano completo** (não só jan–abr/verão) para calibrar a sazonalidade real e estimar ocupação/renda inverno — removendo a maior limitação da análise.
2. **Custos operacionais reais de short stay** (limpeza, energia, taxa da plataforma, vacância, gestão) para transformar o "retorno líquido de encargos" em um **NOI/cap rate completo**.
3. **Modelo preditivo de precificação e demanda** mais robusto (testes com validação cruzada, VIF, árvores) + feature engineering (proximidade da praia, densidade de oferta).
4. **Análise qualitativa de liquidez imobiliária**: tempo de venda por bairro/tipo, dispersão de preços e de diária no mesmo bairro.
5. **Comparação com ports/benchmarks** de operação (Seazone) e análise de **competição local** (nº de hosts profissionais por bairro-tipo).
6. **Validação com dados externos** (IBGE/setores censitários, IPTU/IPTU, oferta de lançamentos) para testar a hipótese de renda da terra em Morretes.
7. **Análise de sensibilidade do limiar de confiabilidade** (5/10/15/20 listings) para apresentar a robustez da decisão 2Q.

## 3 — Roteiro do vídeo (até 3 minutos)

**Abertura (0:00–0:15)**
> "Recomendação de investimento imobiliário em Itapema para a Seazone, com base em 4.441 anúncios de Airbnb e 8.329 de venda."

**A pergunta e o método (0:15–0:50)**
> "Qual perfil, localização e características explicam a melhor receita? Usei dados de diária (`Price_AV`), perfil dos imóveis (Details), localização (Mesh) e preços de venda (VivaReal), com receita projetada em cenários de ocupação. A tese interna falava em compactos 1Q no Centro — eu testei essa tese nos dados."

**Números-chave (0:50–1:35)**
> "Dois fatos: (1) apartamentos de 3Q/4Q dominam o faturamento bruto, mas (2) em retorno sobre capital, unidades menores vencem — o 2Q dá 10,3% de retorno vs 5,7% de 4Q+. Em localização, Meia Praia lidera a receita. Os drivers de receita são tamanho/capacidade, não ratings."

**A decisão (1:35–2:15)**
> "Compraria parcela de 2Q em Morretes (retorno líquido de encargos 10,8%), depois Centro (9,2%) e Meia Praia (7,9%) — priorizando reprodutibilidade estatística e ticket acessível. Sobre os compactos: tese parcialmente validada, mas reposicionada para 2Q e Morretes."

**Fechamento (2:15–3:00)**
> "Como usei a IA: a ferramenta explorou, gerou scripts, identificou que o Price_AV é disponibilidade (não ocupação) e auditou a análise; eu decidi cada critério. Com mais uma semana eu acrescentaria ano completo, custos operacionais e validação externa da tese de Morretes."

---

*Documento de apoio — análise completa em `relatorio.md`.*