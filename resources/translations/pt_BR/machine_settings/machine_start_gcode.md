Iniciar o código G.
====
Com este parâmetro, é possível escrever um pequeno código G que será executado no início de cada impressão.Graças a este código G, a impressora pode ser configurada para estar pronta para a impressão.

Aqui estão alguns exemplos de coisas que geralmente são executadas na partida G-Code:
* Impressão dos bocais (s).
* Aquecimento da bandeja de impressão.
* Aquecimento do (s) bico (s).
* Verifique se a boa extrusora está selecionada.
* Configure fãs, acelerações ou idiotas.
* Nivelamento automático da bandeja.
* Configure o avanço linear.

Para uma lista bastante completa dos códigos G disponíveis que você pode escrever aqui, consulte o [reprimprap wiki](https://reprap.org/wiki/G-Code).

Referências a configurações
----
Quando você altera o código de partida G, você pode consultar os valores de outros parâmetros.Isso usa uma certa sintaxe.Os parâmetros são designados por sua chave *.Esta chave é um nome interno em Cura.Não é visível na interface do usuário.Para obter uma lista completa de todas as teclas, consulte [Este documento](https://github.com/ultimaker/cura/blob/master/resources/definitions/fdmprinter.def.json) no código -fonte da cura.

A sintaxe para obter o valor de um parâmetro global é o seguinte:

`{Setting_key}` (chave de ajuste)

Em outras palavras, escreva a chave para o local entre parênteses.Assim, você obterá o valor geral de um ajuste.No entanto, muitas configurações podem ser diferentes para cada extrusora.Eles devem ser referenciados da seguinte maneira:

`{Setting_key, #}`

Aqui, no lugar do símbolo "#", você deve escrever o número da extrusora cuja configuração deseja obter.As extrusoras começam a contar a partir de 0. As configurações globais também podem ser obtidas especificando uma extrusora, mas serão as mesmas para todas as extrusoras.Quando você tenta obter uma temperatura específica para a extrusora sem especificar o número da extrusora, você obterá a configuração padrão da impressora padrão, antes que um perfil de material ou qualquer coisa seja aplicado (já que os materiais são específicos para a extrusora).

Você pode usar essas referências, por exemplo, para pré -aquecer na temperatura certa ou para ajustar as acelerações.Aqui estão alguns exemplos :

`M104 s {material_print_temperature_layer_0, 0}; pré -flafage`

`M140 s {material_bed_temperature_layer_0}; platô de motorista`

`M204 p {aceleração_print, 0} t {aceleração_travel, 0}`

`M205 x {jerk_print, 0}`

Preste atenção às velocidades.O código G normalmente aceita a velocidade de avanço em milímetros por *minuto *, enquanto as configurações são indicadas em milímetros por *segundo *.Não é possível selecionar a velocidade de avanço correta no momento.É impossível fazer cálculos nessas referências.

Outra informação
----
Pela mesma sintaxe que as referências aos parâmetros, certas informações auxiliares também estão disponíveis:

* `{Time}` Referência à hora local atual do dia em que foi cortada.
* `{Data} Consulte a data em que foi cortada.
* `{dia}` refere -se no dia da semana em que foi cortado.
* `{Initial_ extruder_nr}` Consulte a extrusora com a qual a impressão será iniciada.
<!-se Cura_version> = 4.12->
* `{Material_id}` Consulte um identificador exclusivo do material ativo.Especifique a extrusora da mesma maneira que os outros parâmetros.
* `{Material_name}` Referência ao nome da matéria ativa.Geralmente, esse é o nome que você verá em um site vendendo este material.
* `{Material_type}` Referência à classe de material ativo, como PLA ou ABS.
* `{Material_brand}` Referência ao fabricante de material ativo.
* `{print_time}` Consulte a duração estimada da impressão (formatada de acordo com a ISO-8601).
* `{filamento_amount}` refere -se ao comprimento do filamento usado, em metros, para cada extrusora separadamente.É formatado na forma de uma lista com ganchos ao redor.
* `{filament_weight}` Designa o peso do filamento usado, em gramas, para cada extrusora separadamente, formatada como uma lista com ganchos.Se o peso da bobina for desconhecido, o valor será 0.
* `{filamento_cost}` Consulte o custo do filamento usado, para cada extrusora separadamente.A unidade de custo é a mesma indicada na página de gerenciamento de materiais em preferências.Se for desconhecido, será igual a 0.
<!-endif->

Aquecimento antes da inicialização do código G
----
O Cura emite automaticamente os controles de aquecimento antes do início do seu código G inicial.Dessa forma, seu código G inicial não deve levar em consideração o fato de que o bico deve esquentar.Você pode começar imediatamente a iniciar o bico.Se o seu código G de inicialização contiver uma referência a qualquer temperatura (para o bico ou a bandeja), ela será desativada (para o bico ou a bandeja, respectivamente).

*Essa configuração é uma configuração da máquina, portanto, não aparecerá na lista normal de configurações.Ele pode ser modificado indo para a lista de impressoras na tela de preferência e clicando em "Configurações da máquina".*

