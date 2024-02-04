Ângulo de galhos de apoio à arorescente
====
Esse ajuste determina o ângulo máximo de saliência que os ramos do eixo de suporte podem fazer.Se o ângulo for aumentado, os ramos poderão ser impressos mais horizontalmente, o que lhes permite ir além.

![Um ângulo de ramo de 20 °](../../../articles/images/support_tree_angle_20.png)

![Um ângulo de ramo de 40 °](../../../articles/images/support_tree_angle_40.png)

A redução no ângulo do ramo tornará os ramos mais verticais.Aumentar isso os tornará mais horizontal.Como os galhos podem ter maiores ângulos de saliência, eles podem atingir obstáculos mais distantes, o que permite que o suporte repouso com mais frequência no conjunto de impressão do que no modelo.Isso também permitirá que as filiais se destacem mais tarde.

Os efeitos mais importantes de aumentar o ângulo dos ramos para o apoio das árvores são os seguintes:
* Redução de cicatrizes, porque o suporte geralmente deve repousar no modelo, e não na bandeja de impressão.Se o [posicionamento dos suportes](../support/support_type.md) estiver definido para entrar em contato com a bandeja, uma parte maior do modelo poderá ser suportada.
* Redução do tempo de impressão e o uso de materiais, devido à separação de galhos para altitudes mais altas.Os galhos são cortados bem a tempo de poder alcançar toda a saliência.
* Confiabilidade reduzida.Se o ângulo da saliência se tornar muito grande, o suporte será fortemente enfraquecido, o que aumentará o risco de o suporte quebrar ou mudar.

É preferível combinar os grandes ângulos de ramificações com valores baixos para o parâmetro [resolução de colisão do suporte do arborescente](support_tree_collision_resolution.md).Isso reduzirá as compensações nas posições das árvores devido à evitar colisões.Isso impede que a distância pendente de se torne muito grande quando a distância de colisão é ajustada.