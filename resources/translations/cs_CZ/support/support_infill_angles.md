Směr linií výplně podpěry
====
Vzor podpěry je obvykle orientován tak, že linie jsou kolmé k většině věcí, které podpírá. Tímto způsobem je vzdálenost, kterou musí podpíraný materiál procházet, snížena na minimum. S tímto nastavením lze přizpůsobit orientaci linií podpěry.

![Úhel 0°](../../../articles/images/support_infill_angle_0.png)
![Úhel 30°](../../../articles/images/support_infill_angle_30.png)
![Střídání mezi 30° a 60°](../../../articles/images/support_infill_angles.png)

Tento parametr umožňuje zadat více úhlů oddělených čárkami. Když zadáte více úhlů, Cura bude střídat mezi těmito úhly ve vrstvách.

Pokud byl [horní/dolní směr linií](../top_bottom/skin_angles.md) upraven, je vhodné odpovídajícím způsobem upravit úhel podpěry tak, aby byl vždy kolmý na linie na spodní straně tisku. To umožňuje, aby tyto spodní linie spočívaly správně na podpěře, místo aby propadaly mezi liniemi podpěry. To je zvláště důležité pro lineární a cikcak [vzor podpěry](support_pattern.md), kde jsou mezi liniemi podpěry dlouhé přímky, které nenabízejí žádnou podporu.