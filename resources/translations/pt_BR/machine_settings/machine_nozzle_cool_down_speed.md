Velocidade de resfriamento
====
Esse ajuste indica a cura a velocidade com que seu bico esfria quando não é aquecido.É usado para prever quando é necessário iniciar a pré-refrescamento do bico antes de alterar sua extrusora.

![Os bicos estão começando a aquecer com antecedência antes de mudar sua extrusora](../images/temperature_regulation.svg)

Quando ele muda de extrusora, Cura começa a pré-reprimir o bico ativo antes de terminar, para que ela ganhe um pouco menos enquanto espera.O Cura também tentará prever a quantidade de resfriamento do bico quando estava inativo.Dessa forma, ele sabe quanto tempo precisará aquecê -la depois.

Se o bico esfriar efetivamente mais rápido que essa configuração indicada, o bico estará na temperatura de vigília mais rapidamente do que o Cura fornece.Consequentemente, o aquecimento do bico pode levar mais tempo do que o esperado pela Cura, e a impressora esperará, no nível da mudança do ruído, que aquece mais.

Se o bico esfriar mais lentamente do que essa configuração indica, é possível que ainda esteja quente quando o Cura envia um comando de pré -aquecimento, que o aquece muito rapidamente.Será a uma temperatura de impressão por um tempo antes que seja a virada do bico de impressão.Enquanto isso, isso ocupa um pouco mais e o plástico se degrada um pouco mais.

A velocidade real de resfriamento não é um nível constante em graus por segundo.Provavelmente dependerá da diferença entre a temperatura atual do bico e a temperatura do volume de produção.Assim, esfriará mais rápido quando estiver quente e mais lentamente quando se aproxima da temperatura de espera.Se você definir este parâmetro, tente ajustá -lo medindo o tempo de resfriamento entre a [Imprima a temperatura final](../MATEMCIAL/MATTER_FINAL_PRINT_TEMPERATURA.MD) e a [temperatura de espera](../material/MATHIAL_STANDBY_TEMPERATURA .MD).É a faixa mais importante que o Cura tentará prever.Para impressões pequenas, você pode aumentar ligeiramente a velocidade de resfriamento para ajustar a temperatura, para que ela permaneça quente com mais frequência.

*Como é um ajuste da máquina, esse ajuste normalmente não é visível na lista de parâmetros.*

