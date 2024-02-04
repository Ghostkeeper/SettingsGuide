Impressão desagradável
====
Às vezes, uma impressão não termina completamente.Várias razões podem explicar esse fenômeno, algumas das quais podem ser resolvidas ajustando os parâmetros da cura.

![O filamento parou de fluir no meio desta impressão](../../../articles/images/unfinished_print.jpg)

Falhas das impressoras
----
Às vezes, a causa da impressão inacabada é uma falha na impressora, quando a impressora não faz o que é esperado dela.Em geral, Cura não pode fazer muito para remediar esses problemas.Aqui estão algumas causas comuns.
* Falta de energia.O Cura não pode fazer muito a respeito, se não imprimir mais rápido para reduzir o risco de falha de energia durante a impressão.
* Fonte de energia.Se uma das temperaturas (a [bandeja](../material/material_bed_temperature.md) ou o [ruído](../material/material_print_temperature.md)) for muito alto, algumas impressoras têm um modo de falha onde a energia Queimaduras de fornecimento ou sensores de temperatura dão erros.A impressora sai e não acaba com a impressão.
* O microprograma congela.Devido aos barramentos de microprograma, a impressora não pode mais responder.Se você puder determinar onde, no código G, ele congela (na maioria das vezes no início ou no final da impressão), poderá ver qual código g é a causa.É possível que o código g de partida ou final seja ajustado.
* A bobina do filamento está emaranhada.É uma boa idéia * sempre * manter a ponta do filamento se não estiver bem fixada na extrusora ou envolvida em um dos orifícios da tempestade do filamento (se sua bobina tiver esses orifícios).Se você deixar ir e o final do filamento saltar novamente na bobina, ele poderá deslizar sob um dos outros enrolamentos e ficar emaranhado.Como o filamento geralmente tem centenas de metros de comprimento, esse nó pode ser muito difícil de desenrolar se chegar.

Moagem de filamento
----
A extrusora às vezes empurra fortemente o filamento para transmiti -lo no trem da extrusora.Isso danifica o filamento.Quando o dispositivo de alimentação empurra e muitas vezes puxa o mesmo pedaço de filamento, isso pode danificar tanto que o dispositivo de energia não pode mais ter um filamento.O material então para de fluir e o restante da impressão está impresso vazio em vez de plástico.

![O filamento foi cortado pela extrusora](../../../articles/images/grinding.jpg)

Você pode sentir que isso acontece durante a impressão colocando um dedo na abertura onde o filamento entra na extrusora.Durante a impressão, você deve sentir o movimento do filamento.Se ele não se move, provavelmente ela esmagou o material e que ela não tem uma captura nele.Você também pode tirar o filamento da impressora e ver onde ela está danificada.

Para evitar esse problema, você pode fazer as seguintes configurações nas configurações de cura:
* Reduza a [Remoção máxima](../Travel/Retraction_Count_Max.MD) ou aumente o [intervalo de distância mínima de extrusão](../Travel/Retaction_extrusion_Window.md).Isso limitará o número de retrações feitas durante a extrusão de um determinado comprimento de filamento.De fato, isso limita a frequência à qual o dispositivo de energia pode rolar na frente e nas costas em cada pedaço de filamento.
* Reduza a [Distância de Retracração](../Travel/Retraction_amount.md).Isso mais uma vez limitará o número de vezes que a extrusora voltará e voltando no mesmo pedaço de filamento.
* Reduza a [velocidade de retração](../Travel/retraction_speed.md)).Se o material se mover rapidamente, mas estiver entupido em qualquer lugar do caminho, a extrusora usará o material.Se o material se mover mais lentamente, há menos chance de que isso aconteça.
* Imprima mais lentamente, reduzindo a [altura da camada](../Resolução/Layer_Height.md), a [largura da linha](../Resolução/Line_width.md) ou [Speeds](../Velocidade/speed_print.md)).Isso reduz a força que a extrusora deve exercer sobre o filamento, o que reduz o risco de desgaste do filamento.

