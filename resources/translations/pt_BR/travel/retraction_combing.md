Modo Detours
====
O desvio é um método de calcular as trajetórias que consistem em evitar atravessar as paredes da marca durante uma viagem de um lugar para outro.A travessia das paredes tende a deixar uma cicatriz na superfície onde um bico quente sai ou entrou no volume da impressão, o que geralmente é indesejável.

Somente o desvio significa que o bico evita as paredes quando atravessa o interior do recheio.No entanto, isso também torna possível usar a função [Evite as peças impressas durante a viagem](Travel_avoid_Other_Parts.md), que permite que o bico evite objetos quando estiver fora do volume impresso.

![Divisão Desativada, o movimento de deslocamento atravessa as paredes da impressão](../../../articles/images/retraction_combing_off.png)

![Desvio ativado, é feito um desvio para evitar atravessar as paredes](../../../articles/images/retraction_combing_on.png)

Se houver um caminho através do objeto do início ao fim sem atingir a parede, esse caminho será seguido sem fazer a retirada.Se os locais de partida e chegada estiverem localizados em trajetórias completamente separadas, o bico primeiro passará para a posição em que as duas partes estão mais próximas uma da outra, então acabará retrando (se [as retrações forem ativadas](retraction_enable.md)), Vai passar para a trajetória alvo, acabará se retrando e depois passará pela nova parte para o seu destino final.Em ambas as partes, isso evitará bater nas paredes ao se mover para dentro.Durante uma viagem de uma sala para outra, ele apenas evitará as peças se o parâmetro [Evite as peças impressas durante a viagem](Travel_avoid_other_Parts.md) for ativado.

O objetivo do modo de desvio é evitar passar pelas paredes do objeto, reduzindo a quantidade de cicatrizes na superfície.Ele também reduzirá o spray visível do lado de fora, porque durante a viagem, sempre terá sucesso, mas essa suintração é colocada dentro do modelo.No entanto, o modo de desvio também aumentará o comprimento do movimento do movimento.Às vezes você tem que fazer um grande desvio.

Existem quatro opções no menu Drop -Raplow para este ajuste:
*** desativado **: O modo de desvio está desativado.As viagens sempre serão diretamente em direção ao seu destino.Se ele não tocar em nenhuma parede, ele não se retrairá.
*** tudo **: O bico toca qualquer parede quando se move dentro da impressão, conforme descrito acima.
<!-se Cura_version> = 4.12-> ** Não na superfície externa **: Além de ignorar as paredes, o bico também evitará a camada mais alta e mais baixa da pele.Essas são camadas visíveis onde você pode ver uma cicatriz na superfície se o bico passou nela.Se não for possível evitar a superfície, será feita uma retração.
*** Não na pele **: O bico evitará tocar a pele, se possível.Embora essa opção esteja sempre disponível em versões antigas do Cura, causa retrações desnecessárias e viagens mais longas do que a opção não na superfície externa, porque evita camadas de pele, mesmo que a cicatriz não seja visível para fora. <!-endif- >
<!-Se Cura_version <4.12-> ** não na camada externa **: O bico também evitará tocar a pele, se possível.Isso pode reduzir as cicatrizes na face superior da impressão, fazendo o bico correr ao longo das paredes, em vez de cortar a pele.No entanto, em alguns casos, o bico não será capaz de escapar e terá que se retrair, caso contrário, teria cortado a pele. <!-endif->>
*** dentro do recheio **: o modo mais rigoroso de todos, que apenas permite o desvio através do recheio.Isso evita marcar as paredes internas e as paredes externas e também evita marcar a pele.Se o bico tocar nas paredes interiores, às vezes pode ser visível do lado de fora, porque seu raio externo pode ser mais largo que as paredes.Isso evita esse efeito.No entanto, será necessário fazer ainda mais retrações, porque muitas vezes não haverá passagem.