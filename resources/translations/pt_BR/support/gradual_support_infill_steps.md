Estágios de apoio gradual do suporte
====
O suporte gradual reduz a quantidade de material de suporte usado, reduzindo a densidade de suporte nas camadas inferiores.Isso economiza tempo e material de impressão, apesar de não reduzir muito a qualidade da saliência.O objetivo principal do apoio é apoiar as áreas de excesso.Essa característica permite que o suporte se concentre nessa extremidade.

Este parâmetro indica em quantas etapas a densidade do suporte é reduzida.Em cada estágio, a densidade do suporte é reduzida pela metade.Por exemplo, de uma densidade de 20 % e dois estágios de suporte progressivo, a densidade de suporte das partes inferiores será de 10 % e 5 %, respectivamente.

![O suporte é reduzido a uma densidade mais baixa em 3 etapas](../../../articles/images/gradual_support_infill_step_height_1mm.png)

O aumento no número de etapas leva a uma redução cada vez mais significativa na densidade, o que resulta em uma diminuição no apoio à densidade.Isso economiza muito material e tempo de impressão, mas torna o suporte mais baixo.

Parte do suporte flutuará no ar.No entanto, na prática, com a maioria dos modelos de suporte, isso será reparado rapidamente porque as camadas podem se acumular corretamente, mesmo nas camadas inferiores enfraquecidas.O objetivo da altura do estágio de preenchimento [gradual de suporte gradual](gradual_support_infill_step_height.md) é deixar tempo suficiente para reparar antes que a próxima etapa de suporte gradual seja empilhada na parte superior.

Este parâmetro deve ser combinado com pelo menos um [número de linhas da parede do suporte](support_wall_count.md).Isso oferece às linhas de suporte algo para aguentar, em vez de serem suspensas no ar.