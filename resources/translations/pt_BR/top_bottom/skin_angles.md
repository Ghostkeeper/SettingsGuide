Sens da linha acima/abaixo
====
Este parâmetro permite modificar a direção em que as linhas de fundo e os resultados estão impressos.Você pode especificar uma lista de ângulos separados por vírgulas (em graus), e as linhas alternarão as direções por camada.

![Padrão de linha com ângulos de 0 °, 60 ° e 120 ° alternando](../../../articles/images/skin_angles.gif)

Por padrão, o padrão de linha é impresso nas duas direções diagonais.Para sistemas de portal cartesiano, é o mais preciso, porque a impressora pode usar os motores X e Y para acelerar o bico ao voltar para a próxima linha.

Pode haver várias razões para alterar essas direções:
* Para obter um efeito óptico.
* Para otimizar a força.A impressão normalmente será mais resistente quando submetida a um impulso e tração paralelamente às linhas da pele (e recheio).
* Para reduzir a saliência.Se uma impressão é muito boa em uma direção, fazer uma ponte de pele nessa direção pode ser uma maneira eficaz de economizar material sobre o preenchimento.Nenhum recheio será necessário para preencher a lacuna.Da mesma forma, você também pode escolher uma direção perpendicular ao recheio para minimizar o excesso no recheio.Isso fornece melhor qualidade da superfície.
* Para otimizar a precisão se a sua impressora não tiver um motor para a direção X e um motor para a direção D, como uma impressora com um gantry H ou uma impressora delta.

Vários números podem ser inseridos para alterar a direção de cada camada.Por exemplo, a entrada de `[0, 30, 60]` alternativa entre 0 grau de distância do eixo x, 30 graus de distância e 60 graus de distância.