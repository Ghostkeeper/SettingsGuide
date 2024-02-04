Disposição com a extrusora
====
Este parâmetro decide se o Cura deve escrever as coordenadas da cabeça de impressão ou do bico.

Se a sua impressora tiver apenas um bico, o sistema de coordenadas para sua impressora provavelmente estará alinhado com o seu bico.Isso significa que, movendo -se em direção à posição [50.50], a ponta do bico realmente se move para essa posição.Se a sua impressora tiver vários bicos e esses bicos estiverem lado ao lado da cabeça de impressão, é importante.

Algumas impressoras movem a cabeça de impressão no mesmo local, qualquer que seja o bico atualmente ativado.Embora o Code-G possa ordenar que a impressora se colocasse em posição [50.50], o final do bico atualmente ativo pode ser colocado em posição [68.50], pois é, por exemplo, a 18 mm à direita do primeiro bico .Se for esse o caso, esse parâmetro deve ser ativado.

Outras impressoras ajustam automaticamente a posição da cabeça de impressão para que o bico ativo seja movido para a posição indicada no código-g.Isso significa que, se o Code-G comandar a impressora para se mover na posição [50.50], a extrusora atualmente ativa se moverá nessa posição.A própria cabeça de impressão se moveria um pouco do lado para posicionar a extrusora ativa.Se a sua impressora se comportar dessa maneira, esse parâmetro deve ser desativado.

*Como é uma configuração da máquina, esse ajuste normalmente não é visível na lista de configurações.*