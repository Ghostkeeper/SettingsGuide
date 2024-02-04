Limite regular/máximo de velocidade do ventilador
====
Este parâmetro determina o tempo de impressão da camada para a qual é tão curto que a velocidade do ventilador começa a aumentar para atingir a [velocidade máxima do ventilador](cool_fan_speed_max.md).As camadas que levam mais tempo para imprimir usarão [velocidade normal do ventilador](cool_fan_speed_min.md).Para camadas cujo tempo de impressão é mais curto, a velocidade do ventilador será interpolada entre os parâmetros de velocidade normal e a velocidade máxima, até a [duração mínima da camada](cool_min_layer_time.md), onde a velocidade do ventilador estará em velocidade máxima do ventilador.

![Que velocidade do ventilador é usada](../images/cool_fan_speed.svg)

De fato, reduzindo esse limiar (em direção a camadas mais curtas), o ventilador será executado com mais frequência em velocidade normal.Ao aumentar esse limite, o ventilador será executado com mais frequência a uma velocidade mais alta, mesmo que as fraldas não sejam muito pequenas.

É bom manter uma certa distância entre o tempo mínimo da camada e esse limiar de velocidade regular/máxima do ventilador.Se o limiar for ajustado no tempo mínimo da camada, o ventilador parará repentinamente se as camadas ficarem ligeiramente abaixo do limite.Isso leva à formação de faixas visíveis na superfície da impressão, porque há uma borda dura onde o ventilador começou de repente.Se, pelo contrário, houver uma diferença entre as duas configurações, a alteração da velocidade do ventilador será mais progressiva e as bandas não serão visíveis na impressão.