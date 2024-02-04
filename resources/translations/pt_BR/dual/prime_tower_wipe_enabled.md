Limpe o bico de impressão inativo na torre inicial
====
Se essa função for ativada, a impressora limpa o bico anterior depois de iniciar o próximo na torre de priming.

A ordem dos eventos será a seguinte se esta opção for ativada:
1. A impressora vai para a nova extrusora.
2. A nova extrusora é iniciada pela impressão de uma torre de priming.
3. O bico que estava ativo antes da transição para a nova extrusora é limpada na torre de priming.
4. A impressora continua imprimindo a peça com a nova extrusora.

Observe que a impressora limpa o bico que estava ativo antes do início da extrusora, não o bico atualmente ativo.Se sua impressora tiver vários bicos com uma certa distância entre eles, você poderá ver um deslocamento para a camada que parece inútil.De fato, o movimento em direção a este local significa que o bico anterior se move acima da torre de priming (que não é representada em vista nas fraldas).

Quando um bico é colocado em espera, ainda está muito quente por um tempo.Enquanto estiver quente, alguns materiais tendem a escorrer.Ao iniciar o próximo bico na torre inicial, ela terá a chance de esfriar um pouco, o que terá diminuído a velocidade.Esse ajuste possibilita limpar a vazamento que passou no meio da torre de priming, para que ela não seja encontrada na lateral do seu modelo impresso.