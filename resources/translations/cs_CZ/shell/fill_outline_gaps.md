Tisk tenkých stěn
====
Normálně Cura vynechává tenčí stěny než [šířka linie vnější stěny](../resolution/wall_line_width_0.md), odmítne je, jako příliš malé pro tisk.

Pokud je toto nastavení povoleno, bude se Cura stále pokoušet tyto části tisknout. Výsledný tisk bude nepřesný a chaotický, ale měl by spolehlivě produkovat požadovaný tvar.

![Některé části jsou příliš tenké pro tisk](../../../articles/images/fill_outline_gaps_disabled.png)
![Při aktivaci tohoto parametru se vytisknou i tenké části](../../../articles/images/fill_outline_gaps_enabled.png)

Drobné kousky jsou plné velmi tenkých linií. Tyto linie jsou pak spojeny, pokud jsou vedle sebe a nejsou příliš dlouhé. Funguje to v mnoha případech, ale v některých případech produkuje malý cikcak, což výrazně prodlužuje dobu tisku.

Před použitím tohoto nastavení je vhodné zkusit mírně upravit [šířku linií vnější stěny](../resolution/wall_line_width_0.md). Pokud je vaše část mírně tenčí než šířka linie, můžete dosáhnout lepších výsledků, pokud pro celý tisk zmenšíte šířku linie vnější stěny tak, aby se tenké části tiskly normálně. Pokud však šířku linie příliš omezíte, materiál nebude proudit spolehlivě, což povede k pod-extruzi.

**Toto bude tisknout tenké části pouze ve vodorovné rovině. Pro tenké části ve směru Z viz nastavení [Tolerance slicování](../experimental/slicing_tolerance.md) nebo zvětšení výšky vrstvy.**