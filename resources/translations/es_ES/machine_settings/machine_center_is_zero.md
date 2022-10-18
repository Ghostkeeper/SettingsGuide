Origen en el centro
====
Si este ajuste está habilitado, la coordenada 0,0 de la impresora se establece para estar en el centro del volumen de construcción, en lugar de la esquina frontal izquierda.

En algunas impresoras el firmware considera que la coordenada 0,0 está en el centro del volumen de construcción. Esto es común para las impresoras de estilo delta, que generalmente tienen volúmenes de construcción cilíndricos en lugar de cuboides.

Si la coordenada cero de la impresora está en el centro, entonces el código g final contendrá coordenadas negativas así como coordenadas positivas. El origen de coordenadas estará en el centro del volumen de construcción de Cura. Cura también mostrará su marcador de coordenadas tricolor en el centro. Sin embargo, las coordenadas de los archivos 3MF seguirán siendo tratadas como si el origen de coordenadas estuviera en la esquina frontal izquierda de la impresora, ya que el formato de archivo 3MF así lo requiere.

**Dado que se trata de un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes. Sin embargo, hay una casilla de verificación para este ajuste en el diálogo de configuración de la impresora, que se puede encontrar en la lista de impresoras añadidas en el diálogo de preferencias.**