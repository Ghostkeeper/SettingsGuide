Kapky (blobs)
====
Blobs jsou malé kapky na boku modelu. Někdy to jsou jen body. Někdy jsou to pruhy. Představují vizuální vadu povrchu a mohou zvýšit tření mezi povrchy, které se musí k sobě v mechanismu klouzat.

![Nějaké kapky na povrchu](../../../articles/images/blobs.jpg)

Existuje několik možných příčin kuliček. Je to jedna z nejčastějších poruch 3D tisku. Tento článek uvádí některé možné příčiny a jejich řešení.

Tryska se zpomaluje
----
Pokud se tryska pohybuje v určité cestě pomaleji než v jiných, uloží tam více materiálu. Tento materiál vytéká ven z povrchu stěny a vytváří kapku.

Přísun materiálu se tím pravděpodobně sníží. I když se však extrudér pohybuje pomaleji, může to trvat několik sekund, než se odpovídajícím způsobem sníží průtok vycházející z otvoru trysky. Během této doby bude vytlačováno příliš mnoho materiálu, což dává tyto kapky.

Chcete-li bojovat proti tomuto jevu, podívejte se na následující nastavení:
* Vyrovnejte rychlost [vnější stěny](../speed/speed_wall_0.md) tak, aby byla identická s rychlostí toho, co je před ní vytištěno (jako [vnitřní stěny](../speed/speed_wall_x.md) nebo [výplň](../speed/speed_infill.md). Pak nedojde ke zpomalení.
* Zvyšte hodnotu [ryvu (jerku) vnější stěny](../speed/jerk_wall_0.md). To zabrání zpomalení trysky v rozích.
* Můžete snížit hodnotu [rozlišení](../meshfix/meshfix_maximum_resolution.md) a zvýšit [odchylku](../meshfix/meshfix_maximum_deviation.md), abyste zabránili ovladači pohybu zpomalit trysku, abyste udrželi krok s g-kódy, které musí zpracovat.
* Deaktivujte parametr [Kompenzovat překrytí vnější stěny](../shell/travel_compensate_overlapping_walls_0_enabled.md). Tento parametr se používá k vytvoření nových pohybových příkazů s různými rychlostmi posuvu. Deaktivace této funkce snižuje počet příkazů pohybu ve stěně.

Tryska se zastaví
----
Pokud se tryska zastaví během tisku vnější stěny, je velmi pravděpodobné, že čeká, až procesor vaší 3D tiskárny zpracuje nové příkazy k pohybu. Software pro plánování pohybu tiskárny obvykle udržuje vyrovnávací paměť s předem zpracovanými příkazy připravenými pro takové případy, když již byly zpracovány příkazy k pohybu, takže tiskárna přesně zná časy aktivace krokových motorů nebo jiných pohybů. Pokud dojde tato vyrovnávací paměť, hovoříme o "podběhu vyrovnávací paměti". To způsobí, že se na povrchu objeví kapky.

Chcete-li tomu zabránit, měli byste snížit rozlišení g-kódu.
* Zvyšte parametr [Maximální rozlišení](../meshfix/meshfix_maximum_resolution.md), který umožňuje aplikaci Cura produkovat delší segmenty linií.
* Zvyšte parametr [Maximální odchylka](../meshfix/meshfix_maximum_deviation.md), což umožňuje aplikaci Cura dále snížit rozlišení odchylkou od původní cesty.
* Deaktivujte parametr [Kompenzovat překrytí vnější stěny](../shell/travel_compensate_overlapping_walls_0_enabled.md). Pokud se vnější stěna překrývá s ostatními vnějšími stěnami, bylo by to části stěny odlišné šířky linií, ale to vyžaduje další příkaz k pohybu. Chcete-li omezit ovládání pohybu, můžete toto nastavení vypnout. To však může také způsobit nad-extruzi do těchto stěn, což také způsobuje kapky.
* Snižte [rychlost tisku vnější stěny](../speed/speed_wall_0.md). Tím se snižuje rychlost provádění příkazů pro přesun, což umožňuje CPU dohnat.

Přesuny prochází stěnami
----
Přestože se Cura obecně vyhýbá co nejvíce překročení vnější zdi, je to někdy nevyhnutelné. Pokud tryska nese vytékající  materiál, když prochází vnější stěnou, může být tento materiál tam setřen a zanechává kapku.

Je možné se vyhnout této příčině kapek úpravou následující parametrů:
* Ujistěte se, že je aktivována funkce [objezd](../travel/retraction_combing.md). To umožňuje, aby tryska obcházela stěny co nejvíce, místo aby jimi procházela.
* Aktivujte [Z-skoky](../travel/retraction_hop_enabled.md). Pokud jsou stěny zkřížené, tryska se bude pohybovat trochu nahoru, aby prošla přes stěny místo aby je překročila. Vytékající materiál pravděpodobně nebude setřen na zdi, ale v bodě, kde tryska přistane po pohybu. Cura se bude vždy snažit přistát na výplni nebo na plášti, pokud to bude možné.
* Ujistěte se, že [pořadí tisku stěn je optimalizováno](../shell/optimize_wall_printing_order.md). To snižuje počet pohybů prováděných při tisku na stěny, což umožňuje efektivnější pohyby a snižuje riziko, že některé z těchto pohybů budou muset projít vnější stěnou.

Zvýšený tlak
----
Pokud je tryska nadměrně vytlačována, může být vytlačování nepravidelné. To může někdy najednou najít cestu ven, když se vytiskne určitý roh vašeho tisku (zejména na převisech). Někdy tento přetlak exploduje a zanechává velkou skvrnu. Obvykle potom bude pruh za kapkou postupně klesajícího tlaku.

Pro snížení tohoto efektu je třeba vzít v úvahu některé parametry:
* Zmenšete [šířku linií stěny](../resolution/wall_line_width.md). To obecně snižuje tlak v komoře trysky.
* Zmenšete [vnoření vnější stěny](../shell/wall_0_inset.md). Toto nastavení způsobí, že vnější stěna překrývá sousední vnitřní stěnu, takže stěna je tlačena silněji proti vnitřní stěně, což zvyšuje pevnost. Tento tah však také zvyšuje tlak uvnitř tryskové komory.

Mokré vlákno
----
Pokud vlákno nahromadilo vlhkost, zatímco bylo stále na cívce, bude tato voda zahřívána v trysce za bod varu. Vodní pára exploduje z trysky, když je z ní vytlačena. Tato malá exploze může způsobit prasknutí plastu, což má za následek malé kapky na povrchu.

Švy
----
Šev bude vytvořen tam, kde je obvod vnější stěny zahájen a uzavřen. Není to to, co lidé obvykle nazývají kapkou, i když má podobný vzhled. V článku o [švech](seam.md) najdete informace o tom, jak tento účinek snížit.

Pokud je parametr [Zarovnání švu v Z](../shell/z_seam_type.md) nastaven na "Náhodné", šev se rozloží kolem modelu a vytvoří všude malé švy. Může to vypadat přesně jako skvrna, i když je to vlastně šev. Upravte parametr Zarovnání švu v Z a skryjte tyto švy.