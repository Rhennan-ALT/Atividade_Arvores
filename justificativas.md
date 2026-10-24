# Questão 1 - Justificativa

Escolha: AVL
------------------------------------------------------------------------

## 1) O que domina a carga?
   
   A BUSCA. O catálogo é montado uma vez de manhã e depois consultado
   milhares de vezes por minuto nos caixas.

   - Custo de reequilibrar a árvore: pago só uma vez, na montagem.
   - Custo de cada comparação a mais: pago em toda consulta do dia.

   Dessa forma o que importa é ter a árvore o mais baixa possível.

## 2) Qual árvore fica mais baixa?
   
   A AVL, porque ela é mais rígida no equilíbrio:

   - AVL:         altura no máximo ~ 1,44 · log2(n)
   - Rubro-Negra: altura no máximo ~ 2 · log2(n)

   Na AVL, a diferença de altura entre os dois lados de qualquer nó é
   de no máximo 1. Na Rubro-Negra, só se garante que o caminho mais
   longo não passa do dobro do mais curto, então a árvore pode ficar
   mais "torta".

## 3) O que os números mostram?
  
   Inserindo 10, 20, 30, ..., 150 (ordem crescente, 15 chaves):

                                  AVL     Rubro-Negra
   Altura final                    4           6
   Pior caso de busca (compar.)    4           6
   Média de comparações por busca  3,27        3,67

   A AVL chegou a altura 4, que é o mínimo possível para 15 nós
   (árvore perfeita). Isso dá ~33% menos comparações no pior caso.

## 4) E o custo de montar a árvore?
   
   A AVL fez 11 rotações e a Rubro-Negra fez 9. A diferença é pequena e
   acontece uma única vez, na montagem. Já a diferença de altura vale
   para TODA consulta do expediente.

## 5) Por que a ordem crescente é um problema?
   
   Numa árvore de busca comum (sem balanceamento), as chaves em ordem
   crescente formariam uma "escada": uma lista de altura 15, com busca
   lenta. As rotações da AVL transformam essa escada numa árvore
   perfeita, que é o melhor resultado possível.



# Questão 2 - Justificativa 

Escolha: Rubro-Negra
------------------------------------------------------------------------

## 1) O que domina a carga?
   
   A INSERÇÃO. O app registra um evento a cada poucos milissegundos, o dia
   inteiro. Já a busca é rara: o relatório roda uma vez por dia, de
   madrugada.

  Assim a altura da árvore importa pouco. O que pesa é o custo de manter o equilíbrio a cada inserção.

## 2) Quanto custa manter o equilíbrio em cada árvore?

   - Rubro-Negra:
       Faz no máximo 2 rotações por inserção. As recolorações só sobem
       pela árvore de vez em quando, então o custo médio de arrumar a
       árvore é constante.

   - AVL:
       Depois de inserir, precisa voltar por todos os ancestrais do nó
       novo para recalcular altura e fator de balanço, mesmo quando não
       há rotação nenhuma.

## 3) O que os números mostram?

   a) Amostra do enunciado (5, 10, 15, ..., 50):

                          AVL     Rubro-Negra
      Rotações              6          5
      Ajustes              25         25
      Altura final          4          5

      Com apenas 10 chaves a diferença ainda é pequena, e a AVL fica
      um nível mais baixa.

   b) Teste em escala (20 mil timestamps crescentes, impresso ao rodar
      o script):

                                      AVL     Rubro-Negra
      Ajustes por inserção            13          5
      Altura final                    15         26
      Tempo para montar               1x        ~1/4 do tempo

      A Rubro-Negra faz bem menos trabalho de manutenção por inserção.
      Em troca fica mais alta (26 níveis contra 15), mas isso só
      atrapalha buscas, que aqui quase não acontecem.

## 4) Uma observação importante.
   
   Nas duas árvores, cada inserção faz no máximo uma reestruturação
   "de verdade": a AVL faz 1 rotação (simples ou dupla) e a Rubro-Negra
   faz até 2. Ou seja, a vantagem da Rubro-Negra NÃO está no número de
   rotações, e sim no custo de percorrer e ajustar o caminho até a raiz.

## 5) Por que a altura maior não atrapalha?
   
   Porque a altura só influencia a busca, e a busca acontece uma vez por
   dia.


# Questão 3 - Justificativa 

Escolha: AVL
------------------------------------------------------------------------

## 1) O que domina a carga?

   A BUSCA. A tabela é montada uma vez, na análise do código, e depois é
   consultada o tempo todo, cada uso de uma variável nas fases de
   verificação de tipos e geração de código é uma busca.

   Nesse cenario quando a leitura domina, vale pagar um equilíbrio mais
   rigoroso na montagem para ter uma árvore mais baixa em toda consulta.

## 2) Qual árvore tem a melhor garantia de altura?

   A AVL:

   - AVL:         altura no máximo ~ 1,44 · log2(n)
   - Rubro-Negra: altura no máximo ~ 2 · log2(n)


## 3) O que os números mostram?

   a) Amostra do enunciado (50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65):

                                  AVL     Rubro-Negra
      Altura final                  4          4
      Rotações                      0          0
      Média de comparações        3,08       3,08
      Ajustes                      25          9

      Nesta amostra pequena há empate técnico. A ordem já é "bem
      comportada" e nenhuma árvore precisa girar. A Rubro-Negra até gasta
      menos ajustes (9 recolorações contra 25 nós revisitados na AVL).

   b) Teste em escala (20 mil chaves aleatórias, impresso ao rodar o
      script):

                                  AVL     Rubro-Negra
      Altura final                 17         18
      Média de comparações       13,58      13,61

      A AVL nunca fica pior na consulta, mas com chaves aleatórias a
      margem é pequena. Em troca, a Rubro-Negra monta a árvore mais
      rápido, o que aqui não ajuda: a montagem acontece uma única vez.

