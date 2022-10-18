Aceleración máxima del filamento
====
Este ajuste indica la aceleración máxima que manejan los motores del alimentador de su impresora, según el firmware de la misma.

Este ajuste sólo se utiliza para obtener estimaciones de tiempo correctas. La [aceleración](../velocidad/aceleración_impresión.md) establecida por Cura no tiene límite, pero Cura asumirá que su firmware establece un cierto límite por eje. Si la aceleración para el alimentador excede esta configuración, la estimación de tiempo de esos movimientos se ajustará para asumir que su firmware limita la aceleración. La aceleración total puede seguir siendo mayor cuando se acelera en diagonal con varios ejes al mismo tiempo.

Es bastante común que los límites de aceleración para el alimentador sean golpeados, ya que (dependiendo del firmware) la aceleración establecida por Cura también afecta al alimentador. Por lo tanto, es crucial que este ajuste se configure correctamente con el fin de obtener estimaciones de tiempo correctas para las retracciones.

**Dado que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**