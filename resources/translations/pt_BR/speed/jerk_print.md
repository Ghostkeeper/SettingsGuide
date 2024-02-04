Idiota
====
O idiota (idiota) determina a velocidade com que o bico pode passar em turnos.Com altos valores de empurrão, o bico não diminui tanto ao se aproximar de uma curva, o que resulta em uma velocidade mais constante, mas também em maiores vibrações.

** O termo "Jerk" foi introduzido por Marlin no campo da impressão 3D, mas não é idêntico ao da física.Foi projetado lá como uma solução de desvio do problema inerente à tentativa de seguir um caminho perfeitamente.Como o bico não pode se desviar da trajetória (em teoria), ele deve desacelerar a 0 mm/s em cada canto.Isso arruinaria sua impressão, porque a desaceleração a 0 mm/s causaria uma mancha em cada canto.Não é permitido fazer curvas para encurtar a esquina, nem excedê -la.Em vez disso, o Marlin permite uma alteração instantânea no vetor de velocidade em cada canto.A magnitude dessa mudança do vetor de velocidade é chamada de "Jerk".Assim, o idiota é a mudança instantânea máxima de velocidade, aplicada a cada canto do movimento. **

O aumento do choque terá efeitos positivos e negativos na sua impressão:
* O tempo de impressão será reduzido, porque o bico diminui menos nos cantos.
* O tempo de impressão será reduzido, porque o bico diminui menos nos cantos.O bico se move em um ritmo mais constante, de modo que não permanece nos cantos enquanto o material continua a fluir pela abertura.
* A impressora geralmente vibra mais em cada canto, porque a cabeça de impressão visa alterar instantaneamente a direção para a aceleração teoricamente infinita.Essas vibrações tendem a criar ondulações em sua impressão, o que leva ao toque e uma redução na precisão dimensional.
* Tem valores extremos, existe o risco de seus motores perderem algumas etapas nos cantos, o que pode causar a camada da camada.