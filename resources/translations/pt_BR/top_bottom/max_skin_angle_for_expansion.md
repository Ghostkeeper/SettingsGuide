Ângulo máximo da camada externa para expansão
====
Como a pele está presente em todo o modelo, não há necessidade de estender todas essas áreas.Pelo contrário, apenas as áreas onde o ângulo entre a superfície da pele e o horizonte é menor que esse ajuste será estendido.Dessa forma, as superfícies planas com elementos salientes serão reforçados, sem aumentar desnecessariamente o tempo de impressão para o restante do modelo.

![Definido a 90 graus, toda a pele é aumentada com o parâmetro de distância para expandir a pele](../../../articles/images/max_skin_angle_for_expansion_90.png)

![Definido para 45 graus, apenas as áreas planas são ampliadas](../../../articles/images/max_skin_angle_for_expansion_45.png)

A expansão da pele é útil para fortalecer o vínculo entre a parte superior ou a parte inferior da impressão e as paredes laterais.No entanto, também pode aumentar consideravelmente o tempo de impressão e o uso do material.Este parâmetro permite filtrar o material das laterais da impressão, onde é menos útil para fortalecer o vínculo entre as paredes e a pele.

Para esta configuração, 0 ° é horizontal.Se essa configuração for 0 °, nenhuma pele se expande.90 ° é vertical e causa a expansão de todas as áreas da pele.