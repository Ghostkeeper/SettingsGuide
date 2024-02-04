Espessura da camada de enchimento
====
Como a altura da camada de enchimento não é importante para a qualidade visual, você pode usar camadas mais grossas para encher para reduzir o tempo de impressão.Essa configuração permite combinar camadas de preenchimento, desde que várias camadas de enchimento sejam sobrepostas diretamente.Em seguida, não imprimirá nenhum recheio em algumas das camadas, mas na maior das camadas combinadas, extrudará mais material para compensar.

Na visão das fraldas, será preso que as linhas de enchimento se tornassem muito mais largas.Quando impresso, as linhas de enchimento abaixam mais, em vez de esticar horizontalmente.

![A espessura da camada de enchimento é fixada em três vezes a altura da camada](../../../articles/images/infill_sparse_thickness.png)

A espessura da camada de enchimento deve ser um múltiplo da altura da camada comum.Caso contrário, será arredondado para a camada mais próxima.

* Cuidado para não aumentar demais.Ao ir para a camada de enchimento e vice -versa, o fluxo através do bico deve acelerar e desacelerar significativamente.Há um certo atraso nesse ponto, de modo que haverá muito pouca extrusão no início do enchimento e muita extrusão após o final do recheio.
* Nas camadas intermediárias, ele sempre imprimirá um recheio com uma espessura de camada mais baixa, onde não há preenchimento nas camadas ao seu redor.Isso pode levar à impressão de pequenas linhas de enchimento ao longo das paredes inclinadas.