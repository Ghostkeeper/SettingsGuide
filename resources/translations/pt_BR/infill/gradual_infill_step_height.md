Altura progressiva de etapa de enchimento
====
Em caso de enchimento progressivo, a densidade de enchimento será reduzida de cima para baixo em vários estágios.Em cada estágio, a densidade de enchimento é reduzida pela metade.Esse ajuste indica a altura dessas etapas, a distância entre dois lugares onde o recheio é reduzido pela metade.

![1,5 mm de etapas de altura](../../../articles/images/gradual_infill_step_height_small.png)

![Preenchimento progressivo, etapas de 5 mm](../../../articles/images/gradual_infill_step_height_large.png)

Por natureza, o preenchimento progressivo cria parte do preenchimento do vazio.No entanto, em regra, é reparado automaticamente.A primeira camada de enchimento será suspensa no vazio e será anexada apenas às laterais da impressão corretamente.As camadas colocadas nele podem descansar um pouco na camada anterior nas extremidades, mas sempre cederá no meio.Isso melhora gradualmente, camada por camada.

* Reduza o tamanho da etapa de enchimento gradual para descer rapidamente a uma baixa densidade de enchimento.Isso economiza tempo de impressão e material.
* Aumente o tamanho da etapa de enchimento progressiva se o preenchimento não puder ser reparado no próximo estágio de densidade de preenchimento.Aumentar o valor desse parâmetro torna a impressão mais confiável.