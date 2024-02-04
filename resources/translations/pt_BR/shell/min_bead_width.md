Largura mínima da linha de parede fina
====
Este parâmetro permite imprimir detalhes muito pequenos com uma largura de linha que é realmente grande demais para eles.Em vez de imprimir linhas muito finas, ele imprime com uma largura de linha mais razoável.

Se o [tamanho mínimo das entidades](min_feature_size.md) for muito baixo, as peças muito finas poderão ser impressas.Não funciona bem.É possível imprimir linhas menores que o tamanho do bico, mas não muito.A impressão de linhas muito finas leva à extrusão incoerente.

Em vez disso, essas linhas muito finas são mais amplas para que sejam extrudadas de maneira mais coerente.Qualquer parte do modelo mais fina que a largura mínima da linha de parede fina será impressa usando uma única linha da largura mínima da linha de parede fina.As linhas se tornam mais largas que a largura original do modelo.Isso reduz a precisão dimensional, mas pelo menos a impressão será confiável.

O valor desse parâmetro deve corresponder à melhor largura da linha que a impressora pode alcançar de maneira confiável antes de começar a criar superfícies grosseiras e extrusão inconsistente.Esse valor é normalmente entre o tamanho do bico e a metade do tamanho do bico.Aumentar isso leva à impressão de partes finas muito grandes, mas reduz o risco de subestusão devido à impressão de linhas muito finas.