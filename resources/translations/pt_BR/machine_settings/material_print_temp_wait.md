Aguarde o aquecimento do bico
====
A camada inicial pode ter uma [camada inicial de temperatura de impressão](../material/MATTERSIAL_PRINT_TEMPERATURA_LAYER_0.MD) diferente da [temperatura de impressão padrão](../material/MATHIAL_PRINT_TEMPERATURA.MD).Se esse parâmetro for ativado, a impressora esperará até que essa temperatura seja atingida antes de continuar a impressão.

Ele esperará que a temperatura seja aquecida ou resfriada na temperatura apropriada.Embora o rótulo deste parâmetro indique que ele esperará para ser aquecido, ele também esfriará.O bico não espera outras mudanças de temperatura, como [temperatura inicial de impressão](../material/material_initial_print_temperature.md), [temperatura final de impressão](../material/material_final_print_temperature.mdd) ou [temperatura de espera](../Material/MATTERSIAL_STANDBY_TEMPERATURA.MD).Se a impressão for causada no modo de impressão [um de cada vez](../Blackmagic/print_sequence.md), o bico também aguardará a temperatura da camada inicial a ser alcançada quando precisará retornar à primeira camada Para os seguintes objetos.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de configurações.*