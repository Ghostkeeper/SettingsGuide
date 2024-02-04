Otimize a ordem de impressão das paredes
====
Se essa função for ativada, o Cura dedicará um tempo de corte adicional para otimizar a ordem em que as paredes são impressas.O objetivo é reduzir o número de viagens e saques imprimindo as paredes ao redor da mesma sala uma após a outra.

![Otimização desativada](../../../articles/images/optimize_wall_printing_order_disabled.gif)

![Otimização ativada](../../../articles/images/optimize_wall_printing_order_enabled.gif)

Se essa otimização for ativada, o bico primeiro imprimirá todas as paredes em torno de uma sala antes de mudar para a próxima sala, em vez de imprimir todas as paredes interiores primeiro antes de imprimir as paredes externas.A otimização é geralmente positiva, mas para certas partes, pode ter um impacto na precisão dimensional, porque a parede anterior ainda não solidificou durante a colocação do próximo próximo a ele.