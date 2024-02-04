Sequência de impressão
====
Quando vários modelos são colocados na bandeja de impressão, isso determina a ordem em que as camadas desses objetos são impressas.Existem duas opções:

Tudo ao mesmo tempo
----
Todos os objetos serão impressos ao mesmo tempo, o que significa que as camadas serão impressas de baixo para cima para todos os objetos ao mesmo tempo.Imprimiremos uma camada de cada objeto antes de alternar para a próxima camada.

Isso tem duas grandes vantagens:
* A camada anterior tem mais tempo para esfriar, o que torna possível obter melhor qualidade ao imprimir pequenos objetos.
* O volume total pode ser usado para sua impressão.

Um por vez
----
Os objetos serão impressos um a um, o que significa que eles imprimirão todas as camadas de um objeto e depois retornarão à bandeja de impressão para imprimir o seguinte objeto.

As principais vantagens deste modo são as seguintes:
* Se a impressão falhar por qualquer motivo, todos os objetos que foram concluídos antes da falha são bastante utilizáveis.
* Menos viagens são necessárias para mudar de um modelo para outro.Isso economiza um pouco de tempo de impressão e reduz o número de cicatrizes na superfície onde o bico está fora e entrou no objeto.

No entanto, esse modo é acompanhado por algumas restrições, a fim de impedir que a cabeça e o pórtico colidam com o modelo.
* Você não pode imprimir objetos superiores do que a altura da pórtica da sua impressora.A altura do pórtico pode ser ajustada na caixa de diálogo Configurações da máquina de impressora.Essa altura do pórtico indica a distância vertical entre a ponta do bico e o sistema que carrega a cabeça de impressão.O motivo dessa limitação é que a cabeça de impressão terá que descer ao conjunto de impressão para imprimir o segundo objeto.Isso significa que o primeiro objeto pode ser afetado pelo pórtico quando o segundo objeto é impresso.Em teoria, o último objeto impresso pode ser autorizado a ser maior que o pórtico, mas, para simplificar, o Cura não o permitirá de qualquer maneira.
* Os objetos devem estar mais distantes um do outro, para impedir que a cabeça da impressão atinge os modelos anteriormente impressos no lado.
* A ordem em que os objetos são impressos é corrigida e otimizada para permitir que os objetos sejam impressos mais próximos um do outro.Se a sua cabeça de impressão não for simétrica, isso pode economizar muito espaço no conjunto de impressão.

** Um de cada vez está disponível apenas em extrusão simples.Se você usar uma impressora de múltiplas Extrusão, deve desativar todas as extrusoras, exceto uma para que este parâmetro apareça. **

