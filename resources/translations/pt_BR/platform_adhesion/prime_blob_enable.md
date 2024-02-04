Ative a queda de preparação
====
Quando ativado, essa função permite que a Cura envie um pedido para a impressora para preparar, pouco antes da extrusora ser usada pela primeira vez.A impressora começa criando uma pequena gota de material na bandeja de impressão.

O priming principal visa garantir que o material flua corretamente.Se a queda de queda não for ativada, a impressora começará a criar a saia ou a borda.Esta é a principal razão para usar a saia, mas para uma borda, reduzirá ligeiramente sua força de aderência.

O efeito desse ajuste no código G é que o Cura colocará o comando M280 em um determinado local.** Atualmente, isso está trabalhando apenas em impressoras Ultimaker do Ultimaker 3 ** porque elas são as únicas a implementar o comando M280.Para outras impressoras, o parâmetro não será visível.