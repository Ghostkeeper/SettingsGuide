Etapa gradual de enchimento do suporte
====
Ao usar um suporte gradual, a densidade do suporte é periodicamente reduzida de cima para baixo em várias etapas.Em cada estágio, a densidade do suporte é dividida por dois.Este parâmetro indica a altura dessas etapas, a distância entre dois lugares onde a densidade do suporte é dividida por dois.

![1 mm de altura](../../../articles/images/gradual_support_infill_step_height_1mm.png)

![3 mm de altura](../../../articles/images/gradual_support_infill_step_height_3mm.png)

O suporte progressivo, por sua natureza, criará parte do suporte no vazio.No entanto, isso é normalmente reparado automaticamente.A primeira camada de suporte será suspensa no vazio e só será fixada nas laterais do suporte corretamente.As camadas acima podem repousar um pouco na camada anterior nas extremidades, mas caem no meio.Isso melhora gradualmente, camada por camada.Se a altura da etapa de suporte progressiva for grande o suficiente, o suporte será adequadamente robusto quando o próximo estágio de densidade ocorrer.

Reduza a altura da etapa de suporte gradual para descer rapidamente a uma baixa densidade de suporte.Isso economiza tempo de impressão e o uso do material.Aumente a altura do estágio gradual de enchimento do suporte se o suporte não tiver espaço suficiente para se reparar quando ocorrer a próxima etapa do suporte.O aumento no valor desse parâmetro torna a impressão mais confiável.