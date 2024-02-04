É a origem do centro
====
Se esse parâmetro for ativado, a coordenada 0.0 da impressora será definida para estar no meio do volume de construção, e não no canto dianteiro esquerdo.

Em algumas impressoras, o microprograma considera que a coordenada 0.0 está no centro do volume de construção.Isso é comum para impressoras do tipo delta, que geralmente têm volumes de construção cilíndricos e não cúbicos.

Se a coordenada zero da impressora estiver no centro, o código final G conterá coordenadas negativas e detalhes de contato positivos.A origem das coordenadas estará no meio do volume de construção de cura.Cura também exibirá seu marcador de coordenação tricolor no centro.No entanto, os detalhes de contato dos arquivos 3MF sempre serão tratados como se a origem das coordenadas estivesse no canto dianteiro esquerdo da impressora, pois o formato de arquivo 3MF exige.

*Como é um ajuste da máquina, normalmente não será listado na lista normal de configurações.No entanto, existe uma caixa de seleção para este parâmetro na caixa de diálogo Parâmetros da impressora, que está na lista de impressoras adicionadas na caixa de diálogo Preferência.*