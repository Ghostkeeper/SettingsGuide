Largura mínima da camada externa para expansão
====
Como a pele está presente em todo o modelo, não há necessidade de estender todas essas áreas.Pelo contrário, apenas os ângulos da pele que já são mais largos que esse parâmetro serão ampliados.Dessa maneira, as superfícies planas com elementos salientes serão reforçados, sem aumentar desnecessariamente o tempo de impressão para o restante do modelo.

![Definido em 0 mm, toda a pele está aumentada com o parâmetro de distância para expandir a pele](../../../articles/images/max_skin_angle_for_expansion_90.png)

![Definido em 0,8 mm, apenas as áreas planas são ampliadas](../../../articles/images/max_skin_angle_for_expansion_45.png)

A expansão da pele é útil para fortalecer o vínculo entre a parte superior ou a parte inferior da impressão e as paredes laterais.No entanto, também pode aumentar consideravelmente o tempo de impressão e o uso do material.Este parâmetro permite filtrar o material das laterais da impressão, onde é menos útil para fortalecer o vínculo entre as paredes e a pele.

Você também pode configurar esse parâmetro com o parâmetro [ângulo máximo da camada externa para expansão](max_skin_angle_for_expass.md).Se esse parâmetro for alterado, ele será automaticamente.Este parâmetro é o que é realmente usado para cortar.