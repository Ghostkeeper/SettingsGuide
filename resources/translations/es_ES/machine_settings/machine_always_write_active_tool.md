Herramienta "Always Write Active" (Siempre Escribir Activo)
====
Este ajuste indica cómo ciertos comandos de g-code con un parámetro de herramienta son interpretados por la impresora. Algunos comandos de g-code pueden incluir un parámetro para indicar a qué extrusor se aplica. Algunos firmware interpretan este parámetro como un comando para cambiar a esa herramienta y luego ejecutar el g-code, mientras que otros firmware interpretan este parámetro como un comando para hacer que el g-code se aplique a un extrusor diferente al actualmente activo.

Los únicos comandos a los que se aplica esto y que son relevantes para la impresión 3D son los comandos de calentamiento de boquilla, `M104` y `M109`. Tomemos el siguiente ejemplo de un comando de calentamiento, ejecutado mientras el primer extrusor (`T0`) está imprimiendo:

M104 S210 T1

Hay dos posibles interpretaciones de este comando:
* Mientras se sigue imprimiendo en el primer extrusor, empezar a calentar el segundo extrusor a 210°C. Esta es la interpretación que tienen Marlin, Reprap, Sailfish y sus paquetes de firmware derivados.
* Primero cambiar al segundo extrusor, luego calentar el segundo extrusor a 210°C. Esta es la interpretación que hacen Smoothieware y sus programas derivados.

Debido a la estrategia de regulación de temperatura de Cura, nunca necesita ejecutar la segunda interpretación. Si la impresora interpreta el comando g-code de la segunda manera, Cura escribirá el siguiente g-code en su lugar:

`M104 S210 T1`

`T0`

Esencialmente, sabe que la impresora cambiará al segundo extrusor debido a ese comando, y por lo tanto debe cambiar de nuevo al primer extrusor para continuar imprimiendo allí.

**Como este es un ajuste de la máquina, normalmente no aparecerá en la lista normal de ajustes.**