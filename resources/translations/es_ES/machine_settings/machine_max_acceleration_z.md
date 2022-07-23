Aceleración máxima Z
====
Este ajuste indica la aceleración máxima que el motor y el bastidor de su impresora pueden manejar en la dirección Z, según el firmware de la impresora.

Este ajuste sólo se utiliza para obtener estimaciones de tiempo correctas. La [aceleración](../velocidad/aceleración_impresión.md) establecida por Cura no tiene límite, pero Cura asumirá que su firmware establece un cierto límite por eje. Si la aceleración en el eje Z excede esta configuración, la estimación de tiempo de esos movimientos se ajustará para asumir que tu firmware limita la aceleración. La aceleración total puede seguir siendo mayor cuando se acelera en diagonal con varios ejes al mismo tiempo.

**Puesto que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes.**