Descascando
====
A descolagem é um problema com a impressão final, onde a impressão se enquadra após a impressão, deixando o objeto distorcido final.Geralmente, os cantos na parte inferior da impressão podem ser usados ​​para cima, ou partes finas da impressão se tornam onduladas.

![As pontas envolvem](../../../articles/images/warping.jpg)

Causa
----
O desapego é causado por uma combinação de efeitos, mas principalmente por uma restrição interna devido à tração do bico no plástico derretido.Quando em uma transição vítrea, o plástico se comporta um pouco como borracha ou gengiva.Se você atirar, o material se estende, mas se você parar de atirar, retoma sua forma inicial.O mesmo também ocorre durante a impressão.Ao imprimir uma linha longa, o bico puxa a linha de plástico, que se estende por cima do comprimento da linha.Quando o bico se afasta e para de puxar, a linha plástica se contrai.Essa contração causa uma tração em tudo o que se apega a ela.Quando um número suficiente de linhas plásticas se baseia em uníssono, elas podem distorcer a impressão.Isso é particularmente comum quando muitas linhas são paralelas, como na pele.

Um segundo efeito que causa desapego é o estreitamento do material quando esfria.A maioria dos materiais tende a encolher quando esfriar.Se o objeto esfriar de maneira não uniforme, certas partes da impressão encolhem mais do que outras, o que deforma o objeto.À medida que o objeto continua a esfriar, ele solidifica mais, o que bloqueia essa deformação permanentemente.

Alguns materiais são mais sensíveis ao estreitamento do que outros devido ao seu cristalino inerente.Aqui estão alguns materiais de estreitamento para materiais de impressão 3D atuais.Essa é aproximadamente a quantidade de estreitamento de cada tipo de material quando esfria sua temperatura de transição vítrea à temperatura ambiente.Uma certa variação ocorre entre misturas.Uma retirada maior causará maior esquerda.
* PLA: 0,21%.
* ABS: 0,70 %.
* TPU: 0,63%.
* Quadris: 0,64%
* PETG e CPE: 0,45%.
* Nylon: 0,62%
* PC: 0,70%.
* Pp: 1,2%

Além disso, o desapego pode ser evitado se outros materiais estiverem do outro lado da estrada.Se parte da impressão for completamente densa, o material circundante poderá retirar menos ou não.Se outras peças não forem completamente densas, você terá uma impressão parcialmente retraída.A parte retraída da impressão atirará no restante, o que também pode causar uma esquerda.Esse fenômeno é frequente na fronteira entre a pele e o recheio, porque a pele é completamente densa, mas o recheio não é.

O desapego é o mais frequente na parte inferior da impressão.É aqui que o gradiente de temperatura é o mais importante, porque o fundo da impressão é frequentemente aquecido por um leito aquecido e o restante da impressão não é.A parte inferior é geralmente composta de muitas longas filas de pele.Se o [Motivo inferior](../top_bottom/top_bottom_pattern.md) estiver definido como linhas ou zigue -zague, essas linhas são longas, retas e paralelas, o que lhes permite disparar em uníssono na mesma direção para deformar o objeto '.

Prevenção
----
* Se o destacamento ocorrer na parte inferior da impressão, ajuste a [camada inicial do padrão abaixo](../top_bottom/top_bottom_pattern_0.md) no concêntrico.Dessa forma, a contração do fundo da pele inferior não será feita em uníssono.A tensão interna será distribuída uniformemente dentro da camada inferior.Se isso não for suficiente para evitar a deformação, você também pode ajustar o modelo comum [padrão acima/abaixo](../top_bottom/top_bottom_pattern.md) no concêntrico.
* Para reduzir os gradientes de temperatura dentro da impressão, reduza a [temperatura da plataforma de impressão](../material/material_bed_temperature.md).O objeto deve esfriar de maneira mais uniforme.
* Dependendo do material da sua impressora, a impressão em uma sala aquecida fechada também pode impedir a esquerda.Por um lado, isso reduzirá a diferença de temperatura entre o volume de construção e a bandeja de impressão e a diferença entre o volume de construção e o bico.Isso também permitirá o plástico de [Recuire](https://en.wikipedia.org/wiki/annealing_%28glass%29) por mais tempo, reduzindo assim as restrições internas e, portanto, a tração das linhas impressas que causam a esquerda.Se a sua impressora permitir, lembre -se de aumentar a [temperatura do volume de impressão](../material/build_volume_temperature.md).
* Para impedir que a parte inferior se deforme, uma boa adesão da bandeja de impressão é útil.Isso aumenta a força necessária para que o material se deforme.Por exemplo, aumente a [largura da borda](../plataform_adhiction/brim_width.md) ou a [margem de jangada adicional](../plataform_adhiction/raft_margin.md).
* O uso de uma [jangada em vez de uma borda](../plataform_adhiction/aderence_type.md) remove a impressão direta na bandeja de impressão e coloca um pedaço de plástico entre a sala e a bandeja, projetada para resistir à esquerda -dendo -se .
* Tente imprimir [Ativando o escudo](../Experimental/Draft_Shield_enabled.md).Isso cria uma sala ao redor da impressão, o que impede que as correntes de ar externo resfriem sua impressão antes de terminar.No entanto, não se esqueça que o próprio escudo também pode se retrair.Se o escudo não funcionar, você poderá ver muitos filmes na sua impressão.
* A impressão é feita em um material que encolhe menos, como o PLA.
* Se você estiver livre para fazer ajustes no modelo impresso, tente evitar colocar cantos externos muito sofisticados na bandeja de impressão.Você pode optar por arredondar alguns cantos externos.Isso impede que toda a força da restrição interna se concentre em um ponto, reduzindo assim a probabilidade de deformação.