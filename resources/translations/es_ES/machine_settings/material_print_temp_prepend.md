Incluir la temperatura de la placa de construcción
====
Este ajuste comunica al back-end de corte si debe o no escribir los comandos de temperatura de la placa de construcción para el inicio de la impresión antes del código g de inicio. Se establece automáticamente al iniciar un corte.

Para la mayoría de las operaciones durante el [start g-code] (machine_start_gcode.md) tiene sentido tener la placa de construcción a la temperatura correcta para la impresión. Para facilitar el diseño de las definiciones de la impresora, Cura calentará automáticamente la placa de impresión antes de que se ejecute el g-code de inicio. Sin embargo, si el g-code de inicio contiene alguna referencia a un ajuste de temperatura de la placa de impresión, ya no calentará la placa de impresión automáticamente.

**Dado que se trata de un ajuste de la máquina, este ajuste no suele ser visible en la lista de ajustes. Cambiarlo tampoco tiene efecto ya que será cambiado automáticamente por Cura.**