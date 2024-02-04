Temperatura de ruptura
====
Para algumas impressoras, quando um material é retraído para um interruptor de filamento, o material deve ser cortado corretamente para passá -lo para o carregador sem ficar emaranhado.Essa configuração configura parte do procedimento para quebrá -lo corretamente.

Esse ajuste define a temperatura na qual deve ser fria antes de cortar o filamento.Esse resfriamento ocorrerá entre o segundo e o terceiro passo (como mostrado nas imagens abaixo).O objetivo é permitir que o filamento endureça, o que permite que a impressora o quebre corretamente, em vez de esticá -lo em uma fita longa que poderia se levar no carregador.

![Primeiro, o material é retraído para parar de escorrer](../../../articles/images/filament_switch_anti_ooze.svg)

![Segundo, o filamento é retraído lentamente para puxar um fio fino que é fácil de quebrar e deixar este fio solidificar](../../../articles/images/filament_switch_break_preparation.svg)

![Terceiro, o filamento é rapidamente retraído mais para quebrá -lo](../../../articles/images/filament_switch_break.svg)

** Atualmente, este parâmetro nunca está visível na interface da cura.Só pode ser definido por perfis.Nem é usado por Cura durante o corte.No entanto, as impressoras que incluem o formato do arquivo de hardware de cura podem usá-lo para configurar corretamente o procedimento de alteração do filamento ** graças a um script pós-processamento, o comando "M600" pode ser inserido na impressão, que desencadeará uma mudança de filamento.