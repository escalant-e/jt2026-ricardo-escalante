# 04 — A natureza do Price_AV e a modelagem de receita por cenários

## Questionamento do analista (ponto de virada)
> "Acho que podemos ter cometido um equívoco nos dias ocupados. O Price_AV é descrito como 'Preço por anúncio, por data de estadia e por data de captura'. Pode ser que as datas sejam, na verdade, as datas em que o imóvel está desocupado e disponível."

## O que a IA fez
- Reconheceu que `Price_AV` = **"AVailability"**, não ocupação.
- Investigou com `scripts/06_diagnostico_av.py`:
  - Distribuição de preços **uniforme por dia da semana** (seg–dom, ~8.200–8.550 linhas cada) — incompatível com "dias ocupados" (esperaríamos concentração em fins de semana/verão).
  - **Preenchimento alto do calendário**: mediana 83% dos dias com preço na janela de cada listing; exemplo com 105/105 dias.
- **Conclusão da investigação**: o `Price_AV` contém **preço de diária vigente (disponibilidade/precificação)**, não ocupação confirmada. O mesmo vale para o padrão de sazonalidade (jan R$ 790 → abr R$ 480).

## Decisões do analista
1. **Descartar** a interpretação de "datas com preço = dias ocupados" e também o modelo de receita simples por soma de dias.
2. **Usar o Price_AV estritamente** para: diária de cada anúncio (mediana) e análise de sazonalidade.
3. **Renomear** a métrica de contagem de datas para `dias_observados_calendario`.
4. **Modelar Receita Anual Bruta por cenários de ocupação**: Conservador 40%, Base 55%, Otimista 70%:
   `ReceitaAnual = diária_mediana × 365 × taxa_ocupação`.
5. Registrar a limitação da **janela de verão** (jan-abr/2025) na documentação.

## Implementação
- `scripts/07_receita_cenarios.py`: renomeia métrica, gera sazonalidade, calcula receitas nos 3 cenários.

## Resultado
- **Sazonalidade**: jan R$ 790 → fev R$ 675 → mar R$ 550 → abr R$ 480 (diária mediana).
- **Receita por cenário (mediana, 994 listings)**: conservador R$ 80.300 | base R$ 110.413 | otimista R$ 140.525.
- Arquivos: `sazonalidade_*.csv`, `preco_ok.csv` (com colunas de receita por cenário).

## Lição registrada
O maior risco de viés da análise estava na interpretação do dado. A decisão de **cenarizar a ocupação** (em vez de assumir) transformou uma premissa frágil numa abordagem transparente e defensável. Este momento ficou registrado como evidência do processo analítico.