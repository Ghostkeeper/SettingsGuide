Aceleração máxima do filamento
====
Este parâmetro indica a aceleração máxima de que os motores da extrusora do suporte à sua impressora, de acordo com o microprograma da impressora.

Este parâmetro é usado apenas para obter estimativas de tempo corretas.[Aceleração](../Speed/aceleração_print.md) definido por Cura não tem limite, mas o Cura assume que seu microprograma fixa um certo limite por eixo.Se a aceleração da extrusora exceder esse parâmetro, a estimativa do tempo desses movimentos será ajustada para supor que o seu microprograma limite a aceleração.A aceleração total ainda pode ser maior ao acelerar a diagonal com vários eixos ao mesmo tempo.

É bastante comum que os limites de aceleração da extrusora sejam alcançados, pois (dependendo do microprograma) a aceleração definida pela cura também afeta a extrusora.Portanto, é crucial que esse parâmetro esteja configurado corretamente para obter estimativas de tempo corretas para as retrações.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de configurações.*