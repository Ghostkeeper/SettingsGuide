Separação de fraldas
====
A adesão entre as camadas é frequentemente o principal ponto fraco da estrutura dos objetos impressos em 3D.Se a adesão entre as camadas diminuir durante ou logo após a impressão, falamos de separação das camadas, a colocação das fraldas ou a dilapidação.

![As camadas separadas ao lado deste contêiner](../../../articles/images/layer_splitting.jpg)

As quebras de camada podem ser difíceis de gerenciar, porque a impressão é sempre dividida no link mais baixo.As sugestões abaixo visam tornar a impressão mais constante e a extrusão mais confiável, a fim de remover as zonas de associação baixa entre as camadas.

Deformação
----
A maioria das camadas de camadas é causada pelo [desapego](Warping.md).Esse fenômeno é particularmente frequente com polímeros semi-cristalinos.Estes formam estruturas cristalinas microscópicas quando esfriam e se retraem muito para formar essas estruturas.A forma mais comum da esquerda é a da parte inferior da impressão que se deforma para cima, o que não causa camadas de camadas.No entanto, se o dependência da esquerda ocorrer acima na impressão, as camadas se deformam e se separam de suas camadas adjacentes.

Para evitar que a esquerda seja feita nas camadas superiores, pode -se tomar um certo número de medidas para reduzir o risco de separação de camadas:
* Use um [padrão de enchimento superior/inferior](../top_bottom/top_bottom_pattern.md) Concentric.Um padrão linear possui linhas que se retirarão na mesma direção, o que puxará essas camadas na mesma direção.O motivo concêntrico torna possível distribuir as tensões.
* O aumento da [temperatura do volume de construção](../material/build_volume_temperature.md) reduz a esquerda -de [Recuisher](https://en.wikipedia.org/wiki/annealing_%28Glass%29) o plástico.Para fazer isso, a impressora precisa de um volume de construção fechado, que mantém o calor dentro.
* Da mesma forma, o uso de um [SHIELD](../Experimental/Draft_Shield_enabled.md) torna possível manter parte do calor, mas com menos eficácia do que um volume de construção fechado.
* Evite ângulos animados no modelo 3D.A adição de uma licença nos cantos agudos impede que as linhas de pele atirem diretamente nas paredes subjacentes.É frequentemente neste local que ocorre a separação das fraldas.
* Use um material que não se retraia tanto.Por exemplo, o PLA é menos deformado que o polipropileno.No entanto, a maioria das pessoas escolhe seu material com base em requisitos específicos, o que não é uma opção para elas.

Pressão insuficiente
----
Para que as camadas sigam bem umas às outras, é necessário empurrar fortemente o plástico na camada anterior.Se o bico não extrudar material suficiente ou se o material não for empurrado forte o suficiente contra a camada anterior, a força de adesão entre as camadas será reduzida, o que lhes permite se separar mais facilmente.Mesmo que não cause imediatamente a quebra de uma camada, isso também reduz a resistência da parte final.

Isso é principalmente um problema para as paredes.A pele tem uma superfície que não tende a se separar.Entre o recheio e as paredes, as paredes fornecem a maioria dos membros da camada, pois o recheio é frequentemente impresso muito rapidamente, usando linhas de baixa distribuição e muitas vezes não é empilhado verticalmente.

Para garantir uma pressão suficiente, é importante garantir que não haja [subestriamento](subrextrusion.md).Todas as causas de subestusão são aplicáveis, mas algumas delas são particularmente preocupantes para o fracionamento de fraldas:
* Quando você tem a impressão no meio do caminho, leva um tempo para a extrusão retomar sua velocidade.O script de pausa na altura tem uma opção para <!-se cura_version> = 4.7-> refazer uma camada <!-endif-> <!-se cura_version <4.7: refazer as últimas camadas->.Isso iniciará o material antes de continuar para cima, impedindo uma camada baixa com pressão insuficiente do bico.
* Reduza a [velocidade de impressão da parede](../speed/speed_wall.md) torna a impressão das paredes mais constantes.Isso reduz o risco de desenvolver pontos fracos, reduzindo o subestimado nas paredes.
* Reduza a [altura da camada](../Resolução/Layer_Height.md) ou [largura da linha de parede](../Resolução/Wall_Line_Width.md).Altas velocidades requerem maior pressão.Se a impressora não puder fornecer essa pressão, o material extrudado será insuficiente para preencher as camadas grossas ou linhas largas.Isso torna a impressão mais baixa.
* Aumente a [temperatura da impressão](../MATEMCIAL/MATTER_PRINT_TEMPERATURA.MD) para garantir que o material flua com mais facilidade, usando totalmente a superfície de contato, em vez de permanecer concentrado no centro do cordão.
* Reduza [Distância das retrações](../Travel/Retaction_amount.md).As retrações longas permitem que mais material funcione durante a retração, causando uma sub-extrusão subsequente.Eles também interrompem mais fluxo.Levará mais tempo para o fluxo do que se estabilizar.Ao reduzir a distância da retração, reduzimos o risco de ver ligações baixas se desenvolverem na altura da impressão devido a um fluxo irregular.

Superfície insuficiente
----
A adesão entre as camadas depende da força da conexão entre os materiais, multiplicada pela superfície à qual se liga.O aumento da superfície reduz o risco de separação de camadas.

O parâmetro mais importante a esse respeito é [espessura da parede](../shell/wall_thickness.md).Um número maior de paredes aumenta consideravelmente a superfície.As paredes são impressas mais lentamente e estão localizadas, onde começarão a se separar, por isso são uma maneira muito eficaz de aumentar a adesão das fraldas.No entanto, a impressão de um número maior de paredes também aumenta consideravelmente o tempo de impressão e o uso de materiais.

Uma superfície insuficiente geralmente é um problema ao imprimir grandes impressões, onde a deformação é forte, com uma única parede e sem encher.A parede começará a se deformar por causa da esquerda e não há nada para impedi -lo.Isso pode ser um motivo para desativar o uso do modo de [espiralização do contorno externo](../Blackmagic/Magic_spiralize.md), pois imprime uma única parede e impede a geração de enchimento.Em vez disso, pode ser necessário imprimir com duas paredes e ajustar manualmente a densidade de enchimento em 0 % para obter um efeito semelhante.

Materiais incompatíveis
----
Em impressões com diferentes tipos de plástico, verifique se os plásticos aderem um ao outro.Em geral, plásticos cujas taxas de retração são muito diferentes não poderão aderir um ao outro.Devido a diferentes efeitos químicos, os plásticos também são repelidos, o que os impede de grudar.Se isso acontecer em uma grande área plana no meio da sua impressão, há uma boa chance de a impressão sair lá.

Para evitar que isso aconteça, pode ser necessário projetar uma articulação de travamento mecânica entre as duas superfícies.Trate os diferentes materiais como se fossem impressos separadamente, exceto que não precisarão ser montados posteriormente.