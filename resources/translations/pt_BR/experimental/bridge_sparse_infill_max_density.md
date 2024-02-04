Ponte de densidade de enchimento máximo
====
Se você imprimir com uma densidade de enchimento muito baixa, a pele superior tende a ceder, o que causa [almofadas](../solucionando problemas/travesseiros.md) e geralmente superfícies irregulares no lado superior da impressão.Como opção, as técnicas de cerdas também podem ser aplicadas à pele superior.Este parâmetro configura a velocidade de enchimento à qual a técnica de ponte começará a ser aplicada.

![A pele forma uma ponte sobre o recheio](../../../articles/images/bridge_sparse_infill_max_density.png)

Este parâmetro é configurado como um limite, a fim de permitir que os perfis contenham um único valor.Enquanto o usuário ajusta a densidade de preenchimento constantemente, a punção da pele será ativada ou desativada automaticamente.

Pontagem para a pele superior geralmente produz uma superfície superior mais suave a taxas de enchimento muito baixas.No entanto, verifique se você usar essa técnica, há [camadas superiores] suficientes (../top_bottom/top_layers.md) para fechar a superfície corretamente sem aplicar a técnica de direção às camadas mais altas.A técnica de ponte, em particular com uma [largura da linha](Bridge_skin_material_flow_3.md) não fechará completamente a superfície.Se a pele superior não tiver camadas suficientes, você acabará com orifícios na impressão e resistência comprometida.