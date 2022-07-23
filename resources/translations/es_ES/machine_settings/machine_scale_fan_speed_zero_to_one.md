Escala de velocidad del ventilador a 0-1
====
Para controlar la velocidad a la que giran los ventiladores de la impresora, Cura pone comandos en el g-code con un parámetro que controla la velocidad. Normalmente este parámetro es un número entre 0 y 255. Sin embargo, algunas impresoras aceptan un número entre 0 y 1 también, y lo interpretan de forma diferente entonces. Este ajuste hace que Cura escriba las velocidades de los ventiladores como un número entre 0 y 1, en lugar de entre 0 y 255.

Hay 3 tipos de comportamientos del firmware en varias impresoras del mercado.
* La mayoría de las impresoras aceptan las velocidades de los ventiladores sólo como un número entre 0 y 255. Este ajuste debe ser desactivado entonces, o de lo contrario el ventilador nunca girará realmente.
* Algunas impresoras (particularmente RepRapFirmware) aceptan números entre 0 y 255, pero si es 1 o menor, lo interpretan como un número entre 0 y 1. Esta configuración debe ser activada entonces, o de lo contrario podría haber un caso raro en el que Cura intenta establecer la velocidad del ventilador como 0,4% (1 de 255), pero la impresora lo establece en el 100% en su lugar.
* Algunas impresoras sólo aceptan números entre 0 y 1. Este ajuste también debería estar habilitado entonces, o el ventilador siempre estará completamente apagado o completamente encendido.