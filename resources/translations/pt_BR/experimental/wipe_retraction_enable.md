Ativação da retração de limpeza
====
Se esse parâmetro for ativado, o material será retraído durante todo o procedimento de limpeza.Este parâmetro pode ser configurado separadamente de [retrações normais](../Travel/retraction_nable.md).

O procedimento de limpeza significa que o bico vai para o lado da impressora, se move para frente e para trás e depois retorna à sua posição inicial.É essencialmente uma viagem muito longa.Como esse movimento é maior que os movimentos médios de movimento durante toda a impressão, você pode desejar que o material seja retraído durante esse procedimento, mesmo que as retrações sejam normalmente desativadas.

A retração do material reduzirá a quantidade de material que escorre durante o procedimento de limpeza.O material que escorre durante o procedimento de limpeza normalmente será limpo pelo pincel.No entanto, este material é então perdido.Consequentemente, haverá uma certa subestusão logo após o final da limpeza, porque esse material apareceu em vez de ser colocado em seu local correto.

Por outro lado, a retração pode demorar um pouco e causar desgaste desnecessário do filamento.Se a subestusão não for um problema, a retração desativada pode economizar tempo e melhorar a confiabilidade.Isso pode funcionar corretamente se, por exemplo, o [preenchimento for impresso antes das paredes](../preenchimento/refill_before_walls.md), porque uma certa subestusão durante o enchimento não é realmente um problema.