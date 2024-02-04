Formato do código G.
====
Embora o código G seja um formato padronizado para a comunicação de instruções para máquinas de controle digital, como impressoras 3D, ainda existem algumas diferenças na maneira como os códigos G são suportados por cada impressora, em seu estado inicial e às vezes na maneira como eles interpretam ordens.Com o formato do código G, você pode indicar amplamente qual conjunto de pedidos que sua impressora aceita.

A diferença entre esses formatos de código G geralmente é bastante baixa.Os comandos mais importantes, como mover e aquecer o bico, são geralmente os mesmos.

Para selecionar o código G direito, consulte a documentação do firmware da sua impressora.Deve dizer quais funções são suportadas e quais não são.Estes são os formatos disponíveis em Cura e suas diferenças.

Marlin
----
Marlin é considerado o formato padrão do código G.Destina -se ao microprograma principal [firmware marlin](https://marlinfw.org/), que é o microprograma de impressão 3D mais popular e a base da maioria dos microprogramas alternativos disponíveis no mercado.

Marlin (volumétrico)
----
É uma variante do marlin, onde os controles de extrusão especificam a quantidade de extrusão em milímetros cúbicos, e não nos comprimentos dos filamentos.Estas são as mudanças notáveis:
* O parâmetro "E" do comando "G1" é calculado em milímetros cúbicos, o volume do plástico alimentado, em vez do comprimento do filamento para poder durante esse movimento.
* As estatísticas no início do Código G também mencionam o filamento usado em milímetros cúbicos.

Reprepiar
----
Este é um formato focado no suporte de impressoras, que provêm do [Projeto Reprap](https://reprap.org/wiki/reprap).Tem várias exceções notáveis:
* Sempre mencione a extrusora ao definir a temperatura da camada inicial, mesmo que haja apenas uma extrusora.
* Retorne à extrusão relativa após a impressão.
* Altere as acelerações usando os parâmetros "P" e "T" do comando "M204", para a aceleração de impressão e a aceleração do movimento, respectivamente, em vez da configuração "S".
* Altere o idiota usando o comando `M566 ', em vez do comando` m205'.

Ultimaker 2
----
Esse formato de código G é destinado ao Ultimaker 2. O firmware dessa família teve a estranha idéia de permitir que a impressora controlasse os ajustes ligados ao equipamento e não ao fatador.Estas são as exceções:
* Não haverá controle de temperatura de impressão no código G.
* Não haverá controle de temperatura da bandeja de impressão no código g.
* Não haverá controle de temperatura de construção no código G.
* O primeiro bico deve ter a [temperatura de impressão da camada inicial](../material/material_print_temperature_layer_0.md) quando a impressão começa.
* A bandeja de impressão deve ter a [temperatura da bandeja de impressão da camada inicial](../material/material_bed_temperature_layer_0.md) quando a impressão começa.
* O parâmetro "E" do comando "G1" é calculado em milímetros cúbicos, o volume do plástico alimentado, em vez do comprimento do filamento para poder durante esse movimento.
* Estatísticas no início do Código G mencionam o filamento usado em milímetros cúbicos.

Griffin
----
Esta é a versão G-Code das impressoras Ultimaker Modern, Ultimaker 3 e a mais recente.Essas impressoras requerem um conjunto de metadados em um determinado formato no início do cocodee G.As diferenças neste formato de código G são as seguintes:
* Há um cabeçalho grande no início do código G contendo informações sobre metadados, como a duração da impressão, o nome do trabalho de impressão e algumas informações práticas, como a temperatura inicial e a impressão da estrutura.
* Não haverá controles de temperatura de construção no código G.
* O primeiro bico deve ter a [temperatura de impressão da camada inicial](../material/material_print_temperature_layer_0.md) quando a impressão começa.
* A bandeja de impressão deve ter a [temperatura da bandeja de impressão da camada inicial](../material/material_bed_temperature_layer_0.md) quando a impressão começa.
* A impressora não deve começar na primeira extrusora, por isso sempre irá para a extrusora inicial no início da impressão usando um `t`r.
* Uma gota de primer é impressa com `g280` para cada extrusora quando começa a imprimir, em vez de retirada.

Makerbot
----
Este é um formato de código G para microprogramas com base em [Sailfish](https://www.sailfishfirmware.com/).Este microprograma é usado na geração de impressoras Makerbot originais.Algumas diferenças notáveis ​​devem ser observadas:
* Ao modificar a temperatura de impressão, "M109" (ajuste de temperatura e espera) não é suportado.Em vez disso, produz `m104 ', que não espera que a temperatura seja alcançada.Ele então usa o `M116 'para ordenar que a impressora aguarde que essa temperatura seja alcançada.
* A dimensão "E" do comando de extrusão "G1" não é redefinida durante a impressão.Para os outros sabores, esse parâmetro é redefinido a cada 10 metros de filamento por um comando `g92 e0`, para evitar erros de arredondamento em vírgula flutuante no firmware, mas não com ele.
* A mudança da extrusora é feita com o comando `M135 ', em vez de com os comandos t`.
* A velocidade do ventilador não está fora.O ventilador está funcionando completamente ou desligado.O Cura comandará a impressora para iniciar o ventilador se quiser uma velocidade de 50% ou mais.

Bits de bytes
----
É uma versão do código G para bits de bits de bytes que tinham seu próprio microprograma personalizado.Seu formato de código G difere consideravelmente dos outros.Essas são as mudanças que o Cura trará:
* As quantidades de extrusão são escritas usando o RPM do carregador em vez do parâmetro "E".
* As retrações são escritas com "M101" ou "M201", de acordo com a extrusora ativa.
* A velocidade de retração é gravada com um comando separado `m108 '.
* Os movimentos são indicados por um comando `m103`, em vez de substituir` g1` por `g0`.Não haverá comando "G0".
* A impressora está configurada para usar a retração automática usando o comando "M227".
* O Cura produzirá novas linhas de estilo Windows com um retorno de caminhão, em vez de um simples símbolo de nova linha.
* A dimensão "E" do comando de extrusão "G1" não é redefinida durante a impressão.Para os outros sabores, esse parâmetro é redefinido a cada 10 metros de filamento por um comando `g92 e0`, para evitar erros de arredondamento em vírgula flutuante no firmware, mas não com ele.

Mach3
----
É um formato de código G que se aproxima da maneira pela qual as máquinas CNC aguardam o código G Há apenas uma diferença notável:
* As quantidades de extrusão são escritas usando o parâmetro "A" do comando "G1", em vez do parâmetro "E".

Repetidor
----
Este é um formato de código G para repetidas impressoras 3D.Ele imita a saída do fator de repetição.Essas são as diferenças notáveis ​​com este formato de código G:
* Se as retrações de firmware forem ativadas, a retração de retração use "G10 S1" para indicar que é uma retração para um comutador de extrusão.
* As alterações de aceleração são feitas com os comandos "M201" e "M202" (para imprimir a aceleração e a aceleração do movimento) em vez de "M204".
* As alterações de aceleração são feitas usando o comando "M207" em vez do comando "M205".

*Como é uma configuração da máquina, normalmente não será listada na lista normal de configurações.No entanto, existe um menu de seleção para este parâmetro na caixa de diálogo Configurações da impressora, que pode ser encontrada na lista de impressoras adicionadas na caixa de diálogo de preferência.*