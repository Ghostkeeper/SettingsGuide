Úhel větve stromové podpěry
====
Toto nastavení určuje maximální úhel převisu, který mohou vytvářet větve stromové podpěry. Pokud je úhel zvětšen, mohou být větve vytištěny vodorovněji, což jim umožní dále dosáhnout.

![Úhel větve 20°](../../../articles/images/support_tree_angle_20.png)
![Úhel větve 40°](../../../articles/images/support_tree_angle_40.png)

Zmenšením úhlu větve se větve zvýší. Pokud je zvýšíte, budou vodorovnější. Protože větve mohou mít větší úhly převisu, mohou dosáhnout vzdálenějších překážek, což umožňuje, aby podpěra spočívala častěji na podložce tisku než na modelu. To také umožní, aby se větve později uvolnily.

Nejdůležitější efekty zvětšení úhlu větví pro stromovou podpěru jsou:
* Snížení jizev, protože podpěra musí spočívat spíše na modelu než na podložce tisku. Pokud je [Umístění podpěry](../support/support_type.md) nastaveno na kontakt s deskou, lze podepřít více částí modelu.
* Zkrácení doby tisku a použití materiálů díky oddělení větví ve vyšších úrovních. Větve jsou nařezány právě včas, aby bylo možné dosáhnout přesahu. Snížení doby tisku a spotřeby materiálu v důsledku odštěpení větví ve vyšších úrovních. Větve se oddělí právě včas, aby bylo možné dosáhnout převisu.
* Snížená spolehlivost. Pokud je úhel převisu příliš velký, bude podpěra výrazně oslabena, což zvyšuje riziko zlomení nebo převrácení podpěry.

Je výhodné kombinovat velké úhly větví s malými hodnotami parametru [Rozlišení kolize stromové podpěry](support_tree_collision_resolution.md). Tím se sníží posuny v pozicích stromu kvůli zamezení kolize. Při nastavení kolizní vzdálenosti se zabrání příliš velké vzdálenosti převisu.
