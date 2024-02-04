Rebocar
====
Quando a impressora terminar de imprimir parte de uma camada e deve mudar para outra parte, deve interromper temporariamente a extrusão.Se o material continuar fluindo enquanto se move, uma extremidade de plástico será disparada entre as duas partes.Isso é chamado de filass.

![Linhas de plástico finas são visíveis para o local onde o bico se moveu de um para outro](../../../articles/images/stringing.jpg)

Freqüentemente, os fios estão alinhados um no outro, porque o bico completa uma sala no mesmo local em cada camada.Isso cria uma tira vertical.O plástico adicional também pode se acumular nas cordas das camadas anteriores, o que dá às bolas plásticas em todos os lugares.

Filass às ​​vezes é acompanhado por um subestimado.O treinador geralmente começa com o princípio de que nenhum material é perdido durante a viagem e, portanto, pede à impressora que extrate material suficiente para imprimir sua próxima parte.Se o material escapar do bico durante um deslocamento (que fornece um fio), esse material não será usado para imprimir a próxima parte, o que leva a uma subestimação neste local.O filass normalmente não é um problema se ocorrer dentro do enchimento, mas se a fiação for muito extrema, pode representar um problema mesmo neste local, porque leva a uma subestusão depois.

Causas
----
Filasses ocorre porque o material escorrendo do bico durante um movimento de viagem.Embora a impressora não coma material novo durante um deslocamento, o fluxo do material não para imediatamente.Durante a impressão, há uma certa pressão dentro da sala do bico causada pelo filamento que acumula uma certa força como mola.Quando o bico se move no ar, essa pressão pode ser liberada, empurrando involuntariamente o material para fora do bico.

Mesmo que o material seja retraído antes do deslocamento, ainda haverá material dentro da sala dos bicos.Isso acontece porque o material neste bico está em fusão.Remover -o de um lado não volta o líquido.A menos que seja solidificado, um cabo de material derretido permanece no bico.Durante uma viagem, essa bola escorre do bico se for líquida o suficiente.

Prevenção
----
A retração é a principal técnica para evitar o filass.Se você vir traços de tópicos em suas impressões, aqui estão algumas coisas que você pode tentar:
* Certifique -se de que [a retração seja ativada](../Travel/retraction_nable.md).Leva um pouco mais de tempo de impressão, mas reduz consideravelmente o número de threads.
* Reduza a [temperatura da impressão](../material/material_print_temperature.md).Isso torna o material menos líquido, o que o torna menor que o bico.Isso também permite retrações mais eficazes, porque uma parte maior do material será sugada da sala de bicos.
* Se o seu material for viscoso, o aumento na [velocidade de retração](../Travel/retraction_speed.md) geralmente reduzirá o filasse para movimentos curtos, exercitando uma sub-pressionamento na sala de bicos.Essa pressão reduzida mantém o material sugado por dentro, para que não escorra para fora.
* Para viagens longas, o aumento da [distância de retração](../Travel/Retaction_amount.md) mantém o material em um local mais frio durante o movimento, reduzindo assim a velocidade à qual o material derrete e escorre do bico.
* Às vezes, o Cura tenta impedir o desgaste do filamento, limitando o número de retrações em um certo comprimento de filamento.Como não há retrações naquele momento, ele produzirá um fio como um mal necessário, em vez de falhar na impressão.Se sua extrusora não usar muito o material, você poderá aumentar o [número de retrações autorizadas](../Travel/Retaction_Count_Max.MD) ou reduzir o [comprimento do filamento](../Travel/Retaction_extrusion_Window.md) de longo que ele tem essas retrações.
* Se permitirmos [Detours Mode](../Travel/Retaction_Combing.md) no preenchimento do preenchimento, o bico passará dentro do modelo em vez de fora.Isso realmente não impede a fiação, mas o tornará invisível colocando -o dentro do modelo.
* Se tivermos [otimizarmos a ordem de impressão das paredes](../shell/otimize_wall_printing_order.md), o bico se moverá com menos frequência de uma sala para outra, o que reduzirá a quantidade de.
* O aumento da [velocidade de movimento](../Speed/Speed_Travel.md) geralmente torna possível diminuir os fios durante viagens mais longas.Para viagens curtas, isso realmente não faz diferença, pois os limites de aceleração das impressoras impedem que o bico atinja essas velocidades.
* A impressão com um bico menor também reduzirá normalmente o número de fios.É mais fácil para o plástico esclarecer um bico maior.