Largura mínima de linhas de parede de pares
====
Ao imprimir peças finas, o Cura ajusta a largura das linhas de parede para se adaptar à largura exata do modelo.Cura também pode decidir usar menos linhas.Este parâmetro é o limite do qual a cura combinará duas linhas em uma.Ele pode ser definido separadamente do [limite no qual a linha central é excluída](min_odd_wall_line_width.md).

![A linha central é estendida para se adaptar](../../../articles/images/min_wall_line_width_0_34.png)

![Ao reduzir este parâmetro, ele usa duas linhas](../../../articles/images/min_wall_line_width_even_0_1.png)

Número de pares ou linhas ímpares
----
Este parâmetro possibilita ajustar o limiar de exclusão de linhas especificamente quando houver um número de linhas de pares.É o caso quando há duas linhas no centro, em vez de uma linha.Ele determina o momento em que essas duas linhas no centro se combinam em uma única linha.

A largura mínima de uma linha de parede de par pode ser diferente da [largura mínima da linha de parede impura](min_odd_wall_line_width.md) por causa da maneira como eles se encontram.As linhas de pares se encontram nas pontas, aproximando as pontas.Há alguma sobreposição nessas linhas neste local, o que leva a uma superextrusão.Isso é diferente da situação em que há um número ímpar de cordões: a linha do meio e simplesmente para, deixando um vazio na impressão.Reduza a largura mínima das linhas das paredes dos pares reduz a superextrusão para transições entre pares e linhas ímpares.Ao reduzir a largura mínima das linhas das paredes ímpares, o tamanho do vácuo é reduzido para as transições entre os pares e as linhas ímpares.

Os vazios deixados no final de uma linha impura são mais visíveis no resultado final do que uma ligeira ultrapassagem em uma articulação.Portanto, poderia ser útil corrigir a largura mínima das linhas de parede de pares um pouco mais altas que a largura mínima das linhas de parede ímpares.

A redução deste parâmetro leva a:
* Redução da área de sobreposição onde duas linhas se reúnem para se misturar em uma única linha.
* Redução da largura máxima de linhas centrais únicas.
* Linhas menores, que podem não ser bem extrudadas.
* Mais linhas, que demoram mais para imprimir.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **