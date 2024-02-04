Compensação pelo estreitamento do fator de escala horizontal
====
Este parâmetro coloca automaticamente o modelo em uma escala antes de cortar, na direção horizontal.O objetivo é compensar qualquer estreitamento que ocorra quando a impressão esfria à temperatura ambiente.Ao tornar a impressão um pouco maior do que desejável, o resultado final pode ser mais fiel às dimensões originais do modelo de entrada.Esse fator de escala é aplicado apenas às direções x e y.

A retirada nas direções horizontais é mais importante porque é nessa direção que as restrições internas da impressão são as mais importantes.Em geral, o estreitamento horizontal é maior que o estreitamento vertical.As linhas sendo impressas horizontalmente, elas se contraem mais no sentido horizontal do que no sentido vertical.

Toda a cena é montada em seu centro.Quando você imprime vários modelos, eles estão todos esclarecendo o mesmo ponto do ponto original.Isso permite que você posicione esses modelos muito próximos um do outro, sem que eles se sobreponham na impressão final.As áreas de colisão modelo são escadas, para que você possa ver exatamente onde sua impressão terminará.Isso também impedirá que você coloque modelos na cena em lugares onde eles colidiriam com elementos de impressão ou impressora, como a Torre Particular ou os clipes da bandeja de impressão.

Um fator de 100 % não causa escala.Um fator ligeiramente maior que 100 % é mais adequado para muitos materiais técnicos, como ABS ou polipropileno.Um fator de escala inferior a 100 % indicaria que o material está se expandindo durante o resfriamento, como uma espuma, talvez.

Dados puramente químicos sobre o estreitamento de um material entre a temperatura de impressão e a temperatura ambiente não são suficientes para prever um bom valor para esse parâmetro, porque o processo de impressão também influencia o estreitamento.Quando extrudado on -line, o plástico é esticado na direção do comprimento da linha e retrai mais neste eixo.