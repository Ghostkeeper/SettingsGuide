Posição anti-suntory retraída
====
Para algumas impressoras, quando um material é retraído para um interruptor de filamento, o material deve ser cortado corretamente para passá -lo para o carregador sem ficar emaranhado.Essa configuração configura parte do procedimento para quebrá -lo corretamente.

Esse ajuste ajusta a primeira posição na qual o material é retraído para impedir que ele escorra.O material ainda não foi quebrado nesta fase.O objetivo é apenas remover rapidamente a pressão na sala do bico puxando -a para dentro.

![Primeiro, o material é retraído para parar de suar, de acordo com esse ajuste](../../../articles/images/filament_switch_anti_ooze.svg)

![Segundo, o filamento é retraído lentamente para puxar um fio fino que é fácil de quebrar e deixar este fio solidificar](../../../articles/images/filament_switch_break_preparation.svg)

![Terceiro, o filamento é rapidamente retraído mais para quebrá -lo](../../../articles/images/filament_switch_break.svg)

** Atualmente, este parâmetro nunca está visível na interface da cura.Só pode ser definido por perfis.Nem é usado por Cura durante o corte.No entanto, as impressoras que incluem o formato do arquivo de hardware de curva podem usá-lo para configurar corretamente o procedimento de alteração do filamento ** graças a um script de pós-processamento, o comando "M600" pode ser inserido na impressão, que desencadeará uma mudança de filamento. * *