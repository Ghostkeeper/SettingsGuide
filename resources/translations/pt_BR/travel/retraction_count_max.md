Número de retração máxima
====
A roda elétrica deve pegar o filamento para movê -lo corretamente.A retração do material geralmente tende a usar o filamento a ponto de a roda de alimentação não poder mais segurá -lo corretamente.Esse ajuste limita o número de retrações a um certo comprimento de filamento para evitar essa moagem.

O ajuste indica quantas vezes o filamento pode ser retraído durante o comprimento do filamento indicado pelo ajuste [intervalo de distância mínima de extrusão](retração_extrusion_window.md).Qualquer outra retração durante esta janela não será feita, mas simplesmente se moverá sem se retrair.

![Visualização de retrações para um certo comprimento de filamento](../images/retraction_count_max.svg)

O comprimento do filamento durante o qual o número de retrações é limitado é uma janela deslizante.Por exemplo, com um comprimento de janela de 3 mm e um número máximo de retrações de 10, isso significa que uma nova retração é autorizada assim que a 10ª retração anterior foi feita mais de 3 mm de volta ao filamento.

Reduzir o número máximo de retrações reduzirá a moagem do filamento.Isso é útil para mais materiais macios, como o PVA.No entanto, isso também aumentará a rotação, porque não se retrairá mais em uma posição em que aparentemente era desejado.