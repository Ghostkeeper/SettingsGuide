Comprimento da purga do material
====
Se a impressora precisar alterar o filamento que passa por um certo bico, deve evacuar os restos da matéria que ainda estavam na sala do bico.Esse ajuste determina a quantidade de material usado para enxaguar o assunto anterior.

Isso só se aplica quando você vai a outro tipo de material.Se o mesmo tipo de material for recarregado (por exemplo, porque a bobina anterior estava vazia), é usado um [comprimento diferente](material_end_of_filament_purge_length.md).

** Atualmente, este parâmetro nunca está visível na interface da cura.Só pode ser definido por perfis.Nem é usado por Cura durante o fatiamento.No entanto, as impressoras que incluem o formato do arquivo de material de cura podem usá-lo para configurar corretamente o procedimento de alteração do filamento ** por um script pós-processamento, o comando `m600` pode ser inserido na impressão, o que desencadeará uma mudança de filamento.