Umístění podpěry
====
Toto nastavení umožňuje vybrat, jakou podpěru lze umístit na povrch.

![Podpěra je generována pro všechny převislé povrchy](../../../articles/images/support_type_everywhere.png)
![Podpěra je generována pouze tam, kde může spočívat na podložce tisku](../../../articles/images/support_type_touching_buildplate.png)

Umístění podpěr kdekoliv je spolehlivější pro podpěru. Jakékoli převisy jsou správně podpírány. Podpěra však může také spočívat na modelu a zanechat jizvu tam, kde je postavena. To snižuje vizuální kvalitu a hladkost povrchu modelu po odstranění podpěry.

Naopak umístění podpěry pouze v případě, že se dotkne podložky tisku, zabrání podpěře spočívat na modelu. Některé části vašeho modelu však nemusí být podpírány.

**Jako trik pro použití podpěry pouze na tiskové podložce, zkuste [aktivaci kónické podpěry](support_conical_enabled.md) a zadejte parametru [Úhel kónické podpěry](support_conical_angle.md) zápornou hodnotu. To umožňuje, aby se podpěra rozvinula kolem modelu a zároveň podpírala většinu sítě, aniž by spočívala na modelu. Alternativně zkuste stromovou podpěru.**