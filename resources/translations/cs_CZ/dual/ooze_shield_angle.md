Úhel štítu proti výtoku
====
Štít proti výtoku bude sledovat tvar modelu. Musí zůstat blízko, jinak cestou mezi štítem a modelem vyteče nový materiál. Model však může mít vodorovné povrchy, které by ve štítu vytvořily náhlé převisy. Toto nastavení omezuje náklon ochranného štítu tak, aby se nerozpadl.

![Namísto sledování modelu dolů a nahoru není strmější než zadaný úhel](../images/ooze_shield_cs.svg)

* Hodnota 0 způsobuje, že ochranný štít je po celém tvaru zcela svislý. Čím menší je úhel, tím bude štít stabilnější.
* Hodnota 90 zajistí, že štít proti úniku přesně odpovídá modelu. Čím vyšší je úhel, tím lépe bude ochranný štít bránit prosakování na model.
I když by teoreticky mělo smysl použít podobnou hodnotu jako u [Úhel převisu pro podpěru](../support/support_angle.md), štít proti výtoku je pouze jedna linie. Tato jediná linie je slabší než váš model a více podléhá deformaci. Je dobré použít o něco mělčí úhel, než jaký by se normálně ve vašem modelu dobře tiskl, aby se zabránilo rozštěpení štítu.