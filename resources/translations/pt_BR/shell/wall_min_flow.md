Fluxo mínimo da parede
====
A compensação por sobreposição das linhas de parede reduzirá o fluxo de algumas das paredes.Isso pode ser problemático porque pode reduzir a velocidade arbitrariamente baixa, até 1 % se as paredes se sobreporem quase completamente.A impressão em fluxos extremamente baixos não funciona bem.Tende a formar um padrão de gotículas em vez de linhas de extrusão contínuas.

Essa configuração transformará linhas de fluxo extremamente baixas em movimentos de tradução, passando efetivamente seu fluxo para 0 %.A matéria continuará a escorrer como nos movimentos normais do movimento, mas não formará pérolas.

![As sobreposições entre as paredes são compensadas normalmente](../../../articles/images/wall_min_flow_0.png)

![As paredes com menos de 50% de extrusão são transformadas em movimentos de movimento](../../../articles/images/wall_min_flow_50.png)

O bico sempre seguirá o layout da parede para escorrer no lugar certo.

Ao aumentar essa configuração, suas paredes serão mais finas do que o desejado.Em vez de desenhar linhas muito finas, você não desenha mais nada.Tecnicamente, isso é uma subestimação, o que significa que seu quarto é mais fino do que o desejado.No entanto, a parede não teria sido impressa bem de qualquer maneira.Em vez de desenhar uma longa linha de pontos ou pérolas na parede, nada será impresso, o que tornará a parede um pouco mais suave.

Ajuste este parâmetro no fluxo mínimo da parede que seu bico pode alcançar sem formar gotículas.Em geral, essa taxa é de cerca de 60 %.Se a largura das linhas foi reduzida abaixo de 60%, essas gotículas são formadas, portanto, é preferível transformar essas linhas em movimentos de movimento.Se você imprimir em alturas de camada maior ou se usar linhas de parede mais espessas, poderá reduzir um pouco essa configuração para obter maior precisão dimensional.