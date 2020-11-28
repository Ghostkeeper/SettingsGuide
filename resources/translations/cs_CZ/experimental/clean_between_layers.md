Otřít trysku mezi vrstvami
====
Toto nastavení umožňuje provedení postupu na konci každé vrstvy, aby se z hrotu trysky setřel jakýkoli materiál. Pokud máte tiskárnu s vestavěným stíracím kartáčem, aktivace tohoto nastavení způsobí, že Cura dá tiskárně pokyn k pravidelnému setření trysky tímto kartáčem.

![Vizualizace pohybů při otírání](../images/clean_between_layers_cs.svg)

Tento postup otírání sestává z několika kroků:
1. Je-li [aktivována retrakce pro otírání](wipe_retraction_enable.md), je materiál retrahován.
2. Pokud je aktivován [Z-skok pro otírání](wipe_hop_enable.md), tryska je posunuta nahoru nebo tisková podložka dolů.
3. Tryska se přesune za [pozici kartáče](wipe_brush_pos_x.md).
4. Tryska se [několikrát](wipe_repeat_count.md) otře o kartáč.
5. Tryska se vrátí do výchozí polohy.
6. Z-skok je ukončen, pokud byl aktivován. Materiál se uvolní.
7. Tisk se na [určitou dobu](wipe_pause.md) zastaví.

Účelem tohoto postupu je pravidelné čištění trysky od všech nečistot. Některé materiály mají tendenci stoupat směrem k trysce kapilárním působením kvůli vysokému povrchovému napětí. Tyto materiály se mohou infiltrovat a hromadit se v tiskové hlavě, což může způsobit zlomení tiskové hlavy. Jiné materiály obsahující vlákna nebo jiné náplně mohou způsobit, že se náplň během tisku nastříká na trysku. Tato akce tento materiál otře.