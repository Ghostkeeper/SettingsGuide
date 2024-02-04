A mudança de camada
====
Um layout de camadas ocorre quando as camadas de uma impressão não são empilhadas adequadamente.Se a cabeça de impressão for movida durante a impressão de uma camada por qualquer motivo, a impressora continuará imprimindo com uma lacuna.O lado superior da impressão é então compensado da parte inferior.

![Uma única descarga de camada devido a obstrução](../../../articles/images/layer_shift_single.jpg)

Causas
----
As mudanças nas camadas estão em duas formas.

O primeiro tipo de mudança de camada é causado pela obstrução da cabeça de impressão em algum lugar a caminho.Isso faz com que uma camada seja deslocada para um local localizado durante a impressão.Isso pode ser devido ao fato de o usuário colocar algo dentro do pórtico durante a impressão, ou quando a cabeça da impressão atinge outro objeto durante a impressão em [um de cada vez](..../blackmagic/print_sequence.md).Se a cabeça de impressão colidir com um objeto e não conseguir se mover, os motores tomam alguns passos.Se a impressora não conseguir detectar que isso aconteceu, simplesmente continuará sem o conhecimento desse erro, mudando o restante da impressão.

Outro tipo de mudança de camada ocorre quando a própria tarefa de impressão requer uma força excessiva na cabeça da impressão, o que significa que as etapas da impressora perdem as etapas.Sempre que as etapas são perdidas, a impressão é compensada a partir daí.Em geral, os passos perdidos ocorrem no mesmo local em cada camada devido a um canto particularmente pontudo.O resultado é que toda a impressão ou uma certa parte parece tendenciosa.

Prevenção
----
O primeiro tipo de deslocamento da camada não é normalmente corrigido pelas configurações de cura.O Cura foi projetado para evitar atingir as laterais do volume de impressão.Se o tamanho do volume de impressão for inserido corretamente na cura, não deve gerar código G, que se move para fora do volume imprimível.Se gerar um código G, a caixa de diálogo Configurações da máquina em Gerenciamento de impressoras permitirá ajustar o tamanho do volume de impressão para fazer uma correção.Você também deve garantir que não haja obstrução no volume de impressão de que a cabeça de impressão ou o sistema de movimento possa tocar durante a impressão.As impressoras geralmente não podem detectar esse tipo de problema e, portanto, continuarão imprimindo a partir de uma posição incomum.Encontre se houver cabos que incomodam e certifique -se de que todos os cabos sejam longos o suficiente para permitir que a impressora se mova em toda a sua praia de movimento.Verifique também se os drivers de etapa -passo da placa de circuito de impressão da impressora não estão superaquecendo, o que pode levar a uma parada temporária de sua operação.

O outro tipo de mudança de camada, aquele que ocorre continuamente por toda a impressão, é provavelmente devido a uma força excessiva exercida no seu sistema de movimento.Existem várias soluções possíveis.

Você deve primeiro examinar seu equipamento.Os cintos estão apertados?Caso contrário, você pode procurar uma maneira de apertá -los.Algumas impressoras têm motores com uma posição ajustável que permite apertar os cintos.As polias deslizam?Aperte os parafusos das polias para ter certeza.Finalmente, um problema elétrico comum é que os motores não recebem corrente suficiente para gerar forças fortes o suficiente para fazer uma guinada apertada.Nesse caso, verifique se a fonte de alimentação é suficiente.

Se o material funcionar bem, você também poderá ajustar a cura para que as viagens de hardware sejam mais fáceis.Aqui estão algumas configurações que você pode ajustar:
* Diminua [taxa de formas](../speed/jerk_print.md).Ele desacelerará a cabeça da impressão antes de fazer os cantos.Isso torna a passagem nos cantos mais flexível, suavizando a área em vez de fazer uma guinada apertada.
* Diminuição [taxa de aceleração](../speed/aceleração_print.md).A cabeça da impressão diminuirá mais e mais antes de fazer uma curva (a velocidade com que a cabeça de impressão passará pelo topo da curva não será afetada; esse é o objetivo do ajuste da aceleração).
* Diminuir [velocidade de movimento](../speed/speed_travel.md).Isso reduz a força com a qual o bico esfrega nas peças já impressas.
* Ative o [ZO Shift durante uma retração](../Travel/Retraction_hop_nabled.md).Isso impede que a cabeça de impressão atinja as peças impressas anteriormente se elas excederem um pouco para cima devido a manchas ou deformações.

