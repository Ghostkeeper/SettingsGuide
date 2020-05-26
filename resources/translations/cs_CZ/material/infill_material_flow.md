Tok pro výplň
====
Toto nastavení upravuje tok pouze pro výplň. Rychlost toku výplně lze nastavit odděleně od toku pro zbytek tisku.

Úprava toku během tisku výplně je metoda zastavení prostoru pro vyřešení problémů s rychlostí vytlačování nebo problémy s pevností. Stejného efektu lze dosáhnout úpravou [vzdálenosti mezi liniemi](../infill/infill_line_distance.md) a [šířky linií](../resolution/infill_line_width.md) výplně, ale toto nastavení může být intuitivnější.

Problémy s rychlostí vytlačování nebo silou výplně jsou obvykle způsobeny jednou ze dvou příčin: křížení ve vzoru výplně nebo příliš velká změna průtoku mezi výplní a jinými strukturami. Spíše než přizpůsobení tohoto toku může být efektivnější upravit [vzor výplně](../infill/infill_pattern.md) nebo [šířku linie výplně](../resolution/infill_line_width.md). Vyberte vzor výplně, který se nekříží, jako je cikcak, a zvolte šířku linie blíž k rychlosti vytlačování pro stěny a plášť. Pokud musí být šířka linie zvětšena z důvodu pevnosti, ale tok je omezený, je vhodné místo zvýšení toku, použít [násobitel linií výplně](../infill/infill_multiplier.md).
