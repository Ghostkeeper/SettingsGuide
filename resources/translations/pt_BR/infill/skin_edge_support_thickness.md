Suporte a espessura das bordas da camada
====
Ao imprimir formulários côncavos, se houver uma pele mais alta que termine perto do recheio, essa configuração adiciona uma linha adicional através do recheio para suportar a borda da pele, de modo que ela se afasta um pouco menos.

![Um perímetro é criado através do recheio sob a borda da pele externa](../../../articles/images/skin_edge_support_thickness.png)

Uma única linha através dos interstices de enchimento sempre será fag, por isso é necessário criar várias camadas sob a borda da pele que precisa ser sustentada.Esse ajuste permite a espessura vertical da linha sob a borda da pele.Você também pode ajustar diretamente o [número de camadas](skin_edge_support_layers.md) sob a borda da pele, onde essas linhas serão rastreadas.

O aumento dessa espessura geralmente terá os seguintes efeitos na impressão:
* A borda da pele será melhor suportada, o que tornará a face superior mais suave, porque a pele pode ir completamente de um lado para o outro.
* A impressão leva um pouco mais de tempo e usa mais material.

Se a taxa de enchimento for alta, esse ajuste praticamente não terá efeito na superfície superior e poderá causar [superextrusão](../distúrbios/superextrusion.md) no enchimento.Portanto, é preferível deixá -lo a 0 mm.