Remova as primeiras camadas vazias
====
Quando essa opção for ativada, camadas vazias na parte inferior da impressão serão excluídas.Toda a impressão se moverá para baixo até repousar no conjunto de impressão.Em vez de ter camadas vazias que falham na impressão, a impressão será ligeiramente menor.

Se a preferência de Cura de "colocar automaticamente os modelos na bandeja de impressão" for ativada, esse parâmetro provavelmente terá muito pouco efeito.No entanto, pode ter um efeito.Quando você deposita automaticamente modelos na bandeja de impressão, os modelos estão exatamente alinhados com a bandeja de impressão.No entanto, se os primeiros (s) contiverem apenas elementos pequenos demais para serem impressos (talvez porque o fundo não seja totalmente liso), a primeira camada ainda poderá estar vazia na impressão final.Esse ajuste evita isso movendo as outras camadas de uma camada para baixo.

Depois de mover a impressão para baixo, os parâmetros que se aplicam à primeira camada são sempre aplicados.Assim, mesmo que a primeira camada original seja excluída, a [temperatura de impressão da camada inicial](../material/material_print_temperature_layer_0.md) e os parâmetros semelhantes são sempre aplicados à nova primeira camada.

Normalmente, esse parâmetro sempre deve ser ativado para impedir que as impressões se decomam porque o fundo não é totalmente liso ou porque está mal alinhado na bandeja de impressão.No entanto, você pode optar por desativar esse parâmetro se imprimir o trabalho em várias etapas que devem começar em vôo completo.

Se [o suporte for ativado](../support/support_nable.md), esse suporte se estenderá à bandeja de impressão, para que as primeiras camadas não estejam mais vazias.Nenhuma camada será removida e a impressão não se moverá para baixo.

Se o parâmetro [tolerância ao corte](../experimental/slicing_tolerance.md) estiver definido como "exclusivo", a primeira camada estará sempre vazia.Se esse parâmetro não for ativado, a primeira camada estará realmente vazia e sua impressão provavelmente falhará.


