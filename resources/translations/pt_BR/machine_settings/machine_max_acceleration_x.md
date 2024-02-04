Aceleração máxima x
====
Este parâmetro indica a aceleração máxima que o motor e o chassi da sua impressora podem suportar na direção x, dependendo do microprograma da impressora.

Este parâmetro é usado apenas para obter estimativas de tempo corretas.O valor de [aceleração](../speed/aceleração_print.md) fixado por cura não tem limite, mas o Cura assume que o microprograma corrige um certo limite por eixo.Se a aceleração no eixo x exceder esse parâmetro, a estimativa do tempo desses movimentos será ajustada para assumir que o seu microprograma limita a aceleração.A aceleração total ainda pode ser maior ao acelerar a diagonal com vários eixos ao mesmo tempo.

*Como é uma configuração da máquina, esse ajuste normalmente não é visível na lista de parâmetros.*