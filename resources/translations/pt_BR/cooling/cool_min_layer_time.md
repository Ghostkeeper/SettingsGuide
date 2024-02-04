Duração mínima de uma camada
====
O tempo mínimo da camada configura a duração mais curta autorizada para imprimir uma camada.A impressora não tem permissão para imprimir fraldas mais rapidamente do que isso.

Isso é necessário para permitir que a camada anterior esfrie antes que a próxima camada seja colocada em cima.Isso torna possível garantir que a camada anterior tenha solidificado completamente, para impedir que ela caísse.

![Que velocidade de ventilação é usada](../images/cool_fan_speed.svg)

Esta opção tem três efeitos:
* Se uma camada imprimir mais rápido que indicar o parâmetro [Velocidade regular/limite máximo do ventilador](Cool_min_Layer_Time_Fan_Speed_Max.MD), a velocidade do ventilador será aumentada para atingir [a velocidade máxima do ventilador](Cool_Fan_Speed_Max. MD).Quando uma camada é tão pequena que leva menos tempo para imprimi -la, a velocidade máxima do ventilador será usada.A velocidade do ventilador é interpolada entre os dois.
* Se a camada levar menos tempo do que o tempo mínimo da camada para imprimir, a velocidade de impressão será desacelerada para que sempre leve o tempo mínimo da camada.
* Se a cabeça de impressão estiver muito lenta (impressão mais lenta do que o parâmetro [velocidade mínima](cool_min_speed.md)), a cabeça de impressão esperará no final de uma camada e possivelmente levantará a cabeça um pouco.

Há um compromisso a ser feito quando você diminui o bico para permitir que a camada esfrie melhor.O tempo mínimo da camada visa dar o material por um tempo para esfriar, desacelerando o movimento da cabeça da impressão.Enquanto isso, os ventiladores sopram com seu poder máximo para esfriá -lo mais rapidamente, mas o bico quente também está sempre em plástico.Para peças muito pequenas, o bico quente pode transferir mais calor com a impressão de que o que os fãs podem evacuar.Ele derrete o plástico ainda mais do que se você não tivesse um tempo mínimo da camada.

Ao imprimir materiais relativamente frios ou se os ventiladores da cabeça de impressão forem particularmente poderosos, o material tolerará um tempo mínimo mais alto da camada para reduzir a flacidez.Se o tempo mínimo da camada estiver muito alto, o bico diminuirá cada vez mais frequentemente, o que causa rebarbas e flacidez em certos lugares.