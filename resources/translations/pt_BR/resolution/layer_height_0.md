Altura inicial da camada
====
Este parâmetro define a espessura da primeira camada da sua impressão.A camada inicial é normalmente impressa mais espessa que o restante, a fim de criar uma adesão mais forte com a bandeja de impressão.Com esse ajuste, a espessura da camada inicial pode ser aumentada sem reduzir a resolução do restante da impressão.

![A camada inicial é mais espessa que o restante das camadas](../../../articles/images/layer_height_0.png)

O aumento na espessura da camada inicial significa que o bico de extrude mais material sobre a mesma distância.Isso requer força adicional, porque o material se espalha para as laterais para preencher toda a largura da linha.Essa força adicional significa que o material adere melhor à placa de impressão.Além disso, a camada mais espessa torna possível alcançar as irregularidades da planicidade da superfície.Se a bandeja de impressão for um pouco torcida, a variabilidade será absorvida pela espessura da primeira camada, enquanto o bico poderá raspá -la na segunda camada.

Muita espessura da primeira camada leva a uma maior flacidez da primeira camada, o que causa pernas de elefante.O parâmetro [expansão horizontal da camada inicial](../shell/xy_offset_layer_0.md) pode impedir isso, dando -lhe um pequeno valor negativo.