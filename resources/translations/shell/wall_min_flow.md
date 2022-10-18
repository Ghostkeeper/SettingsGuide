Flujo mínimo de pared
====
La compensación de los solapamientos en las líneas de pared reducirá el caudal de algunas de las paredes. Esto puede ser problemático, porque puede reducir el caudal de forma arbitraria, hasta un 1% si las paredes se solapan casi por completo. La impresión con caudales extremadamente bajos no funciona bien. Tiende a formar un patrón de gotas en lugar de líneas de extrusión continua.

Este ajuste convertirá esas líneas con un caudal extremadamente bajo en movimientos de desplazamiento, ajustando efectivamente su caudal al 0%. El material seguirá rezumando como en los movimientos de desplazamiento normales, pero no formará gotas.

![Los solapamientos entre paredes se compensan normalmente](../images/wall_min_flow_0.png)
![Las paredes con menos del 50% de extrusión se convierten en movimientos de desplazamiento](../images/wall_min_flow_50.png)

La boquilla seguirá la trayectoria de la pared para rezumar en el lugar correcto.

Aumentar este ajuste hará que tus paredes sean más finas de lo deseado. En lugar de dibujar líneas muy finas ya no se dibuja nada. Técnicamente esto es subextrusión, causando que su pieza sea más delgada de lo deseado. Sin embargo, la pared no se habría impreso bien de todos modos. En lugar de dibujar una larga línea de puntos o cuentas a través de la pared, no se imprimirá nada, haciendo la pared un poco más suave.

Establezca este ajuste al caudal mínimo de pared que su boquilla puede alcanzar sin formar gotas. Típicamente esto es alrededor del 60%. Si el ancho de la línea se redujera por debajo del 60% se formarían esas gotas, por lo que es mejor convertir esas líneas en movimientos de desplazamiento. Si está imprimiendo a mayores alturas de capa o utilizando líneas de pared más gruesas, puede reducir un poco este ajuste para obtener una mayor precisión dimensional.