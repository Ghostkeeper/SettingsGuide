Pořadí tisku
====
Když je na podložce tisku umístěno více modelů, určuje se pořadí, ve kterém se vrstvy těchto objektů tisknou. Existují dvě možnosti.

Vše současně
----
Všechny objekty budou vytištěny současně, což znamená, že vrstvy budou vytištěny zdola nahoru pro všechny objekty současně. Před přechodem na další vrstvu bude vytištěna  jedna vrstva každého objektu.

To má dvě hlavní výhody:
* Předchozí vrstva má více času na vychladnutí, což poskytuje lepší kvalitu při tisku malých objektů.
* Pro tisk můžete použít celý objem.

Jeden po druhém
----
Objekty budou vytištěny jeden po druhém, což znamená, že vytiskne všechny vrstvy objektu, poté se vrátí na tiskové lože a vytiskne další objekt.

Hlavní výhody tohoto režimu jsou:
* Pokud tisk z jakéhokoli důvodu selže, všechny objekty, které byly dokončeny před selháním, jsou plně použitelné.
* Pro přemístění z jednoho modelu na druhý je třeba méně přesunů. To šetří trochu času tisku a snižuje počet jizev na povrchu, kde tryska vyšla a vstoupila do objektu.

V tomto režimu je však několik omezení, která zabraňují kolizi hlavy a portálu s modelem.
* Nelze tisknout objekty vyšší než je výška portálu vaší tiskárny. Výšku portálu lze upravit v dialogovém okně nastavení tiskárny. Tato výška portálu udává vertikální vzdálenost mezi špičkou trysky a systémem nesoucím tiskovou hlavu. Důvodem tohoto omezení je, že tisková hlava bude muset sestoupit na podložku tisku, aby vytiskla druhý objekt. To znamená, že při tisku druhého objektu se může portál dotknout prvního objektu. Teoreticky může být poslední tištěný objekt vyšší než je výška portálu, ale pro jednoduchost to Cura stejně nedovolí.
* Objekty by měly být dále od sebe, aby se zabránilo tiskové hlavě zasáhnout dříve vytištěné modely na straně.
* Pořadí, ve kterém jsou objekty tisknuty, je pevné a optimalizované, aby to umožňovalo tisknout objekty blíže k sobě. Pokud vaše tisková hlava není souměrná, může to ušetřit spoustu místa na podložce tisku.

**Jeden po druhém je k dispozici pouze u jednoduchého extrudéru. Pokud používáte tiskárnu s více extrudéry, je nutné, aby se toto nastavení zobrazilo až po deaktivaci všech extrudérů kromě jednoho.**