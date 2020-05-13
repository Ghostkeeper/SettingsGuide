Posun vrstvy
====
K posunu vrstvy dochází, když nejsou vrstvy v tisku správně naskládány na sebe. Pokud se tisková hlava z jakéhokoli důvodu během tisku vrstvy posune, tiskárna pokračuje v tisku s ofsetem. Horní strana tisku je poté odsazena od spodní strany.

![Posun jedné vrstvy kvůli překážce](../../../articles/images/layer_shift_single.jpg)

Příčiny
----
Posuny vrstev přicházejí ve dvou formách.

První typ posunu vrstvy je způsoben tím, že tisková hlava je někde po cestě blokována To pak způsobí posun vrstvy v místě uprostřed tisku. Může to být způsobeno tím, že uživatel během tisku umístí něco do portálu nebo když tisková hlava narazí na jiný objekt během tisku v režimu [jeden po druhém](../blackmagic/print_sequence.md). Pokud se tisková hlava srazí s objektem a nemůže se pohybovat, motory vynechají určité kroky. Pokud tiskárna nedokáže zjistit, že k tomu došlo, bude pokračovat bez tohoto pohybu a posouvat zbytek tisku.

K jinému typu posunu vrstvy dochází, když samotná tisková úloha klade příliš velkou sílu na tiskovou hlavu, což způsobuje, že krokové motory tiskárny ztratí kroky. Kdykoli dojde ke ztrátě kroků, tisk se odtud posouvá. Obecně se ztracené kroky vyskytují na stejném místě v každé vrstvě kvůli obzvláště ostrému rohu. Výsledkem je, že celý tisk nebo jeho část se zdá být zkosená.

Prevence
----
Prvnímu posunutí vrstvy obvykle nastavení Cura nebrání. Cura je navržena tak, aby se zabránilo nárazům do stran objemu tisku. Pokud je velikost tiskového objemu v aplikaci Cura zadána správně, neměla by vygenerovat g-kód, který se pohybuje mimo objem tisku. Pokud vygeneruje takový g-kód, dialogové okno parametry tiskárny ve správě tiskárny vám umožní upravit velikost objemu tisku a provést opravu. Také byste se měli ujistit, že v objemu tisku nejsou žádné překážky, které by se tisková hlava nebo pohybový systém mohly během tisku dotknout. Tiskárny obecně nedokážou rozpoznat tento druh problému, takže budou pokračovat v tisku z ofsetové pozice. Zkontrolujte kabely, které jsou v cestě a ujistěte se, že všechny kabely jsou dostatečně dlouhé, aby umožnily tiskárně pohybovat se v plném rozsahu pohybu. Zkontrolujte také, zda se krokové ovladače na desce plošných spojů tiskárny nepřehřívají, což by mohlo dočasně zastavit jejich provoz.

Druhý typ posunu vrstvy, ten, který probíhá nepřetržitě během tisku, je pravděpodobně způsoben přílišnou silou vyvíjenou na váš pohybový systém. Existuje několik možných řešení.

Nejprve byste měli prozkoumat vaše zařízení. Jsou řemeny napnuté? Pokud ne, můžete hledat způsob, jak je utáhnout. Některé tiskárny mají nastavitelné polohy motorů, které vám umožňují napnout pásy. Prokluzují kladky? Utáhněte šrouby řemenice, pro jistotu. Konečně je běžným elektrickým problémem to, že motory nedostávají dostatečný proud, aby generovaly dostatečnou sílu, aby provedly ostrý obrat. V takovém případě zkontrolujte, zda je napájení dostatečné.

Pokud hardware funguje dobře, můžete také upravit Curu, aby na hardwaru byla o něco jednodušší. Zde je několik nastavení, která můžete upravit:
* Snižte hodnotu [ryvu (jerku)](../speed/jerk_print.md). To způsobí, že se tisková hlava před vytvořením rohů zpomalí. Díky tomu je roh měkčí, hlava vjíždí do rohu namísto tvrdého obratu.
* Snižte velikost [zrychlení](../speed/acceleration_print.md). To způsobí, že se tisková hlava před vytvořením rohu opatrněji a dříve zpomalí (ačkoliv rychlost, kterou tisková hlava projde horní částí zatáčky, není ovlivněna; to je účel nastavení ryvu (jerku).
* Snižte [rychlost přesunů](../speed/speed_travel.md). Tím se snižuje síla, kterou tryska klouže po dříve vytištěných částech.
* Aktivujte [Z-skok při retrakci](../travel/retraction_hop_enabled.md). Tím se zabrání tomu, aby tisková hlava zasáhla dříve vytištěné části, pokud vyčnívají mírně nahoru kvůli kapkám nebo deformacím.

