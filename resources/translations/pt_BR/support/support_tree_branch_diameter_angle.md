Ângulo de diâmetro de galhos de apoio à arborescente
====
Os galhos do suporte das árvores são mais largos do que no topo.Isso garante que os ramos permaneçam estáveis, independentemente da altura do apoio.Com essa configuração, você pode controlar a velocidade na qual o suporte aumenta.

![A forma de um ramo com um ângulo de diâmetro de 5 °](../../../articles/images/support_tree_branch_diameter_1_4mm_5.png)

![A forma de um ramo com um ângulo de diâmetro de 10 °](../../../articles/images/support_tree_branch_diameter_angle_10.png)

Quanto maior o ângulo, maior o fundo do suporte da árvore, especialmente com os grandes modelos.Isso tem vários efeitos:
* O fundo mais amplo torna o suporte mais difícil de reverter.Isso aumenta a confiabilidade do suporte da árvore.
* O fundo mais amplo requer mais material e tempo para impressão.
* O ângulo do suporte é adicionado ao ângulo máximo (support_tree_angle.md) ao qual as ramificações podem sobrecarregar, para que valores muito altos também possam tornar o suporte menos sólido em certos casos.
* Os ramos mais largos têm mais dificuldade em navegar na malha, o que dificulta o acesso a certas partes da saliência da bandeja de impressão.Consequentemente, o suporte pode ter que descansar no modelo, e não na bandeja de impressão, o que aumenta a quantidade de cicatrizes.
* A prevenção das colisões da árvore é mais difícil de calcular para a cura, o que aumenta o tempo de corte.É possível remediar esse problema aumentando o parâmetro [resolução de colisão do suporte arborescente](support_tree_collision_resolution.md), mas isso também reduz a integridade estrutural do suporte da árvore.

Em geral, você deseja que o ângulo seja tal que o apoio da árvore seja largo o suficiente para se sustentar em qualquer altura sem se tornar muito ramo.