Úhel převisu bleskové výplně
====
Blesková výplň bude podpírat pouze horní stranu modelu z vnitřní strany, kde přesahuje. Toto nastavení určuje úhel přesahu, který bude zevnitř modelu bleskovou výplní podepřen.

![Přesah až 30° zůstává bez podpěry](../../../articles/images/lightning_infill_support_angle_30.png)
![Až do úhlu 70° není koule podepřena, takže je podepřena pouze její horní část](../../../articles/images/lightning_infill_overhang_angle_70.png)

Zvětšením tohoto úhlu se sníží množství vytvářených výplní. Pokud se nejedná o velmi strmý převis, bude podepřena menší část horní plochy. Tím se ušetří čas a materiál, ale také může dojít k tomu, že se horní plocha místy prohne. Výsledkem může být [polštářování](../troubleshooting/pillowing.md) nebo obecně drsnější povrch.

Na rozdíl od nadřazeného nastavení [Podpěrný úhel bleskové výplně](lightning_infill_support_angle.md) nemá toto nastavení vliv na přesah samotného vzoru výplně.