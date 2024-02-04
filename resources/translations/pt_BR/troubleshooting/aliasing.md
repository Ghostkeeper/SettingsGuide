Prato
====
Etapa -By -NeSep Motores ficam sem discretos.Sua capacidade de permanecer em posição entre essas etapas é limitada.O tamanho das etapas dos motores serve como um limite para a resolução que a impressora pode alcançar.Durante a impressão de paredes que estão quase, mas não exatamente, alinhadas no eixo x ou y, essa resolução às vezes resulta em um padrão de linha.

![O motivo de nicho aparecendo nas laterais deste objeto](../../../articles/images/aliasing.jpg)

A resolução de um mecanismo de etapa -passo em uma impressora 3D de consumo típica é de cerca de 50 a 200 etapas por milímetro.O tamanho de cada etapa é, portanto, cerca de 10 micrômetros.Se uma linha for desenhada quase em paralelo ao outro eixo, digamos a 0,5 ° da ortogonal, essa etapa ocorrerá todos 1,15 mm ao longo da linha.Esta etapa é por si só pequena demais para ser visível, mas as vibrações são visíveis, especialmente se ressoam com a frequência natural da estrutura.

Prevenção
----
Os motores PAS -by -Step podem escolher entre várias estratégias para administrar sua árvore, mas é um compromisso entre resolução, torque e ruído.Alguns microprogramas ajustam automaticamente esses parâmetros, dependendo da velocidade de movimento.Alguns microprogramas também permitem que você ajuste isso do código G. Por exemplo, o comando "M350" do código G pode ser colocado no código G de partida para configurá-lo manualmente.O Cura (atualmente) não possui um método para configurar isso automaticamente, dependendo da velocidade ou estrutura.

A maneira mais confiável de evitar esse fenômeno é, no entanto, ajustar o modelo para que a crenela não seja visível.Gire o seu modelo para que o efeito de alias não ocorra.Se o seu modelo apresentar uma parede reta, verifique se está completamente alinhado com os eixos ou inclinado por vários graus em comparação com ele.