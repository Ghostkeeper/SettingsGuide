Vzdálenost větví stromové podpěry
====
Toto nastavení určuje vzdálenost mezi dvěma sousedními větvemi, když se větve dotknou tiskové podložky.

![Větve umístěné 1,4 mm od sebe](../../../articles/images/support_tree_branch_distance_1_4.png)
![Větve umístěné 5 mm od sebe](../../../articles/images/support_tree_branch_distance_5.png)

Pro podpěru modelu umístí podpěra ve tvaru stromu kontaktní body pod model do rozloženého rastru. Toto nastavení v podstatě určuje velikost této mřížky a tedy vzdálenost mezi větvemi. V důsledku zarovnání větví vzhledem k (výchozímu) směru linií pláště bude vzdálenost, kterou musí linie pláště procházet, s největší pravděpodobností větší než tato vzdálenost.

Zmenšením vzdálenosti mezi větvemi můžeme dosáhnout lepší kvality převisu, protože linie spočívající na podpěře nemusí tuto vzdálenost překročit. Podpěra bude také pevnější, protože více materiálu bude použito směrem k horní části vnější vrstvy, což zlepší spolehlivost tisku.

Zmenšení vzdálenosti mezi větvemi však také zvýší množství použitého materiálu a dobu tisku.

Pokud je vzdálenost mezi větvemi menší než [průměr větve](support_tree_branch_diameter.md), větve se sloučí, než budou správně vytvořeny. V důsledku toho nemusí být střed velkých převislých oblastí v tuto chvíli správně podpírán.