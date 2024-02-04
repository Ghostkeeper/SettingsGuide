Posição de ruptura retraída
====
Para algumas impressoras, quando um material é retraído para um interruptor de filamento, o material deve ser cortado corretamente para passá -lo para o carregador sem ficar emaranhado.Essa configuração configura parte do procedimento para quebrá -lo corretamente.

Essa configuração regula a terceira posição na qual o material é retraído para quebrar definitivamente a queda da queda, o que inevitavelmente permanece no bico.Embora a queda no bico não possa ser removida por causa de seu estado de fusão, a parte que é retirada não deve ter um fio fino no final, porque pode estar preso no carregador.Essa retração final quebra o filamento, mas com um pouco de sorte, ela quebra de maneira limpa, graças às duas etapas anteriores.

![Primeiro, o material é retraído para parar de escorrer](../../../articles/images/filament_switch_anti_ooze.svg)

![Segundo, o filamento é retraído lentamente para puxar um fio fino que é fácil de quebrar e deixar este fio solidificar](../../../articles/images/filament_switch_break_preparation.svg)

![Terceiro, o filamento é rapidamente retraído mais para quebrá -lo](../../../articles/images/filament_switch_break.svg)

** Atualmente, este parâmetro nunca está visível na interface da cura.Só pode ser definido por perfis.Nem é usado por Cura durante o corte.No entanto, as impressoras que incluem o formato do arquivo de hardware de cura podem usá-lo para configurar corretamente o procedimento de alteração do filamento ** graças a um script pós-processamento, o comando "M600" pode ser inserido na impressão, que desencadeará uma mudança de filamento.