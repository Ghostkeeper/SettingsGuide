Posicionamento de suportes
====
Este parâmetro permite escolher o suporte no qual deseja colocar seus elementos de suporte.

![O suporte é gerado para todas as superfícies salientes](../../../articles/images/support_type_everywhere.png)

![O suporte é gerado apenas onde pode descansar no conjunto de impressão](../../../articles/images/support_type_touching_buildplate.png)

A colocação de suportes em todos os lugares é mais confiável para o suporte.Todas as saliências que SAG são adequadamente suportadas.No entanto, o suporte também pode ser baseado no modelo, deixando uma cicatriz onde é construída.Isso reduz a qualidade visual e a suavidade da superfície do modelo depois de remover o suporte.

Pelo contrário, o fato de colocar o suporte apenas se isso afetar a bandeja de impressão impede que o suporte repouse no modelo.No entanto, certas partes do seu modelo podem não ser suportadas.

** Como uma dica para usar o suporte apenas na bandeja de impressão, tente [Ativação do suporte cônico](support_conical_enabled.md) e dê um valor negativo ao [ângulo de suporte cônico](support_conical_angle.md).Isso permite que o suporte se desenvolva em torno do modelo, suportando a maior parte da malha sem descansar no modelo.Caso contrário, tente o apoio da árvore. **