Velocidade de impressão com fio ascendente
====
Esse ajuste especifica a velocidade na qual o bico aumentará ao realizar um movimento vertical na configuração de travamento.A velocidade do movimento para cima pode ser configurada separadamente do restante da velocidade de impressão do fio.

![Onde as diferentes velocidades de impressão de roscas se aplicam](../images/wireframe_printspeed.svg)

O movimento ascendente não terá a velocidade especificada para todo o movimento.Para o bit mais baixo do movimento ascendente, conforme definido pelo parâmetro [diferença ascendente na impressão com fio](Wireframe_up_half_speed.md), a cabeça de impressão se moverá para a metade dessa velocidade.

Um movimento mais lento levará mais tempo, mas dará mais tempo ao material para solidificar.Dessa forma, não será arrastado tanto na direção da diagonal.No entanto, um deslocamento muito lento também empurrará a linha para baixo devido à inércia do filamento com a pressão na sala de bicos.O filamento então tende a oscilar, o que torna menos provável que a próxima linha horizontal possa estabelecer uma conexão correta.