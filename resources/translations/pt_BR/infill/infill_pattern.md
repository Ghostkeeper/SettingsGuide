Padrão de enchimento
====
O modelo de enchimento define uma estrutura usada para preencher o volume do objeto.Existem vários modelos, cada um com suas próprias vantagens.Alguns são especializados em aplicações muito específicas.

Grade
----
! [Grille](../../../Artigos/Images/Infill_pattern_grid.png)

A grade de enchimento cria dois conjuntos de linhas perpendiculares.Juntos, eles formam um motivo quadrado.
* O motivo mais forte na direção vertical.
* Bastante forte nas duas direções das linhas.
* Não é tão forte na diagonal.
* Suporte muito bom para a superfície superior.Sua superfície ficará muito suave.

Linhe
----
! [Lignes](../../../artigos/imagens/infill_pattern_lines.png)

O padrão de linha cria linhas paralelas.Por padrão, o padrão de linha alterna sua direção perpendicular de uma camada para outra, o que faz com que pareça o motivo da grade à primeira vista.No entanto, é possível modificar essa aparência com o parâmetro [direções da linha de preenchimento](Infill_angles.md).
* O melhor padrão para uma superfície superior lisa ao mesmo tempo que o zigue -zague, pois a distância entre as linhas é a menor.
* Tende a ser baixo na direção vertical, porque as camadas têm apenas pequenos pontos de ligação entre eles.
* Será extremamente baixo na direção horizontal, exceto na direção sozinha, onde as linhas são orientadas.Mas mesmo nessa direção, ele não é resistente ao cisalhamento, de modo que ele gera bastante rapidamente sob a carga.

Triângulos
----
! [Triangles](../../../Artigos/Images/Infill_pattern_triangles.png)

O padrão dos triângulos cria três linhas de linhas em três direções diferentes.O todo forma um padrão de triângulos.
* Muito resistente ao cisalhamento.
* A força é quase igual em cada direção horizontal.
* As linhas superiores devem ser longas o suficiente, o que requer muitas camadas de pele para obter uma superfície superior uniforme.
* O fluxo é consideravelmente interrompido nos cruzamentos, o que leva a uma resistência relativamente baixa a altas taxas de enchimento.

Trihexagonal
----
! [Tri-hexagonal](../../../Artigos/Images/Infill_pattern_trihexagon.png)

O modelo Tri-hexágono cria três linhas de linhas em três direções diferentes, bem como o modelo triangular, mas se mudaram para que nem todas cruzem na mesma posição.
* O motivo mais forte na direção horizontal.
* A força é quase igual em todas as direções horizontais.
* Muito resistente ao cisalhamento.
* As linhas superiores devem ser muito longas, o que requer muitas camadas de pele mais alta para obter uma superfície superior uniforme.

Cúbico
----
! [Cubic](../../../Artigos/Images/Infill_pattern_cubic.png)

O padrão cúbico cria cubos, um padrão tridimensional.Os cubos são orientados em pé em um canto, o que lhes permite imprimi -los sem transbordar as superfícies internas.
* Força aproximadamente igual em todas as direções, incluindo direção vertical.
* Bastante forte em todas as direções.
* Efeito reduzido do travesseiro, pois não produz bolsos verticais longos de ar quente.

Subdivisão cúbica
----
! [Subdivisão cúbica](../../../Artigos/Images/Infill_pattern_cubic_subdivision.png)

O modelo de subdivisão cúbica cria cubos, um modelo tridimensional.Os cubos são orientados em pé em um canto, o que lhes permite imprimi -los sem transbordar as superfícies internas.No entanto, esse motivo produz cubos maiores dentro do volume, o que salva a matéria.Deixa de lado as linhas de enchimento nos lugares onde são os menos úteis.

Esse motivo pode produzir quaisquer densidades de enchimento inferiores às desejadas.É aconselhável aumentar consideravelmente a densidade de enchimento ao usar esse modelo.A otimização funciona melhor a altas taxas de enchimento.

