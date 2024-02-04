Temperatura da bandeja padrão
====
Algumas impressoras têm uma bandeja aquecida.Esse ajuste determina a temperatura da bandeja.

Ao aquecer a bandeja, o material permanece levemente fluido e pegajoso.Alguns materiais formam cristais durante o congelamento, o que leva a um estreitamento significativo do material durante o congelamento.O leito de aquecimento mantém o material logo acima da temperatura de congelamento para evitar essa retirada.Tudo isso tem como objetivo melhorar a aderência da impressão no conjunto de impressão.

No entanto, se a bandeja de impressão estiver muito quente, a impressão será muito fluida no local onde toca a bandeja.O material então se afasta um pouco, o que causa uma pata de elefante na parte inferior da marca.Esse fenômeno pode ser compensado pelo parâmetro [expansão horizontal da camada inicial](../shell/xy_offset_layer_0.md), mas afeta a precisão dimensional.O aquecimento da bandeja de impressão também cria uma diferença de temperatura entre o material baseado na bandeja e o material localizado acima no modelo, que causa um [esquerda -dendulado](../solucionando problemas/Warping.md) quando o material localizado acima começa a se retrair.

Se este parâmetro estiver definido em 0 graus, o Cura não emitirá nenhum comando para modificar a temperatura da bandeja de impressão, o que poderá perturbar o microprograma se não houver bandeja de impressão.

** Quando você ajusta a temperatura da bandeja de impressão em um perfil de material, o parâmetro [temperatura da bandeja padrão](default_material_bed_temperature.md) é ajustado.Normalmente, a temperatura da bandeja de impressão será igual à temperatura da bandeja de impressão padrão, mas às vezes a escolha de qualidade diferente pode causar ajustes de luz na temperatura de impressão.Esse ajuste da temperatura da bandeja de impressão é o que é realmente usado para impressão. **