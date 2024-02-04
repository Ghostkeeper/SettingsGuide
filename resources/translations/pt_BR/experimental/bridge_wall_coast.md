Roda livre para parede da ponte
====
Ao imprimir uma ponte com linhas de parede, pouco antes de uma ponte ser impressa, o suprimento de material é interrompido por um tempo.Enquanto isso, o material restante dentro da sala dos bicos é deixado, para reduzir a pressão dentro da sala do bico.Esta técnica é chamada [Freewheel](Coasting_enable.md).Essa configuração permite controlar a quantidade de roda livre.É essencialmente uma questão de controlar a distância à qual o material parar de fluir na frente de uma ponte.

Quando a ponte terminar, o material que não foi extrudado será expulso de qualquer maneira.A quantidade total de material extrudado permanecerá o mesmo.Isso restaura a pressão no bico, o que impede a subestusão.

![Nenhuma extrusão de um lado da ponte e extrusão adicional no outro](../../../articles/images/bridge_skin_density_100.png)

A unidade desta configuração não deve ser intuitiva.A distância em frente à ponte para a qual o material parará de fluir depende de vários fatores:
* O comprimento da parede até a ponte.Quanto mais a parede, mais o bico pode se mover em uma roda livre.
* O bico flui durante a parede normal, que depende da [velocidade](../Speed/Speed_Wall.md), [largura da linha](../Resolução/Wall_line_width.md), [débito](./material/wall_material_flow.md) e [Hight_Couche](../Resolução/Layer_Height.md) dessas paredes.Quanto maior a vazão nas paredes normais, maior a distância percorrida.
* A taxa de saída do bico durante a parede da ponte, que depende da [velocidade](Bridge_Wall_Speed.MD) e do [débito](Bridge_Wall_Material_Flow.md) dessas paredes.Quanto maior a vazão nas paredes lixadas, menor a distância de cruzamento.

Este parâmetro é um fator multiplicador no comprimento final.

O objetivo desta roda livre é diminuir a pressão dentro da sala do bico.Isso é necessário, porque qualquer pressão restante na câmara do bico surge a matéria a uma distância considerável antes de solidificar assim que a contra -impressão desaparece.Este jato de material leva a uma subsidência.De fato, as linhas salientes são empurradas pelo restante do material que ainda está dentro do bico.Se a pressão dentro do bico do bico diminuir, essa força também será reduzida e haverá menos flacidez.

O aumento do curso de roda livre reduzirá a pressão dentro da sala do bico quando a ponte for impressa, o que reduzirá a flacidez.A impressão será mais precisa.No entanto, se houver muito o clamor, haverá um período de subestusão pouco antes de imprimir a ponte.Como essa subextrusão está nas paredes da impressão, ela será muito visível na lateral da impressão.