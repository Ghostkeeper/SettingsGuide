Extrusão relativa
====
Cura escreve instruções para que a impressora imprima seu objeto no código G.Essas instruções movem a cabeça de impressão em determinadas posições e a direção da extrusora.Cura normalmente registra as coordenadas da cabeça de impressão e a rotação da extrusora como coordenadas absolutas.No entanto, se esse parâmetro for ativado, as coordenadas da extrusora serão registradas relativamente.

Se esse parâmetro estiver desativado (ou seja, se a extrusão for absoluta), a posição do filamento no início da impressão será definida como zero coordenado.A posição do filamento aumentará em todo o arquivo à medida que o material for extrudado e o filamento terá que se mover cada vez mais do ponto de partida no início da impressão.

No entanto, se essa função for ativada, cada linha do Code-G terá sua extrusão escrita relativamente comparada à posição da linha anterior.Cada linha contém apenas a quantidade de material extrudado para essa linha específica.

A extrusão relativa facilita a edição do código G após sua geração.Se o material adicional deve ser extrudado em algum lugar entre os dois (para adicionar ou excluir segmentos de linha ou para ajustar os fluxos), a nova extrusão deve ser simplesmente escrita na parte que é editada.Se a extrusão absoluta for usada, a posição da extrusora deve ser redefinida usando "G92" posteriormente para garantir que todos os comandos subsequentes estejam corretos.

No entanto, se os erros de arredondamento forem introduzidos a qualquer momento no processamento do código do código (em cura, firmware ou movimento), a extrusão absoluta o corrigirá automaticamente na próxima linha.Em extrusão relativa, isso levará a uma extrusão excessiva ou uma subestusão, embora extremamente menor.

Nem todos os microprogramas da impressora suportam extrusão relativa.

** Quando a extrusão absoluta é usada, a cura sempre redefinirá a posição do filamento a cada 10 metros, a fim de evitar erros de arredondamento em vírgula flutuante no firmware. **


