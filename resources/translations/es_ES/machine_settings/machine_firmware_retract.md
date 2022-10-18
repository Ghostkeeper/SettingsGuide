Retracción del firmware
====
Normalmente, Cura provoca una retracción controlando el movimiento del alimentador, ordenándole que mueva el filamento un poco hacia atrás. Si este ajuste está habilitado, en su lugar escribirá un comando `G10` para significar que la impresora debe retraer el filamento, o un comando `G11` para desretraerlo.

Al elegir el uso de retracciones de firmware, el firmware de la impresora controla la distancia y la velocidad de retracción del filamento. La impresora puede conocer mejor su propia geometría que Cura, por lo que puede decidir mejor cómo retraer el filamento. Sin embargo, esto significa que Cura ya no tiene el control de estas retracciones y Cura sabe más sobre la propia impresión. Esencialmente, la cortadora y el firmware tienen información diferente, y este ajuste decide cuál de los dos puede elegir.

**Como se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**