## 4) Por que o custo extra da AVL não pesa?

   Porque a construção é feita uma só vez e as buscas se repetem
   continuamente. O trabalho extra de reequilibrar é diluído em milhares
   de consultas, enquanto a altura menor beneficia todas elas.

## 5) Então por que escolher a AVL se as chaves são aleatórias?

   Porque, com chaves aleatórias, as duas árvores ficam próximas em
   média. O que desempata é o objetivo: minimizar o pior caso de BUSCA,
   e é nesse ponto que a AVL oferece a garantia mais forte.


# Questão 4 - Justificativa 

Escolha: Rubro-Negra
------------------------------------------------------------------------

## 1) O que domina a carga?

   A ESCRITA. Usuários entram e saem o tempo todo, então o índice muda
   sem parar. As buscas são secundárias.

   O que mais pesa é o custo de cada inserção. 

## 2) Quanto custa manter o equilíbrio em cada árvore?

   - Rubro-Negra:
       Reequilibra de forma mais "frouxa". Usa recolorações (baratas) e
       no máximo 2 rotações por inserção. As recolorações que sobem pela
       árvore são raras, então o custo médio é constante, O(1).

   - AVL:
       É mais rígida. A cada inserção, volta por todo o caminho até a
       raiz recalculando altura e balanço. Com chaves aleatórias, também
       faz mais rotações.

## 3) O que os números mostram?

   a) Amostra do enunciado (42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70):

                                  AVL     Rubro-Negra
      Altura final                  4          4
      Rotações                      0          0
      Média de comparações        3,08       3,08
      Ajustes                      25          9

      Mesmo numa sequência que não exige nenhuma rotação, a Rubro-Negra
      faz cerca de um terço do trabalho de manutenção.

   b) Teste em escala (20 mil IDs aleatórios, impresso ao rodar o script):

                                  AVL     Rubro-Negra
      Ajustes por inserção         13         2,3
      Altura final                 17         18
      Tempo para montar            1x       ~1/3 do tempo

      A Rubro-Negra monta a árvore bem mais rápido e a altura fica
      praticamente igual.

## 4) O que se perde com a Rubro-Negra?

   Ela pode ficar um ou dois níveis mais alta que a AVL, mas isso só
   encarece as buscas, que aqui são raras. O custo de manutenção, por
   outro lado, é pago a cada entrada e saída de usuário. Por isso a
   Rubro-Negra compensa.


# Questão 5 - Justificativa 

Escolha: AVL
------------------------------------------------------------------------

## 1) Qual é o problema de a entrada já vir ordenada?

   Numa árvore de busca comum, as chaves 1, 2, 3, ..., 7 formariam uma
   "escada": uma lista de altura 7, com busca lenta, O(n). As duas
   árvores resolvem isso com rotações, então a escolha entre elas
   depende do que vem depois.

## 2) O que domina a carga depois da importação?

   A BUSCA. A importação acontece uma única vez e depois a árvore é só
   consultada o dia todo.

   O custo de reequilibrar é irrelevante diante do volume de
   consultas. O que importa é a menor altura possível.

## 3) O que os números mostram?

   a) Amostra do enunciado (1, 2, 3, 4, 5, 6, 7):

                                  AVL     Rubro-Negra
      Altura final                  3          4
      Rotações                      4          3
      Média de comparações        2,43       2,71

      A Rubro-Negra economiza 1 rotação na carga, mas deixa a árvore um
      nível mais alta para sempre. A AVL gasta 1 rotação a mais, uma
      única vez, e ganha 1 comparação a menos no pior caso de toda
      consulta.

   b) Teste em escala (20 mil chaves crescentes, impresso ao rodar o
      script):

                                  AVL     Rubro-Negra
      Altura final                 15         26
      Média de comparações       13,36      13,88

      Com chaves em ordem crescente, a AVL produz árvores praticamente
      perfeitas (altura próxima de log2(n)). A Rubro-Negra chega perto de
      2 · log2(n).

## 4) Então por que a AVL?

   Porque a diferença de altura se paga em cada consulta, e a diferença
   de rotações acontece uma só vez, na importação.


# Questão 6 - Justificativa 

Escolha: Rubro-Negra
------------------------------------------------------------------------

## 1) O que domina a carga?

   A ESCRITA, de forma extrema: dezenas de milhares de inserções por
   segundo, no caminho crítico do escalonador. Cada microssegundo gasto
   reorganizando a árvore é tempo roubado da CPU.

   Buscar um elemento específico quase nunca acontece. Isso elimina a
   principal vantagem da AVL, que é ter a árvore mais baixa.


## 2) Quanto custa manter o equilíbrio em cada árvore?

   - Rubro-Negra:
       No máximo 2 rotações por inserção, e recolorações com custo
       médio constante, O(1). Não precisa recalcular alturas.

   - AVL:
       A cada inserção, recalcula altura e balanço em todo o caminho até
       a raiz, o que custa cerca de O(log n) sempre.

## 3) O que os números mostram?

   a) Amostra do enunciado (40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45):

                                  AVL     Rubro-Negra
      Altura final                  4          4
      Rotações                      0          0
      Ajustes                      25          9

      A sequência não exige nenhuma rotação, mas a AVL ainda faz quase 3
      vezes mais trabalho de manutenção.

   b) Teste em escala (20 mil chaves aleatórias, impresso ao rodar o
      script):

                                  AVL     Rubro-Negra
      Ajustes por inserção         13         2,3
      Tempo para montar            1x       ~1/3 do tempo
