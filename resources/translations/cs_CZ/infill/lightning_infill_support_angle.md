Podpěrný úhel bleskové výplně
====
Vzor bleskové výplně je určen pouze k podepření tisku zevnitř. Toto nastavení určuje maximální úhel přesahu nejen ploch, které bude podpírat, ale i vnitřních v samotné výplni. Snížení tohoto nastavení způsobí, že se vytvoří více výplně. Jeho zvýšením se množství výplně sníží.

Vzor podpírá horní stranu tisku z vnitřní strany, ale pouze horní stranu, která výrazně přečnívá, více než tento úhel. Vzor má také koncové body, které přečnívají pod určitým úhlem, aby vytvořily rozvětvenou stromovou strukturu, a strany této rozvětvené struktury mají vnitřní úhel, aby zasahovaly dále do určitých oblastí. Tyto tři aspekty převisu lze také individuálně ovládat pomocí nastavení [úhlu převisu bleskové výplně](lightning_infill_overhang_angle.md), [úhlu prořezávání bleskové výplně](lightning_infill_prune_angle.md) a [úhlu vyrovnání bleskové výplně](lightning_infill_straightening_angle.md).

![Při nízkém úhlu převisu je zapotřebí velká podpěra](../../../articles/images/lightning_infill_support_angle_30.png)
![Při vysokém úhlu převisu jsou povoleny strmé převisy](../../../articles/images/lightning_infill_support_angle_60.png)

Zvýšením tohoto nastavení se výrazně sníží množství potřebného materiálu a zkrátí se doba tisku. Zároveň to však způsobí prověšení. Toto prověšení se nachází na vnitřní straně modelu, takže není okamžitě viditelné. Pokud však [Horní tloušťka](../top_bottom/top_thickness.md) není dostatečná, může to vést k [polštářování](../troubleshooting/pillowing.md). Protože vnitřní úhly ve výplni mohou také více přesahovat, je pravděpodobné, že výplň bude začínat výše podél stěn.