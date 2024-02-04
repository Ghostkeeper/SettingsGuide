Retração de firmware
====
Normalmente, o Cura causa uma retração controlando o movimento do carregador, ordenando que ele mova o filamento um pouco para trás.Se esse parâmetro for ativado, ele escreverá um comando "G10" para significar que a impressora deve retirar o filamento ou um comando "G11" para removê -lo.

Ao optar por usar as retrações de microprograma, a microprograma da impressora controla a distância e a velocidade de retração do filamento.A impressora pode saber mais sobre sua própria geometria do que o Cura e, portanto, pode decidir melhor como retrair o filamento.No entanto, isso significa que o Cura não controla mais essas retrações e que Cura sabe mais sobre a própria impressão.Essencialmente, o slicer e o microprograma têm informações diferentes, e esse ajuste decide qual dos dois pode ser escolhido.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de configurações.*