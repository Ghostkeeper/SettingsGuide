Je počátek ve středu
====
Pokud je toto nastavení povoleno, je souřadnice 0,0 tiskárny nastavena tak, aby byla ve středu objemu tisku a ne v levém předním rohu.

U některých tiskáren považuje firmware souřadnice 0,0 za střed objemu tisku. To je běžné u tiskáren stylu delta, které obecně mají spíše válcové objemy než kvádry.

Pokud je nulová souřadnice tiskárny ve středu, bude konečný g-kód obsahovat negativní i kladné souřadnice. Počátek souřadnic bude uprostřed objemu tisku Cury. Cura také ve středu zobrazí svou tříbarevnou značku souřadnic. Souřadnice souborů 3MF však budou stále považovány, jako by počátek souřadnic byl v levém předním rohu tiskárny, protože to vyžaduje formát souboru 3MF.

**Protože se jedná o nastavení stroje, nebude obvykle uvedeno v normálním seznamu nastavení. Zaškrtávací políčko pro toto nastavení je však v dialogu nastavení tiskárny, které lze nalézt v seznamu přidaných tiskáren v dialogu předvoleb.**