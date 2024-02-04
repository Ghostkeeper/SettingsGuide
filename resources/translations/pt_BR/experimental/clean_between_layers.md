Limpe o bico entre as camadas
====
Esse ajuste possibilita executar um procedimento no final de cada camada para limpar todo o material do bico do bico.Se a sua impressora estiver equipada com um pincel de limpeza integrado, a ativação deste parâmetro levará à cura para pedir à impressora para limpar periodicamente a ponta deste pincel.

![Visualização dos movimentos do procedimento de limpeza](../images/clean_between_layers.svg)

Este procedimento de apagamento inclui uma série de etapas:
1. Se [retração for ativada](wipe_retraction_enable.md), o material será retraído.
2. Se o [Z Jump for ativado](wipe_hop_enable.md), o bico será movido para cima ou a bandeja de impressão para baixo.
3. O bico é movido além da [posição do pincel](wipe_brush_pos_x.md).
4. O bico é limpo [um certo número de vezes](wipe_repeat_count.md) no pincel.
5. O bico é reduzido à sua posição inicial.
6. O Z Jump está terminado, se tiver sido ativado.O material se destaca.
7. Impressão termina para um [determinado período](wipe_paux.md).

O objetivo deste procedimento é limpar periodicamente o bico de detritos.Alguns materiais tendem a voltar ao bico por capilaridade devido a uma alta tensão superficial.Esses materiais podem se infiltrar na cabeça de impressão e se acumular lá, o que pode levar à ruptura da cabeça de impressão.Outros materiais que contêm fibras ou outras cargas podem causar o spray de carga no bico durante a impressão.Essa ação possibilita limpar este material.