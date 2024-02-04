Flacidez
====
A fabricação de filamentos derretidos consiste em depositar uma linha plástica derretida.Essa linha é flexível e, se não for baseada em nada, ela se afasta.Isso é chamado de flacidez.

![Caído nas partes pendentes](../../../articles/images/sagging.jpg)

A Sussement tende a dar um aspecto pendente a uma parte pendente.Em vez de seguir suavemente a superfície planejada do modelo, ele será muito baixo.Em casos extremos, a parte inferior de uma superfície fica tão desfiada que pode ser vista o interior oco da sala.

Causas
----
A flacidez não é, de fato, ou mal causada pela gravidade.É causado principalmente pela força da matéria que é empurrada para fora do bico.Assim, mesmo as impressoras que são devolvidas ou que imprimem em microgravidade conhecerão esse fenômeno.A pressão pela qual o material é extrudado empurra o material para baixo porque o bico é (normalmente) orientado para baixo.

Normalmente, é necessária a pressão dentro da sala do bico para empurrar o material (viscoso) para o exterior e achatá -lo na forma de uma linha de material largo e plano, esmagando -o entre o bico e a camada anterior ou a bandeja de impressão.No entanto, se não houvesse material na camada anterior, não haverá uma contra -impressão para achatar o cordão.Em vez disso, será empurrado muito para baixo.

Ponte
----
Uma técnica para melhorar a qualidade das saliências é otimizar a maneira pela qual a lacuna pendente é preenchida.Isso envolve reduzir a pressão com a qual o material é empurrado para fora do bico, bem como tenta aumentar a viscosidade do material ou torná -lo solidificar mais rapidamente.Além disso, as linhas impressas podem ser redirecionadas para reduzir a distância na qual as linhas não são suportadas.Todas essas técnicas são chamadas de "ponte".

O Cura fornece um certo número de meios para melhorar a ponte.Ele fornecerá ainda mais se você tiver ativado os parâmetros da ponte](../Experimental/Bridge_settings_nabled.md).A ativação desta função aparecerá mais parâmetros e também ajustará os parâmetros de impressão para áreas de saliência.

Ao configurar a ponte para reduzir a flacidez, leve em consideração as seguintes configurações:
* Reduce a [temperatura da impressão](../material/material_print_temperature.md) torna os termoplásticos mais viscosos, o que reduz sua flacidez.
* Reduza a [altura da camada](../Resolução/Layer_Height.md) ou a [largura da linha](../Resolução/linha_width.m) reduz a pressão com a qual o material é empurrado para fora do bico.Por si só, isso reduz a flacidez, mas essas linhas também têm uma capacidade térmica mais baixa, tornando os ventiladores da cabeça de impressão mais eficazes para o resfriamento.
* A redução na [velocidade de impressão](../speed/speed_print.md) também reduz a pressão com a qual o material é empurrado para fora do bico.Nesse caso, a capacidade térmica não é reduzida, mas os ventiladores sopram o material por mais tempo, o que também aumenta sua eficácia e reduz a flacidez.Se os ajustes das pontes forem ativados, a velocidade de impressão das pontes poderá ser ajustada separadamente.Redução da [velocidade de impressão das paredes da ponte](../Experimental/Bridge_Wall_Speed.MD) é eficaz para melhorar as saliências.A redução da [velocidade de impressão da pele da ponte](../Experimental/Bridge_skin_speed.md) é eficaz na redução do colapso em áreas completamente horizontais.Há também uma variante que permite ajustar a [velocidade da parede de parede](../experimental/wall_overhang_speed_factor.md).Essa configuração é aplicada mesmo que a superfície não seja completamente horizontal, o que possibilita obter uma velocidade de impressão específica para paredes salientes, apenas para paredes inclinadas.
* A redução em [fluxo](../material/material_flow.md) é semelhante à redução na largura da linha.Isso reduzirá a pressão com a qual o material é expulso, bem como a capacidade térmica, o que permitirá que o material se solidifique mais rapidamente.Este parâmetro também pode ser ajustado apenas para zonas de ponte, separadamente para [Walls](../Experience/Bridge_Wall_Material_Flow.md) ou [Skin](../Experience/Bridge_skin_material_flow.md).A redução no fluxo em grandes superfícies tende a produzir espaços vazios e uma aparência irregular também, para que a saliência ainda possa ter um aspecto visual ruim se for alterado.No entanto, a precisão dimensional deve ser melhorada.
* Aumente a [velocidade do ventilador](../resfriamento/cool_fan_speed.md) para esfriar o material mais rápido.Isso solidifica o material mais rápido, impedindo que ele caísse.
* Imprima as paredes de [o interior para o exterior](../shell/outer_inset_first.md).Isso permitirá que a parede externa confie na parede interna adjacente, o que impedirá que ela caia.Este método é particularmente eficaz com uma pequena [largura da linha](../Resolução/Wall_line_width_0.md).

Apoiar
----
! [Uma estrutura de suporte suporta o modelo](../../../Artigos/Images/Support_able.png)

A maneira mais comum e confiável de melhorar as peças salientes é apoiá -las por uma estrutura de suporte durante a impressão.Essa estrutura de suporte é então removida após a solidificação do material.O suporte de impressão é muito eficaz na prevenção de flacidez, independentemente do tamanho da área de saliência, mas requer mais tempo e material e deixa uma cicatriz onde o suporte foi fixo.

