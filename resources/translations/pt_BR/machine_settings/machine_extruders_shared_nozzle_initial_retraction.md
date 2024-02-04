Remoção inicial do bico compartilhado
====
Se as extrusoras de uma impressora [compartilham um bico](Machine_ extrushers_share_nozle.md), o Cura não assume que todas as extrusoras começarem com o filamento no final do bico.Este parâmetro indica a distância do bico que o filamento começa.O filamento pode começar a uma distância diferente da [distância de retração do interruptor do bico](../dual/switch_ extruder_retraction_amount.md) porque o filamento pode ser armazenado ainda mais enquanto a impressora estava inativa do que quando a extrusora está pendente durante a impressão.

![Distância do filamento inativo antes de imprimir](../../../articles/images/machine_extruders_shared_nozzle_initial_retraction.svg)

O Cura o usará para garantir que o filamento esteja no final do bico antes de lançar seu procedimento de preparação para a primeira mudança de extrusora.