Velocidade mínima
====
O microprograma de Marlin para impressoras 3D, a maioria das quais derivadas, tem uma velocidade mínima para todos os seus movimentos.Este parâmetro indica qual é essa velocidade mínima para o microprograma da sua impressora.

A velocidade mínima é um ajuste destinado a evitar erros no microprograma devido a divisões por zero.O microprograma deve calcular os intervalos de tempo entre as etapas para enviar um sinal aos motores com o tempo certo.Se o motor tiver que se mover a uma velocidade de 0 (ou seja, pare), é um intervalo de tempo infinito, que o microprograma não poderá gerenciar bem.Isso só se aplica se nenhum dos motores da impressora realmente executar.Por exemplo, movendo -se na direção x, o motor que controla o eixo ainda não gira, mas devido à complexidade das etapas passo a passo, a velocidade mínima de avanço não se aplica aqui.

O Cura usa essa velocidade mínima de avanço para produzir estimativas de tempo corretas.É aplicado durante a aceleração no início da impressão ou após um intervalo, e ao desaceleração até parar no final de uma impressão ou antes de um intervalo.

*Como é um ajuste da máquina, esse parâmetro normalmente não é visível na lista de parâmetros.*