Altura do pórtico
====
Esse ajuste mede a distância entre a bandeja de impressão e o sistema de portão ao qual a cabeça de impressão está suspensa.Essa altura é um limite quando você imprime [um objeto ao mesmo tempo](../Blackmagic/print_sequence.md), porque os objetos impressos anteriormente podem colidir com o pórtico.

![Dimensões da cabeça de impressão](../images/head_dimensions.svg)

A maioria das impressoras 3D tem sua cabeça de impressão suspensa de uma ou duas barras transversais.A forma deste pórtico não é modelada por Cura: se são duas barras transversais, um braço proveniente de uma direção ou uma única barra transversal ao longo da qual a cabeça de impressão pode se mover em uma direção.O Cura considera este pórtico como um limite de matéria quando imprime [um objeto ao mesmo tempo](../Blackmagic/print_sequence.md), qualquer que seja a ordem em que os modelos forem impressos.Ao imprimir [um objeto ao mesmo tempo](../Blackmagic/print_sequence.md), a altura do volume de construção é limitada a essa altura de pórtico, para indicar que nenhum modelo acima da altura do pórtico não está autorizado.

Uma exceção é feita quando apenas um objeto é carregado no conjunto de impressão.Esse objeto está autorizado a ser maior que a altura do pórtico, porque não haverá mais nada no conjunto de impressão que possa colidir com o pórtico.

*Como é uma configuração da máquina, normalmente não aparecerá na lista normal de configurações.A altura do pórtico pode ser modificada na caixa de diálogo Configurações da impressora, que está na lista de impressoras adicionadas na caixa de diálogo Preferência.*