Prověšování
====
Výroba taveného vlákna spočívá v nanesení linie roztaveného plastu. Tato linie je měkká a pokud na ničem nespočívá, klesá. Toto se nazývá prověšování.

![Prověšování v převislých částech](../../../articles/images/sagging.jpg)

Prověšování má tendenci dodávat převislým částem strnulý vzhled. Spíše než hladké sledování plánovaného povrchu modelu bude příliš nízká. V extrémních případech je spodní strana povrchu natolik roztřepená, že můžete vidět dutý vnitřek tisku.

Příčiny
----
Prověšování není vlastně ani stěží způsobeno gravitací. Je hlavně způsobeno silou materiálu, který je vytlačován z trysky. Tento jev zažijí dokonce i tiskárny, které jsou obráceny vzhůru nohama nebo které tisknou v mikrogravitaci. Tlak, kterým je materiál vytlačován, tlačí materiál dolů, protože tryska je (normálně) orientována dolů.

Normálně je tlak v komoře trysky nutný k vytlačení (viskózního) materiálu ven a jeho vyrovnání do linie širokého, plochého materiálu tím, že se rozdrtí mezi tryskou a předchozí vrstvou nebo podložkou tisku. Pokud však v předchozí vrstvě nebyl žádný materiál, nebude existovat žádný protitlak pro zploštění kuličky. Místo toho bude tlačena příliš daleko dolů.

Přemostění
----
Jednou technikou pro zlepšení kvality převisů je optimalizace vyplnění mezery přesahu. To zahrnuje snížení tlaku, kterým je materiál vytlačován z trysky, stejně jako pokusy o zvýšení viskozity materiálu nebo  urychlení jeho tuhnutí. Kromě toho mohou být tištěné linie přesměrovány, aby se zmenšila vzdálenost, po které nejsou linie podpírány. Všechny tyto techniky se nazývají „přemostění“.

Cura nabízí řadu způsobů, jak zlepšit přemostění. Poskytne to ještě více, pokud jsou povoleny [parametry přemostění](../experimental/bridge_settings_enabled.md). Aktivace této funkce vyvolá další parametry a také upraví parametry tisku pro výchozí přemostění oblastí.

Při konfiguraci přemostění pro snížení prověšení zvažte následující nastavení:
* Snížením [teploty tisku](../material/material_print_temperature.md) se termoplast stává viskóznějším, což snižuje jeho ochabnutí.
* Snížení [výška vrstvy](../resolution/layer_height.md) nebo [šířky linie](../resolution/line_width.md) snižuje tlak, kterým je materiál vytlačován z trysky. To samo o sobě snižuje ochabování, ale tyto linie mají také nižší tepelnou kapacitu, což zvyšuje účinnost ventilátorů tiskové hlavy při chlazení.
* Snížení [rychlosti tisku](../speed/speed_print.md) také snižuje tlak, kterým je materiál vytlačován z trysky. V tomto případě se tepelná kapacita nesníží, ale ventilátory foukají na materiál déle, což také zvyšuje jejich účinnost a snižuje ochabování. Pokud jsou aktivována nastavení přemostění, lze rychlost tisku přemostění upravit samostatně. Snížení [rychlost tisku stěn přemostění](../experimental/bridge_wall_speed.md) je účinné při zlepšování převisů. Snížení rychlosti tisku přemostění (../experimental/bridge_skin_speed.md) je účinné při snižování průvěsů v úplně vodorovných převislých oblastech. K dispozici je také varianta, která umožňuje upravit [rychlost pro tisk převislé stěny](../experimental/wall_overhang_speed_factor.md). Toto nastavení se použije, i když povrch není zcela vodorovný, což umožňuje získat rychlost tisku, specifickou pro převislé stěny, pouze pro šikmé stěny.
* Snížení [toku](../material/material_flow.md) je podobné redukci šířky linií. Tím se sníží tlak, kterým je materiál vytlačován, jakož i tepelná kapacita, která umožní materiálu rychleji tuhnout. Tento parametr lze také upravit pouze pro přemostěné oblasti, zvlášť pro [stěny](../experimental/bridge_wall_material_flow.md) nebo [plášť](../experimental/bridge_skin_material_flow.md). Snížení toku na velkých plochách má sklon k vytváření dutin na povrchu a také k nepravidelnému vzhledu, takže přesah může mít i nadále špatný vizuální vzhled, pokud se toto změní. Rozměrová přesnost by se však měla zlepšit.
* Zvyšte [Rychlost ventilátoru](../cooling/cool_fan_speed.md) pro rychlejší chlazení materiálu. Tím se materiál rychleji zpevní, čímž se zabrání průvěsu.
* Vytiskněte stěny [zevnitř ven](../shell/outer_inset_first.md). To umožní, aby vnější stěna spočívala na sousední vnitřní stěně, což zabrání jejímu pádu. Tato metoda je zvláště účinná při malé [šířce linií](../resolution/wall_line_width_0.md).

Podpěra
----
![Podpůrná struktura podpírá model](../../../articles/images/support_enable.png)

Nejobvyklejším a nejspolehlivějším způsobem, jak vylepšit přesahy, je jejich podpora během tisku pomocí podpěrné struktury. Tato nosná struktura se potom po ztuhnutí materiálu odstraní. Podpěra tisku je velmi účinná při prevenci ochabování, bez ohledu na velikost převislé oblasti, ale vyžaduje více času a materiálu a zanechává jizvu tam, kde byla podpěra připojena.

