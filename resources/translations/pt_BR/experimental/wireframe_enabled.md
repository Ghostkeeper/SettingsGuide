Impressão de arame
====
Este parâmetro permite um modo de impressão completamente diferente chamado impressão de fios.Quando a impressão de arame é usada, a impressora não faz um objeto sólido, mas apenas uma treliça triangular da forma externa de fios finos.

Esta técnica tem várias vantagens:
* Permite imprimir muito mais rápido que um objeto sólido.
* Ele usa apenas uma fração do material usado pela impressão normal.
* Tem uma aparência especial, como se fosse construída manualmente com uma caneta de impressão 3D.

O objeto resultante, no entanto, não é funcional.Ele terá aproximadamente o tamanho certo, o que o torna útil para prototipar a sensação da escala de impressão, embora o tamanho também não seja muito preciso.O objeto obtido é extremamente frágil, não apenas durante a impressão, mas também depois.É difícil removê -lo da bandeja de impressão sem danificá -la.O modelo também perderá a maioria de seus detalhes.

Imprimir sobre o fio é colocar anéis de material com um espaçamento vertical bastante grande de vários milímetros.Entre esses anéis, ele desenha uma forma de dente de serra que permite que o seguinte anel repouse no anterior.Quando a superfície do modelo é horizontal, uma técnica semelhante é usada para fechar o cume.No telhado, existem anéis concêntricos mantidos juntos por uma forma de dente de serra, cuidadosamente suspensos no ar por um edifício externo (onde pode descansar em uma parede) para dentro.

A impressão sobre o fio realmente não funciona de maneira confiável com formas quase totalmente verticais, como o tipo de modelo que funcionaria bem com o modo [espiraliza o contorno externo](../BlackMagic/Magic_Spiralize.md).Se a superfície for horizontal em grandes superfícies, a técnica de fechamento do telhado deve cobrir uma distância extremamente grande.Nesse caso, é muito provável que a técnica falhe.Se o modelo continuar a subir no meio de uma superfície horizontal, ele quase certamente será impresso ao ar livre.

** A vista da camada de cura não exibirá corretamente a impressão sobre o fio diretamente após o corte.No entanto, o resultado sempre pode ser visualizado gravando o código G no disco e abrindo este código G novamente com cura. **