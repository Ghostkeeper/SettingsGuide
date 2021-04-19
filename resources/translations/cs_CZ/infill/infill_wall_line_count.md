Počet dalších stěn výplně
====
Toto nastavení přidá několik obrysů kolem oblastí výplně. To znamená zvýšení [počtu stěn](../shell/wall_line_count.md), ale kontury nejdou kolem pláště a stěny budou také mezi pláštěm a výplní. Je to podobné přidávání [dalších stěn pláště](../top_bottom/skin_outline_count.md), ale kolem výplně místo kolem pláště.

Tyto stěny jsou vytištěny s parametry výplně.

![Další dvě stěny kolem výplně](../../../articles/images/infill_wall_line_count.png)

Ve srovnání s přidáním dalších stěn kolem pláště toto nastavení výrazně zvyšuje odolnost modelu a snižuje prosvítání výplně pláštěm, ale také zvyšuje dobu tisku a spotřebu materiálu. Zatímco další stěny pláště nahradí materiál, který by byl stejně vytištěn jako plášť, toto nastavení skutečně přidá materiál, pokud hustota výplně již není 100%.

Vypadá to jako přidání dalších stěn kolem celého tisku. Je však vhodné přidat alespoň jednu další stěnu kolem výplně nebo pláště, protože to zabrání tomu, aby linie pláště končily ve vzduchu.