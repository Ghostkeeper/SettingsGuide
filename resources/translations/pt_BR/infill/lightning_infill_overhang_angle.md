Ângulo de preenchimento do eclair
====
O enchimento do tipo Eclair suportará apenas o lado superior do modelo por dentro, onde está no vácuo.Este parâmetro determina o ângulo da saliência que é suportada pelo preenchimento eclair de dentro do modelo.

![O excesso até 30 ° não é suportado](../../../articles/images/lightning_infill_support_angle_30.png)

![Até 70 ° não é suportado, deixando apenas o topo da esfera sustentada](../../../articles/images/lightning_infill_overhang_angle_70.png)

O aumento desse ângulo reduzirá a quantidade de preenchimento gerada.Uma parte menor da superfície superior será sustentada, se não for uma saliência muito importante.Isso economiza tempo e materiais, mas também pode causar a superfície superior em locais.O resultado pode ser um tipo de tipo [colchão](../solucionamento de problemas/travesseiro.md) ou geralmente uma superfície menos lisa.

Ao contrário da configuração pai [ângulo de enchimento do Eclair](Lightning_infill_support_angle.md), esse parâmetro não influencia a saliência no próprio padrão de enchimento.