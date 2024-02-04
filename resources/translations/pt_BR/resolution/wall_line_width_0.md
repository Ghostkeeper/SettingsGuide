Largura da linha da parede externa
====
A largura da linha de parede externa pode ser ajustada separadamente da das paredes internas.Esse ajuste indica a largura da linha de parede externa.

![O contorno da parede externa é muito mais largo que o resto](../../../articles/images/wall_line_width_0.png)

Sabemos que a redução da parede externa para uma largura de linha ligeiramente menor que o tamanho do bico é benéfico para a resistência.O bico extrudará um pouco menos material, mas sua abertura se sobreporá à parede interna adjacente.O material é então empurrado pela parede anteriormente colocada em seu local correto.Mas isso também permitirá que o plástico se mostre melhor com as paredes adjacentes.Assim, a parede externa se funde melhor com as paredes internas, para que possam combinar suas forças.Isso melhora consideravelmente a resistência das paredes.

A redução na largura da linha de parede externa também permite que o bico imprima detalhes mais finos, porque a linha mais fina se adaptará melhor a pequenos detalhes.

O aumento da largura da linha de parede externa pode reduzir o tempo de impressão.Você pode obter uma parede de espessura semelhante com menos paredes internas.A resistência ainda será um pouco reduzida porque a parede externa não se fundirá tão bem com as paredes internas.

Ajuste as linhas
----
Ao imprimir peças finas, ajustar a largura das linhas de parede é uma ferramenta importante para obter peças precisas e sólidas.A Cura nunca desenha apenas contornos completos; portanto, se um contorno não for adequado, um espaço cairá nas paredes, o que compromete bastante a solidez e a precisão da sala.

Cura tentará preencher essas lacunas entre as paredes se [preencher os orifícios entre as paredes](../shell/FILL_PERIMETER_GAPS.MD) for ativado, mas essa técnica está longe de ser ideal para formas arbitrárias e geralmente leva muito tempo a imprimir .Quando duas paredes se sobrepõem, a função [compensa para cavalos de parede](../shell/Travel_compense_overlapping_walls_nabled.md) reduz a largura da linha de parede para garantir que a parte seja dimensionalmente, mas isso causa alterações no fluxo qualidade e resistência da impressão.

Para um ajuste ideal, a sala deve ser um múltiplo exato da largura da linha de parede, para que as paredes se adaptem precisamente à sala.Se você conhece a largura do seu quarto, isso pode ser feito facilmente ajustando a largura das paredes.Você primeiro vê quanto contornos deseja ajustar para que as linhas ainda tenham uma largura razoável.Em seguida, você pode ver quanto precisa ajustar a largura das linhas das paredes para que as linhas se ajustem corretamente.Lembre -se de que você pode ajustar a [largura da linha da parede externa](Wall_Line_Width_0.md) e a [largura da linha da (s) parede (s) interna (s)](Wall_Line_Width_X.MD) separadamente.Corporativo O número de vezes que cada tipo de parede será desenhado para prever o efeito da modificação da largura da linha de parede.

O ajuste das linhas de parede é uma competência importante para a impressão 3D, que distingue especialistas em operadores de impressoras 3D de outras pessoas.Alguma prática é necessária.