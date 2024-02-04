Ative o escudo
====
Quando esse parâmetro é ativado, a impressora constrói um envelope ao redor da impressão que a protege das correntes de ar do meio ambiente.

![Uma tela é impressa em torno do modelo](../../../articles/images/draft_shield_enabled.png)

Algumas impressoras e certos materiais de impressão são muito sensíveis ao ambiente em que são impressos.A impressão em diferentes lugares na bandeja de impressão pode levar a resultados diferentes, porque são mais sensíveis às correntes de ar do lado de fora.Se a impressão for deixada no caminho durante a noite e a sala esfria, ela pode ter um impacto significativo na impressão.A tela visa reduzir esse efeito, criando um pequeno volume isolado em torno da impressão.Este serve como uma "sala aquecida" de fortuna para manter a impressão quente e protegê -la do ar frio vindo de fora.

A tela é impressa no local como a impressão do modelo.Se várias extrusoras estiverem envolvidas na impressão, a tela será impressa usando a extrusora que inicia a camada.Isso alternará de uma camada para outra.

A tela tem vários efeitos principais na impressão:
* Mantém a temperatura de impressão mais constante.Este é o efeito desejado da tela.Portanto, as bandas devido a variações de temperatura na sala devem ser reduzidas.
* Em geral, a temperatura dentro da tela é maior do que se não houvesse tela.De fato, o calor tem mais dificuldade em escapar e não pode haver convecção atual que sobe com o ar quente da impressão.Isso afeta todos os aspectos da impressão.Em particular, haverá mais cordas e subsidência.
* Os ventiladores da cabeça de impressão serão menos eficazes.O escudo também interrompe a circulação do ar lá.Para aumentar a eficiência dos ventiladores na cabeça da impressão, a [Distância](Draft_Shield_Dist.MD) da tela pode ser aumentada.
* A tela pode ser dobrada como [Escudo anti-umidade](../dual/ooze_shield_enabled.md).Se os movimentos forem feitos em direção a um objeto protegido por uma tela, qualquer restante no bico será limpo na tela.
* A tela pode servir como [torre de amorcação](../dual/prime_tower_enable.md).Como é impresso antes do objeto, a impressão da tela é uma maneira de purgar o material e fazê -lo fluir corretamente.No entanto, esse método é eficaz apenas com duas extrusoras, porque nem todas as extrusoras são purificadas se houver mais de duas.