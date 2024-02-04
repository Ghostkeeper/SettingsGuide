Conecte as linhas de enchimento
==
Essa opção possibilita adicionar uma trajetória que vincula os pontos finais do modelo de enchimento, onde o enchimento atende à parede interna ou à pele, usando uma linha que segue a borda da área de enchimento.

![Sem linha de enchimento conectada](../../../articles/images/infill_pattern_grid.png)

![Linhas de enchimento conectadas](../../../articles/images/zig_zaggify_infill_enabled.png)

Isso torna possível converter todo o esquema de preenchimento em uma única linha ou em muito poucas linhas.A conversão em uma única linha nem sempre é possível.O ponto de partida dessa linha é arbitrário, por isso pode não ser o mesmo para cada camada, especialmente se a forma do recheio for diferente de uma camada para outra.

O preenchimento do recheio tem algumas vantagens, mas também algumas desvantagens:
* Seu quarto será mais sólido no final, pois há praticamente meio contorno.
* O material de enchimento adere melhor às paredes graças ao aumento da superfície, o que torna a sala mais resistente.
* O fluxo será mantido mais constante, o que permitirá imprimir o preenchimento a uma velocidade mais alta sem problemas de fluxo.Isso é particularmente importante para materiais difíceis de extrudar adequadamente.
* O número de retiradas feitas durante a impressão é muito menor, o que impede que o material moa.
* O efeito do parâmetro [porcentagem de sobreposição do enchimento](Infill_overlap.md) é amplificado, porque uma parte maior das linhas de enchimento monta as paredes.
* Será necessário mais material para imprimir o preenchimento.
* Geralmente, é mais tempo para imprimir o preenchimento, porque a viagem normalmente é mais rápida do que imprimir as linhas de enchimento.
* O recheio geralmente será mais visível através das paredes, porque será empurrado para uma parte maior das paredes.