Cura má dvě techniky pro generování podpěry. Existuje výchozí metoda „oblasti podpěry“, která se vygeneruje, pokud je [podpěra povolena](../support/support_enable.md). Pokud je [povolena stromová podpěra](../experimental/support_tree_enable.md), je vygenerována jiná metoda stromové podpěry. Výchozí technika je obecně účinnější při snižování průvěsů, ale někdy také poskytuje nerovnoměrnější spodní stranu. Stromová podpěra má tendenci nechat řetězce prohýbat se trochu více, ale také rovnoměrněji.

Při generování podpěry se Cury automaticky rozhodne, kam podpěru umístit. Ve většině případů to funguje dobře, ale u některých modelů může být podpěra příliš velká nebo příliš malé. Naštěstí, Cura také nabízí mnoho metod přizpůsobení umístění podpěr.
* Úprava [úhlu převisu](../support/support_angle.md) je nejjednodušší metodou úpravy množství podpěr, které mají být umístěny. Toto nastavení musíte upravit tak, aby byly podpírány všechny vaše převislé oblasti. Tento parametr také určuje oblasti, které budou během přípravné fáze vykresleny červeně. Zmenšení úhlu přesahu způsobí tisk více podpěr, což sníží průhyby ve více částech tisku, ale také to zabere více času a materiálu a způsobí další jizvy.
* Převislé části nad ostatními částmi můžete odstranit nastavením parametru [Umístění podpěry](../support/support_type.md) na „Pouze v dotyku s podložkou tisku“. Pokud místo toho nastavíte tento parametr na „Všude“, se můžete vyhnout špatnému převisu.
* Ujistěte se, že nastavení parametru [Minimální podpíraná plocha](../support/minimum_support_area.md) nevymaže tenké části podpěry.
* Pomocí nástroje pro blokování podpěr můžete do své scény umístit kostky, abyste tam zabránili vytváření podpěry. Můžete také vybrat tyto bloky a v nástroji nastavení podle modelu pověřit Curu, aby je „vytiskla jako podpěru“. Poté budou vytištěny jako nová podpěra. Tímto způsobem můžete pečlivě přizpůsobit přesné umístění, kde je podpěra umístěna. Dokonce si můžete do Cury načíst úplný 3D model s přesným tvarem vaší podpěry a požádat Curu, aby ho vytiskla jako podpěru v ​​nástroji nastavení podle modelu.

I když je převis podpírán podpěrou, může se trochu prohýbat. Aby byla podpěra odstraněna, je mezi modelem a podpěrou udržována určitá [vertikální vzdálenost](../support/support_z_distance.md). Model se o tuto vzdálenost bude prohýbat, než dosáhne účinnosti podpěry, takže zmenšení vzdálenosti Z sníží poklesy (ale bude obtížnější podpěru odstranit). Některé materiály jsou navrženy tak, aby se daly snadněji odstraňovat, a to chemickým navázáním na stavební materiál nebo rozpouštěly. Tyto materiály si mohou dovolit zmenšit vzdálenost Z, což dále snižuje průhyby, zatímco umožní opěrku odstranit později. Tisk se může také prohýbat mezi podpůrnými liniemi, takže zmenšení [vzdálenost mezi podpůrnými liniemi](../support/support_line_distance.md) také sníží průhyby (ale zvýší dobu tisku a bude ještě obtížnější podpěru odstranit).

Úprava modelu
----
Pokud máte volnost upravovat tištěný model, ​​může to přinést mnohem čistší výsledek než pokus o vyplnění nebo podpěru přesahů. Místo toho, abyste nechali materiál v převisech poklesnou, navrhněte a nasměrujte svůj model tak, aby neexistovaly žádné převisy

![Tato orientace umožňuje tisknout objekt s velmi malou podpěrou](../../../articles/images/support_minimise_overhang.png)

Nejzákladnějším trikem při aplikaci tohoto je otočení modelu. Pokud je vaše tiskárna schopna tisknout úhly 45 stupňů bez průvěsů, můžete otočit model se svislou a vodorovnou částí tak, aby existovaly dva sklony 45 stupňů, což mírně snižuje kvalitu svislé stěny, ale zabraňuje prohýbání vodorovné části. Dbejte však na to, aby nedocházelo k tomu, aby kontaktní plocha s podložkou tisku byla příliš malá, jinak by mohl tisk z tiskové podložky vypadnout a dále se poškodit.

Přidání zkosení může také pomoci snížit množství převisů v modelu s relativně malým množstvím přidaného materiálu. Cura nabízí automatizovaný způsob přidávání zkosení do vašeho modelu pomocí funkce [Učinit převis tisknutelný](../experimental/conical_overhang_enabled.md). Přidání zkosení v podstatě přidá nosnou strukturu ke skutečnému modelu. Poté budou transparentně vytištěny v modelu, který vypadá lépe. To také šetří materiál ve srovnání s tiskem podpěry, protože materiál podpěry rychle přivádí síly do zbytku modelu. A nakonec bude váš objekt pevnější.

Obecně platí, že při navrhování objektů pro 3D tisk je nejlepší se převisům vyhnout. Pokud to geometrie objektu neumožňuje, zvažte rozdělení modelu na několik částí a jejich následné sestavení.
