# 02 — Exploração dos dados

## Pedido do analista
> "Vamos visualizar os 5 arquivos de uma vez e você pode exportar para a pasta output/. No terminal, exiba linhas/colunas, tipos, nulos e as 5 primeiras linhas. Na pasta output/, salve um arquivo com as 5 bases em tabelas HTML (UTF-8, preservando todos os campos). Ainda não aplique filtros."

## O que a IA fez
- Criou `scripts/01_visualizar.py`, que imprime as métricas no terminal e gera `output/visualizacao_brutos.html` (tabelas das 5 bases + metadados por coluna).

## Achados iniciais (brutos)

| Arquivo | Linhas | Colunas | Principais campos |
|---|---|---|---|
| Details_Itapema.csv | 4.441 | 35 | listing_id, título, descrição, quartos, banheiros, hóspedes, ratings, tipo, owner_id, amenities |
| Hosts_ids_Itapema.csv | 4.440 | 11 | owner_id, nome, superhost, reviews, anos |
| Mesh_Ids_Data_Itapema.csv | 4.441 | 8 | listing_id, lat/long, bairro |
| Price_AV_Itapema.csv | 118.839 | 4 | listing_id, date, price, aquisition_date |
| VivaReal_Itapema.csv | 8.329 | 22 | preço venda, condomínio, IPTU, área, quartos, bairro |

- **Details**: `listing_type` (apartamento 3.710, casa 443, outros, hotel); quartos variam 0–16.
- **Mesh**: bairros — Meia Praia 2.860, Centro 657, Morretes 441, etc.
- **Price_AV**: calendário de preço 06/01/2025 → 20/04/2025, 1.005 listings únicos (de 4.441); datas/capturas repetidas.
- **VivaReal**: `rental_price` 100% nulo (só venda); `yearly_iptu` e `monthly_condo_fee` ~30% nulos.
- **Hosts**: campo `response_rate_shown` 100% nulo; `owner_id` duplicados (snapshots).

## Decisões do analista
- Validou a leitura dos dados como "informações dos listings, host, localização, preço ao longo do tempo, e o norte de preço de venda do VivaReal".
- Concordou que a métrica de análise por bairro/fatores era viável e que o "melhor perfil" precisaria de critério.

## Resultado
- Base bruta compreendida e documentada; sem filtros aplicados (conforme pedido).

## Lição registrada
O `Price_AV` parecia ser a chave para "receita", mas sua interpretação ainda não estava definida — isso viraria o ponto de virada da análise.