Algoritmicamente, esse modelo é gerado pela criação de um cubo gigante em torno de todo o volume e subdividiu esse cubo em 8 subcubes quando afeta qualquer parede.Esta operação é então repetida, de modo que os subcubes que afetam qualquer parede são subdivididos repetidamente.Isso é repetido até que a distância da linha de enchimento seja atingida.
* O padrão mais forte, dependendo do peso e do tempo de impressão.
* A força é quase igual em todas as direções, incluindo a direção vertical.
* Concentre o preenchimento em partes finas.
* O efeito do travesseiro é reduzido porque não produz longos bolsos verticais de ar quente.
* Se usarmos uma densidade de enchimento aumentada, o enchimento não brilha muito nas paredes, o que produz melhor qualidade da superfície para um tempo de impressão igual.
* Introduz retrações, que não funcionam bem com materiais flexíveis ou fluidos.
* Leva mais tempo para cortar.

Octaédrique
----
! [Octaédrique](../../../Artigos/Images/Infill_pattern_octet.png)

O motivo octaédrico cria uma combinação de tetraédricos e cubos regulares, um padrão tridimensional.De tempos em tempos, várias linhas de enchimento são colocadas um ao lado do outro.
* Cria uma estrutura interna sólida, onde várias linhas paralelas tocam.A carga é rapidamente dissipada em direção a essa estrutura interna.
* Forte em modelos de uma espessura média de cerca de um centímetro.
* Efeito reduzido do travesseiro, pois não produz bolsos verticais longos de ar quente.
* O resultado é uma distância de ponte muito longa para a pele superior, o que reduz a superfície superior que

Trimestre cúbico
----
! [Quarter Cubic](../../../Artigos/Images/Infill_pattern_quarter_cubic.png)

O motivo do quarto cúbico cria uma tessa tridimensional composta por tetraédricos e tetraedria truncada.De tempos em tempos, várias linhas de enchimento são colocadas um ao lado do outro.
* Cria dois quadros internos disjuntos, semelhante a um byte, onde várias linhas paralelas tocam.A carga é rapidamente dissipada em direção a essa estrutura interna.Os quadros são orientados em duas direções diferentes, o que os torna mais baixos individualmente, mas reduz a distância para distribuir a carga nesses quadros.
* Forte em modelos de baixa espessura de alguns milímetros.
* Efeito reduzido do travesseiro porque não produz bolsos verticais longos de ar quente.
* Resulta em uma distância de ponte muito longa para a pele superior, o que reduz a qualidade da superfície superior.

Concêntrico
----
! [Concentric](../../../Artigos/Images/Infill_pattern_concentric.png)

O motivo concêntrico cria anéis paralelos às paredes.
* O padrão de enchimento mais forte ao usar 100%de enchimento, porque não apenas não é cruzamento de linha, mas as linhas também são orientadas para que a força não isotrópica das linhas distribua a carga.
* Produz as impressões mais flexíveis, com uma força muito fraca e regular em todas as direções horizontais.
* Mais forte na direção vertical do que na direção horizontal.
* Com uma densidade de preenchimento de 100 %, o material pode aglutinar no meio, o que reduziria a confiabilidade da impressão de formas redondas, onde os círculos concêntricos se encontram em um ponto.
* Com alguns formulários, algumas das linhas de enchimento podem pendurar no ar, adicionando qualquer resistência adicional para o custo do material e o tempo de impressão.
* Quando você não usa 100%de enchimento, é o motivo de enchimento mais baixo na direção horizontal.Ele não acrescenta nenhuma resistência.

Ziguezague
----
! [Zigzag](../../../Artigos/Images/Infill_pattern_zigzag.png)

