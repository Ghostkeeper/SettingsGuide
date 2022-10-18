Espiralizar el contorno exterior
====
Spiralize Outer Contour es un truco.

Cuando se imprime capa por capa, la boquilla normalmente necesita moverse de una capa a la siguiente. Este movimiento hace que la boquilla se quede casi quieta durante una fracción de segundo, lo que deja una costura en la superficie llamada costura Z. Este ajuste está pensado para evitar eso y más. Simplifica en gran medida el proceso de impresión al omitir muchos aspectos del mismo.

Al espiralizar el modelo, el modelo no obtendrá ningún relleno ni ninguna parte superior. Sólo tendrá una pared y un fondo. Crucialmente, si [Smooth Spiralized Contours](smooth_spiralized_contours.md) está habilitado, la altura de la boquilla se incrementará gradualmente en el curso de una capa. De esta manera se crea una espiral siguiendo el contorno del modelo. No habrá movimiento al pasar de una capa a otra, porque la boquilla ya se ha desplazado gradualmente hacia la siguiente capa.

El modo de espiralización es común entre muchos cortadores. A veces también se le conoce como "modo jarrón", porque es un buen modo para imprimir jarrones. Algunas otras propiedades son:
* Imprime extremadamente rápido.
* La superficie se vuelve muy suave. Ya no hay [Z seam](../troubleshooting/seam.md) donde se movía a la siguiente capa si [Smooth Spiralized Contours](smooth_spiralized_contours.md) está activado.
* No será muy fuerte. Si el modelo es demasiado grande, tiende a [dividirse](../troubleshooting/layer_splitting.md) debido a la delgada pared.
* Aunque la eliminación de la costura ayuda a que la impresión sea estanca, es difícil conseguir que la impresión sea estanca si tiene algún tamaño. Para ello, es aconsejable tener al menos 2 paredes. Espiralizar el contorno exterior es imposible entonces.

**Spiralize no funciona bien con impresiones con muchas superficies horizontales. No maneja los salientes en absoluto, y no imprime las superficies superiores por lo que nada podrá apoyarse en una superficie horizontal. Tampoco funciona bien cuando hay múltiples partes en una capa.**