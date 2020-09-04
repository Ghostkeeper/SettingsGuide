Optimalizovat pořadí tisku stěn
====
Pokud je tato funkce aktivována, Cura věnuje další čas slicování, pro optimalizaci pořadí, ve kterém jsou stěny tisknuty. Cílem je snížit počet přesunů a přesunů, tiskem stěn, které obklopují stejný díl, jednu po druhé.

![Optimalizace zakázána](../../../articles/images/optimize_wall_printing_order_disabled.gif)
![Optimalizace povolena](../../../articles/images/optimize_wall_printing_order_enabled.gif)

Pokud je tato optimalizace povolena, tryska nejprve vytiskne všechny stěny kolem jednoho dílu před přesunem do další díl, namísto tisku všech vnitřních stěn nejprve před tiskem vnějších stěn. Optimalizace je obecně pozitivní, ale u některých dílů může mít vliv na rozměrovou přesnost, protože předchozí stěna ještě neztuhla, když se vedle ní umístila další.