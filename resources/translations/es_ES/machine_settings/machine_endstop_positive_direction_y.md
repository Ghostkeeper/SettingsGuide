Tope en Y en sentido positivo
====
Este parámetro le indica a Cura en qué dirección se moverá la impresora a lo largo del eje Y cuando se le ordene volver a casa. Si este ajuste está desactivado, se asume que el tope del eje Y está en la coordenada cero (o negativa) del volumen de construcción. Si el ajuste está activado, se asume que el tope del eje Y está en la coordenada Y máxima de la impresora. Cuando la impresora se inicia, tendrá que moverse hacia esos topes finales para permitir que la impresora sepa dónde está el cabezal de impresión.

Este ajuste no es utilizado por Cura en absoluto. Sin embargo, es utilizado por el plug-in X3GWriter para implementar el comando g-code homing correctamente cuando se escribe un archivo de ruta de la herramienta X3G.

**Dado que este es un ajuste de la máquina, este ajuste no es normalmente visible en la lista de ajustes.**