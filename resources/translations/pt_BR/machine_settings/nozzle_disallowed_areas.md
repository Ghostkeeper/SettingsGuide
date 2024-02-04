Áreas proibidas para imprimir bicos
====
Essa configuração indica as áreas da sua bandeja de impressão, onde o bico ativo não pode ir.O usuário não tem permissão para colocar objetos nessas áreas ou perto deles para impedir a impressão de algo (como uma borda).

Esse parâmetro se aplica apenas ao *bico ativo *, o que significa que você sempre pode imprimir objetos ao lado dessas áreas proibidas, mesmo que isso leve ao deslocamento de outros bicos nessas áreas proibidas.Assim, esse parâmetro é realmente realmente útil para impressoras que elevam bocais inativos ou estacionam -os fora do volume de construção quando estão inativos.Ao contrário de [áreas proibidas](Machine_Disallowed_AREAs.MD), essas áreas proibidas não são movidas de acordo com o atraso entre os bicos.

Essas áreas proibidas são necessárias para impedir que o bico colidam com objetos.Por exemplo, pode haver clipes na bandeja de impressão, ou um adesivo ou um logotipo.Se o usuário tivesse que imprimir muito perto desses objetos, o bico colidiria com eles.Na melhor das hipóteses, você receberá um [Shift de camada](../solucionando problemas/camada_shift.md).Na pior das hipóteses, você danificaria o bico ou qualquer outro objeto com o qual o bico colide.

As áreas proibidas são representadas por uma sombra cinza na placa de impressão, indicando ao usuário que ele não pode colocar nenhum objeto lá.Essas sombras podem ser estendidas em todas as direções para impedir que a borda ou a saia tocasse e por vários outros motivos.Existem também outras sombras no conjunto de impressão, por exemplo, para limitar a amplitude do movimento se os bicos forem deslocados.

*Como é uma configuração da máquina, esse ajuste normalmente não é visível na lista de configurações.*