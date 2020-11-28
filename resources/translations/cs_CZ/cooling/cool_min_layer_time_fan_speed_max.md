Práh normální/maximální rychlosti ventilátoru
====
Tento parametr určuje dobu tisku vrstvy, která je tak krátká, že se rychlost ventilátoru začíná zvyšovat a dosahuje hodnoty [maximální rychlosti ventilátoru](cool_fan_speed_max.md). Vrstvy, které se tisknou déle, budou používat [normální rychlost ventilátoru](cool_fan_speed_min.md). U vrstev s kratší dobou tisku bude rychlost ventilátoru interpolována mezi parametry normální a maximální rychlosti ventilátoru, až do [minimální doby trvání vrstvy](cool_min_layer_time.md), kde bude rychlost ventilátoru na nejvyšší hodnotě.

![Jaká rychlost ventilátoru se používá, a kde](../images/cool_fan_speed_cs.svg)