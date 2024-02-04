Cicatriz
====
Quando uma pegada tem uma grande parte superior plana, há um risco de cicatrizes.É o caso quando há uma linha claramente visível na parte superior da impressão, que não pertence ao motivo normal.Essa linha marca a superfície superior, também lisa, da impressão.

![Uma cicatriz diagonal na superfície](../../../articles/images/scarring.jpg)

As cicatrizes são criadas pelos movimentos de movimento que atravessam a superfície superior.O bico quente abrange a superfície, cortando a parte do plástico, derreta levemente outros plásticos e possivelmente escorrendo um pouco mais de material nas fendas.A cicatriz é puramente visual.Não há diferença significativa na força ou precisão da impressão.No entanto, se uma cicatriz for criada na primeira camada, o atrito poderá destacar sua camada da bandeja de impressão.

Prevenção
----
Para evitar cicatrizes, você deve impedir que o bico raspa a superfície superior.Você pode evitar a superfície superior horizontalmente (desvio), verticalmente (deslocamento Z) ou evitar qualquer movimento nele.
* Se você definir o [Modo Detours](../Travel/Retraction_Combing.md) em "Não Edans the Camada Externa", o bico evitará acertar a pele durante uma viagem.Ao mover um modelo, ele só pode atravessar o recheio e as paredes.Como não atravessa a pele, você não deve ter cicatrizes.No entanto, se o movimento translacional começar ou terminar na pele ou quando não houver caminho disponível sem tocar a pele, o movimento da tradução será reto sem tocar em nada e, de preferência, ele também se retrairá.
* Ative [Zea Shift durante uma retração](../Travel/Retraction_hop_nabled.md) para que o bico eleve levemente antes de passar pela superfície.Isso manterá uma certa distância entre o bico e a superfície, para que o bico não esfregue.Isso também evita uma cicatriz.Se você usar um modo de contorno, o bico primeiro tentará evitar a pele horizontalmente.Se não houver rota disponível, ela se retrairá e mudará em Z posteriormente.
* Às vezes é possível evitar um deslocamento ou garantir que um deslocamento cruze apenas parte da pele que ainda não foi impressa, simplesmente ajustando a [direção da linha acima/abaixo](../top_bottom/skin_angles.md ).O Cura controlará as linhas para minimizar o tempo de viagem, mas não fornece muito controle sobre esse comando.Ao girar as linhas da pele ou girando o modelo, todas as linhas se ajustam de maneira diferente, a ordem de impressão será diferente e isso torna os movimentos diferentes.Pode não ser mais necessário fazer uma viagem.No entanto, é um processo de testes e erros.