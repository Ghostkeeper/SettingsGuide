Largura mínima de linhas de parede impuras
====
Ao imprimir peças finas, o Cura ajusta a largura das paredes das paredes para se adaptar à largura exata do modelo.Cura também pode decidir usar menos linhas para as paredes.Este parâmetro é o limite do qual o Cura remove uma linha no centro.Ele pode ser ajustado separadamente do [limiar ao qual as duas linhas centrais combinam](min_even_wall_line_width.md).

![Quando a linha central é muito pequena, as duas linhas ao redor são ampliadas.](../../../articles/images/min_wall_line_width_0_34.png)

![Ao reduzir essa configuração, a linha central começa e termina muito menor](../../../articles/images/min_wall_line_width_odd_0_1.png)

Número de pares ou linhas ímpares
----
Este parâmetro possibilita ajustar o limite para excluir linhas especificamente quando há um número ímpar de linhas.Ou seja, quando há apenas uma linha no centro em vez de duas.Ele determina o momento em que essa linha única é removida em favor das duas linhas que a cercam, um pouco mais larga.

A largura mínima de uma linha de parede impura pode ser diferente da largura mínima de uma linha de pares devido à maneira como elas se transformam.Quando uma linha ímpar é removida, ela para antes da transição e permite que as paredes circundantes se aproximem.Durante a transição, há um pequeno espaço onde as linhas circundantes ainda não se aproximaram.Isso é diferente do que está acontecendo quando há um número de cordões de pares: as duas linhas no meio estão mais próximas, sobrepondo -se ligeiramente.Reduza a largura mínima das linhas das paredes ímpares reduz o tamanho da diferença para transições entre os pares e as linhas ímpares.A redução da largura mínima das linhas das paredes de pares reduz a superextrusão para as transições entre os pares e as linhas ímpares.

Os vazios deixados no final de uma linha impura são mais visíveis no resultado final do que uma ligeira ultrapassagem em uma articulação.Portanto, poderia ser útil corrigir a largura mínima das linhas de parede ímpares ligeiramente inferiores à largura mínima das linhas de parede dos pares.

A redução deste parâmetro leva a:
* Espaços menores quando uma linha central termina.
* Largura máxima reduzida de um par de linhas centrais de potência.
* Mais linhas finas, que podem não estar bem extintas.
* Linhas mais longas, que demoram mais para imprimir.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **