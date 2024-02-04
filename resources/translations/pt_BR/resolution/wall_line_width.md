Largura da linha da parede
====
A largura das paredes das paredes pode ser ajustada separadamente do restante da impressão.Essa configuração indica a largura das linhas individuais das paredes.

![As linhas para as paredes são muito mais largas que as demais](../../../articles/images/wall_line_width.png)

Sabemos que a redução das paredes para uma largura de linha ligeiramente menor que o tamanho do bico é benéfico para a resistência.O bico extrudará um pouco menos material, mas sua abertura se sobreporá às linhas de parede adjacentes.O material é então empurrado pela parede anteriormente colocada em seu local correto.Mas isso também permite que o plástico se mostre melhor com as paredes adjacentes.Isso permite que as paredes se fundam melhor para que possam combinar sua força.Isso melhora consideravelmente a resistência das paredes.

Reduzir a largura da linha de parede também permite que o bico imprima detalhes mais finos.A [largura da linha de parede externa](Wall_line_width_0.md) é particularmente importante para essa propriedade.

O aumento na largura da linha de parede pode reduzir o tempo de impressão.Você precisará de menos linhas de parede para obter peças de força semelhantes.A resistência ainda será um pouco reduzida porque as paredes adjacentes não se fundirão tanto.

Ajuste da linha
----
Ao imprimir peças finas, definir a largura da linha de parede é uma ferramenta importante para peças específicas e sólidas.O Cura nunca desenha apenas contornos completos; portanto, se um contorno não for adequado, um espaço cairá nas paredes, o que compromete bastante a resistência e a precisão da sala.

Cura tentará preencher esses espaços entre as paredes se [encher os espaços entre as paredes](../shell/FILL_PERIMETER_GAPS.MD) for ativado, mas essa técnica está longe de ser ideal para formas arbitrárias e geralmente leva muito tempo .Quando duas paredes se sobrepõem, a função [compensa as paredes das paredes](../shell/Travel_compense_overlapping_walls_enabled.md) reduz a largura da linha de parede para garantir que a parte seja dimensional precise, mas que causa alterações no fluxo de alterações que também Reduza a qualidade e a resistência da impressão.

Para um ajuste ideal, a sala deve ser um múltiplo exato da largura da linha de parede, para que as paredes se adaptem precisamente à sala.Se você conhece a largura do seu quarto, isso pode ser feito facilmente ajustando a largura das paredes.Você primeiro vê quanto contornos deseja ajustar para que as linhas ainda tenham uma largura razoável.Em seguida, você pode ver quanto precisa ajustar a largura das linhas das paredes para que as linhas se ajustem corretamente.Lembre -se de que você pode ajustar a [largura da linha de parede externa](Wall_Line_Width_0.md) e a [largura da linha de interno (s)](s)](Wall_line_width_x.md) separadamente.Corporativo O número de vezes que cada tipo de parede será desenhado para prever o efeito da modificação da largura da linha de parede.

O ajuste das linhas de parede é uma competência importante para a impressão 3D, que distingue especialistas em operadores de impressoras 3D de outras pessoas.Alguma prática é necessária.