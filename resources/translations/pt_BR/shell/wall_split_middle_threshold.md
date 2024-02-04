Limiar da linha média fracionária
====
Ao imprimir peças finas, o Cura ajusta a largura das linhas de parede para se adaptar à largura exata do modelo.Cura também pode decidir usar menos linhas de parede.Este parâmetro é o limite do qual o Cura dividiu uma linha central única ao meio, quando a largura da peça aumenta.Ele pode ser definido separadamente do [limite ao qual uma nova linha central é adicionada](Wall_Add_middle_threshold.md).

Este parâmetro é idêntico ao parâmetro [largura mínima da linha de parede do par](min_even_wall_line_width.md), mas usa uma unidade diferente.A unidade deste parâmetro é expressa nas frações de largura da linha de que a largura de uma peça deve aumentar para dividir a linha central em dois.Como a diferença de largura é distribuída sobre as duas linhas do meio após a divisão, uma largura mínima da linha de pares menores é equivalente a uma linha de meio dividido muito menor do que no caso da remoção de um cordão ímpar.

![A linha central é estendida para se adaptar](../../../articles/images/min_wall_line_width_0_34.png)

![Ao reduzir este parâmetro, ele usa duas linhas](../../../articles/images/min_wall_line_width_even_0_1.png)

Número de pares ou linhas ímpares
----
Esse parâmetro possibilita ajustar o limite para adicionar linhas especificamente quando se torna um número de linhas de pares.É o caso quando há duas linhas no centro, em vez de uma linha.Ele determina o momento em que uma linha no centro é dividida em duas linhas.

O limiar de separação de uma linha média pode ser diferente do limiar de adição de uma linha central por causa de como eles se encontram.As linhas de pares se reúnem nas pontas, fazendo as pontas se aproximarem.Há alguma sobreposição nessas linhas neste local, o que leva a uma superextrusão.Isso é diferente da situação em que há um número ímpar de cordões: a linha do meio e simplesmente para, deixando um vazio na impressão.A redução no limiar de separação da linha central reduz a superextrusão para as transições entre os pares e as linhas ímpares.A redução no limiar de adição de linha mediana reduz o tamanho da diferença para transições entre os pares e as linhas ímpares.

As lacunas restantes ao adicionar uma linha média são mais visíveis no resultado final do que um pouco de superextrusão no nível de uma articulação, portanto, poderia ser útil definir o limiar da linha média dividida um pouco mais alta do que o limiar da linha mediana adicionada .

A redução deste parâmetro leva a:
* Redução da área de sobreposição onde duas linhas se reúnem para se misturar em uma única linha.
* Redução da largura máxima de linhas centrais únicas.
* Linhas menores, que podem não ser bem extrudadas.
* Mais linhas, que demoram mais para imprimir.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **