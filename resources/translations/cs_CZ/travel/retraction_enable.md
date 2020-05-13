Aktivovat retrakci
====
Pokud 3D tiskárna přestane vytlačovat materiál, materiál nezastaví okamžitě tok z trysky. V trysce jsou zbytky materiálu a je pod tlakem, takže i nadále nějakou dobu vytéká. Aby se zabránilo výtoku materiálu, musí ho tiskárna vyjmout z otvoru trysky. To je nezbytné pro provádění čistých přesunů bez stringování.

![Retrakce je deaktivována](../../../articles/images/retraction_enable_disabled.png)
![Retrahované přesuny se objevují ve světle modré barvě](../../../articles/images/retraction_enable_enabled.png)

Retrakce se provádí během přesunu, který je obzvláště citlivý na stringování. Pojezdy, které procházejí pouze výplní nebo přesuny od podpěry k podpěře, nejsou normálně retrahovány. Existuje také omezení na frekvenci retrahování materiálu prostřednictvím parametrů [Maximální počet retrakcí](retraction_count_max.md) a [Interval minimální vzdálenosti extruze](retraction_extrusion_window.md).

Retrakce má významné výhody, ale také nevýhody:
* Výrazně snižuje počet stringování. Žádné nadbytečná vlákna mezi různými částmi tisku.
* Významně sníží množství a velikost kuliček na povrchu, kde tryska vstupuje do obvodu součásti.
* Retrakce zabere trochu času.
* Při retrakci dochází k přerušení toku materiálu. To má negativní důsledky na rozměrovou přesnost, páskování a pod-extruzi.
* Vlákno se může opotřebovat, když je příliš mnoho retrakcí, což brání podavači v uchopení materiálu.

**Ohebné materiály se obtížněji retrahují, protože tahem za vlákno se se vlákno natáhne, místo aby se vytáhlo z trysky. Může být velmi časově náročné a relativně neefektivní umožnit retrakci s takovými materiály.**


