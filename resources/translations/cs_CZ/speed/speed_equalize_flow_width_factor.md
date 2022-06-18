Poměr vyrovnání průtoku
====
Tato funkce umožňuje změnit způsob, který tiskárna použije k úpravě šířky linie: namísto změny průtoku materiálu tryskou tiskárna změní rychlost, kterou se tryska pohybuje.

Tiskárny FFF jsou notoricky známé tím, že neumí měnit rychlost, kterou materiál vytéká z trysky. Pokud tiskárna změní rychlost podavače, trvá zlomek sekundy, než se to skutečně projeví ve změně průtoku. V té době už může být tryska v závislosti na rychlosti tisku několik milimetrů za bodem, kde měla být upravena rychlost průtoku. Ještě horší je to v případě, že tiskárna má podavač oddělený od tiskové hlavy a mezi nimi je bowdenová trubička.

Místo změny rychlosti posuvu může tiskárna měnit také rychlost pohybu tiskové hlavy. Tisková hlava může zrychlovat mnohem rychleji, a tak může získat lepší kontrolu nad šířkou linie. Pokud tisková hlava zrychlí, zatímco rychlost toku zůstane stejná, natáhne se stejné množství materiálu na větší délku, čímž se zmenší šířka linie. Pokud tisková hlava zpomalí, stejné množství materiálu se natáhne na menší plochu, čímž se šířka linie zvětší.

Toto nastavení je poměrové. Může upravovat průtok (0 %) nebo rychlost tisku (100 %) nebo kombinaci obou. Poměr může dokonce překročit 100 %, což znamená, že se sníží průtoková rychlost, aby se vytvořily silnější linie, ale ještě více se sníží rychlost, aby se to kompenzovalo.

Zvýšení tohoto poměru na 100 % znamená, že se ke změně šířky linie použije rychlost namísto průtoku, což má na tisk následující účinky:
* Šířka linie je pravděpodobně přesnější, což zlepšuje rozměrovou přesnost tisku.
* Průtoková rychlost bude zachována stejná, což zvyšuje spolehlivost tisku, zejména u exotických materiálů.
* V některých místech se tisková hlava pohybuje rychleji, což má za následek zvlnění.

Toto nastavení se vztahuje pouze na odchylky šířky linií způsobené přizpůsobením linií šířce tenkých dílů a ostrých rohů. Změny průtoku způsobené nastavením, jako je rozdílná šířka linie pro výplň a stěnu, nebudou kompenzovány, stejně jako vlastnosti jako přemostění nebo zažehlení. Tiskárny, které implementují funkci Linear Advance nebo podobné kompenzační funkce, by je měly používat i v případě, že je toto nastavení nastaveno na 100 %, protože v důsledku těchto nastavení může stále docházet ke změnám průtoku.