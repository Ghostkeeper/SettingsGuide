Activar gotas de cebado
====
Cuando se activa, esto hace que Cura emita un comando para que la impresora se cebe, justo antes de que el extrusor se utilice por primera vez. La impresora cebará creando una pequeña mancha de material en la placa de impresión.

El cebado se hace para que el material fluya correctamente. Si la mancha de cebado no está activada, la impresora cebará durante la falda o el borde. Este es el principal caso de uso para la falda en primer lugar, pero para un borde esto reducirá la fuerza de adhesión del borde ligeramente.

El efecto de este ajuste en el g-code es que Cura pondrá el comando M280 en un lugar determinado. **Esto actualmente sólo funciona en las impresoras Ultimaker desde la Ultimaker 3** ya que son las únicas que implementan el comando M280. Para otras impresoras la configuración no será visible.