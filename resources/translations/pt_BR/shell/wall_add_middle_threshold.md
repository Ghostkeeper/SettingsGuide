Adicione um limite da linha média
====
Ao imprimir peças finas, o Cura ajusta a largura das linhas de parede para se adaptar à largura exata do modelo.Cura também pode decidir usar menos linhas de parede.Este parâmetro é o limite do qual a cura adicionará uma linha ao centro.Ele pode ser resolvido separadamente do [limiar ao qual as duas linhas do ambiente se combinam](Wall_split_middle_threshold.md).

Este parâmetro é idêntico ao parâmetro da [largura mínima da linha de parede impura](min_odd_wall_line_width.md), mas usa uma unidade diferente.A unidade deste parâmetro é expressa nas frações de largura de linha de que a largura de uma peça deve aumentar para adicionar uma nova linha central.

![Quando a linha central é muito pequena, as duas linhas ao redor são ampliadas.](../../../articles/images/min_wall_line_width_0_34.png)

![Ao reduzir essa configuração, a linha central começa e termina muito menor](../../../articles/images/min_wall_line_width_odd_0_1.png)

Número de pares ou linhas ímpares
----
Esse parâmetro possibilita ajustar o limite para adicionar linhas especificamente quando se torna um número ímpar de linhas.Ou seja, quando há apenas uma linha no centro em vez de duas.Determina quando uma nova linha é adicionada entre as duas linhas centrais.

O limite para adicionar uma linha central pode ser diferente do limite para a divisão da linha central em dois, devido ao seu modo de transição.Quando uma linha ímpar é adicionada, ela começa apenas quando as duas linhas circundantes o tornaram espaço.Durante a transição, há um pequeno espaço onde as linhas circundantes ainda não fizeram espaço suficiente.Isso é diferente do que está acontecendo quando há um número de cabos de pares: a linha média se separa ao meio, e essas duas linhas se sobrepõem levemente até que estejam suficientemente distantes.Reduza o limiar de adição da linha média reduz o tamanho da diferença para transições entre pares e linhas ímpares.Reduza o limiar de separação da linha média reduz a superextrusão às transições entre pares e linhas ímpares.

Os vazios deixados no início de uma linha impura são mais visíveis no resultado final do que um pouco de superextrusão no nível de uma junta.Portanto, poderia ser útil definir o limiar de adição de linha média ligeiramente menor que o limiar de separação do meio -campista.

A redução deste parâmetro leva a:
* Espaços menores quando uma linha central termina.
* Largura máxima reduzida de um par de linhas centrais de potência.
* Mais linhas finas, que podem não estar bem extintas.
* Linhas mais longas, que demoram mais para imprimir.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **