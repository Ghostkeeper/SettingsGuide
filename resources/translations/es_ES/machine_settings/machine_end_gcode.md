G-code final
====
Con este ajuste, se puede escribir un bloque de g-code que se ejecute al final de cada impresión. Usando este g-code, la impresora puede apagar sus componentes y limpiar después de la impresión.

Algunos ejemplos de cosas que se ejecutan comúnmente en el g-code final son:

* Retirar el material.
* Enfriar la(s) boquilla(s).
* Enfriar la placa de impresión.
* Apagar los ventiladores.

Para una lista razonablemente completa de los g-codes disponibles que puedes escribir aquí, consulta el [RepRap Wiki](https://reprap.org/wiki/G-code).

Referencias a la configuración
----
Cuando se edita el g-code final, se puede hacer referencia a los valores de otros ajustes. Esto utiliza una sintaxis determinada. Las configuraciones son referidas por su *clave*. Esta clave es un nombre interno en Cura. No es visible en la interfaz de usuario. Para una lista completa de todas las claves, consulte [este documento](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) en el código fuente de Cura.

La sintaxis para obtener el valor de un ajuste global es la siguiente

`{setting_key}`

En otras palabras, escriba la clave del ajuste entre corchetes. Esto obtendrá el valor global de un ajuste. Sin embargo, muchos ajustes pueden ser diferentes para cada extrusor. Estos deben ser referenciados de la siguiente manera:

`{setting_key, #}`

Aquí, en lugar del símbolo `#` debe escribir el número del extrusor del que se obtiene el ajuste. Los extrusores comienzan a contar en 0. Los ajustes globales también pueden obtenerse especificando un extrusor, pero serán los mismos para todos los extrusores. Cuando intente obtener una temperatura específica del extrusor sin especificar el número de extrusor, obtendrá el valor del primer extrusor que no esté desactivado.

Puedes utilizar estas referencias, por ejemplo, para enfriar a una temperatura de espera, o para restaurar la aceleración y el tirón por defecto de la impresora. Estos son algunos ejemplos:

`M104 T0 S{material_standby_temperature, 0} ;stand-by for the next print`

`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

Tenga cuidado con las velocidades. El código G normalmente acepta la velocidad de avance en milímetros por *minuto*, mientras que los ajustes aparecen en milímetros por *segundo*. De momento no hay forma de seleccionar la velocidad de avance correcta. Hacer cálculos en estas referencias es imposible.

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
* `{material_brand}` se refiere al fabricante del material activo.
<!--endif-->

**Este ajuste es un ajuste de la máquina, por lo que no aparecerá en la lista normal de ajustes. Se puede cambiar yendo a la lista de impresoras en la pantalla de preferencias y haciendo clic en "Configuración de la máquina".**