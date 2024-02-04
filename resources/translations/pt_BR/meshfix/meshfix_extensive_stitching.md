Consertando
====
O Cura deve saber onde está o interior do modelo para preenchê -lo com material.Se a superfície do seu modelo não estiver fechada com precisão ou tiver paredes internas, pode ser ambíguo saber onde está o interior do modelo.

Um caso frequente de um modelo não multiplicado é o que uma parte adicional do modelo é fixada em uma peça fechada.Este caso é frequente quando você publica malhas com software CAD, que não foi projetado para fabricação (mas apenas para renderização digital), como Blender ou Sketchup.Você pode ver um exemplo nas imagens abaixo.

![A Visualização de Raio X revela uma superfície adicional dentro](../../../articles/images/meshfix_extensive_stitching_xray.png)

![Com este parâmetro desativado, apenas o volume fechado corretamente é impresso](../../../articles/images/meshfix_extensive_stitching_disabled.png)

![Com este parâmetro ativado, a peça adicional é anexada corretamente](../../../articles/images/meshfix_extensive_stitching_enabled.png)

Esse ajuste permite que a cura tente preencher melhor os orifícios na malha, se não for à prova d'água adequadamente.Isso aumenta as chances de obter uma boa impressão, mas aumenta o tempo de corte e às vezes pode conectar as superfícies ruins entre eles.