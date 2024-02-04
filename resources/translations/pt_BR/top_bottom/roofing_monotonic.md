Ordem monótona da superfície superior
====
Normalmente, o Cura ordena as linhas para que a distância de deslocamento entre elas seja baixa.Se esse parâmetro for ativado, ele ordenará as linhas da superfície superior para que as linhas adjacentes sejam sempre impressas pela sobreposição na mesma direção.

Ao imprimir as linhas de superfície superior, as linhas geralmente se sobrepõem às linhas vizinhas, porque a forma de uma linha não é um retângulo perfeito.Essa sobreposição dá às linhas uma ligeira inclinação, o que significa que elas refletem a luz de maneira diferente em direções diferentes.Se as linhas adjacentes se sobreporem de maneira diferente, essa reflexão mudará.Você pode vê -lo no resultado final.Dá a diferentes áreas da superfície um brilho diferente.A impressão em uma ordem monótona garante que a sobreposição seja a mesma em toda a superfície, para que não haja diferença na maneira como reflete a luz.A superfície, portanto, parece mais homogênea e suave.

![Ordem não monótona](../../../articles/images/skin_monotonic_disabled.gif)

![Ordem monótona, sempre do canto inferior direito](../../../articles/images/skin_monotonic_enabled.gif)

A ordem monótica aumenta ligeiramente o comprimento dos movimentos, mas esse efeito é muito mínimo.Tem apenas um efeito visual na impressão.A ordem monótica não tem vantagem mecânica.

Para obter uma superfície lisa, considere combinar este parâmetro com o parâmetro [Detours Mode](../Travel/Retaction_Combing.md) para evitar skins e talvez ativar a [altura do z-z](../travel/retraction_hop.md ).Você também pode [ativar o alongamento](../top_bottom/ferroing_enabled.md), mas isso cancela completamente a utilidade desse parâmetro.O alongamento tem sua própria [opção monótona](../top_bottom/ferroing_monotonic.md).