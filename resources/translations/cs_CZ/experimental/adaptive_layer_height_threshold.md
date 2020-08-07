Velikost topografie adaptivních vrstev
====
Tento parametr se používá ke konfiguraci vzdálenosti (horizontální) mezi okraji vrstev na libovolném svahu. Výška vrstev je upravena tak, aby bylo dosaženo požadovaného posunu. Aby se zabránilo topografickému efektu, tento parametr v podstatě konfiguruje vzdálenost mezi topografickými obrysy.

Snížení tohoto nastavení způsobí, že vrstvy budou celkově tenčí, protože vodorovné okraje vrstev musí být umístěny blíže k sobě. Zvýšení tohoto nastavení způsobí, že vrstvy budou silnější, protože okraje vrstev mohou být od sebe vzdálenější. Tloušťka vrstev však zůstane v rozsahu definovaném nastavením parametru [Výška vrstvy](../resolution/layer_height.md) a [Maximální variace adaptivních vrstev](adaptive_layer_height_variation.md).

Zmenšením tohoto nastavení snížíte efekt topografie na horní nebo spodní straně tisku. Tisk však bude trvat déle. Zvýšením tohoto nastavení zkrátíte dobu tisku.

Je téměř vždy lepší upravit výšku vrstvy namísto tohoto parametru a podle toho upravit zbývající parametry. Začněte profilem, jehož výška vrstvy je nezbytná ke snížení efektu topografie na přijatelnou úroveň. Poté pomocí adaptivních vrstev povolte určité změny kolem této tloušťky vrstvy. Tím je zajištěno, že zbývající nastavení tisku jsou správně upravena pro tloušťku vrstvy, ve které se budete skutečně tisknout. S tímto nastavením můžete mírně zvážit adaptivní vrstvy a vybrat si více ve spodní nebo horní části povoleného rozsahu.
