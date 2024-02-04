Deslocamento de limpeza
====
Este parâmetro permite definir a largura dos movimentos de limpeza.O bico se moverá sobre essa distância para [cada movimento de limpeza](wipe_repeat_count.md).

No início, o bico será colocado logo além do pincel WIP em uma [certa coordenada x](wipe_brush_pos_x.md).A distância indicada nesse ajuste deve ser tal que o deslocamento dessa distância o local do outro lado da escova.Muito deslocamento introduz movimentos desnecessários e pode levar ao retorno do bico no volume de construção, o que pode levá -lo a atingir desnecessariamente o modelo se [os saltos z não forem ativados](wipe_hop_enable.md).Deslocamento insuficiente pode impedir que ele atinja o pincel corretamente.

A distância também pode ser negativa.O bico então limpará o outro lado.Dependendo da sua escolha de [coordenar x](wipe_brush_pos_x.md), isso pode ser necessário para limpar na direção certa.