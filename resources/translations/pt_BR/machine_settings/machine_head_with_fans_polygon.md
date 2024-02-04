Máquina Cabeça e Polígono de Fan
====
Essa configuração diz a Cura qual é a forma da sua cabeça de impressão, vista de cima.Esta função é necessária para evitar colisões durante a impressão no modo [uma de cada vez](../Blackmagic/print_sequence.md).

![Dimensões da cabeça de impressão](../images/head_dimensions.svg)

Este parâmetro contém uma lista de coordenadas que formam um polígono.Os detalhes de contato estão relacionados à "posição" da cabeça, em relação à qual os bicos também estão posicionados em um relativamente.

O Cura o usa para criar uma área de colisão ao redor dos objetos que você imprimir no modo "um de cada vez".Essa área de colisão impede que você coloque objetos muito próximos um do outro, para que eles não possam ser impressos sem a cabeça de impressão atingindo o modelo impresso anteriormente.A área de colisão, no entanto, não tem a mesma forma que a própria cabeça de impressão: será uma concha convexa ao redor da cabeça de impressão para evitar colisões durante a viagem.Também será reduzido para ser simétrico.Por exemplo, se o bico estiver mais à esquerda da cabeça de impressão (como na imagem acima), a área de colisão será reduzida para que outro objeto possa ser colocado perto do lado direito, objetos impressos anteriormente.A ordem em que esses objetos são impressos serão ajustados para que possam ser impressos sem colisão.

*Como é um ajuste da máquina, normalmente não aparecerá na lista de configurações normais.No entanto, o tamanho da cabeça de impressão pode ser observado aproximadamente na caixa de diálogo Configurações da impressora, que está na lista de impressoras adicionadas na caixa de diálogo Preferência.Você pode especificar apenas a posição dos lados esquerdo, direito, superior e inferior da cabeça de impressão.*