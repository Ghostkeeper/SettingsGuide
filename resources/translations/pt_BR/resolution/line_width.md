Espessura da linha
====
Esta é a largura horizontal das linhas que a impressora colocará para baixo.Normalmente, o diâmetro da abertura do bico determina a largura das linhas, mas, extrudando mais ou menos material, a impressora pode variar ligeiramente a largura das linhas.

![Linhas muito finas](../../../articles/images/line_width_small.png)

![Linhas muito amplas](../../../articles/images/line_width_large.png)

Reduzir a largura da linha permite que a impressora imprima mais detalhes.Em particular, isso também permite que a impressora imprima peças finas.A largura da linha é um dos parâmetros mais influentes da sua impressão.Aqui estão alguns efeitos:
* A impressão de linhas mais finas permite imprimir peças mais finas, pois pode até manter uma linha nas melhores peças.
* Ajustar a largura da linha para um ponto múltiplo da espessura da sua impressão pode tornar o objeto mais sólido e melhorar o fluxo do material.
* Uma largura de linha menor tornará sua superfície superior mais suave.
* Linhas de impressão ligeiramente menores do que o tamanho do seu bico tende a melhorar a resistência.Isso permite que o bico mescla as linhas adjacentes entre elas quando faz uma segunda passagem um pouco mais alta que a linha anterior.
* As linhas de impressão muito grandes causam uma subestimada.A impressora tentará extrudar mais material, o suficiente para preencher a largura da linha desejada.Este material tentará fluir em qualquer direção.No entanto, em algum momento, a falsificação se torna muito grande, de modo que o material não flui mais até a borda das linhas muito amplas.Isso deixa os espaços entre as linhas.
* As linhas de impressão muito pequenas também causam uma subestimada.Se o material não fluir rápido o suficiente através do bico, a tensão superficial do material o tornará coagular em pequenas gotículas, o que tornará a extrusão desigual e deixará espaços entre as gotículas.
* A impressão de linhas mais finas aumentará consideravelmente o tempo de impressão.

*Não é aconselhável reduzir a largura das linhas abaixo de 60% do tamanho do bico ou acima de 150%.Nos dois casos, o material pode não ser suficientemente extrudado.*

Ajuste a largura das linhas para que elas se adaptem a um número suficiente de paredes
----
Ao imprimir objetos mecânicos que devem ser finos, mas sólidos, você enfrenta regularmente o problema de que sua parte não é um múltiplo líquido e regular da largura da linha.Se não for um ponto múltiplo, o Cura normalmente reduzirá o fluxo de certas linhas devido ao parâmetro [compensar os cavalos de parede](../shell/Travel_compense_overlapping_walls_vabled.md).Isso modifica o fluxo através do bico, o que prejudica a qualidade visual.Se for um múltiplo líquido da largura da linha, mas não um número de pares, uma das paredes será reduzida para 0.

A produção de contornos líquidos com linhas de pares pode tornar a impressão mais forte e mais bonita.Uma das principais habilidades de qualquer usuário especialista em cura é poder modificar a largura da linha para que o número desejado de contornos atenda à impressão.

![Largura da linha padrão, quando os contornos não são ajustados e certas linhas são mais espessas do que outras](../../../articles/images/line_width_fit_bad.png)

![Reduzir a largura da linha permite ajustá -la uniformemente](../../../articles/images/line_width_fit_good_small.png)

![Aumente a largura da linha também funciona](../../../articles/images/line_width_fit_good_large.png)

Mantenha o fluxo constante
----
As grandes flutuações de fluxo às vezes são problemáticas para impressoras FDM.A sala do bico mantém parte do material de pressão, que atrasa o fluxo real na saída do bico.Demora um pouco para que a taxa de fluxo aumente ou diminua.As impressoras equipadas com um sistema Bowden para fornecer o filamento também têm um efeito de mola no tubo de Bowden, o que piora ainda mais o efeito.Portanto, você receberá uma subestimação quando for para um fluxo mais alto e uma superextrusão quando for para um fluxo mais baixo.É por isso que é bom manter a velocidade o mais constante possível.

A largura da linha influencia muito o fluxo.É aconselhável manter as larguras de linhas próximas uma da outra e próximas ao tamanho do bico.Se a largura da linha for importante, você também poderá ajustar a velocidade de impressão para manter o fluxo mais constante.Isso melhorará a precisão dimensional da sua impressão.