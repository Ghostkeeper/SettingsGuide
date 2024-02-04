Padrão de suporte
====
Com este parâmetro, você pode escolher o modelo que será usado para preencher o volume da estrutura de suporte.Os diferentes modelos têm forças e fraquezas diferentes.

Linhe
----
! [Lignes](../../../artigos/imagens/support_pattern_lines.png)

As linhas das linhas traçam linhas retas.As linhas são orientadas para que nunca sejam perpendiculares às linhas da pele que ela deve suportar (por padrão).
* O mais fácil de remover do modelo de todos os padrões.Isso é muito útil se houver uma área pendente que esteja próxima da bandeja de impressão.Uma faca pode ser usada para cortar os restos, se necessário.
* Oferece a melhor qualidade de saliência de todos os modelos com Zigzag.As linhas estão muito próximas e orientadas para que não sejam perpendiculares à pele.
* As linhas tendem a ser instáveis ​​porque tendem a mudar.

Grade
----
! [Grille](../../../Artigos/Images/Support_pattern_grid.png)

A grade desenha dois conjuntos de linhas retas perpendiculares uma à outra.Eles se sobrepõem, formando um motivo quadrado.Por padrão, um perímetro é desenhado em torno desse motivo.
* Muito robusto, aumentando de maneira confiável.
* Oferece uma qualidade de saliência medíocre, porque as linhas estão bastante distantes uma da outra.
* Pode ser difícil de remover, porque o suporte não é flexível.

Triângulos
----
! [Triangles](../../../Artigos/Images/Support_pattern_triangles.png)

O padrão dos triângulos desenha três conjuntos de linhas retas, formando cantos de 60 graus entre eles, formando um padrão de triângulos equilaterais.Por padrão, um perímetro é desenhado em torno desse motivo.
* O mais forte de todos os modelos de suporte.
* Oferece baixa qualidade de saliência, porque as linhas estão muito distantes uma da outra.
* Pode ser difícil de remover, porque o suporte não será flexionado em nenhuma direção.

Concêntrico
----
! [Concentric](../../../Artigos/Images/Support_pattern_concentric.png)

O motivo concêntrico significa que o suporte consiste em anéis concêntricos regularmente espaçados de fora para dentro.
* As linhas são aproximadas entre si, o que possibilita apoiar as áreas salientes para obter uma superfície lisa, se as linhas forem orientadas perpendiculares.
* Muito sólido, porque os cachos individualmente têm uma grande largura para se levantar.
* Fácil de remover, porque a estrutura de suporte se dobra facilmente para dentro.
* Muitas vezes, ela acaba sendo paralela às paredes que deve apoiar.Isso leva a uma deterioração na qualidade da saliência, porque certas paredes não são de todo o apoio.
* Às vezes, o suporte é suspenso no ar.

Ziguezague
----
! [Zigzag](../../../Artigos/Images/Support_pattern_zigzag.png)

O padrão em zigue -zague é como a linha na linha, mas as linhas são conectadas às extremidades.
* Bastante robusto, o que aumenta consideravelmente a confiabilidade.
* Oferece a melhor qualidade de saliência de todos os modelos com as linhas.As linhas estão muito próximas e orientadas para que não sejam perpendiculares à pele.
* Fácil de remover.A estrutura de suporte se dobra para dentro e, puxando -a, o suporte sai em tiras.
* Quase sempre atrai o suporte para uma única linha, o que minimiza a necessidade de retração ou viagem.

Croix
----
! [Croix](../../../Artigos/Images/Support_pattern_cross.png)

O motivo cruzado desenha um padrão fracionário ao longo do volume com formas cruzadas.
* O mais fácil de dobrar de todos os padrões, porque não há linhas retas longas nesse padrão.
* O suporte quase sempre é desenhado em uma única rota, o que minimiza a necessidade de retração ou viagem.

<!-se Cura_version> = 4.1->
Gyroïde
----
! [Gyroïde](../../../artigos/imagens/support_pattern_gyroid.png)

O padrão de giroscópio é ondulado, com uma curva que vai e volta ao bico.O ângulo da curva varia de uma camada para outra.
* Modelo bastante robusto, o que aumenta a confiabilidade.
* O ar entre o suporte é um volume único.Durante a impressão com materiais de suporte solúvel, isso permite que o solvente (água, etanol ou outro) exceda dentro da estrutura de suporte, mesmo que haja uma borda abaixo.Isso permite que ele dissolva o suporte mais rapidamente.
* Suporta todas as linhas da saliência igualmente, qualquer que seja sua direção.
<!-endif->