O motivo de enchimento em zigue -zague significa que o bico desenha linhas em zigue -zague.É como linhas, mas as linhas estão conectadas em uma linha longa, o que evita interrupções de fluxo.
* O segundo modelo de enchimento mais forte é o que usa 100%de preenchimento.No entanto, é mais confiável do que preenchimentos concêntricos de formas redondas.
* O melhor padrão para uma superfície superior lisa com ziguezague, pois a distância entre as linhas é a menor.
* Tende a ser bastante fraco no sentido vertical, porque as camadas têm apenas pequenos pontos de ligação entre eles.
* Será extremamente baixo na direção horizontal, exceto na direção sozinha, onde as linhas são orientadas.Mas mesmo nessa direção, ele não é resistente ao cisalhamento, de modo que ele gera bastante rapidamente sob a carga.

Croix
----
! [Croix](../../../Artigos/Images/Infill_pattern_cross.png)

O modelo de enchimento cruzado produz uma curva de preenchimento de espaço que produz algo que parece cruzamentos ao longo do interior do volume.
* A curva está enrolada uniformemente em todas as direções horizontais, o que a torna útil para imprimir objetos flexíveis e flexíveis.
* Não produz linhas retas longas na direção horizontal, o que torna esse motivo uniformemente curvado em todo o perímetro.Não há pontos fortes.
* Não produz nenhuma retração, o que facilita a impressão com materiais flexíveis.
* Será mais forte no sentido vertical do que no sentido horizontal.
* Demore muito tempo para cortar.
* Estará muito baixo em todas as direções horizontais.

Croix 3D
----
! [CROIX 3D](../../../Artigos/Images/Infill_pattern_cross_3d.png)

O modelo de enchimento 3D cruzado produz uma curva de preenchimento de espaço que produz algo que se parece com cruzes ao longo do interior do volume.Esse padrão de pulso ao longo do eixo z para enfraquecê -lo na direção vertical.
* Esse padrão é, portanto, o mais útil para imprimir objetos flexíveis e flexíveis.
* Não produz linhas retas longas, o que a torna uniformemente enrolada por toda a superfície.
* Não produz nenhuma retração, o que facilita a impressão com materiais flexíveis.
* Demore muito tempo para cortar.
* Estará muito baixo em todas as direções.

Gyroïde
----
! [Gyroïde](../../../Artigos/Images/Infill_pattern_gyroid.png)

O padrão de preenchimento de giroside produz um padrão ondulado que alterna as direções.
* Produz um volume completamente permeável a fluidos, tornando -o um modelo útil para dissolver materiais.
* Resistência igual em todas as direções, mas não muito rígida.Isso o torna útil para materiais flexíveis, mas o resultado será um pouco mais difícil, menos esponjoso, do que os padrões de enchimento cruzado (3D).
* Não há linhas que se sobreponham nesse padrão, o que permite imprimir mais facilmente com materiais com maior tensão superficial e torna o preenchimento muito confiável e coerente.
* Cisalhamento -resistente.
* Demore muito tempo para cortar e produzir grandes arquivos de código G.Para algumas impressoras, pode ser difícil seguir as muitas ordens de código G por segundo, e pode ser difícil seguir uma conexão serial com baixa velocidade em bauds.

<!-se Cura_version> = 4.12->
Clarão
----
! [Eclair](../../../Artigos/Images/Infill_pattern_lightning.png)
! [O motivo do flash construído pelos lados.](../../../Artigos/Images/Infill_pattern_lightning_side.png)

O padrão de enchimento do tipo flash é um padrão mínimo de dente de serra que visa apenas suportar a superfície superior.A densidade de enchimento especificada será alcançada logo abaixo do lado superior do volume de enchimento.
* A densidade de enchimento especificada será alcançada apenas sob o lado superior do volume de enchimento.
* O aumento da densidade de enchimento permite obter a melhor qualidade da superfície de todos os padrões, sem exigir mais tempo ou material.
* Impede que os recheios transparentes através das paredes em muitos lugares, simplesmente não tenham recheios.
* Não aumenta significativamente a resistência da peça.
<!-endif->