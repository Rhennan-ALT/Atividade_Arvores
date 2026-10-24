# Árvores Balanceadas: AVL vs Rubro-Negra

Questionário "Inserção em Árvores Balanceadas" (Estrutura de Dados Avançados).
Cada questão tem um script que insere as chaves do enunciado nas duas árvores,
mede o resultado e imprime a justificativa da escolha.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `arvores.py` | Implementação de AVL e Rubro-Negra, com contagem de rotações, ajustes, altura e custo de busca |
| `questao1.py` a `questao6.py` | Um script por questão, com a resposta e a justificativa |

Mantenha todos os arquivos na mesma pasta.

## Como executar

Requer Python 3, sem bibliotecas externas.

```bash
python questao1.py
```

Troque o número para rodar as outras questões.

## O que cada script imprime

1. Tabela comparando AVL e Rubro-Negra: altura, rotações, ajustes e comparações médias por busca
2. Passos de rebalanceamento de cada árvore
3. Desenho das duas árvores finais
4. Teste em escala com 20 mil chaves
5. Justificativa e resposta

O teste em escala existe porque, com poucas chaves, as duas árvores quase empatam.
Ele mostra a diferença real de comportamento.

