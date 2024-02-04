Sempre escreva a ferramenta ativa
====
Este parâmetro indica como certos comandos do código G com um parâmetro de ferramenta são interpretados pela impressora.Alguns comandos do código G podem incluir um parâmetro para indicar a que a extrusora se aplica.Alguns microprogramas interpretam esse parâmetro como uma ordem que permite que essa ferramenta vá e, em seguida, execute o código G, enquanto outros interpretam esse parâmetro como um comando que permite aplicar o código G a uma extrusora diferente daquele que está atualmente ativo.

As únicas ordens a que isso se aplica e que são relevantes para a impressão 3D são os controles de aquecimento do bico, "M104" e "M109".Veja o exemplo a seguir de um comando de aquecimento, executado enquanto a primeira extrusora (`t0`) está sendo impressa:

`M104 S210 T1`

Existem duas interpretações possíveis desta ordem:
* Ao continuar a imprimir na primeira extrusora, comece a aquecer a segunda extrusora a 210 ° C.É a interpretação escolhida por Marlin, Reprap, Sailfish e seu software derivado.
* Comece passando a segunda extrusora e depois aqueça a segunda extrusora a 210 ° C.É a interpretação do Smoothiewe e seus microprogramas derivados.

Devido à estratégia de regulação da temperatura da cura, nunca é necessário executar a segunda interpretação.Se a impressora interpretar o comando G-Code da segunda maneira, a Cura escreverá o seguinte código G no lugar:

`M104 S210 T1`

`T0`

Ela sabe essencialmente que a impressora irá para a segunda extrusora por causa dessa ordem e, portanto, deve voltar à primeira extrusora para continuar a imprimir.

** Como este é um parâmetro da máquina, ele não aparecerá na lista padrão de parâmetros. **