<!-se Cura_version> = 4.7-> Cura tem duas técnicas para gerar um suporte.Existe um método padrão de "suporte à zona".Outro método de suporte à arorescente é gerado se o suporte à arborescente for ativado.A técnica padrão é geralmente mais eficaz na redução do colapso, mas às vezes também fornece um fundo mais irregular.O apoio à arorescente tende a deixar as cordas caírem um pouco mais, mas também mais regularmente. <!-endif->>
<!-Se Cura_version <4.7: Cura tem duas técnicas para gerar um suporte.Existe um método padrão de "suporte à zona", que é gerado se [o suporte for ativado](../support/support_nable.md).Outro método de suporte à arorescente é gerado se [o suporte à arborescente for ativado](../Experimental/Support_Tree_able.md).A técnica padrão é geralmente mais eficaz na redução do colapso, mas às vezes também fornece um fundo mais irregular.O apoio à arorescente tende a deixar as cordas caírem um pouco mais, mas também mais regularmente .-->

A geração de suportes de cura decidirá automaticamente onde colocar os suportes.Na maioria dos casos, funciona bem, mas para alguns modelos, o suporte pode não ser muito importante.Felizmente, a Cura também oferece muitos métodos para personalizar a colocação de suportes.
* O ajuste do [ângulo de suporte de suporte](../support/support_angle.md) é o método mais simples para ajustar a quantidade de suporte a ser colocada.Você deve ajustar este parâmetro para que todas as suas áreas de saliências sejam suportadas.Este parâmetro também determina as áreas que serão desenhadas em vermelho durante a fase de preparação.A redução no ângulo de saliência resultará na impressão de um número maior de suportes, o que reduzirá a flacidez de um número maior de peças de impressão, mas também levará mais tempo, matéria e matéria e causará mais cicatrizes.
* Você pode excluir as peças pendentes acima das outras partes, definindo o parâmetro [suporte de posicionamento](../support/support_type.md) em "Touch the Print Bandey".Se você preferir ajustar esse parâmetro em "Everywhere", pode evitar transbordamentos ruins.
* Certifique -se de que a [superfície mínima de suporte](../Support/Minimum_Support_ARea.md) não apagarem pedaços finos de suporte.
* Com a ferramenta de suporte do suporte, você pode colocar cubos em sua cena para evitar gerar suporte.Você também pode selecionar esses blocos e, na ferramenta de configurações do modelo, informar a Cura para "imprimir como suporte".Eles serão impressos como um novo suporte.Dessa forma, você pode personalizar cuidadosamente o local exato onde o suporte é colocado.Você pode até carregar um modelo 3D completo em Cura com a forma exata do seu suporte e dizer a Cura para imprimi -lo como um suporte na ferramenta de parâmetros por modelo.

Mesmo que a saliência seja apoiada pelo suporte, ela ainda pode ceder um pouco.Para permitir que o suporte seja removido, uma certa [distância z dos suportes](../support/support_z_distance.md) é mantida entre o modelo e o suporte.O modelo cairá a essa distância antes que o suporte seja eficaz; portanto, a redução na distância Z reduzirá a flacidez (mas tornará o suporte mais difícil de remover).Alguns materiais são projetados para serem removidos com mais facilidade, não se ligando quimicamente ao material de construção ou dissolvendo.Esses materiais podem se dar ao luxo de reduzir a distância z, o que reduz ainda mais a flacidez, permitindo que o suporte seja removido posteriormente.A impressão também pode entrar em colapso entre as linhas de suporte; portanto, a redução na [distância da distância do suporte](../support/support_line_distance.md) também reduzirá a flacidez (mas aumentará a impressão e tornará ainda mais difícil para retirar o suporte).

Adaptar o modelo
----
Se você tiver a liberdade de ajustar o modelo impresso, ele pode dar um resultado muito mais limpo do que tentar preencher as saliências ou apoiá -las.Em vez de deixar o material cair nas saliências, projete e orie seu modelo para que não haja saliências.

![Essa orientação possibilita imprimir o objeto com muito pouco suporte](../../../articles/images/support_minimise_overhang.png)

A dica mais básica para aplicar isso é executar o modelo.Se a sua impressora for capaz de imprimir ângulos de 45 graus sem cair, você pode girar um modelo com uma sala vertical e uma sala horizontal para que haja duas inclinações de 45 graus, o que reduz ligeiramente a qualidade da parede vertical, mas impede a queda da parte horizontal.No entanto, certifique -se de não fazer a área de contato com a bandeja de impressão muito pequena; caso contrário, a impressão poderá se destacar da bandeja de impressão e ainda ser danificada.

A adição de chanfros também pode ajudar a reduzir os excessos do modelo com relativamente pouco material adicionado.Cura oferece um método automatizado para adicionar chamfers ao seu modelo, graças ao parâmetro [Torne a excesso de impressão
](../experimental/conical_overhang_enabled.md).A adição de chamfers adiciona essencialmente a estrutura de suporte ao modelo real.Eles então serão transparentes no modelo, o que é mais bonito.Isso também salva o material, em comparação com a impressão do suporte, uma vez que o material de suporte rapidamente traz as forças ao restante do modelo.E no final, seu objeto será mais sólido.

Em geral, ao projetar objetos para a impressão 3D, é melhor evitar qualquer estouro.Se a geometria do objeto não permitir, considere dividir o modelo em várias partes e montá -las depois.