A posição inicial absoluta da extrusora
====
Se a opção [ativar a queda de preparação](../plataform_adhiction/prime_blob_enable.md) for usada, a posição desse procedimento de priming poderá ser ajustada com uma posição [x](../platafort_adhiction/extruder_prime_x_x.mdd) e [y ](../plataform_adhiction/extruder_prime_pos_y.md).Este parâmetro determina se é a posição na bandeja de impressão ou uma posição relacionada à posição atual da impressora.

Se esse parâmetro for ativado, as coordenadas X e Y se relacionam com uma certa posição fixa na bandeja de impressão.A extrusora sempre se moverá para lá para criar uma gota de plástico de preparação.

Se esse parâmetro estiver desativado, as coordenadas X e Y se relacionam com a posição que o bico ocupa durante a primeira visita a esta extrusora.Para a primeira extrusora, esta é a coordenada [0,0].Para outras extrusoras, é a posição inicial deles, conforme definido no arquivo de definição da extrusora.Essa posição inicial também pode ser relativa.

É fortemente aconselhado usar uma primeira posição absoluta.Uma posição inicial absoluta é garantida sem colisão com outras partes da impressão, pois você não pode colocar objetos neste local na bandeja de impressão.Uma primeira posição relativa pode estar em qualquer lugar da bandeja de impressão e, portanto, você pode acabar com uma camada de preparação em algum lugar acima da sua primeira camada.O uso de uma primeira posição relativa pode economizar tempo de viagem, mas realmente não se preocupa em correr esse risco.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de configurações.*