Tamanho dos estágios de variação de camadas adaptativas
====
Se a espessura desejada de uma camada for muito diferente da de uma camada adjacente, haverá uma grande diferença no fluxo na saída do bico, que pode causar uma ou uma subestimação.Essa configuração permite garantir que a diferença na espessura da camada seja uma mudança progressiva, para evitar isso.Com este parâmetro, você pode especificar a variação máxima na espessura da camada entre duas camadas adjacentes.

![Uma grande etapa de etapas permite mudanças muito repentinas na espessura da camada](../../../articles/images/adaptive_layer_height_variation_step_0_05.png)

![Um tamanho pequeno requer alterações de espessura da camada para serem mais suaves](../../../articles/images/adaptive_layer_height_enabled.png)

A redução deste parâmetro exigirá uma transição mais progressiva da espessura da camada.Isso tem vários efeitos na impressão:
* Haverá menos eração excessiva durante a transição para uma espessura da camada mais baixa, porque a saída fora do bico tem um certo tempo para se adaptar a um fluxo mais baixo.Isso evita manchas na superfície.
* Da mesma forma, haverá menos subestimado durante a transição para uma espessura maior da camada, porque a saída para fora do bico pode se adaptar gradualmente a um fluxo maior.
* As bandas serão menos visíveis.Mesmo que áreas de espessura de camada diferente sempre tenham uma textura e cor diferente, essas áreas agora estão mais longe uma da outra, o que as torna mais difíceis de ver.
* Onde houver um ângulo agudo no modelo que deve causar uma transição repentina para camadas mais finas, o efeito da topografia reaparecerá.De fato, a espessura da camada não pode ser ajustada tão rapidamente e, portanto, será necessário usar camadas mais espessas para superfícies rasas.
* Da mesma forma, quando um ângulo agudo do modelo deve causar uma transição repentina para camadas mais espessas, a impressora criar camadas desnecessariamente finas, o que desperdiçará o tempo de impressão onde não é necessário.

Devido à implementação do algoritmo das camadas adaptativas, a transição progressiva para uma espessura de uma camada diferente sempre ocorrerá * acima do ângulo no modelo que causa a transição.


