Áreas proibidas
====
Essa configuração indica as áreas da sua bandeja de impressão, onde a cabeça de impressão não pode ir.O usuário não tem permissão para colocar objetos nessas áreas ou perto deles a ponto de permitir a impressão de algo (como uma borda).

Essas áreas proibidas são necessárias para impedir que a cabeça de impressão colidte com objetos.Por exemplo, pode haver um pincel de limpeza ao alcance da cabeça de impressão em algum lugar ou de uma câmera que esteja um pouco longe demais dentro do volume de construção.Se o usuário tivesse que imprimir muito perto desses objetos, a cabeça de impressão colidiria com eles.Na melhor das hipóteses, você receberá uma [colocação de fraldas](../Solução de problemas/Layer_shift.md).Na pior das hipóteses, você danificaria a cabeça de impressão ou qualquer outro objeto com o qual a cabeça de impressão colidisse.

As áreas proibidas são representadas por uma sombra cinza na placa de impressão, indicando ao usuário que ele não pode colocar nenhum objeto lá.Essas sombras podem ser estendidas em todas as direções para impedir que a fronteira ou a saia tocasse e por vários outros motivos.Também existem outras áreas cinzentas na bandeja impressa, por exemplo, para limitar a amplitude do movimento se os bicos forem compensados.

Se apenas o bico ativo deve colidir com os obstáculos, o ajuste semelhante [zonas proibidas para imprimir bicos](bico_disallowed_areas.md) poderá impedir que o bico coloque com ele enquanto permite que a cabeça de impressão se mova acima.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de configurações.*