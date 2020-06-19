Zakázané oblasti trysky
====
Toto nastavení označuje všechny oblasti na vaší tiskové ploše, kam nesmí aktivní tryska jít. Uživatel nemá dovoleno umisťovat žádné předměty do těchto oblastí ani do jejich blízkosti, aby tam mohly něco vytisknout (jako krempu).

![Šedé plochy označují nepovolené oblasti kolem míst, kde jsou klipy na podložce tisku](../../../articles/images/machine_disallowed_areas.png)

Toto nastavení se vztahuje pouze na *aktivní trysku*, což znamená, že můžete stále tisknout objekty vedle těchto zakázaných oblastí, i když by to způsobilo, že by se další trysky pohybovaly po těchto zakázaných oblastech. Proto je toto nastavení opravdu užitečné pouze pro tiskárny, které zvednou neaktivní trysky nahoru nebo zaparkují mimo objem tisku, když jsou neaktivní. Na rozdíl od obyčejných [zakázaných oblastí](machine_disallowed_areas.md) se tyto nepovolené oblasti nepohybují v závislosti na ofsetu mezi tryskami.

Tyto zakázané oblasti jsou nezbytná, aby se zabránilo kolizi trysky s věcí. Například na tiskové ploše mohou být nějaké klipy nebo nálepka nebo logo. Pokud by měl uživatel tisknout příliš blízko k těmto objektům, tryska by s nimi srazila. V nejlepším případě byste dostali [posun vrstvy](../troubleshooting/layer_shift.md). V nejhorším případě byste poškodili trysku nebo cokoli, co se s ní srazí.

Zakázané oblasti jsou nakresleny jako šedý stín na tiskové ploše, což indikuje uživateli, že tam nemůže umístit žádné objekty. Tyto stíny mohou být rozšířeny ve všech směrech, aby zabránily nárazu při tisku krempy nebo sukénky a z různých jiných důvodů. Na tiskové ploše jsou také jiné stíny, například pro omezení rozsahu pohybu, pokud mají trysky offset.

*Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.*