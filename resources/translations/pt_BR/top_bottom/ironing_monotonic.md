Monótono
====
Normalmente, o Cura ordena as linhas de extensão para que a distância de deslocamento entre elas seja baixa.Se esse parâmetro for ativado, ele solicitará as linhas de estiramento para que as linhas adjacentes sejam sempre impressas por sobrepostas na mesma direção.

As linhas de elástico são, por padrão, muito mais finas que o bico com o qual são impressas, de modo que as linhas se sobrepõem às linhas vizinhas.Essa sobreposição dá às linhas uma ligeira inclinação, o que significa que elas refletem a luz de maneira diferente em direções diferentes.Se as linhas adjacentes se sobreporem de maneira diferente, essa reflexão mudará.Você pode vê -lo no resultado final.Dá a diferentes áreas da superfície um brilho diferente.A impressão em uma ordem monótona garante que a sobreposição seja a mesma em toda a superfície, para que não haja diferença na maneira como reflete a luz.A superfície, portanto, parece mais homogênea e suave.

No entanto, diferentemente do [equivalente para as linhas de fundo e de baixo](Skin_Monotonic.md), esse efeito para o alongamento é cancelado por outro efeito.O piso tem um fluxo tão baixo que a mudança no fluxo da impressão comum é muito importante.Isso torna a camada de alongamento mais espessa quando começa a imprimir e sempre deixa uma borda visível onde a impressão foi interrompida.Uma opção monótona não excluirá essas fronteiras.Embora a superfície possa parecer um pouco mais suave, na prática, a impressão de linhas de estriamento em ordem monótona é amplamente ineficaz, a menos que sua impressora tenha um controle muito preciso do fluxo.

A ordem monótona aumentará ligeiramente o comprimento dos movimentos, mas esse efeito é muito mínimo.

Para obter uma superfície lisa, lembre -se de associar esse parâmetro ao parâmetro [Detours Mode](../Travel/Retaction_Combing.md) para evitar skins e talvez ativar a [altura do z](../Travel/retraction_hop. md).


