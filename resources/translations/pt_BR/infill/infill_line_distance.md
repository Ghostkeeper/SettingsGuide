Distância da distância da linha de enchimento
====
Em vez de definir [densidade de preenchimento](Infill_sparse_Dension.md) em porcentagem, também é possível configurar a densidade de enchimento definindo a distância entre as linhas de enchimento adjacentes.Uma distância maior entre as linhas de enchimento causará uma menor densidade de enchimento global.

A distância entre as linhas de enchimento é uma maneira diferente de considerar essa propriedade que a densidade.A distância entre as linhas de enchimento fornece uma indicação da distância de que as linhas de superfície superior devem viajar de uma linha de enchimento para outra.A redução na distância entre as linhas de enchimento, portanto, possibilita reduzir a distância de ponte e melhorar a qualidade das superfícies superiores.

![Distância de 4 mm entre as linhas, o que fornece uma densidade de 20%](../../../articles/images/infill_pattern_grid.png)

![Distância de 8 mm entre as linhas, o que fornece uma densidade de 10%](../../../articles/images/infill_sparse_density_low.png)

Normalmente, a distância da linha de enchimento é calculada a partir da densidade de preenchimento desejada, dependendo do modelo de enchimento selecionado e da largura da linha.A distância da linha de enchimento está na liderança.

O aumento da densidade de enchimento (reduzindo a distância entre as linhas) tem um efeito importante na sua impressão, a saber:
* Sua impressão será mais forte.
* A superfície superior será melhor sustentada, o que o tornará mais suave e mais impermeável.
* O travesseiro será reduzido porque os bolsos de calor serão menores.
* Seu sorteio exigirá mais material e, portanto, será mais pesado.
* Leva mais tempo para imprimir.