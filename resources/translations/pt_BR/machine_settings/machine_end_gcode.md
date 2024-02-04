Código G da extremidade
====
Com este parâmetro, é possível escrever o código G que será executado no final de cada impressão.Graças a este código G, a impressora pode desligar seus componentes e limpar após a impressão.

Aqui estão alguns exemplos de coisas que geralmente são executadas no código G final:

* Retração de arame.
* Esfriar os bocais (s).
* Resfriamento da bandeja de impressão.
* Desligue os fãs.

Para uma lista bastante completa dos códigos G disponíveis que você pode escrever aqui, consulte [Reprap Wiki](https://reprap.org/wiki/G-Code).

Referências a parâmetros
----
Quando você altera o código G final, você pode consultar os valores de outros parâmetros.Isso usa uma certa sintaxe.Os parâmetros são designados por sua chave *.Esta chave é um nome interno em Cura.Não é visível na interface do usuário.Para obter uma lista completa de todas as teclas, consulte [Este documento](https://github.com/ultimaker/cura/blob/master/resources/definitions/fdmprinter.def.json) no código -fonte da cura.

A sintaxe para obter o valor de um parâmetro global é o seguinte:

`{Setting_key}` (chave de ajuste)

Em outras palavras, escreva a chave para o local entre parênteses.Assim, você obterá o valor geral de um ajuste.No entanto, muitas configurações podem ser diferentes para cada extrusora.Eles devem ser referenciados da seguinte maneira:

`{Setting_key, #}`

Aqui, no lugar do símbolo "#", você deve escrever o número da extrusora cuja configuração deseja obter.As extrusoras começam a contar a partir de 0. As configurações globais também podem ser obtidas especificando uma extrusora, mas serão as mesmas para todas as extrusoras.Quando você tenta obter uma temperatura específica para uma extrusora sem especificar o número da extrusora, você obtém o valor da primeira extrusora que não é desativada.

Por exemplo, você pode usar essas referências para resfriar a uma temperatura de espera, ou restaurar a aceleração e o jato padrão da impressora.Aqui estão alguns exemplos :

`M104 t0 s {material_standby_temperature, 0}; stand-by para a próxima impressão`

`M104 t1 s {material_standby_temperature, 1}`

`M204 P {MACHINE_ACCELATION} T {MACHINE_ACCELEANÇA}`

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
<!-endif->

*Este parâmetro é um parâmetro da máquina, portanto, não aparecerá na lista normal de parâmetros.Ele pode ser modificado indo para a lista de impressoras na tela de preferência e clicando em "Configurações da máquina".*