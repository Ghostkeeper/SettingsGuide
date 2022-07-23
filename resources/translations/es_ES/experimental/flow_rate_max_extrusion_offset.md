Desplazamiento de extrusión máximo del factor de compensación del caudal 
====
La compensación del caudal es un experimento similar a la funcionalidad [Avance Lineal](http://marlinfw.org/docs/features/lin_advance.html) de Marlin. El propósito de la compensación del caudal es compensar la subextrusión y la sobreextrusión cuando el caudal de material que sale de la boquilla cambia. Este ajuste pone un límite a la distancia que el material será retraído o empujado hacia adelante para compensar los cambios de flujo.

La compensación de flujo moverá el filamento más adelante de su posición original o más atrás durante la impresión. Este ajuste limita la distancia que se permite al filamento para alejarse de su posición original.

La compensación introducirá movimientos adicionales del filamento a lo largo de la impresión. Esto hace que el cabezal de impresión se ralentice de vez en cuando para mover el filamento. Para reducir el efecto de esto, puedes limitar la distancia a la que se mueve el filamento. Esto evita que el cabezal de impresión tenga que ralentizar para que el alimentador siga su ritmo. Sin embargo, esto hace que la compensación de flujo sea menos efectiva.