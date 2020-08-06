Rychlost chlazení
====
Toto nastavení říká Cuře, jak rychle se vaše tryska ochlazuje, když není zahřátá. Používá se pro předpovídání, kdy začít předchlazovat trysku před přepnutím extruderů.

![Trysky se zahřívají v předstihu před přepnutím extruderů](../images/temperature_regulation_cs.svg)

Při přepínání extruderů spustí Cura před-chlazením aktivní trysky před jejím dokončením, takže během čekání vytéká o něco méně materiálu. Cura se také pokusí předpovídat, jak moc se tryska ochladila, když byla neaktivní. Tímto způsobem bude vědět, o kolik ji bude muset poté znovu zahřát.

Pokud se tryska ochladí rychleji, než to, co naznačuje toto nastavení, bude tryska na pohotovostní teplotě rychleji, než předpovídá Cura. V důsledku toho může trvat déle, než se tryska zahřeje, než Cura předpokládá a tiskárna bude čekat na přepínači trysek déle, aby se tato tryska zahřála.

Pokud se tryska ve skutečnosti ochlazuje pomaleji, než co naznačuje toto nastavení, může být tryska stále teplá, když Cura vydá příkaz k předehřátí trysky, což způsobí, že se zahřeje příliš rychle. Chvíli bude na teplotě tisku, než bude na řadě k tisku. Během této doby z ní trochu vytéká a plast se poněkud degraduje.

Skutečná rychlost ochlazování není konstantní rychlost ve stupních za sekundu. Pravděpodobněji to bude záviset na rozdílu mezi aktuální teplotou trysky a teplotou tiskového objemu. A tak se ochlazuje rychleji rychleji, když je horká a ochladí se pomaleji, když se přiblíží k pohotovostní teplotě. Pokud to ladíte, zkuste naladit změřením času potřebného k vychladnutí z [konečné teploty tisku](../material/material_final_print_temperature.md) na [pohotovostní teplotu](../material/material_standby_temperature.md). Toto je nejdůležitější stopa, kterou se Cura pokusí předpovědět. Při malých tiscích byste mohli mírně zvýšit rychlost ochlazování a upravit tak, aby zůstala častěji horká.

*Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.*