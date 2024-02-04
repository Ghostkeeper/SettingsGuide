Offset máximo de extrusão.para compensação da dívida
====
A compensação de débito é uma experiência semelhante à funcionalidade [avanço linear](http://marlinfw.org/docs/features/lin_advance.html) de Marlin.O objetivo da compensação da taxa é compensar a subestusão e a superextrusão quando o fluxo do material que sai do bico muda.Esse ajuste limita a distância à qual o material será retraído ou empurrado em direção à frente, a fim de compensar as mudanças de fluxo.

A compensação para o fluxo moverá o filamento ainda mais na frente de sua posição inicial ou mais atrás durante a impressão.Esse ajuste limita a distância à qual o filamento pode se mover em relação à sua posição inicial.

A compensação introduzirá movimentos adicionais do filamento durante toda a impressão.Esses movimentos significam que a cabeça da impressão diminui de tempos em tempos para mover o filamento.Para reduzir esse efeito, você pode limitar a distância que o filamento pode navegar.Isso impede que a cabeça de impressão precise desacelerar para que o carregador possa seguir.No entanto, isso torna a compensação pelo fluxo menos eficaz.