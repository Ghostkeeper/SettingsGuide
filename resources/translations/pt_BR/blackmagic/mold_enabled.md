Mofo
====
Em vez de imprimir o próprio modelo, essa função leva a impressora para criar um negativo do modelo, um molde, no qual você pode afundar um material diferente para criar seu modelo.Este molde possui várias propriedades específicas que o tornam utilizável para moldar e imprimir com a impressão FDM.

![Um modelo que você gostaria de moldar](../../../articles/images/mold_enabled_shell.png)

![O molde para este modelo](../../../articles/images/mold_enabled_mould.png)

A geração de moldes de cura criará um buraco que você deseja moldar.Em torno deste buraco, uma concha será gerada com uma certa largura, configurável graças ao parâmetro [largura mínima do molde](mld_width.md).Acima e abaixo do molde, uma pele será gerada com uma certa altura, configurável graças ao parâmetro [altura do teto do molde](mold_roof_height.md).No entanto, essa pele não será gerada na parte superior do modelo para que você possa derramar o material de moldagem.Também não será gerado na parte inferior do modelo.Você deve mantê -lo na bandeja de impressão durante a moldagem.

Design do seu molde
----
A geração de molde de cura não é perfeita.Alguns elementos estão faltando.Aqui estão algumas dicas para corrigi -las.
* O Cura não cria cenouras para todos os máximos locais do seu modelo.Você deve adicionar hastes verticais ao seu modelo onde quer que precise de uma cenoura.
* O Cura não permite que material adicional flua caso seu material esteja se retraindo no resfriamento.Você deve adicionar hastes adicionais, mesmo no ponto mais alto do seu modelo, se você usar um material que encolhe muito.
* O molde da cura ainda está em uma peça.Para muitas formas, isso significa que o molde deve ser destruído para ser removido.Os moldes podem ser destruídos de maneiras diferentes: por força pura ou aquecendo -os se o material interno permitir ou usar um material como o PVA que se dissolve na água.
* Cura não permite que hastes ou fios fortaleçam o molde.Para fazer isso, coloque barras adicionais em seu modelo para que o Cura os deixe cavidades e, em seguida, insira o caule ou o fio.
* Os contra-relaxos em seu molde são gerados sem aviso prévio.Se o seu molde precisar de muita falsificação, você precisará de algumas cenouras ou outros canais para que o material o entre adequadamente e o ar.Observe também que seu molde pode precisar ser destruído para poder retirar a moldura depois de solidificada.

Materiais para imprimir o molde
----
O molde ideal é:
* Muito rígido
* Resistente a altas temperaturas
* inerte quimicamente para que não se ligue ao seu material de moldagem
* Não encolher

Além disso, alguns moldes devem ser destruídos para poder tirar o modelo.Para fazer isso, você pode escolher um material frágil ou um material que possa ser dissolvido usando água ou outros produtos químicos, como o PVA.

Materiais para usar para moldar
----
Ao escolher um material para fluir, lembre -se de que a impressão FDM pode funcionar apenas com termoplásticos.Os termoplásticos são plásticos que se tornam intrinsecamente macios a alta temperatura.Isso não é compatível com materiais de moldagem quentes no momento da moldagem.Alguns materiais geralmente são incompatíveis com moldes impressos em 3D:
*** metais **, que devem ser aquecidos acima do ponto de fusão dos plásticos para serem líquidos o suficiente para serem moldados.A massa térmica do metal derreterá seu molde.
*** plásticos que ligam ** plástico cujo molde é feito.Você não pode separar o molde do modelo após a moldagem.Você pode pulverizar um pouco desmontando, mas se o material for muito semelhante, ele sempre estará no molde permanentemente.
*** materiais que encolhem ** também depois de se solidificarem.Os materiais que se retraem antes da solidificação são aceitáveis, desde que você tenha cenouras por tempo suficiente para permitir que o novo material preencha a cavidade quando isso acontecer.
*** A resina epóxi ** não é apropriada porque, quando a resina está fria durante a moldagem, a reação química dos dois componentes emite calor suficiente para derreter o plástico.O epóxi também tende a aderir muito bem aos plásticos.

Alguns materiais são mais adequados para derramar:
*** Silicone **.O silicone não se liga aos plásticos, por isso é fácil de remover.O silicone também é muito flexível, o que o torna indulgente para os contra-delicilos.Além disso, os silicones são termodrusáveis ​​e resistentes ao calor, para que você possa considerar derreter o molde depois que ele foi endurecido.No entanto, é preciso uma ferramenta especial para fluir silicone.Em particular, você precisará de uma sala vazia para bombear as bolhas de gás do silicone.
* **Areia**.A areia é um padrão industrial para a fabricação de um negativo de algo porque é muito resistente ao calor, mas não precisa ser aquecido para ser afundado.Depois de afundá -lo, você pode vinculá -lo a concreto ou cola para impedir que ele desmorone.Você pode usá -lo para tornar outro negativo de um material mais resistente ao calor.
*** cera **.Para fazer velas ou estatuetas personalizadas, você pode fluir um modelo de cera.A cera tem uma temperatura de fusão baixa, não derrete o molde.Ela também não liga a cera.
*** Chocolate **, como um tratamento especializado ou presente especial.Para derramar o chocolate, derreta -o logo acima do ponto de fusão e despeje -o, faça com que ele vibre um pouco para tirar as bolhas de ar e colocá -lo imediatamente no freezer.Você pode até colocar o molde em um banho de água fria dentro do freezer para subtrair o calor mais rapidamente.Após cinco minutos, remova cuidadosamente o chocolate do molde.

Se você precisar criar um objeto em um material que não seja diretamente compatível com a impressão 3D, precisará trabalhar em várias etapas de moldagem.Cada etapa cria um negativo da etapa anterior.Por exemplo, você pode imprimir a forma do seu objeto normalmente (com este parâmetro desativado) e criar um negativo dele colocando o molde em um banho de estuque.Como o estuque é muito mais resistente ao calor, você pode usar materiais que devem ser aquecidos mais fortes para derreter, como bronze ou materiais que se ligam a plásticos como epóxi.

O processo de moldagem
----
A moldura com um molde impressa em 3D é amplamente o mesmo que com qualquer outro molde e depende muito dos materiais utilizados.No entanto, existem alguns pontos que merecem atenção especial quando se trata de mexilhões impressos em 3D.

O termoplástico com o qual você imprimiu seu molde tem uma baixa capacidade térmica e pode ter uma temperatura de transição vítrea bastante baixa.Isso significa que o tempo é um fator essencial após moldar o molde.Se o material esfriar muito lentamente, o molde poderá suavizar.Isso pode causar deformação do molde e dificultar o resultado do resultado.Para acelerar o plugue do molde, você pode mergulhá -lo em um banho de gelo.

Os moldes impressos em 3D também têm mais faixas do lado devido aos limites entre as camadas.Portanto, é mais difícil desmatar o molde.Se você usar um agente de demolição entre o molde e a parte moldada, use algo que possa preencher essas deficiências.Lubrificantes finos não são suficientes.As camadas de interface mais apropriadas são a cera ou lubrificantes mais espessos.