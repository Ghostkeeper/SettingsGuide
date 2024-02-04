As extrusoras compartilham um bico
====
Com este parâmetro, você pode indicar que sua impressora possui apenas um bico e que todo o filamento é empurrado por esse mesmo bico.A Cura modificará sua estratégia de preparação.

Normalmente, o Cura assume que, após a execução do [código g de partida](MACHING_START_GCODE.MD), todas as extrusoras têm seu filamento no final do bico, pronto para serem impressas.Quando os extrusionantes compartilham um bico, isso não é possível porque um único filamento pode estar no bico por vez.Em vez do procedimento normal de iniciação com a [ativação da queda de preparação](../plataform_adhen/prime_blob_enable.md) ou linhas de saia adicionais, o bico deve começar como para uma mudança de extrusão completa.Isso implica a impressão na [Torre da Amorcação](../dual/prime_tower_enable.md), se for ativada.

Se todas as extrusoras compartilharem um único bico, é lógico que eles [compartilhem aquecimento](Machine_ Extruders_share_heater.md).No entanto, o Cura não link entre os dois, portanto, certifique -se de ativar se sua impressora tiver um único bico e um único elemento de aquecimento para todas as extrusoras.

** Como este é um parâmetro da máquina, normalmente não será listado na lista normal de parâmetros.No entanto, existe uma caixa de seleção para este parâmetro na caixa de diálogo Parâmetros da impressora, que está na lista de impressoras adicionadas na caixa de diálogo Preferências **.