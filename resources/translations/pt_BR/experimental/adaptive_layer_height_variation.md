Variação máxima em camadas adaptativas
====
Com este parâmetro, você pode limitar o intervalo em que as camadas adaptativas estão autorizadas a modificar a espessura da camada.A altura da camada não deve se desviar mais dessa variação em relação à [altura da camada](../Resolução/Layer_Height.md)).

Por exemplo, com uma altura normal da camada de 0,15 mm e uma variação fixada a 0,1 mm, as camadas adaptativas podem produzir camadas de espessura entre 0,05 mm e 0,25 mm.

Esse ajuste limita a força de modificação da função "camadas adaptativas".Se a faixa de espessura da camada for muito estreita, a espessura da camada sempre estará muito próxima da espessura da camada original, conforme definido ajustando a altura da camada.As camadas adaptativas não farão muito para economizar tempo ou melhorar a qualidade.

No entanto, se o alcance for muito amplo, as camadas podem se tornar muito grossas ou muito finas.Camadas muito espessas requerem um fluxo significativo na saída do bico, o que nem sempre é possível devido ao tamanho limitado do bico e à capacidade de fusão do bloco de aquecimento na cabeça de impressão.Camadas muito finas nem sempre são possíveis devido à viscosidade do material ou à imprecisão do eixo z. Portanto, é bom limitar a praia na qual as camadas adaptativas podem ajustar a espessura da camada.Caso contrário, a impressora achará difícil atingir a espessura desejada da camada.

A espessura da camada nunca pode descer abaixo de 0,001 mm, mesmo que a praia permitir.