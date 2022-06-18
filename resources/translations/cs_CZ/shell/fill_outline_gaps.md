Tisk tenkých stěn
====
Normálně Cura vynechává tenčí stěny než <!--if cura_version<5.0:[Šířka linie vnější stěny](../resolution/wall_line_width_0.md)--><!--if cura_version>=5.0-->[Minimální šířka linie liché stěny](min_odd_wall_line_width.md)<!--endif-->, odmítne je, jako příliš malé pro tisk.

Pokud je toto nastavení povoleno, bude se Cura stále pokoušet tyto části tisknout. Výsledný tisk bude nepřesný <!--if cura_version<5.0: a chaotický-->, ale měl by spolehlivě produkovat požadovaný tvar.

![Některé části jsou příliš tenké pro tisk](../../../articles/images/fill_outline_gaps_disabled.png)
![Při aktivaci tohoto parametru se vytisknou i tenké části](../../../articles/images/fill_outline_gaps_enabled.png)

<!--if cura_version<5.0:
Drobné kousky jsou plné velmi tenkých linií. Tyto linie jsou pak spojeny, pokud jsou vedle sebe a nejsou příliš dlouhé. Funguje to v mnoha případech, ale v některých případech produkuje malý cikcak, což výrazně prodlužuje dobu tisku.

Než se uchýlíte k tomuto nastavení, je vhodné zkusit mírně upravit šířku linie vnější stěny. Pokud je váš díl o něco tenčí než šířka jedné linie, mohlo by přinést lepší výsledek, pokud snížíte šířku linie vnější stěny celého tisku tak, aby se tenké díly tiskly normálně. Přílišné snížení šířky linie však způsobí nespolehlivý tok materiálu, což povede k podextruzi.
-->
<!--if cura_version>=5.0-->
Tenké díly se tisknou pomocí velmi tenké linie stěny. Tato tenká linie se však nemusí dobře tisknout. K nápravě slouží také parametr [Minimální šířka linie tenké stěny](min_bead_width.md). Toto nastavení poskytuje spodní hranici šířky linie. Pokud bude tenčí, bude linie vytištěna příliš tlustá a teoreticky se vytiskne za hranice modelu, ale měla by se alespoň spolehlivě vytisknout. Cokoli tenčího než [Minimální velikost prvku](min_feature_size.md) se nevytiskne vůbec.
<!--endif-->

**Toto bude tisknout tenké části pouze ve vodorovné rovině. Pro tenké části ve směru Z viz nastavení [Tolerance slicování](../experimental/slicing_tolerance.md) nebo snížení výšky vrstvy.**