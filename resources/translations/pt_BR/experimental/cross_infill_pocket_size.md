Tamanho do bolso transversal 3D -seção
====
O 3D Cross [Motif de enchimento](../preenchimento/refill_pattern.md) foi projetado para facilitar impressões flexíveis.O motivo contém encruzilhados de 4 vias que são, no entanto, muito rígidos.Esse ajuste evita cruzamentos para não ser muito rígido em certos lugares.O padrão deixará uma bolsa de ar na travessia.Essa configuração determina o tamanho do bolso.

![O tamanho do bolso padrão é de 2 mm](../../../articles/images/infill_pattern_cross_3d.png)

![Um formato de bolso de 0,5 mm](../../../articles/images/cross_infill_pocket_size_0_5.png)

O modelo varia a distância em torno da passagem de quatro caminhos.Essa configuração determina o tamanho do bolso nas camadas quando as linhas tocam completamente.O tamanho máximo da bolsa é determinado pela densidade de enchimento.O tamanho da bolsa não será maior que a raiz quadrada da duas vezes a distância entre as linhas de enchimento.Se um valor maior for inserido, isso não terá efeito, mas valores maiores sempre podem ser inseridos para facilitar tamanhos maiores de bolso no caso em que [preenchimento progressivo](../preenchimento/gradual_infill_steps.md) ou [densidade de enchimento variável ](Cross_infill_Dension_Image.md) é usado.

O aumento no valor desse parâmetro torna o enchimento mais baixo na direção vertical e torna possível distribuir melhor a força para criar uma distribuição mais uniforme da força.