Minimální objem aktivační věže
====
To indikuje množství materiálu, které má být vypláchnuto pokaždé, když se změní extrudér. Myšlenka je taková, že určitý objem bude z trysky vytékat, když bude v pohotovostním režimu. Účelem tohoto nastavení je vyrovnávací objem indikovaný tímto nastavením.

![Vytlačovaný objem je zvýrazněn zeleně](../images/prime_tower_cs.svg)

Tento parametr označuje minimální množství materiálu, které má být propláchnuto. Obrysy aktivační věže však budou kompletně dokončeny, takže lze vyčistit více materiálu v závislosti na tom, jak dobře se objem vyrovná s objemem obrysu.

Některé tiskárny mají několik samostatných trysek, zatímco jiné podávají více materiálů do jedné trysky. Dobrá hodnota pro toto nastavení se mezi těmito dvěma typy velmi liší.
* Pokud má vaše tiskárna více trysek, jedinou potřebou pro naplněný objem je rekuperace ztraceného materiálu, když byla aktivní druhá tryska. Vypustilo se trochu materiálu a ztratil se tlak v komoře trysky. Malé množství materiálu stačí k tomu, aby se komora trysky vrátila zpět na původní tlak. Více tekuté materiály, jako je PETG, obvykle vyžadují větší objem penetrace. Pokud je minimální objem aktivační věže příliš nízký, dojde na začátku cesty vytlačování, po přepnutí extruderu k [pod-extruzi](../troubleshooting/underextrusion.md).
* Pokud vaše tiskárna vtlačuje více vláken do stejné trysky, musí aktivační věž také vyčistit zbývající materiál z trysky. Při retrakci předchozího vlákna vždy zůstane v trysce malá kapka, protože materiál tam byl pod tepelnou zónou a nedochází k jeho tažení spolu se zbytkem vlákna. Minimální objem aktivační věže proto musí být alespoň objemem celé horké zóny trysky. V praxi to potřebuje podstatně víc, protože když se nové vlákno zasune dovnitř, smíchá se se starým vláknem a vytlačí staré vlákno stranou. Aby se veškerý starý materiál dostal ven, je zapotřebí mnohem více materiálu jako zásobníku, aby se zabránilo kontaminaci. To vše je podstatně více než obava z rekuperace tlaku v trysce v důsledku úniku, takže únik už není problém. Pokud je minimální objem aktivační věže příliš nízký, materiály se v tomto případě smíchají, takže barvy budou více vybledat nebo po rozpuštění rozpustného podpůrného materiálu ve vodě, budete mít v tisku důlky.

Příliš vysoké nastavení minimálního objemu aktivační věže je relativně neškodné, ale tisk trvá déle a ztrácí se více materiálu. Objem bude omezen [Velikostí aktivační věže](prime_tower_size.md). Objem lze nastavit vyšší než celkový objem aktivační věže na této vrstvě, ale pokud je aktivační věž plánována plná, nebude to mít na tisk žádný vliv.

Objem může být pro každý extrudér různý, takže finální věž může mít pro každý z extruderů různý počet kontur.