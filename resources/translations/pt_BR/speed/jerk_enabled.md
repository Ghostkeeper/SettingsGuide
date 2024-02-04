Ative o controle do idiota
====
O idiota (idiota) determina a velocidade com que o bico pode passar em turnos.Se o controle dos idiotas for ativado, o Cura assume o controle da quantidade de jerk para aplicar durante as diferentes partes da impressão.Se for desativado, o microprograma da impressora escolherá um valor de jerk.Esse valor geralmente é alto o suficiente para dar mais controle ao software, mas o fabricante pode ter mais informações sobre seu próprio hardware do que o Cura.

![A relação entre velocidade, aceleração e idiota](../images/velocity_acceleration_jerk.svg)

** O termo "Jerk" foi introduzido por Marlin.Foi concebido lá como uma solução de desvio do problema inerente à tentativa de seguir um curso perfeitamente.Como o bico não pode se desviar da trajetória (em teoria), ele deve desacelerar a 0 mm/s em cada canto.Isso arruinaria sua impressão, porque a desaceleração a 0 mm/s causaria uma marca em cada canto.Não é permitido fazer curvas para encurtar a esquina, nem excedê -la.Em vez disso, o Marlin permite uma alteração instantânea no vetor de velocidade em cada canto.A magnitude dessa mudança do vetor de velocidade é chamada de "Jerk".

Assim, o Jerk (Jerk) é a mudança instantânea máxima de velocidade, aplicada em cada canto do movimento.

Microprogramas que não se baseiam em Marlin, como a família de microprogramas de veleiro, ignoram os empurrões do idiota.Essa configuração não terá efeito.

Exemplo do idiota do idiota
----
Tomemos, por exemplo, uma impressão muito simples: primeiro move 100 mm para a direita e depois a partir de 100 mm.A velocidade de impressão é fixada em 50 mm/s.A aceleração é definida em 1000 mm/s^2.A velocidade do Jerk é definida como 10mm/s.É isso que vai acontecer:
1. No início de uma impressão, Marlin pega metade do valor do idiota para começar, para que teoricamente acelere 5 mm/s instantaneamente.
2. Possui uma aceleração de 1000 mm/s^2, levará 0,045s para ir de 5 mm/s para velocidade máxima de 50 mm/s.Enquanto isso, o bico cobrirá 1.2375 mm.
3. O bico se move por um tempo a 50 mm/s, a velocidade máxima de impressão.
4. Marlin calculará a rapidez com que o bico pode entrar na curva: o bico fará uma curva de 90 graus, primeiro para a direita e depois para baixo.Para limitar essa mudança de velocidade, ela entrará no canto para COS (90/2) * (10/2) mm/s indo para a direita e saia para COS (90/2) * (10/2) mm/S para baixo.Portanto, cruzará a curva em torno de 7,07 mm/s.
5. Será necessário 0,043s para passar de uma velocidade de 50 mm/s a 7,07 mm/s.
6. A curva é feita com uma mudança de velocidade instantânea.A amplitude da diferença entre os vetores [7.07, 0] e [0, 7.07] é exatamente 10 mm/s, o que possibilita que isso faça isso instantaneamente.
7. Levará 0,043s para ir de 7,07 mm/s a 50 mm/s.
8. O bico se move novamente por um tempo a 50 mm/s, a velocidade máxima de impressão.
9. No final da impressão, o bico desacelera de 50 mm/s a 0 mm/s em 0,05s.

