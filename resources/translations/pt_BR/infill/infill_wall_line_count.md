Número de paredes de enchimento adicionais
====
Essa configuração adiciona um certo número de contornos nas áreas de enchimento.Isso equivale a aumentar o [número de linhas da parede](../shell/wall_line_count.md), mas os contornos não contornam a pele e as paredes também estarão entre a pele e o recheio.Também é semelhante à adição de [paredes externas adicionais](../top_bottom/skin_outline_count.md), mas em torno do enchimento em vez de ao redor da pele.

Essas paredes são impressas com os parâmetros de enchimento.

![Duas paredes adicionais ao redor do enchimento](../../../articles/images/infill_wall_line_count.png)

Comparado à adição de paredes adicionais externas, esse ajuste aumenta consideravelmente a resistência do modelo e reduz a visibilidade do recheio através da pele, mas também aumenta o tempo de impressão e o uso do material.Embora as paredes externas adicionais substituam o material que teria sido impresso como pele de qualquer maneira, esse ajuste realmente adiciona material, a menos que a densidade de enchimento já seja 100 %.

É muito semelhante à adição de paredes externas adicionais.No entanto, é aconselhável adicionar pelo menos uma parede adicional ao redor do enchimento ou ao ar livre, pois isso impede que as linhas de pele terminem no vazio.