Rozdělení vrstev
====
Přilnavost mezi vrstvami je často nejvíce slabým místem struktury 3D tištěných objektů. Pokud adheze mezi vrstvami během tisku nebo krátce po něm selže, nazývá se to štěpení vrstev, oddělení vrstev nebo delaminace.

![Rozdělení vrstev na straně tohoto kontejneru](../../../articles/images/layer_splitting.jpg)

S rozštěpením vrstev je obtížné se vypořádat, protože tisk se vždy rozdělí v nejslabším článku. Níže uvedené návrhy jsou zaměřeny na to, aby byl tisk konzistentnější a extruze spolehlivější, aby se odstranily slabé články v přilnavosti vrstev.

Deformace
----
Většina rozdělení vrstev je způsobena [deformací](warping.md). To se týká zejména semikrystalických polymerů. Ty při ochlazování vytvářejí mikroskopické krystalové struktury, které se při vytváření těchto struktur hodně smršťují. Nejběžnější formou deformace je deformace spodní části tisku směrem nahoru, která nezpůsobuje rozdělení vrstev. Pokud však k deformaci dojde výše v tisku, způsobí ohnutí vrstev od sousedních a jejich rozdělení.

Aby se zabránilo deformaci ve vyšších vrstvách, lze provést řadu opatření, která snižují pravděpodobnost rozdělení vrstev:
* Použití soustředného [horního/dolního vzoru](../top_bottom/top_bottom_pattern.md). Lineární vzor má linie, které se smršťují stejným směrem, což tyto vrstvy táhne stejným směrem nahoru. Soustředný vzor tuto sílu rozptyluje.
* Zvýšení hodnoty [teplota objemu tisku](../material/build_volume_temperature.md) snižuje deformace způsobené [žíháním](https://en.wikipedia.org/wiki/Annealing_%28glass%29) plastu. K tomu potřebuje tiskárna uzavřený prostor tisku, který udržuje uvnitř teplo.
* Podobně použití [ochranného štítu](../experimental/draft_shield_enabled.md) udržuje část tepla uvnitř, i když méně efektivně než uzavřený tiskový prostor.
* Zabránění ostrým rohům ve 3D modelu. Přidáním zaoblení do ostrého rohu zabráníte tomu, aby se linie pláště přímo dotýkaly podkladových stěn. Často se jedná o místo, kde dojde k rozdělení vrstvy.
* Použití materiálu, který se tolik nesráží. Například PLA způsobuje menší deformace než polypropylen. Většina lidí by si však materiál vybírá podle specifických požadavků, takže to pro ně nepřipadá v úvahu.

Nedostatečný přítlak
----
Aby vrstvy dobře přilnuly jedna k druhé, je vhodné plast silně přitlačit na předchozí vrstvu. Pokud tryska nevytlačuje dostatečné množství materiálu nebo materiál není dostatečně silně přitlačen k předchozí vrstvě, snižuje se tím adhezní síla mezi vrstvami, což umožňuje jejich snadnější rozdělení. I když to nezpůsobí okamžité rozdělení vrstvy, snižuje to také pevnost výsledného dílu.

To je problém především stěn. Plášť má tak velkou plochu, že není náchylný k rozštěpení. Mezi výplní a stěnami zajišťují stěny většinu přilnavosti vrstev, protože výplň se často tiskne velmi rychle, pomocí řídce rozložených linií a často není vertikálně poskládaná.

Pro zajištění dostatečného tlaku je důležité zajistit, aby nedocházelo k [podextruzi](underextrusion.md). Uplatňují se všechny příčiny podextruze, ale několik z nich se týká zejména dělení vrstev:
* Při pozastavení tisku v polovině trvá chvíli, než se vytlačování opět rozběhne. Skript Pause at Height má možnost <!--if cura_version >= 4.7-->předělat vrstvu<!--endif--><!--if cura_version < 4.7:předělat několik posledních vrstev-->. Tím se materiál před pokračováním směrem nahoru naplní, čímž se zabrání vytvoření slabé vrstvy při nedostatečném tlaku v trysce.
* Snížením [rychlost tisku stěn](../speed/speed_wall.md) se stěny tisknou konzistentněji. Tím se sníží možnost vzniku slabých míst a zároveň se omezí nedotisk na stěnách.
* Snížení [výšky vrstvy](../resolution/layer_height.md) nebo [šířky linie stěny](../resolution/wall_line_width.md). Vysoké průtoky vyžadují vyšší tlak. Pokud ho tiskárna není schopna zajistit, vytlačí se nedostatečné množství materiálu, aby se vyplnily silné vrstvy nebo široké linie. To způsobí, že tisk bude slabší.
* Zvýšení [teploty tisku](../material/material_print_temperature.md) aby se materiál rozléval do větší šířky a plně využíval styčnou plochu, nikoli aby zůstával soustředěný ve středu linie.
* Snížení [vzdálenosti retrakce](../travel/retraction_amount.md). Při dlouhých retrakcích dochází k úniku většího množství materiálu během retrakce, což později způsobuje nederextruzi. Také se více přerušuje tok. Poté trvá déle, než se tok stabilizuje. Zkrácení délky retrakce snižuje možnost vzniku slabého článku po výšce výtisku v důsledku nestejnoměrného toku.

Nedostatečná povrchová plocha
----
Přilnavost mezi vrstvami je funkcí síly vazby mezi materiály vynásobené velikostí povrchu, na který se mohou vázat. Zvětšení plochy povrchu pomáhá snížit pravděpodobnost rozštěpení vrstvy.

Nejdůležitějším parametrem je [tloušťka stěny](../shell/wall_thickness.md). Více stěn výrazně zvětšuje plochu. Stěny se tisknou pomaleji a jsou umístěny v místě, kde se začnou štěpit, takže jsou velmi účinným způsobem, jak zvýšit přilnavost vrstev. Tisk více stěn však také drasticky prodlužuje dobu tisku a zvyšuje spotřebu materiálu.

Nedostatečná plocha je často problémem při tisku velkých výtisků, kde dochází k silné deformaci, pouze s jednou stěnou a bez výplně. Stěna se v důsledku deformace začne prohýbat a není nic, co by to zastavilo. To by mohl být důvod, proč zakázat použití režimu [spiralizace](../blackmagic/magic_spiralize.md), protože tiskne pouze jednu stěnu a zabraňuje generování výplně. Místo toho bude možná nutné tisknout se dvěma stěnami a manuálně nastavit hustotu výplně na 0 %, abyste dosáhli podobného efektu.

Nekompatibilní materiály
----
U výtisků s různými typy plastů dbejte na to, aby se plasty vzájemně lepily. Plasty s výrazně odlišným poměrem smrštění se obvykle nedokážou vzájemně přilepit. Rozdílné chemické účinky také způsobí, že se plasty budou navzájem odpuzovat, což zabrání jejich slepení. Pokud k tomu dojde ve velké ploché oblasti uprostřed tisku, je pravděpodobné, že se tam tisk rozpadne.

Aby k tomu nedošlo, může být nutné navrhnout mechanický blokovací spoj mezi oběma povrchy. K různým materiálům přistupujte, jako by byly vytištěny samostatně, s tím rozdílem, že je později nebude třeba sestavovat.