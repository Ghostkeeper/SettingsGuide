Suporte camadas da pele da pele
====
Ao imprimir formulários côncavos, haverá uma pele superior que terminará em algum lugar a meio caminho do recheio.Essa configuração adiciona uma linha adicional através do recheio para suportar a borda da pele, para que ela ceda um pouco menos.

![Um contorno é criado através do enchimento sob a borda da pele](../../../articles/images/skin_edge_support_thickness.png)

Uma única linha através dos interstices de enchimento sempre cederá, para que a linha possa ser desenhada em várias camadas sob a borda da pele, que precisa ser sustentada.Este parâmetro configura o número de camadas através das quais essa linha será desenhada sob a borda da pele.Você também pode ajustar a [espessura](skin_edge_support_thickness.md) das fraldas através das quais a linha é desenhada.

O aumento do número de camadas geralmente terá os seguintes efeitos na impressão:
* A borda da pele será melhor suportada, o que dará a um lado superior mais suave, porque a pele pode ir completamente de um lado para o outro.
* A impressão leva um pouco mais de tempo e usa mais material.

Se a taxa de enchimento for alta, esse ajuste praticamente não terá efeito na superfície superior e poderá causar [superextrusão](../distúrbios/superextrusion.md) no enchimento.Portanto, é preferível deixar a camada 0.