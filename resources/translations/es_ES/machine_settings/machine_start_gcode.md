G-code inicial
====
Con este ajuste, se puede escribir un bit de g-code que se ejecutará al inicio de cada impresión. Usando este g-code, la impresora puede ser configurada para estar lista para imprimir.

Algunos ejemplos de cosas que se ejecutan comúnmente en el g-code de inicio son:
* Cebar la(s) boquilla(s).
* Calentar la placa de impresión.
* Calentar la(s) boquilla(s).
* Asegurarse de que el extrusor correcto está seleccionado.
* Configurar los ventiladores, aceleraciones o tirones.
* Nivelación automática de la cama.
* Configurar el avance lineal.

Para una lista razonablemente completa de los g-codes disponibles que puedes escribir aquí, consulta el [RepRap Wiki](https://reprap.org/wiki/G-code).

Referencias a la configuración
----
Cuando se edita el g-code de inicio, se puede hacer referencia a los valores de otros ajustes. Esto utiliza una sintaxis determinada. Las configuraciones son referidas por su *clave*. Esta clave es un nombre interno en Cura. No es visible en la interfaz de usuario. Para una lista completa de todas las claves, consulte [este documento](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) en el código fuente de Cura.

La sintaxis para obtener el valor de un ajuste global es la siguiente

`{setting_key}`

En otras palabras, escriba la clave del ajuste entre corchetes. Esto obtendrá el valor global de un ajuste. Sin embargo, muchos ajustes pueden ser diferentes para cada extrusor. Estos deben ser referenciados de la siguiente manera:

`{setting_key, #}`

Aquí, en lugar del símbolo `#` debe escribir el número del extrusor del que se obtiene el ajuste. Los extrusores comienzan a contar en 0. Los ajustes globales también pueden obtenerse especificando un extrusor, pero serán los mismos para todos los extrusores. Cuando intente obtener una temperatura específica del extrusor sin especificar el número de extrusor, obtendrá el valor del primer extrusor que no esté desactivado.

Puede utilizar estas referencias, por ejemplo, para precalentar a la temperatura correcta, o para establecer las aceleraciones. Estos son algunos ejemplos:

`M104 S{material_print_temperature_layer_0, 0} ;precalentar`.

`M140 S{material_bed_temperature_layer_0} ;calentar la cama`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Tenga cuidado con las velocidades. El código G normalmente acepta la velocidad de avance en milímetros por *minuto*, mientras que los ajustes aparecen en milímetros por *segundo*. No hay manera de seleccionar la velocidad de avance correcta por el momento. Hacer cálculos en estas referencias es imposible.

Otras informaciones
----
A través de la misma sintaxis que las referencias a los ajustes, también está disponible alguna información auxiliar:

* `{time}` se refiere a la hora local actual del día en que se cortó.
* `{date}` se refiere a la fecha en que se cortó.
* `{day}` se refiere al día de la semana en que se cortó.
* `{initial_extruder_nr}` se refiere al extrusor con el que comenzará la impresión.
<!--if cura_version>=4.12-->
* `{material_id}` se refiere a un identificador único del material activo. Especifique el extrusor de forma similar a otros ajustes.
* `{material_name}` se refiere al nombre del material activo. Suele ser el nombre que se ve en un sitio web que vende ese material.
* `{material_type}` se refiere a la clase de material que está activo, como PLA o ABS.
* `{material_brand}` hace referencia al fabricante del material activo.
* `{print_time}` hace referencia a la duración estimada de la impresión (formateada según ISO-8601).
* `{filament_amount}` se refiere a la longitud del filamento utilizado, en metros, para cada extrusor por separado. Esto se formatea como una lista con corchetes alrededor.
* `{filament_weight}` se refiere al peso del filamento utilizado, en gramos, para cada extrusor por separado, formateado como una lista con corchetes. Si el peso de la bobina es desconocido, será 0.
* `{filament_cost}` es el coste del filamento utilizado para cada extrusor por separado. La unidad del coste es la misma que aparece en la página de gestión de materiales en las preferencias. Si se desconoce, será 0.
<!--endif-->

Calentamiento antes del g-code de inicio
----
Cura emitirá automáticamente los comandos de calentamiento antes de que comience su g-code de inicio. De esta manera su g-code de inicio no necesita considerar que la boquilla necesita calentarse. Puede comenzar inmediatamente a cebar la boquilla. Si su g-code de inicio contiene una referencia a cualquier temperatura (para la boquilla o la cama), esta será desactivada (para la boquilla o la cama respectivamente).

**Este ajuste es un ajuste de la máquina, por lo que no aparecerá en la lista normal de ajustes. Se puede cambiar yendo a la lista de impresoras en la pantalla de preferencias y haciendo clic en "Configuración de la máquina".**