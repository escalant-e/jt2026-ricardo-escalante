# 01 — Contexto e plano

## Pedido do analista
> "Você é um especialista em análise de dados para investimento imobiliário. Nosso papel é prover assistência num desafio estilo hackathon. Temos uma base do mercado imobiliário de Itapema (SC) e precisamos responder: (1) melhor perfil de imóvel, (2) melhor localização em termos de receita, (3) características que explicam as melhores receitas, (4) se a Seazone fosse investir hoje, o que compraríamos e por quê, com estimativa simples de retorno. Entregas: repositório público com pasta ai-log/, README explicando como rodar, recomendação final em relatorio.md, planilhas/códigos/consultas."

## O que a IA fez
- Confirmou o contexto e mapeou os 5 arquivos do diretório de trabalho.
- Listou a estrutura esperada de entrega (pasta `ai-log/`, `README.md`, `relatorio.md`, scripts, outputs).
- Identificou o enunciado completo do desafio no `index.html` e na pasta, destacando:
  - 4 perguntas abertas (critério é definido pelo candidato);
  - **Tese interna a avaliar**: "apartamentos compactos (studio/1Q) no Centro seriam a aposta mais eficiente" — a resposta deve tomar posição;
  - Entregáveis: repositório público + vídeo de 3 min no Google Drive (link na 1ª linha do README) + `ai-log/` com conversas em texto (print não vale);
  - Avaliação: raciocínio/análise 45%, processo com IA 30%, comunicação 25%.

## Decisões do analista
- Manter a pasta de trabalho `jt2026-ricardo-escalante/` e a configuração de ambiente (Python 3.14 + pandas/numpy).
- Trabalhar passo a passo, com **validação do analista a cada etapa** (a IA não avança sozinha).
- Explorar os dados antes de qualquer modelagem.

## Resultado
- Estrutura criada: `scripts/`, `output/`, `ai-log/`.
- Plano de ataque esboçado: explorar → modelar receita → responder Q1-Q4 → relatório/README → ai-log.

## Lição registrada
O enunciado explicita que "os termos melhor/perfil/localização são propositalmente abertos — você define o critério e justifica". Isso orientou todo o resto: cada escolha de critério precisaria ser **justificada e documentada**.