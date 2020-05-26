Zarovnání švu v Z
====
Tento parametr umožňuje zvolit, kam se má umístit šev každého obrysu. K dispozici je několik možností, které vám umožňují kontrolovat, kde je šev umístěn, aby se minimalizoval jeho dopad, nebo vám to umožní ho snadněji odstranit během následného zpracování.

Šev je místo, kde obrys začíná a končí tisk. I když je cesta trysky uzavřeným kruhem, v místě, kde začíná a končí vytlačování, je šev, protože proces tisku není nikdy úplně přesný. S tímto nastavením lze viditelnost švu minimalizovat skrytím nebo rozložením.

Uživatelsky specifikované
----
![Uživatelsky specifikované](../../../articles/images/z_seam_type_user.png)

Tato možnost umožňuje vybrat umístění manuálně. Šev bude umístěn v rohu nejblíže k vybranému umístění. To obvykle sjednotí linie velmi těsně k rohům, což umožňuje snadno šev odříznout. Rovněž umožňuje přesnou kontrolu umístění švu.

Ve výchozím nastavení je vybráno umístění na zadní straně tiskárny. Myšlenka je taková, že uživatelé obvykle nechávají přední část svých modelů obrácenou k přední části tiskárny, takže umístění na zadní straně lépe skryje šev.

Nejkratší
----
![Nejkratší](../../../articles/images/z_seam_type_shortest.png)

Tato varianta jednoduše minimalizuje délku cesty do švu, aniž by se snažila ho umístit na konkrétní místo. Jelikož je cesta kratší, ušetříte na cestách trochu času. Šev bude také o něco menší, protože tam, kde tryska dopadne na obrys, bude umístěno méně výtoku.

Požadovaná preference rohu je vždy udržována výběrem rohu poblíž místa, kde je umístěna tryska. Nejbližší roh není vybrán, ale vážená preference se používá k minimalizaci posunu, ale také k použití vhodného rohu pro parametr [Preference rohového švu](z_seam_corner.md).

Náhodné
----
![Náhodné](../../../articles/images/z_seam_type_random.png)

Pro šev se vybere náhodné umístění po obvodu. Toto náhodné umístění se mění v každé vrstvě, takže šev je rozložen téměř rovnoměrně kolem modelu. Protože švy různých vrstev nejsou zarovnány, bude šev stěží viditelný. Povrch však bude celkově vypadat trochu špinavější.

Nejostřejší roh
----
![Nejostřejší roh](../../../articles/images/z_seam_type_sharpest.png)

Šev se umístí do nejostřejšího rohu celého obrysu podle preference rohu vybrané v parametru [Preference rohového švu](z_seam_corner.md). To může vést k delším přesunům, ale zajišťuje to, že šev je skrytý nebo vystavený maximu podle předvolby nastavené pro rohy.


