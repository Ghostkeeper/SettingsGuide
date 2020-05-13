Směr linií výplně podpěry
====
Vzor podpěry je obvykle orientován tak, že linie jsou kolmé k většině věcí, které podpírá. Tímto způsobem je vzdálenost, kterou musí podpíraný materiál procházet, snížena na minimum. S tímto nastavením lze přizpůsobit orientaci linií podpěry.

![Úhel 0°](../../../articles/images/support_infill_angle_0.png)
![Úhel 30°](../../../articles/images/support_infill_angle_30.png)

Pokud byl upraven parametr [Směr horní/dolní linie](../shell/skin_angles.md), je vhodné odpovídajícím způsobem upravit úhel podpěry tak, aby byl vždy kolmý na linie spodní strany tisku. To umožňuje, aby tyto spodní linie spočívaly správně na podpěře, než aby propadaly mezi podpůrnými liniemi. To je zvláště důležité pro lineární a cikcak [vzory podpěry](support_pattern.md), kde jsou dlouhé přímky mezi podpůrnými liniemi, které nenabízejí žádnou oporu.

*Od Cura 4.3 tento parametr umožňuje zadat několik úhlů, které se střídají podobně jako parametr [Směr linií výplně](../infill/infill_angles.md).*
