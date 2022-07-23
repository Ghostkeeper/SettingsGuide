Impulso de impresión
====
El impulso determina la velocidad a la que la boquilla puede pasar por las curvas. Con valores de impulso elevados, la boquilla no frenará tanto al acercarse a una curva, lo que se traduce en una velocidad más constante pero también en mayores vibraciones.

**'Impulso' en impresión 3D no es lo mismo que 'impulso' en física.** El término "impulso" fue introducido por Marlin. Fue diseñado allí como una solución para el problema inherente al tratar de seguir perfectamente una trayectoria. Como la boquilla no puede desviarse de la trayectoria (en teoría), la boquilla tendría que desacelerar a 0 mm/s en cada esquina. Esto arruinaría su impresión, porque desacelerar a 0mm/s causaría una mancha en cada esquina. No se permite hacer curvas para acortar la esquina, ni puede sobrepasar la velocidad. En su lugar, Marlin permite un cambio instantáneo en el vector de velocidad en cada esquina. La magnitud de este cambio en el vector velocidad se denomina "impulso". Así, el impulso es el máximo cambio instantáneo de la velocidad, aplicado en cada esquina del movimiento.

Aumentar el impulso tendrá algunos efectos positivos y otros negativos en su impresión:
* El tiempo de impresión se reducirá, porque la boquilla se ralentiza menos en las esquinas.
* Debido a que la boquilla no se ralentiza a un ritmo lento, obtendrá menos de una mancha en las esquinas. La boquilla se mueve a un ritmo más constante, por lo que no se queda en la esquina mientras el material sigue saliendo por la abertura.
* La impresora generalmente vibrará más en cada esquina, porque el cabezal de impresión está instruido para hacer cambios instantáneos de dirección a una aceleración teóricamente infinita. Esas vibraciones tienden a crear ondulaciones en su impresión, lo que resulta en el timbre y la reducción de la precisión dimensional.
* En valores extremos, existe la posibilidad de que sus motores pierdan algunos pasos en las esquinas, lo que puede causar un desplazamiento de la capa.